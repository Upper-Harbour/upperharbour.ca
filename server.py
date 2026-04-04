#!/usr/bin/env python3
"""
Upper Harbour — Webhook Server
Handles Stripe checkout sessions, payment webhooks, Calendly booking webhooks,
and Formspree submission webhooks. Triggers lead brief generation on events.

Deploy on Railway.app — connects to your GitHub repo and auto-deploys.

Endpoints:
  POST /webhook/stripe       — Stripe payment events
  POST /webhook/calendly     — Calendly booking notifications
  POST /webhook/formspree    — Vendor form submissions
  POST /api/checkout         — Create Stripe checkout session (for /comply buy buttons)
  GET  /api/brief            — Manually trigger a lead brief (for testing)
  GET  /health               — Health check

Environment variables (set in Railway dashboard):
  ANTHROPIC_API_KEY          — Claude API key
  STRIPE_SECRET_KEY          — Stripe secret key (sk_live_...)
  STRIPE_WEBHOOK_SECRET      — Stripe webhook signing secret (whsec_...)
  SMTP_HOST                  — smtp.gmail.com (or Resend/Postmark)
  SMTP_PORT                  — 587
  SMTP_USER                  — sender email
  SMTP_PASS                  — app password
  BRIEF_EMAIL                — josh@upperharbour.ca
  SITE_URL                   — https://www.upperharbour.ca
  PORT                       — Railway sets this automatically
"""

import os
import json
import logging
from datetime import datetime

from flask import Flask, request, jsonify, redirect
import stripe

logging.basicConfig(level=logging.INFO, format='%(asctime)s [%(levelname)s] %(message)s')
log = logging.getLogger(__name__)

app = Flask(__name__)

# ── Configuration ────────────────────────────────────────────

STRIPE_SECRET_KEY = os.environ.get("STRIPE_SECRET_KEY")
STRIPE_WEBHOOK_SECRET = os.environ.get("STRIPE_WEBHOOK_SECRET")
SITE_URL = os.environ.get("SITE_URL", "https://www.upperharbour.ca")
PORT = int(os.environ.get("PORT", 5000))

if STRIPE_SECRET_KEY:
    stripe.api_key = STRIPE_SECRET_KEY


# ── Products (map to your /comply pricing) ───────────────────

PRODUCTS = {
    "industry-report": {
        "name": "Industry Compliance Assessment",
        "price": 9900,  # cents
        "description": "Five-factor TIAs for the 18-24 most common tools in your industry.",
    },
    "custom-assessment": {
        "name": "Custom Stack Assessment",
        "price": 50000,
        "description": "TIAs tailored to your exact tool stack. 48-hour delivery.",
    },
    "full-package": {
        "name": "Full Compliance Package",
        "price": 250000,
        "description": "Complete Law 25 binder — TIAs, privacy policy, breach plan, incident register.",
    },
    "alberta-pia": {
        "name": "Alberta PIA Research Tool",
        "price": 19900,
        "description": "Auto-fill OIPC PIA template sections F, G, and H2.",
    },
}


# ── Health Check ─────────────────────────────────────────────

@app.route("/health")
def health():
    return jsonify({
        "status": "ok",
        "service": "Upper Harbour Webhook Server",
        "timestamp": datetime.utcnow().isoformat(),
    })


# ── Stripe Checkout Session ─────────────────────────────────

@app.route("/api/checkout", methods=["POST"])
def create_checkout():
    """
    Create a Stripe checkout session.
    Called from the /comply page buy buttons.
    
    Expects JSON: {"product": "industry-report", "email": "optional@email.com"}
    Returns: {"url": "https://checkout.stripe.com/..."}
    """
    if not STRIPE_SECRET_KEY:
        return jsonify({"error": "Stripe not configured"}), 500
    
    data = request.get_json() or {}
    product_id = data.get("product", "industry-report")
    customer_email = data.get("email")
    
    product = PRODUCTS.get(product_id)
    if not product:
        return jsonify({"error": f"Unknown product: {product_id}"}), 400
    
    try:
        session_params = {
            "payment_method_types": ["card"],
            "line_items": [{
                "price_data": {
                    "currency": "cad",
                    "product_data": {
                        "name": product["name"],
                        "description": product["description"],
                    },
                    "unit_amount": product["price"],
                },
                "quantity": 1,
            }],
            "mode": "payment",
            "success_url": f"{SITE_URL}/comply?success=true&product={product_id}",
            "cancel_url": f"{SITE_URL}/comply?cancelled=true",
            "metadata": {
                "product_id": product_id,
            },
        }
        
        if customer_email:
            session_params["customer_email"] = customer_email
        
        session = stripe.checkout.Session.create(**session_params)
        
        log.info(f"Checkout session created: {product_id} (${product['price']/100})")
        return jsonify({"url": session.url})
    
    except Exception as e:
        log.error(f"Checkout creation failed: {e}")
        return jsonify({"error": str(e)}), 500


# ── Stripe Webhook ───────────────────────────────────────────

