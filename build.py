import os

BASE = "https://sangramsalgar.com"  # ⚠ placeholder — replace before going live (see README)
SITE_ROOT = os.path.join(os.path.dirname(os.path.abspath(__file__)), "deploy")

NAV_ITEMS = [
    ("About", "/about/"),
    ("Projects", "/projects/"),
    ("Experience", "/experience/"),
    ("Research", "/research/"),
    ("Achievements", "/achievements/"),
    ("Contact", "/contact/"),
]

def nav_html(active_path):
    links = []
    for label, href in NAV_ITEMS:
        cur = ' aria-current="page"' if href == active_path else ''
        links.append(f'<a href="{href}"{cur}>{label}</a>')
    return "\n      ".join(links)

def header(active_path):
    return f"""<a href="/" class="skip-link">Skip to content</a>
<header class="nav">
  <div class="nav-inner">
    <a href="/" class="brand"><span class="mark">SS</span> Sangram Salgar</a>
    <nav class="links" id="primaryNav" aria-label="Primary">
      {nav_html(active_path)}
    </nav>
    <div class="nav-right">
      <button class="theme-toggle" aria-label="Toggle light and dark theme">○</button>
      <a href="/resume/" class="nav-cta nav-cta-ghost">Resume</a>
      <a href="/contact/" class="nav-cta">Let's Connect</a>
    </div>
    <button class="menu-toggle" aria-expanded="false" aria-controls="primaryNav" aria-label="Open menu">Menu</button>
  </div>
</header>"""

def breadcrumbs(trail):
    parts = []
    for i, (label, href) in enumerate(trail):
        if href:
            parts.append(f'<a href="{href}">{label}</a>')
        else:
            parts.append(f'<span aria-current="page">{label}</span>')
        if i < len(trail) - 1:
            parts.append('<span class="sep">/</span>')
    return f'<nav class="breadcrumbs container" aria-label="Breadcrumb">{"".join(parts)}</nav>'

def footer():
    return f"""<footer>
  <div class="container">
    <div class="footer-grid">
      <div class="footer-brand">
        <h3>Sangram Santosh Salgar</h3>
        <p>Computer Engineer · Founder, MahaSangram · AI &amp; Social-Tech Innovator</p>
        <p style="margin-top:14px;font-style:italic;">"Building technology with purpose."</p>
      </div>
      <div class="footer-links">
        <div class="footer-col">
          <a href="/about/">About</a>
          <a href="/projects/">Projects</a>
          <a href="/experience/">Experience</a>
        </div>
        <div class="footer-col">
          <a href="/research/">Research</a>
          <a href="/achievements/">Achievements</a>
          <a href="/contact/">Contact</a>
        </div>
        <div class="footer-col">
          <a href="/resume/">Résumé</a>
          <a href="/cv/">CV</a>
          <a href="https://www.linkedin.com/in/sangramsalgar/" target="_blank" rel="noopener">Connect on LinkedIn ↗</a>
        </div>
      </div>
    </div>
    <div class="footer-bottom">
      <span>© 2026 Sangram Santosh Salgar. All rights reserved.</span>
      <span>Pune, Maharashtra, India</span>
    </div>
  </div>
</footer>
<a href="/resume/" class="float-resume" aria-label="Go to résumé">⬇ Résumé</a>
<script src="/assets/script.js"></script>"""

