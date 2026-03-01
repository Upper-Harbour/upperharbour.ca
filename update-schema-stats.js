#!/usr/bin/env node
/**
 * Upper Harbour — Schema Stats Updater
 * 
 * Run after any change to saas-db.js. Updates all hardcoded numbers
 * inside JSON-LD schema blocks across the site.
 * 
 * Usage:  node update-schema-stats.js
 * 
 * Add to GitHub Actions after saas-db.js changes:
 *   - name: Update schema stats
 *     run: node update-schema-stats.js
 */

const fs = require('fs');
const path = require('path');

const ROOT = process.cwd(); // Run from repo root

// ── Load the database ──────────────────────────────────────
const dbCode = fs.readFileSync(path.join(ROOT, 'saas-db.js'), 'utf-8');
eval(dbCode);

// ── Compute stats ──────────────────────────────────────────
const total = saasDB.length;
const categories = new Set(saasDB.map(t => t.category || 'other'));
const catCount = categories.size;

let usCount = 0, cdnCount = 0, cloudActCount = 0;
let caResTotal = 0, caResExposed = 0;
let ownCanadian = 0, ownReview = 0, ownNonExposed = 0, ownExposed = 0;

saasDB.forEach(t => {
  if (t.jurisdiction === 'United States') usCount++;
  if (t.jurisdiction === 'Canada') cdnCount++;
  if (t.cloudAct) cloudActCount++;

  const res = (t.dataResidency || '').toLowerCase();
  if (t.risk !== 'canadian') {
    if (res.includes('canada') || res.includes('ca-central') || 
        res.includes('montreal') || res.includes('montréal') || res.includes('toronto')) {
      caResTotal++;
      if (t.cloudAct) caResExposed++;
    }
  }

  if (t.risk === 'canadian') ownCanadian++;
  else if (t.risk === 'review') ownReview++;
  else if (t.risk === 'non_exposed') ownNonExposed++;
  else ownExposed++;
});

const stats = {
  total,
  catCount,
  usCount,
  usPct: Math.round(usCount / total * 100),
  cdnCount,
  cdnPct: Math.round(cdnCount / total * 100),
  cloudActCount,
  cloudActPct: Math.round(cloudActCount / total * 100),
  foreignPct: Math.round((total - cdnCount) / total * 100),
  canadianPct: Math.round(ownCanadian / total * 100),
  reviewPct: Math.round(ownReview / total * 100),
  nonExposedPct: Math.round(ownNonExposed / total * 100),
  exposedPct: Math.round(ownExposed / total * 100),
  nonCanadianPct: 100 - Math.round(ownCanadian / total * 100),
  caResTotal,
  caResExposed,
  caResExposedPct: caResTotal > 0 ? Math.round(caResExposed / caResTotal * 100) : 0,
};

console.log('Computed stats from saas-db.js:');
console.log(`  Total tools: ${stats.total}`);
console.log(`  Categories: ${stats.catCount}`);
console.log(`  US-parented: ${stats.usPct}%  (${stats.usCount})`);
console.log(`  CLOUD Act exposed: ${stats.cloudActPct}%`);
console.log(`  Canadian-owned: ${stats.canadianPct}%`);
console.log(`  Review: ${stats.reviewPct}%`);
console.log(`  Non-exposed foreign: ${stats.nonExposedPct}%`);
console.log(`  Exposed: ${stats.exposedPct}%`);
console.log(`  CA-resident + CLOUD Act: ${stats.caResExposedPct}%`);
console.log(`  Non-Canadian: ${stats.nonCanadianPct}%`);
console.log('');

// ── Previous values to find-and-replace ────────────────────
// Read from reference file if it exists, otherwise use initial values.
// The reference file is auto-generated at the end of each run.

const refPath = path.join(ROOT, 'assets', 'schema-stats-ref.json');
let OLD;

if (fs.existsSync(refPath)) {
  OLD = JSON.parse(fs.readFileSync(refPath, 'utf-8'));
  console.log('Loaded previous values from schema-stats-ref.json');
} else {
  // First run — these are the original hardcoded values in the schema blocks
  OLD = {
    total: 693,
    catCount: 30,
    usCount: 453,
    usPct: 65,
    canadianPct: 18,
    reviewPct: 11,
    nonExposedPct: 15,
    exposedPct: 54,
    nonCanadianPct: 82,
    caResExposedPct: 89,
  };
  console.log('No reference file found — using initial values (first run)');
}
// Alt stat used on Index page in one FAQ
OLD.caResExposedPctAlt = OLD.caResExposedPctAlt || 91;

console.log('');

// ── Find and process HTML files ────────────────────────────
function findHtmlFiles(dir) {
  let results = [];
  const items = fs.readdirSync(dir);
  for (const item of items) {
    if (item.startsWith('.') || item === '__MACOSX' || item === 'node_modules') continue;
    const full = path.join(dir, item);
    const stat = fs.statSync(full);
    if (stat.isDirectory()) {
      results = results.concat(findHtmlFiles(full));
    } else if (item.endsWith('.html')) {
      results.push(full);
    }
  }
  return results;
}