@app.route("/webhook/stripe", methods=["POST"])
def stripe_webhook():
    """
    Receive Stripe webhook events.
    Triggers lead brief on successful payments.
    """
    payload = request.get_data()
    sig_header = request.headers.get("Stripe-Signature", "")
    
    # Verify webhook signature
    if STRIPE_WEBHOOK_SECRET:
        try:
            event = stripe.Webhook.construct_event(
                payload, sig_header, STRIPE_WEBHOOK_SECRET
            )
        except stripe.error.SignatureVerificationError:
            log.warning("Stripe webhook signature verification failed")
            return jsonify({"error": "Invalid signature"}), 400
    else:
        event = json.loads(payload)
    
    event_type = event.get("type", "")
    log.info(f"Stripe event: {event_type}")
    
    if event_type == "checkout.session.completed":
        session = event["data"]["object"]
        customer_email = session.get("customer_details", {}).get("email", "")
        customer_name = session.get("customer_details", {}).get("name", "Unknown")
        amount = session.get("amount_total", 0)
        product_id = session.get("metadata", {}).get("product_id", "unknown")
        
        log.info(f"Payment received: {customer_name} ({customer_email}) — {product_id} — ${amount/100}")
        
        # Trigger lead brief
        if customer_email:
            try:
                from lead_brief import generate_lead_brief
                product_label = PRODUCTS.get(product_id, {}).get("name", product_id)
                generate_lead_brief(
                    customer_name, 
                    customer_email, 
                    source=f"Stripe purchase: {product_label} (${amount/100})"
                )
            except Exception as e:
                log.error(f"Lead brief generation failed: {e}")
    
    return jsonify({"received": True})


# ── Calendly Webhook ─────────────────────────────────────────

@app.route("/webhook/calendly", methods=["POST"])
def calendly_webhook():
    """
    Receive Calendly booking notifications.
    Triggers lead brief for new bookings.
    """
    data = request.get_json() or {}
    event_type = data.get("event", "")
    
    log.info(f"Calendly event: {event_type}")
    
    if event_type == "invitee.created":
        payload = data.get("payload", {})
        name = payload.get("name", "Unknown")
        email = payload.get("email", "")
        event_name = payload.get("event_type", {}).get("name", "")
        scheduled_time = payload.get("event", {}).get("start_time", "")
        
        log.info(f"Calendly booking: {name} ({email}) — {event_name} at {scheduled_time}")
        
        if email:
            try:
                from lead_brief import generate_lead_brief
                generate_lead_brief(
                    name, 
                    email, 
                    source=f"Calendly booking: {event_name}"
                )
            except Exception as e:
                log.error(f"Lead brief generation failed: {e}")
    
    return jsonify({"received": True})


# ── Formspree Webhook ────────────────────────────────────────

@app.route("/webhook/formspree", methods=["POST"])
def formspree_webhook():
    """
    Receive Formspree vendor form submissions.
    Triggers lead brief for new vendor inquiries.
    """
    data = request.get_json() or {}
    
    name = data.get("name", data.get("company", "Unknown"))
    email = data.get("email", data.get("_replyto", ""))
    
    log.info(f"Formspree submission: {name} ({email})")
    
    if email:
        try:
            from lead_brief import generate_lead_brief
            generate_lead_brief(
                name,
                email,
                source="Vendor form submission"
            )
        except Exception as e:
            log.error(f"Lead brief generation failed: {e}")
    
    return jsonify({"received": True})


# ── Manual Brief Trigger (for testing) ───────────────────────

@app.route("/api/brief")
def manual_brief():
    """
    Manually trigger a lead brief.
    Usage: GET /api/brief?name=Jane+Smith&email=jane@company.com
    """
    name = request.args.get("name", "Test User")
    email = request.args.get("email", "")
    
    if not email:
        return jsonify({"error": "Email parameter required"}), 400
    
    try:
        from lead_brief import generate_lead_brief
        brief = generate_lead_brief(name, email, source="Manual trigger")
        return jsonify({"status": "sent", "name": name, "email": email})
    except Exception as e:
        return jsonify({"error": str(e)}), 500


# ── CORS headers (for /comply page calling /api/checkout) ────

@app.after_request
def add_cors_headers(response):
    """Allow the UH site to call this server."""
    allowed_origins = [
        "https://www.upperharbour.ca",
        "https://upperharbour.ca",
        "http://localhost:8000",  # local dev
    ]
    origin = request.headers.get("Origin", "")
    if origin in allowed_origins:
        response.headers["Access-Control-Allow-Origin"] = origin
        response.headers["Access-Control-Allow-Methods"] = "GET, POST, OPTIONS"
        response.headers["Access-Control-Allow-Headers"] = "Content-Type"
    return response


@app.route("/api/checkout", methods=["OPTIONS"])
def checkout_options():
    """Handle CORS preflight for checkout endpoint."""
    return "", 204


# ── Run ──────────────────────────────────────────────────────

if __name__ == "__main__":
    log.info(f"Starting Upper Harbour server on port {PORT}")
    log.info(f"Stripe: {'configured' if STRIPE_SECRET_KEY else 'NOT configured'}")
    log.info(f"Endpoints:")
    log.info(f"  POST /webhook/stripe")
    log.info(f"  POST /webhook/calendly")
    log.info(f"  POST /webhook/formspree")
    log.info(f"  POST /api/checkout")
    log.info(f"  GET  /api/brief?name=...&email=...")
    log.info(f"  GET  /health")
    
    app.run(host="0.0.0.0", port=PORT)
