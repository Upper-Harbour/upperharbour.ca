# Upper Harbour — Design System Reference

For pasting into Claude Design or any other design tool when building new artifacts (slides, brochures, social cards, ads, etc.) for upperharbour.ca.

Source of truth: `/Users/josh/upperharbour.ca/assets/site.css`.

---

## Colors

### Backgrounds (dark mode native)
| Token | Hex | Use |
|---|---|---|
| `--bg` | `#06090E` | Page background (deep midnight) |
| `--surface` | `#0C1219` | Cards, secondary panels |
| `--surface-2` | `#111A24` | Tertiary panels, hover states |
| `#0e1620` | `#0e1620` | Section alternating background (slightly lighter than --bg) |

### Accents
| Token | Hex | Use |
|---|---|---|
| `--teal` | `#3CB8B0` | Primary brand color. CTAs, highlights, accents, statistics, links |
| `--teal-deep` | `#2A8A84` | Hover state on teal, subtle teal emphasis |
| `--teal-dim` | `rgba(60,184,176,0.08)` | Tinted backgrounds on teal-accented cards |
| `--gold` | `#C9A84C` | Editorial italic emphasis, premium/founder elements (rare, accent only) |
| `--gold-dim` | `rgba(201,168,76,0.08)` | Tinted backgrounds for gold-accent cards |
| `--red` | `#E06050` | Warning, risk callouts (foreign jurisdiction, CLOUD Act exposure) |
| `--red-dim` | `rgba(224,96,80,0.08)` | Risk-card tinted backgrounds |

### Text
| Token | Hex | Use |
|---|---|---|
| `--ice` | `#EAF0F4` | Primary text, headings, white-equivalent (do not use pure white) |
| `--slate` | `#8A9DB0` | Body copy, secondary text, descriptions |
| `--muted` | `#566778` | Tertiary text, labels, eyebrows (when not teal), footer text |

### Borders
| Token | Value | Use |
|---|---|---|
| `--border` | `rgba(234,240,244,0.06)` | Hairline dividers, subtle separators |
| `--border-md` | `rgba(234,240,244,0.1)` | Standard borders on cards, inputs, framed elements |
| `rgba(60,184,176,0.18)` | (teal at 18%) | Teal-accented card borders |
| `rgba(60,184,176,0.3)` | (teal at 30%) | Stronger teal-emphasized borders |

---

## Typography

### Font families
| Token | Stack | Use |
|---|---|---|
| `--display` | `'Newsreader', Georgia, serif` | Display headings, hero H1, section titles, editorial pull-quotes |
| `--body` | `'DM Sans', -apple-system, 'Segoe UI', Helvetica, Arial, sans-serif` | All body copy, UI, navigation, buttons, cards |
| `--mono` | `'JetBrains Mono', monospace` | Eyebrows, labels, stats, technical / code-adjacent elements |

### Google Fonts loading (required in `<head>` of every page)
```html
<link rel="preconnect" href="https://fonts.googleapis.com" />
<link rel="preconnect" href="https://fonts.gstatic.com" crossorigin />
<link href="https://fonts.googleapis.com/css2?family=Newsreader:ital,opsz,wght@0,6..72,300;0,6..72,400;0,6..72,600;0,6..72,700;1,6..72,400&family=DM+Sans:wght@300;400;500;600;700;800&family=JetBrains+Mono:wght@400;600&display=swap" rel="stylesheet" />
```

### Typography scale

**Display / hero (Newsreader serif)**
- Hero H1: `clamp(42px, 6vw, 72px)` — weight 700-900 — letter-spacing -1px
- Big section titles: 40-48px — weight 700 — letter-spacing -0.4 to -0.6px
- Mid section titles: 32-36px — weight 700 — letter-spacing -0.3px
- Editorial pull-quote: 32-34px — italic — weight 400-500 — letter-spacing -0.3 to -0.5px

**Body (DM Sans)**
- Section subhead / lead: 17-18px — weight 400 — line-height 1.6-1.75
- Body copy: 15px — weight 400 — line-height 1.6-1.75
- Small body / card body: 13-14px — weight 400-500 — line-height 1.5-1.65
- UI / nav links: 13px — weight 500
- CTA buttons: 13-15px — weight 700-800 — letter-spacing 0.01em

**Mono (JetBrains Mono) — for eyebrows / labels**
- Eyebrows: 10-11px — weight 600-700 — letter-spacing 0.15-0.2em — UPPERCASE
- Section labels: 10px — weight 700 — letter-spacing 0.2em — UPPERCASE
- Stats / numerical accents: 10-12px — weight 600 — letter-spacing 0.1-0.15em

### Italic usage
- Newsreader italic in `--gold` for editorial emphasis on display headings (sparingly — pull-quotes, the word *sovereignty* on /research)
- Newsreader italic in `--teal` for em-emphasis within display headings on dark backgrounds

---

## Layout

