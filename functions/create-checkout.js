// Cloudflare Pages Function — creates a Stripe Embedded Checkout session
// Environment variable required: STRIPE_SECRET_KEY (set in Cloudflare Dashboard)

export async function onRequestPost(context) {
  const { env } = context;
  const STRIPE_SECRET_KEY = env.STRIPE_SECRET_KEY;

  if (!STRIPE_SECRET_KEY) {
    return new Response(JSON.stringify({ error: 'Stripe not configured' }), {
      status: 500,
      headers: { 'Content-Type': 'application/json' }
    });
  }

  // Create a Checkout Session with embedded mode
  const response = await fetch('https://api.stripe.com/v1/checkout/sessions', {
    method: 'POST',
    headers: {
      'Authorization': `Bearer ${STRIPE_SECRET_KEY}`,
      'Content-Type': 'application/x-www-form-urlencoded',
    },
    body: new URLSearchParams({
      'ui_mode': 'embedded',
      'mode': 'payment',
      'line_items[0][price_data][currency]': 'cad',
      'line_items[0][price_data][product_data][name]': 'Alberta POPA PIA Research Package',
      'line_items[0][price_data][product_data][description]': 'Pre-written answers for Sections F, G, and H2 of the mandatory OIPC PIA template. Jurisdictional research for all selected SaaS tools.',
      'line_items[0][price_data][unit_amount]': '19900',
      'line_items[0][quantity]': '1',
      'return_url': 'https://www.upperharbour.ca/alberta-pia?paid=true',
    }).toString()
  });

  const session = await response.json();

  if (session.error) {
    return new Response(JSON.stringify({ error: session.error.message }), {
      status: 400,
      headers: { 'Content-Type': 'application/json' }
    });
  }

  return new Response(JSON.stringify({ clientSecret: session.client_secret }), {
    headers: {
      'Content-Type': 'application/json',
      'Access-Control-Allow-Origin': 'https://www.upperharbour.ca',
    }
  });
}

// Handle CORS preflight
export async function onRequestOptions() {
  return new Response(null, {
    headers: {
      'Access-Control-Allow-Origin': 'https://www.upperharbour.ca',
      'Access-Control-Allow-Methods': 'POST, OPTIONS',
      'Access-Control-Allow-Headers': 'Content-Type',
    }
  });
}
