# Sangram Santosh Salgar — Portfolio v3

This addresses the round-2 review: clean URLs, the mis-pointed nav CTA, AgriSmart as flagship, more conservative institutional wording, split Awards/Recognition/Competitions/Certifications, WebSite/WebPage schema, accessible mobile nav, and a repo layout that doesn't expose the build scripts on the live site.

## Repo structure
```
portfolio-v3/
├── site/          ← deploy THIS folder — nothing else. Point Cloudflare Pages' "Build output directory" here.
│   ├── index.html
│   ├── about/index.html
│   ├── projects/index.html
│   ├── projects/agrismart/index.html   (+ 6 more project folders)
│   ├── experience/index.html
│   ├── research/index.html
│   ├── achievements/index.html
│   ├── resume/index.html
│   ├── cv/index.html
│   ├── contact/index.html
│   ├── 404.html
│   ├── _redirects        ← 301s from old .html URLs to the new clean ones
│   ├── robots.txt
│   ├── sitemap.xml
│   └── assets/            (style.css, script.js, OG image, résumé PDF, CV PDF)
└── generator/     ← Python build scripts. Keep in the repo for reproducible edits, but this folder is never served — it lives outside `site/`.
```

## What changed since v2 (round-2 review)

**🔴 Fixed:**
- **Clean URLs** — `/projects.html` → `/projects/`, etc., for every page, generated as `folder/index.html` so it works on any static host without extra config
- **"Let's Connect" now points to `/contact/`** — `/resume/` has its own separate CTA button
- **`_redirects`** included so any previously shared v2 `.html` links 301 to the new URLs instead of 404ing
- **AgriSmart is now the visually flagship project** — a large featured card on both the homepage and `/projects/`, with a "★ Flagship" badge on its own page; the other six sit in a "Selected Work" grid below it
- **IndiaAI wording softened** — now "featured / published through IndiaAI, a Government of India AI initiative platform," explicitly noting it's a publication credit, not a government research position or endorsement (appears on the homepage, `/research/`, `/achievements/`, and the AI Content Moderation project page)
- **"ISRO-IIRS Certified Contributor" reworded** to "ISRO–IIRS Geospatial & Remote Sensing Training," pointing to the actual course list rather than implying a formal contributor status
- **Achievements page split into five distinct, separately-headed sections**: Awards → Recognition → Government & Civic Engagement → Competitions → Certifications (previously "Awards & Recognition" was combined)
- **Mobile nav rebuilt for real accessibility** — `aria-expanded`/`aria-controls` on the toggle button, closes on Escape, closes on outside click, closes when a link is clicked, moves focus into the menu on open — replacing the old inline-style JS toggle

**🟠 Fixed:**
- **MahaSangram is now a named, central anchor** — a dedicated homepage section ("The Venture") and foregrounded in the About page's opening line and hero copy, rather than only appearing inside experience bullets
- **Homepage hero rewritten** around the Who/What/Why structure from the review, with the "Er. Sangram Salgar 🇮🇳" name treatment moved to a secondary line under a punchier H1
- **"Impact" renamed to "Selected Highlights"** with numbers reframed as milestones (2019 founded, 10+ initiatives, 30+ publications, 15+ competitions) rather than anything that could be misread as business KPIs
- **Experience entries now carry a `Type · Date · Location` metadata line** (e.g. "Entrepreneurship · Sept 2019–Present · Pune") ahead of the description, for faster recruiter scanning
- **Skills reframed as "Selected Technologies"**, grouped by category with no percentage/proficiency ratings, and cross-linked to the projects that actually use them
- Added `WebSite` schema (homepage) and `WebPage` schema (every subpage) alongside the existing `Person` and `BreadcrumbList` JSON-LD; project pages now also carry `CreativeWork` schema

**🟢 Kept as recommended:** dark theme + amber/teal palette, Space Grotesk/IBM Plex type pairing, the custom 404 line, generator-script architecture.

**🟢 Still open — genuinely needs your input, not more guessing:**
- Real project screenshots / architecture diagrams (each project page now has a one-line note saying visuals are pending, instead of a fake diagram)
- A professional photograph, if/when you want to replace the abstract signal-map graphic
- The actual domain (`sangramsalgar.com` is still a placeholder everywhere — see below)
- Whether you want a dedicated `/mahasangram` venture page beyond the homepage section — skipped for now since your source material doesn't have enough distinct venture-level content (mission, funding, team) to fill a whole page without padding

## Before deploying
1. **Buy the domain (or decide on the `*.pages.dev` URL) before submitting to Search Console.** Until then, everything under `<link rel="canonical">`, Open Graph, and `sitemap.xml` points at the placeholder `https://sangramsalgar.com`. To change it: edit `BASE` in `generator/build.py`, re-run all eight `build_*.py` scripts, and manually update the URLs in `site/robots.txt`, `site/sitemap.xml` and `site/_redirects`.
2. **Deploy only `site/`, not the repo root.** On Cloudflare Pages: set "Build output directory" to `site`. On Netlify: same, set the publish directory to `site`. On GitHub Pages: either point Pages at a `site/` subfolder (Settings → Pages → folder), or push only the contents of `site/` to the branch GitHub Pages serves from — don't publish `generator/`.
3. Submit `sitemap.xml` to Google Search Console + Bing Webmaster Tools once the real domain is live.
4. Validate JSON-LD (Person, WebSite, WebPage, BreadcrumbList, CreativeWork) in the [Rich Results Test](https://search.google.com/test/rich-results).
5. Re-test social previews (LinkedIn Post Inspector, Twitter Card Validator) once the real domain replaces the placeholder in the OG tags.
6. Run Lighthouse — target 90+ across Performance/SEO/Accessibility/Best Practices.

## Editing content
Don't hand-edit the generated `site/*/index.html` files directly if you can help it — edit the matching script in `generator/` and re-run it, or all eight scripts will drift out of sync with each other (nav, footer, and schema all come from `generator/build.py`, shared across every page).

```bash
cd generator
python3 build_home.py         # edits index.html
python3 build_projects.py     # edits projects/ hub + all 7 project pages — add an 8th project by adding one dict to PROJECTS
python3 build_achievements.py # edits achievements/index.html
# etc.
```
Then copy the regenerated files from `generator`'s output location back into `site/` (the scripts write to a `deploy/` folder next to them by default — copy `deploy/*` over `site/*`, or edit `SITE_ROOT` in `build.py` to point straight at `site/`).

## Facts still flagged for your confirmation
| Item | What the site shows | Why |
|---|---|---|
| Academic score | CGPA 8.46/10.0 | Other CV versions say "90%" / "SGPA 9.6" — used the specific, unambiguous figure |
| Certifications count | "20+ additional certifications" | One CV's summary said "500+," unsupported by its own certifications list |
| Founder's starting age | Omitted | Sources disagree (17 vs 19) — site states the founding year (2019) only |
| "International Social Impact Award 2024" | Not included | Appears once, no supporting detail |
| ISRO/IMD/OpenAI "partnerships" | Not included as partnerships | Your résumé describes these as stakeholder discussions, not formal partnerships |
| 30+ co-authored books | Included, softened | Consistent across your documents, but publisher/ISBN unverified |

## Domain suggestions
`sangramsalgar.com` · `sangramsalgar.in` · `ersangramsalgar.com` · `mahasangram.tech`