- Container max-width: **1120px** (research/long-form pages: 1100-1120px)
- Hero/section padding: **80-100px vertical**, 20-52px horizontal
- Mobile: padding tightens to **48-64px vertical**, 20px horizontal
- Card padding: **24-32px** depending on density
- Section gaps: **48px** between section title block and content
- Grid gaps: **16-24px** between cards
- Nav height: **66px** (fixed, position:fixed top:0 left:0 right:0)
- Mobile breakpoint: **900px** (some places 768px / 540px / 480px)

---

## UI Components

### Cards
```
background: rgba(255,255,255,0.02)
border: 1px solid rgba(255,255,255,0.08)
border-radius: 6px
padding: 28-32px
hover: border-color: var(--teal); background: rgba(60,184,176,0.03)
```

### Teal-accent card (highlighted/featured)
```
background: rgba(60,184,176,0.04)
border: 1px solid rgba(60,184,176,0.18-0.3)
border-radius: 6px
```

### Buttons

**Primary (teal pill, dark text)**
```
background: var(--teal) → hover #47cec5
color: var(--bg) (midnight)
padding: 16px 32px
border-radius: 4-5px
font-weight: 700-800
box-shadow: 0 0 16px rgba(60,184,176,0.25), 0 1px 3px rgba(0,0,0,0.3)
font-size: 13-15px
```

**Secondary (ghost / outline teal)**
```
background: transparent
color: var(--teal)
border: 1px solid var(--teal)
padding: 16px 32px
border-radius: 4px
hover: background rgba(60,184,176,0.08)
```

### Navigation pattern
- Fixed nav, 66px tall, full-width
- Background: `rgba(10,16,24,0.92)` with `backdrop-filter: blur(14px)`
- Border-bottom: `1px solid var(--border)`
- Logo (28px) + wordmark on left
- Links + CTA pill on right
- Mobile: hamburger only at ≤540px

### Section dividers
- 1px borders using `--border` or `--border-md`
- Subtle radial gradients in teal (5-8% opacity) for hero backgrounds
- Grid pattern overlay: linear-gradient lines at 72px intervals, opacity ~0.018

---

## Logo

The Upper Harbour mark is a stylized "U" with a gradient teal interior:

```svg
<svg width="28" height="28" viewBox="0 0 80 80" xmlns="http://www.w3.org/2000/svg">
  <defs>
    <linearGradient id="hg" x1="0" y1="0" x2="0" y2="1">
      <stop offset="0%" stop-color="#1C4F5E"/>
      <stop offset="100%" stop-color="#32A8A4"/>
    </linearGradient>
  </defs>
  <path d="M 0,0 L 80,0 L 80,54 Q 80,80 54,80 L 26,80 Q 0,80 0,54 Z M 20,0 L 60,0 L 60,48 Q 60,64 40,64 Q 20,64 20,48 Z" fill="#EAF0F4" fill-rule="evenodd"/>
  <path d="M 20,17 L 33,28 L 60,10 L 60,48 Q 60,64 40,64 Q 20,64 20,48 Z" fill="url(#hg)"/>
</svg>
```

Wordmark uses DM Sans:
- "Upper" — weight 400, color `var(--slate)`
- "Harbour" — weight 800, color `var(--ice)`, letter-spacing -0.5px, margin-left 4px

---

## Voice & Tone Notes (Brief)

- Direct, declarative, expert. Privacy officers and compliance leads are the audience.
- Acronyms (PIPEDA, FIPPA, Law 25, etc.) used naturally without being explained — audience knows them.
- Avoid: hedges ("might", "could help"), patronizing explanations, marketing jargon, US-centric framing.
- Prefer: specific numbers, concrete deliverables, statutory references, the contrast between "what generic AI does" vs. "what Upper Harbour does."
- Italic gold/teal accents for emphasis in display headings — used sparingly.

---

## Background patterns / textures

Subtle radial gradients for hero/section depth:
```css
background:
  radial-gradient(ellipse 65% 60% at 55% 35%, rgba(60,184,176,0.07) 0%, transparent 65%),
  radial-gradient(ellipse 50% 70% at 10% 75%, rgba(201,168,76,0.04) 0%, transparent 55%),
  var(--bg);
```

Grid overlay (very subtle):
```css
background-image:
  linear-gradient(rgba(234,240,244,0.018) 1px, transparent 1px),
  linear-gradient(90deg, rgba(234,240,244,0.018) 1px, transparent 1px);
background-size: 72px 72px;
```

---

## Quick reference for design tools

Plug these into Claude Design / Figma / Sketch / etc.:

**Color palette (hex):**
```
Background:    #06090E
Surface:       #0C1219
Surface 2:     #111A24
Teal:          #3CB8B0
Teal Deep:     #2A8A84
Gold:          #C9A84C
Red:           #E06050
Ice (text):    #EAF0F4
Slate (body):  #8A9DB0
Muted (subdued): #566778
```

**Fonts:**
- Display: **Newsreader** (serif) — for big headlines and editorial pull-quotes
- Body: **DM Sans** (sans) — for everything else
- Mono: **JetBrains Mono** — for eyebrows, labels, technical accents

All three from Google Fonts.

**Brand mode:** dark-only (deep midnight background, no light variant).
