/**
 * Upper Harbour — Dynamic Stats (uh-stats.js)
 * 
 * Load AFTER saas-db.js on any page. Computes all stats from the live database
 * and populates any element with class="uh-stat" and a data-stat attribute.
 * 
 * Usage in HTML:
 *   <span class="uh-stat" data-stat="totalTools">715</span>
 *   <span class="uh-stat" data-stat="cloudActPct">89</span>%
 *   <span class="uh-stat" data-stat="foreignPct">63</span>%
 * 
 * The hardcoded fallback value (715, 89, etc.) is shown if JS fails or for
 * search engine crawlers that don't execute JS. Once JS runs, it's replaced
 * with the live computed value.
 * 
 * Available stats:
 *   totalTools        — total tools in database
 *   categoryCount     — number of distinct categories
 *   foreignCount      — tools under non-Canadian jurisdiction
 *   foreignPct        — percentage under foreign jurisdiction
 *   cloudActCount     — tools subject to CLOUD Act
 *   cloudActPct       — percentage subject to CLOUD Act
 *   canadianCount     — tools classified as 'canadian' risk tier
 *   canadianPct       — percentage Canadian-controlled
 *   reviewCount       — tools classified as 'review'
 *   reviewPct         — percentage review/caution
 *   nonExposedCount   — tools classified as 'non_exposed'
 *   nonExposedPct     — percentage non-exposed foreign
 *   exposedCount      — tools classified as 'exposed'
 *   exposedPct        — percentage exposed
 *   caResTotal        — tools offering Canadian data residency (non-canadian tier)
 *   caResExposed      — CA-resident tools still CLOUD Act exposed
 *   caResExposedPct   — percentage of CA-resident tools that are CLOUD Act exposed
 *   nonCanadianPct    — 100 - canadianPct (for "buy Canadian would disqualify X%")
 *   usCount           — tools under US jurisdiction
 *   usPct             — percentage under US jurisdiction
 *   lastUpdated       — formatted date string from saasDBMeta
 */
(function() {
  if (typeof saasDB === 'undefined') return;

  var total = saasDB.length;
  var usCount = 0, cdnCount = 0, cloudActCount = 0;
  var caResTotal = 0, caResExposed = 0;
  var ownCanadian = 0, ownReview = 0, ownNonExposed = 0, ownExposed = 0;
  var categories = {};

  saasDB.forEach(function(t) {
    if (t.jurisdiction === 'United States') usCount++;
    if (t.jurisdiction === 'Canada') cdnCount++;
    if (t.cloudAct) cloudActCount++;

    var res = (t.dataResidency || '').toLowerCase();
    if (t.risk !== 'canadian') {
      if (res.indexOf('canada') > -1 || res.indexOf('ca-central') > -1 ||
          res.indexOf('montreal') > -1 || res.indexOf('toronto') > -1 ||
          res.indexOf('montréal') > -1) {
        caResTotal++;
        if (t.cloudAct) caResExposed++;
      }
    }

    var c = t.category || 'other';
    if (!categories[c]) categories[c] = true;

    if (t.risk === 'canadian') ownCanadian++;
    else if (t.risk === 'review') ownReview++;
    else if (t.risk === 'non_exposed') ownNonExposed++;
    else ownExposed++;
  });

  var foreignCount = total - cdnCount;
  var catCount = Object.keys(categories).length;

  var stats = {
    totalTools:       total,
    categoryCount:    catCount,
    foreignCount:     foreignCount,
    foreignPct:       Math.round(foreignCount / total * 100),
    cloudActCount:    cloudActCount,
    cloudActPct:      Math.round(cloudActCount / total * 100),
    canadianCount:    ownCanadian,
    canadianPct:      Math.round(ownCanadian / total * 100),
    reviewCount:      ownReview,
    reviewPct:        Math.round(ownReview / total * 100),
    nonExposedCount:  ownNonExposed,
    nonExposedPct:    Math.round(ownNonExposed / total * 100),
    exposedCount:     ownExposed,
    exposedPct:       Math.round(ownExposed / total * 100),
    caResTotal:       caResTotal,
    caResExposed:     caResExposed,
    caResExposedPct:  caResTotal > 0 ? Math.round(caResExposed / caResTotal * 100) : 0,
    nonCanadianPct:   100 - Math.round(ownCanadian / total * 100),
    usCount:          usCount,
    usPct:            Math.round(usCount / total * 100),
  };

  // Format date from saasDBMeta
  if (typeof saasDBMeta !== 'undefined' && saasDBMeta.lastUpdated) {
    var d = new Date(saasDBMeta.lastUpdated);
    var months = ['January','February','March','April','May','June','July',
                  'August','September','October','November','December'];
    stats.lastUpdated = months[d.getMonth()] + ' ' + d.getDate() + ', ' + d.getFullYear();
    stats.lastUpdatedShort = months[d.getMonth()] + ' ' + d.getFullYear();
  }

  // Populate all elements with class="uh-stat"
  document.querySelectorAll('.uh-stat').forEach(function(el) {
    var key = el.getAttribute('data-stat');
    if (key && stats[key] !== undefined) {
      el.textContent = stats[key];
    }
  });

  // Also populate animated counters (data-target) if they have data-stat
  document.querySelectorAll('[data-stat][data-target]').forEach(function(el) {
    var key = el.getAttribute('data-stat');
    if (key && stats[key] !== undefined) {
      el.setAttribute('data-target', stats[key]);
    }
  });

  // Expose globally for pages that need custom logic
  window.uhStats = stats;

  // ═══ Application-layer-only stats (excludes cloud_infrastructure) ═══
  var appTools = saasDB.filter(function(t) { return t.category !== 'cloud_infrastructure'; });
  var appTotal = appTools.length;
  var appUS = 0, appCdn = 0, appCloudAct = 0, appCanadian = 0;
  var appCaResTotal = 0, appCaResExposed = 0;

  appTools.forEach(function(t) {
    if (t.jurisdiction === 'United States') appUS++;
    if (t.jurisdiction === 'Canada') appCdn++;
    if (t.cloudAct) appCloudAct++;
    if (t.risk === 'canadian') appCanadian++;

    var res = (t.dataResidency || '').toLowerCase();
    if (t.risk !== 'canadian') {
      if (res.indexOf('canada') > -1 || res.indexOf('ca-central') > -1 ||
          res.indexOf('montreal') > -1 || res.indexOf('toronto') > -1 ||
          res.indexOf('montréal') > -1) {
        appCaResTotal++;
        if (t.cloudAct) appCaResExposed++;
      }
    }
  });

  var appForeign = appTotal - appCdn;

  stats.appTotal = appTotal;
  stats.appForeignPct = Math.round(appForeign / appTotal * 100);
  stats.appCloudActPct = Math.round(appCloudAct / appTotal * 100);
  stats.appCanadianPct = Math.round(appCanadian / appTotal * 100);
  stats.appCaResExposedPct = appCaResTotal > 0 ? Math.round(appCaResExposed / appCaResTotal * 100) : 0;

  // Re-populate after adding new stats
  document.querySelectorAll('.uh-stat').forEach(function(el) {
    var key = el.getAttribute('data-stat');
    if (key && stats[key] !== undefined) {
      el.textContent = stats[key];
    }
  });
  document.querySelectorAll('[data-stat][data-target]').forEach(function(el) {
    var key = el.getAttribute('data-stat');
    if (key && stats[key] !== undefined) {
      el.setAttribute('data-target', stats[key]);
    }
  });
})();
