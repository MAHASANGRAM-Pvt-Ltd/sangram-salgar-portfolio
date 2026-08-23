from build import page, breadcrumb_jsonld, webpage_jsonld, BASE

PROJECTS = [
    dict(slug="agrismart", num="01", title="AgriSmart", tag="AI Crop Advisory System", flagship=True,
         oneliner="An end-to-end AI pipeline helping farmers detect crop disease, read soil health and get advisory in their own language.",
         problem="Smallholder farmers often lack timely, localised access to agronomic expertise — leading to preventable crop loss and inefficient input use.",
         solution="AgriSmart combines crop-disease detection, soil-health analysis and a multilingual voice/text advisory interface, so farmers can get usable guidance without needing to read a dashboard.",
         technology="Python and TensorFlow power the disease-detection models; Google Earth Engine supplies satellite-based remote-sensing data for field-level context; Firebase handles data sync for the farmer-facing app.",
         role="Founder — led product direction, model development and the field-facing advisory design.",
         status="Active — the flagship MahaSangram initiative.",
         recognition="Selected for BIRAC's National Bio-Entrepreneurship Programme; onboarded to IBM Cloud Startup Programme and Google Cloud for Startups.",
         stack=["Python","TensorFlow","IoT","Google Earth Engine","Firebase"]),
    dict(slug="ai-content-moderation", num="02", title="AI Content Moderation Tool", tag="NLP · Computer Vision", flagship=False,
         oneliner="A multilingual classifier for detecting harmful content in real time, with research featured via IndiaAI.",
         problem="Harmful and misleading content spreads across multilingual digital platforms faster than manual moderation can keep up with.",
         solution="A classifier combining NLP and computer vision detects harmful content in real time, with adjustable sensitivity thresholds and transparency reporting so moderation decisions stay explainable.",
         technology="Built with Python and TensorFlow, using NLP models for text and computer-vision models for image/video content.",
         role="Founder & researcher — designed the detection approach and authored the underlying research.",
         status="Research featured; tool in ongoing development.",
         recognition="Research featured via IndiaAI, a Government of India AI initiative (2024) — a publication credit, not a government employment or endorsement relationship.",
         stack=["Python","TensorFlow","NLP","Computer Vision"]),
    dict(slug="foodbank", num="03", title="FoodBank", tag="Hyperlocal Food Redistribution", flagship=False,
         oneliner="Connecting surplus food donors with nearby communities in need, using geolocation and predictive demand.",
         problem="Usable surplus food frequently goes to waste simply because donors and nearby recipients have no easy way to coordinate in time.",
         solution="FoodBank uses geolocation and AI-driven logistics with predictive demand analytics to match surplus donors to nearby need in near real time.",
         technology="Geolocation services, an AI logistics/matching layer and demand-prediction models.",
         role="Founder — product design and logistics-matching approach.",
         status="Pilot / early deployment.",
         recognition="Recognised at World Food India 2024, Ministry of Food Processing Industries, Government of India.",
         stack=["Geolocation","AI Logistics","Predictive Analytics"]),
    dict(slug="asgt", num="04", title="ASGT — Adaptive Smart Traffic System", tag="Computer Vision · IoT", flagship=False,
         oneliner="Real-time adaptive traffic signal control with emergency-vehicle priority routing.",
         problem="Fixed-timing traffic signals don't respond to real-time congestion or emergency vehicles, adding avoidable delay — including for ambulances.",
         solution="ASGT uses computer vision and IoT sensors for real-time vehicle-density detection, adapting signal timing dynamically and giving emergency vehicles priority routing.",
         technology="Python, IoT sensor integration, computer-vision models and Google Cloud Platform for the analytics dashboard.",
         role="Founder — system design and municipal-facing dashboard.",
         status="Prototype; dashboard deployed for evaluation, built in the context of India's Smart Cities Mission.",
         recognition="",
         stack=["Python","IoT","Computer Vision","GCP"]),
    dict(slug="smartvillages", num="05", title="SmartVillages", tag="Rural E-Commerce", flagship=False,
         oneliner="A digital marketplace connecting farmers and artisans directly to wider markets.",
         problem="Rural producers often depend on intermediaries that limit their market reach and margins.",
         solution="SmartVillages is a marketplace connecting 100+ farmer and artisan producers directly with wider digital markets, supporting income diversification and self-reliance.",
         technology="Full-stack marketplace architecture built for low-bandwidth, rural-first usage.",
         role="Founder — product and partnerships with local producers.",
         status="Active.",
         recognition="",
         stack=["Full-Stack","Marketplace","Rural Tech"]),
    dict(slug="breathe", num="06", title="BREATHE (AgriPrint)", tag="Climate / Carbon Tracking", flagship=False,
         oneliner="A community-level carbon-footprint tracking system, built toward a future carbon-credit exchange.",
         problem="Grassroots communities have few accessible tools to measure or act on their collective carbon footprint.",
         solution="BREATHE tracks community-level carbon footprint data as a foundation for local climate resilience, with a carbon-credit exchange planned as a next step.",
         technology="Data tracking and sustainability-focused analytics.",
         role="Founder — concept and early system design.",
         status="Early stage; carbon-credit exchange planned, not yet live.",
         recognition="",
         stack=["Sustainability","Data Tracking"]),
    dict(slug="spl-quantum", num="07", title="Sanskrit Programming Language + Quantum Computing", tag="Language Design · Quantum SDK", flagship=False,
         oneliner="An in-progress programming framework exploring Sanskrit's formal grammar as a basis for quantum-optimised algorithms.",
         problem="Most programming-language grammars weren't designed with quantum-algorithm structure or entanglement handling in mind.",
         solution="A cross-platform, procedural + object-oriented, AI/ML-integrated framework that uses Sanskrit's formal grammar as a structural basis for quantum-optimised algorithms, entanglement handling and quantum-cryptography applications.",
         technology="Python, a quantum SDK, and AI/ML tooling for language-model-assisted grammar design.",
         role="Founder / researcher — language and system design.",
         status="Research / design stage — not yet a working release.",
         recognition="",
         stack=["Python","Quantum SDK","AI/ML"]),
]

