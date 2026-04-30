/**
 * Upper Harbour — Dynamic Stats (uh-stats.js)
 *
 * Fetches the full Sovereignty Index aggregate stats from the Railway API
 * and populates any element with class="uh-stat" and a data-stat attribute.
 *
 * As of April 2026 this no longer reads window.saasDB. The legacy
 * saas-db.js script is being removed from the public deployment so that
 * the analytical 'note' field stays gated behind the server-side API.
 * The helper now talks to /api/stats which returns ~29 pre-computed
 * aggregate values, none of them tool-detail.
 *
 * Usage in HTML (unchanged from the legacy version):
 *   <span class="uh-stat" data-stat="totalTools">715</span>
 *   <span class="uh-stat" data-stat="cloudActPct">89</span>%
 *   <span class="uh-stat" data-stat="foreignPct">63</span>%
 *
 * The hardcoded fallback value (715, 89, etc.) is shown if the fetch
 * fails or for search engine crawlers that don't execute JS. Once the
 * fetch resolves, it's replaced with the live computed value.
 *
 * Available stats (all returned by /api/stats):
 *   totalTools          — total tools in database
 *   categoryCount       — number of distinct categories
 *   foreignCount        — tools under non-Canadian jurisdiction
 *   foreignPct          — percentage under foreign jurisdiction
 *   cloudActCount       — tools subject to CLOUD Act
 *   cloudActPct         — percentage subject to CLOUD Act
 *   canadianCount       — tools classified as 'canadian' risk tier
 *   canadianPct         — percentage Canadian-controlled
 *   reviewCount         — tools classified as 'review'
 *   reviewPct           — percentage review/caution
 *   nonExposedCount     — tools classified as 'non_exposed'
 *   nonExposedPct       — percentage non-exposed foreign
 *   exposedCount        — tools classified as 'exposed'
 *   exposedPct          — percentage exposed
 *   caResTotal          — tools offering Canadian data residency (non-canadian tier)
 *   caResExposed        — CA-resident tools still CLOUD Act exposed
 *   caResExposedPct     — percentage of CA-resident tools that are CLOUD Act exposed
 *   nonCanadianPct      — 100 - canadianPct
 *   usCount             — tools under US jurisdiction
 *   usPct               — percentage under US jurisdiction
 *   appTotal            — application-layer tools (excludes cloud_infrastructure)
 *   appCdnCount         — Canadian app-layer tools
 *   appUsCount          — US app-layer tools
 *   appForeignPct       — percentage of app-layer tools under foreign jurisdiction
 *   appCloudActPct      — percentage of app-layer tools subject to CLOUD Act
 *   appCanadianPct      — percentage of app-layer tools that are Canadian-controlled
 *   appCaResExposedPct  — percentage of CA-resident app-layer tools still CLOUD Act exposed
 *   zeroCatCount        — number of categories (3+ tools) with zero Canadian options
 *   loadedAt            — ISO timestamp of when the server loaded the database
 *   lastUpdated         — formatted from loadedAt, e.g., "April 9, 2026"
 *   lastUpdatedShort    — formatted from loadedAt, e.g., "April 2026"
 */
(function() {
  var API_BASE = 'https://web-production-b1856.up.railway.app';

  function populate(stats) {
    // Plain inline stats — overwrite textContent with the live value.
    document.querySelectorAll('.uh-stat').forEach(function(el) {
      var key = el.getAttribute('data-stat');
      if (key && stats[key] !== undefined && stats[key] !== null) {
        el.textContent = stats[key];
      }
    });
    // Animated counters — these have data-target which an in-page
    // count-up animation reads on viewport-enter. The fetch usually
    // resolves AFTER that animation has already painted the stale
    // hardcoded value, so we (a) update the data-target so any
    // not-yet-started animation lands on the right number, and
    // (b) ALSO overwrite textContent unconditionally so an
    // already-completed animation gets corrected on top. Includes
    // suffix support (data-suffix="%") to match how the page-level
    // count-up animation formats values.
    document.querySelectorAll('[data-stat][data-target]').forEach(function(el) {
      var key = el.getAttribute('data-stat');
      if (key && stats[key] !== undefined && stats[key] !== null) {
        el.setAttribute('data-target', stats[key]);
        var suffix = el.getAttribute('data-suffix') || '';
        el.textContent = stats[key] + suffix;
      }
    });
  }

  function formatLoadedAt(stats) {
    if (!stats.loadedAt) return;
    try {
      var d = new Date(stats.loadedAt);
      var months = ['January','February','March','April','May','June','July',
                    'August','September','October','November','December'];
      stats.lastUpdated = months[d.getMonth()] + ' ' + d.getDate() + ', ' + d.getFullYear();
      stats.lastUpdatedShort = months[d.getMonth()] + ' ' + d.getFullYear();
    } catch (e) { /* leave fields unset */ }
  }

  fetch(API_BASE + '/api/stats', { cache: 'no-store' })
    .then(function(res) {
      if (!res.ok) throw new Error('HTTP ' + res.status);
      return res.json();
    })
    .then(function(stats) {
      formatLoadedAt(stats);
      // Expose globally for pages that need custom logic (research.html
      // legacy code still references window.uhStats — kept for compatibility)
      window.uhStats = stats;
      populate(stats);

      // Fire a custom event so pages that wait on stats (e.g., animated
      // counters that initialize on page load) can react.
      try {
        window.dispatchEvent(new CustomEvent('uh-stats-ready', { detail: stats }));
      } catch (e) { /* IE11 fallback not needed in 2026 */ }
    })
    .catch(function(e) {
      // On failure, the hardcoded fallback values stay in place — they
      // were the SEO baseline anyway. Log to console but don't break.
      if (window.console && console.warn) {
        console.warn('uh-stats: failed to load /api/stats —', e.message);
      }
    });
})();