function updateSchemaBlocks(filepath) {
  let content = fs.readFileSync(filepath, 'utf-8');
  const original = content;
  let changes = 0;

  // Find all JSON-LD blocks
  const schemaRegex = /<script\s+type="application\/ld\+json">([\s\S]*?)<\/script>/g;
  
  content = content.replace(schemaRegex, (fullMatch, jsonContent) => {
    let updated = jsonContent;

    // Replace tool count: any "693" in schema that's clearly a tool count
    // Broad match: 693 followed by any word (tools, SaaS, mapped, tracked, commonly, etc.)
    // Also matches "of the 693" and "693+" patterns
    const toolCountRegex = new RegExp(`\\b${OLD.total}\\b(?=\\+?\\s|\\+?-)`, 'g');
    updated = updated.replace(toolCountRegex, (m) => { changes++; return m.replace(String(OLD.total), String(stats.total)); });

    // "approximately 453 tools" → new usCount
    if (OLD.usCount !== stats.usCount) {
      const usCountRegex = new RegExp(`approximately ${OLD.usCount} tools`, 'g');
      updated = updated.replace(usCountRegex, (m) => { changes++; return `approximately ${stats.usCount} tools`; });
    }

    // "30 categories" → new catCount  
    const catRegex = new RegExp(`\\b${OLD.catCount} categories\\b`, 'g');
    updated = updated.replace(catRegex, (m) => { changes++; return `${stats.catCount} categories`; });

    // Percentage replacements — only in specific contexts to avoid false positives
    const pctReplacements = [
      // "65% (approximately N tools)" or "65% are parented"
      { old: OLD.usPct, new: stats.usPct, context: /(\b)65(%[^"]*(?:parented|subject|tools))/g, label: 'usPct' },
      // "Canadian-owned (18%)" or "18% of the"  
      { old: OLD.canadianPct, new: stats.canadianPct, context: /(\b)18(%[^"]*(?:Canadian|are Canadian))/g, label: 'canadianPct' },
      // "review (11%)" or "11% require review"
      { old: OLD.reviewPct, new: stats.reviewPct, context: /(\b)11(%[^"]*(?:review|require|caution))/g, label: 'reviewPct' },
      // "15% are non-US"
      { old: OLD.nonExposedPct, new: stats.nonExposedPct, context: /(\b)15(%[^"]*(?:non-US|foreign vendor))/g, label: 'nonExposedPct' },
      // "54% are CLOUD Act" or "remaining 54%"
      { old: OLD.exposedPct, new: stats.exposedPct, context: /(\b)54(%[^"]*(?:CLOUD Act|exposed))/g, label: 'exposedPct' },
      // "disqualify roughly 82%"
      { old: OLD.nonCanadianPct, new: stats.nonCanadianPct, context: /(\b)82(%[^"]*(?:disqualify|tools Canadian))/g, label: 'nonCanadianPct' },
      // "89% of tools offering Canadian" or "89% of tools with"
      { old: OLD.caResExposedPct, new: stats.caResExposedPct, context: /(\b)89(%[^"]*(?:tools offering|tools with|residency))/g, label: 'caResExposedPct' },
      // "91% of non-Canadian tools" (alternate stat on Index page)
      { old: OLD.caResExposedPctAlt, new: stats.caResExposedPct, context: /(\b)91(%[^"]*(?:non-Canadian tools|tools offering))/g, label: 'caResExposedPctAlt' },
    ];

    for (const r of pctReplacements) {
      if (r.old !== r.new) {
        const before = updated;
        updated = updated.replace(r.context, (m, pre, rest) => {
          changes++;
          return `${pre}${r.new}${rest}`;
        });
      }
    }

    // Simple number-only replacements for remaining patterns
    // "maps 693 SaaS" in founder schema
    updated = updated.replace(
      new RegExp(`maps ${OLD.total} SaaS`, 'g'),
      (m) => { changes++; return `maps ${stats.total} SaaS`; }
    );

    // "for 693 SaaS tools" in methodology
    updated = updated.replace(
      new RegExp(`for ${OLD.total} SaaS`, 'g'),  
      (m) => { changes++; return `for ${stats.total} SaaS`; }
    );

    return `<script type="application/ld+json">${updated}</script>`;
  });

  // Also update meta description/og tags that have exact numbers
  // (but NOT ones already using "Nearly 700" approximate language)
  const metaRegex = new RegExp(`(content="[^"]*?)\\b${OLD.total}\\b([^"]*?")`, 'g');
  content = content.replace(metaRegex, (m, pre, post) => {
    // Skip if already approximate
    if (m.includes('Nearly')) return m;
    changes++;
    return `${pre}${stats.total}${post}`;
  });

  if (content !== original) {
    fs.writeFileSync(filepath, content, 'utf-8');
    const rel = path.relative(ROOT, filepath);
    console.log(`  UPDATED: ${rel} (${changes} replacements)`);
    return changes;
  }
  return 0;
}

// ── Run ────────────────────────────────────────────────────
console.log('Updating JSON-LD schema blocks across site...\n');

const files = findHtmlFiles(ROOT);
let totalChanges = 0;
let filesChanged = 0;

for (const f of files) {
  const c = updateSchemaBlocks(f);
  if (c > 0) {
    totalChanges += c;
    filesChanged++;
  }
}

console.log(`\nDone. ${totalChanges} replacements across ${filesChanged} files.`);

// ── Update OLD values hint ─────────────────────────────────
// Write current stats to a reference file so next run knows what to find
fs.writeFileSync(refPath, JSON.stringify({
  _note: 'Current values in schema blocks. Used by update-schema-stats.js to know what to find-and-replace. Auto-generated — do not edit.',
  _updated: new Date().toISOString(),
  total: stats.total,
  catCount: stats.catCount,
  usCount: stats.usCount,
  usPct: stats.usPct,
  canadianPct: stats.canadianPct,
  reviewPct: stats.reviewPct,
  nonExposedPct: stats.nonExposedPct,
  exposedPct: stats.exposedPct,
  nonCanadianPct: stats.nonCanadianPct,
  caResExposedPct: stats.caResExposedPct,
}, null, 2));
console.log(`\nReference file written to ${refPath}`);