def chips(items):
    return "".join(f'<span class="chip">{c}</span>' for c in items)

flagship = PROJECTS[0]
rest = PROJECTS[1:]

rest_cards = ""
for p in rest:
    rest_cards += f"""
    <a class="project-card" href="/projects/{p['slug']}/">
      <span class="pnum">{p['num']}</span><h3>{p['title']}</h3><span class="ptag">{p['tag']}</span>
      <p>{p['oneliner']}</p>
      <div class="stack">{chips(p['stack'])}</div>
      <span class="viewlink">View case study →</span>
    </a>"""

hub_content = f"""
<section class="section" style="padding-top:56px;">
  <div class="container">
    <div class="section-head">
      <p class="eyebrow">Selected Work</p>
      <h2>Seven projects, one thread.</h2>
      <p>Each case study covers the problem, the approach, the technology, my role, and current status — kept to what's actually documented.</p>
    </div>

    <p class="eyebrow" style="margin-bottom:20px;">Flagship</p>
    <a class="project-card" href="/projects/{flagship['slug']}/" style="display:block;padding:44px;border:1px solid var(--line);margin-bottom:56px;">
      <span class="pnum">{flagship['num']} · Flagship</span>
      <h3 style="font-size:28px;margin-top:12px;">{flagship['title']}</h3>
      <span class="ptag">{flagship['tag']}</span>
      <p style="max-width:640px;">{flagship['oneliner']}</p>
      <div class="stack">{chips(flagship['stack'])}</div>
      <span class="viewlink">View full case study →</span>
    </a>

    <p class="eyebrow" style="margin-bottom:20px;">Selected Work</p>
    <div class="project-grid">{rest_cards}
    </div>
  </div>
</section>
"""
trail_hub = [("Home", "/"), ("Projects", None)]
page("/projects/", "Projects | Sangram Santosh Salgar",
     "Case studies across AgriSmart, AI Content Moderation, FoodBank, ASGT, SmartVillages, BREATHE and the Sanskrit Programming Language project.",
     "/projects/", hub_content, breadcrumb_trail=trail_hub,
     jsonld=breadcrumb_jsonld(trail_hub) + webpage_jsonld("/projects/", "Projects", "Selected work by Sangram Santosh Salgar."))

# Detail pages
for p in PROJECTS:
    others = [x for x in PROJECTS if x['slug'] != p['slug']][:3]
    related_cards = "".join(f"""
      <a class="related-card" href="/projects/{o['slug']}/" style="display:block;">
        <span class="rtag">{o['tag']}</span><h4>{o['title']}</h4>
      </a>""" for o in others)

    recognition_block = f"""
    <div class="pd-block">
      <h2>Recognition</h2>
      <p>{p['recognition']}</p>
    </div>""" if p['recognition'] else ""

    flag_badge = '<span class="pd-tag" style="color:var(--accent);">★ Flagship project</span><br>' if p.get('flagship') else ''

    content = f"""
<section class="pd-hero">
  <div class="container">
    {flag_badge}<span class="pd-tag">{p['tag']}</span>
    <h1>{p['title']}</h1>
    <p class="oneliner">{p['oneliner']}</p>
    <div class="pd-meta">
      <div><strong>Role</strong><br>{p['role']}</div>
      <div><strong>Status</strong><br>{p['status']}</div>
    </div>
  </div>
</section>
<section class="pd-body">
  <div class="container">
    <div class="pd-block">
      <h2>Problem</h2>
      <p>{p['problem']}</p>
    </div>
    <div class="pd-block">
      <h2>Solution</h2>
      <p>{p['solution']}</p>
    </div>
    <div class="pd-block">
      <h2>Technology</h2>
      <p>{p['technology']}</p>
      <div class="stack" style="margin-top:14px;">{chips(p['stack'])}</div>
    </div>
    {recognition_block}
    <div class="pd-block" style="border-top:1px solid var(--line);padding-top:20px;">
      <p style="color:var(--fg-faint);font-family:var(--mono);font-size:11.5px;">No product screenshots or architecture diagrams are shown here yet — this page will be updated with real visuals as they become available, rather than a generic stock illustration.</p>
    </div>
  </div>
</section>
<section class="related">
  <div class="container">
    <p class="eyebrow">Related Projects</p>
    <div class="related-grid">{related_cards}
    </div>
  </div>
</section>
"""
    trail = [("Home", "/"), ("Projects", "/projects/"), (p['title'], None)]
    creativework = f"""<script type="application/ld+json">
{{"@context":"https://schema.org","@type":"CreativeWork","name":"{p['title']}","description":"{p['oneliner']}","creator":{{"@type":"Person","name":"Sangram Santosh Salgar"}},"url":"{BASE}/projects/{p['slug']}/"}}
</script>"""
    page(f"/projects/{p['slug']}/",
         f"{p['title']} | Sangram Santosh Salgar",
         p['oneliner'],
         "/projects/", content, breadcrumb_trail=trail,
         jsonld=breadcrumb_jsonld(trail) + creativework)
