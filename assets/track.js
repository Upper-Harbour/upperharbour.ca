// Conversion tracking - fires GA4 events on key CTA clicks
document.addEventListener('click', function(e) {
  var link = e.target.closest('a');
  if (!link) return;
  var href = link.getAttribute('href') || '';
  
  if (href.indexOf('/comply') === 0) {
    gtag('event', 'cta_click', { cta_type: 'comply', cta_text: link.textContent.trim(), page: location.pathname });
  } else if (href.indexOf('calendly.com') > -1) {
    gtag('event', 'cta_click', { cta_type: 'calendly', cta_text: link.textContent.trim(), page: location.pathname });
  } else if (href.indexOf('/vendors') === 0) {
    gtag('event', 'cta_click', { cta_type: 'vendors', cta_text: link.textContent.trim(), page: location.pathname });
  } else if (href.indexOf('/harbourscan') === 0 && !link.classList.contains('nav-cta') && !link.classList.contains('mobile-cta')) {
    gtag('event', 'cta_click', { cta_type: 'harbourscan', cta_text: link.textContent.trim(), page: location.pathname });
  } else if (href.indexOf('/consulting') === 0) {
    gtag('event', 'cta_click', { cta_type: 'consulting', cta_text: link.textContent.trim(), page: location.pathname });
  } else if (href.indexOf('buy.stripe.com') > -1) {
    gtag('event', 'purchase_click', { cta_text: link.textContent.trim(), page: location.pathname });
  }
});