def page(path, title, description, active_path, content, breadcrumb_trail=None, jsonld=""):
    """path: clean URL, e.g. '/', '/about/', '/projects/agrismart/'. 404 uses '/404.html' literally."""
    canonical = BASE + path
    og_image = BASE + "/assets/og-er-sangram-salgar-founder-ai.jpg"
    crumbs = breadcrumbs(breadcrumb_trail) if breadcrumb_trail else ""
    html = f"""<!DOCTYPE html>
<html lang="en">
<head>
<meta charset="UTF-8">
<meta name="viewport" content="width=device-width, initial-scale=1.0">
<title>{title}</title>
<meta name="description" content="{description}">
<meta name="author" content="Sangram Santosh Salgar">
<link rel="canonical" href="{canonical}">
<meta property="og:type" content="website">
<meta property="og:title" content="{title}">
<meta property="og:description" content="{description}">
<meta property="og:url" content="{canonical}">
<meta property="og:site_name" content="Sangram Santosh Salgar">
<meta property="og:image" content="{og_image}">
<meta name="twitter:card" content="summary_large_image">
<meta name="twitter:title" content="{title}">
<meta name="twitter:description" content="{description}">
<meta name="twitter:image" content="{og_image}">
<link rel="icon" href="data:image/svg+xml,%3Csvg xmlns='http://www.w3.org/2000/svg' viewBox='0 0 64 64'%3E%3Crect width='64' height='64' rx='14' fill='%230B120F'/%3E%3Cpath d='M18 44 L18 22 Q18 18 24 18 L38 18 Q46 18 46 26 Q46 32 38 32 L24 32' stroke='%23E8A33D' stroke-width='4' fill='none' stroke-linecap='round'/%3E%3Cline x1='24' y1='32' x2='46' y2='46' stroke='%233FA796' stroke-width='4' stroke-linecap='round'/%3E%3C/svg%3E">
<link rel="preconnect" href="https://fonts.googleapis.com">
<link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
<link href="https://fonts.googleapis.com/css2?family=Space+Grotesk:wght@400;500;600;700&family=IBM+Plex+Sans:wght@400;500;600&family=IBM+Plex+Mono:wght@400;500&display=swap" rel="stylesheet">
<link rel="stylesheet" href="/assets/style.css">
{jsonld}
</head>
<body>
{header(active_path)}
{crumbs}
<main id="main">
{content}
</main>
{footer()}
</body>
</html>"""
    if path == "/404.html":
        full_path = os.path.join(SITE_ROOT, "404.html")
    elif path == "/":
        full_path = os.path.join(SITE_ROOT, "index.html")
    else:
        full_path = os.path.join(SITE_ROOT, path.strip("/"), "index.html")
    os.makedirs(os.path.dirname(full_path), exist_ok=True)
    with open(full_path, "w") as f:
        f.write(html)
    print("wrote", path, "->", os.path.relpath(full_path, SITE_ROOT))


PERSON_JSONLD = f"""<script type="application/ld+json">
{{
  "@context": "https://schema.org",
  "@type": "Person",
  "name": "Sangram Santosh Salgar",
  "alternateName": ["Er. Sangram Salgar", "Sangram Salgar"],
  "url": "{BASE}/",
  "image": "{BASE}/assets/og-er-sangram-salgar-founder-ai.jpg",
  "jobTitle": "Founder & CEO, Computer Engineer",
  "description": "Computer Engineer and Founder & CEO of MahaSangram Private Limited, building AI, IoT and full-stack systems for agriculture, food security, civic technology and public-interest research.",
  "worksFor": {{"@type": "Organization", "name": "MahaSangram Private Limited", "foundingDate": "2019"}},
  "alumniOf": {{"@type": "CollegeOrUniversity", "name": "Smt. Kashibai Navale College of Engineering, Savitribai Phule Pune University"}},
  "address": {{"@type": "PostalAddress", "addressLocality": "Pune", "addressRegion": "Maharashtra", "addressCountry": "IN"}},
  "sameAs": ["https://www.linkedin.com/in/sangramsalgar/"],
  "knowsAbout": ["Artificial Intelligence", "Machine Learning", "Geospatial Technology", "IoT", "Civic Technology", "AgriTech", "Software Engineering"]
}}
</script>"""

WEBSITE_JSONLD = f"""<script type="application/ld+json">
{{"@context":"https://schema.org","@type":"WebSite","name":"Sangram Santosh Salgar","url":"{BASE}/","author":{{"@type":"Person","name":"Sangram Santosh Salgar"}}}}
</script>"""

def webpage_jsonld(path, name, description):
    return f"""<script type="application/ld+json">
{{"@context":"https://schema.org","@type":"WebPage","name":"{name}","description":"{description}","url":"{BASE}{path}","isPartOf":{{"@type":"WebSite","name":"Sangram Santosh Salgar","url":"{BASE}/"}}}}
</script>"""

def breadcrumb_jsonld(trail):
    items = []
    for i, (label, href) in enumerate(trail):
        url = BASE + href if href else None
        item = f'{{"@type":"ListItem","position":{i+1},"name":"{label}"' + (f',"item":"{url}"' if url else '') + '}'
        items.append(item)
    return f"""<script type="application/ld+json">
{{"@context":"https://schema.org","@type":"BreadcrumbList","itemListElement":[{",".join(items)}]}}
</script>"""

print("helpers loaded")
