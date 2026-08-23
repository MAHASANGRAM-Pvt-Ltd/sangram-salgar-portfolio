from build import page, PERSON_JSONLD, WEBSITE_JSONLD

SIGNAL_SVG = """<div class="signal-wrap" aria-hidden="true">
  <svg viewBox="0 0 420 460" xmlns="http://www.w3.org/2000/svg">
    <defs><radialGradient id="g1" cx="50%" cy="40%" r="70%">
      <stop offset="0%" stop-color="#3FA796" stop-opacity="0.18"/>
      <stop offset="100%" stop-color="#3FA796" stop-opacity="0"/>
    </radialGradient></defs>
    <rect width="420" height="460" fill="url(#g1)"/>
    <g stroke="rgba(243,241,231,0.16)" stroke-width="1" fill="none">
      <path d="M20 380 Q120 300 210 340 T400 300"/>
      <path d="M10 300 Q140 220 220 260 T410 220"/>
      <path d="M0 220 Q150 150 230 180 T420 140"/>
    </g>
    <g fill="#E8A33D">
      <circle cx="70" cy="330" r="4"/><circle cx="150" cy="280" r="3"/><circle cx="230" cy="300" r="5"/>
      <circle cx="310" cy="250" r="3"/><circle cx="360" cy="210" r="4"/><circle cx="120" cy="190" r="3"/><circle cx="270" cy="150" r="4"/>
    </g>
    <g stroke="#3FA796" stroke-width="1.2" opacity="0.6">
      <line x1="70" y1="330" x2="150" y2="280"/><line x1="150" y1="280" x2="230" y2="300"/>
      <line x1="230" y1="300" x2="310" y2="250"/><line x1="310" y1="250" x2="360" y2="210"/>
      <line x1="150" y1="280" x2="120" y2="190"/><line x1="120" y1="190" x2="270" y2="150"/>
    </g>
    <text x="20" y="40" font-family="IBM Plex Mono, monospace" font-size="11" fill="#6B7A72">AI · AGRICULTURE · CIVIC · CLIMATE · PEOPLE</text>
  </svg>
  <p class="signal-caption">— technology → impact network, across MahaSangram's initiatives</p>
</div>"""

CONTENT = f"""
<section class="hero" id="home">
  <div class="container hero-grid">
    <div>
      <p class="eyebrow">Computer Engineer · Founder · AI Innovator</p>
      <h1>Engineering technology<br>for real-world impact.</h1>
      <p class="role">Er. Sangram Santosh Salgar <span class="flag">🇮🇳</span></p>
      <p class="desc">I build AI, software and technology systems across agriculture, civic infrastructure and social impact — as Founder &amp; CEO of <strong>MahaSangram</strong>, turning engineering ideas into things people actually use.</p>
      <div class="hero-ctas">
        <a href="/projects/" class="btn btn-primary">Explore My Work →</a>
        <a href="/resume/" class="btn btn-outline">View Résumé →</a>
        <a href="https://www.linkedin.com/in/sangramsalgar/" class="btn btn-outline" target="_blank" rel="noopener">LinkedIn ↗</a>
      </div>
      <div class="hero-meta">
        <div><strong>Founded</strong> MahaSangram Pvt. Ltd., 2019</div>
        <div><strong>Research</strong> featured via IndiaAI, 2024</div>
        <div><strong>Recognition</strong> Young Achiever of the Year 2024</div>
      </div>
    </div>
    {SIGNAL_SVG}
  </div>
</section>

<section class="currently" aria-label="Currently">
  <div class="container currently-grid">
    <div class="currently-item"><div class="clabel">Building</div><div class="cval">MahaSangram &amp; its technology initiatives</div></div>
    <div class="currently-item"><div class="clabel">Exploring</div><div class="cval">AI · AgriTech · CivicTech · Geospatial Systems</div></div>
    <div class="currently-item"><div class="clabel">Research</div><div class="cval">AI &amp; responsible content moderation</div></div>
    <div class="currently-item"><div class="clabel">Based</div><div class="cval">Pune, India 🇮🇳</div></div>
  </div>
</section>

<section class="impact" aria-label="Selected highlights">
  <div class="container">
    <p class="eyebrow" style="margin-bottom:14px;">Selected Highlights</p>
    <div class="impact-grid">
      <div class="impact-item"><div class="num">2019</div><div class="label">MahaSangram founded</div></div>
      <div class="impact-item"><div class="num">10+</div><div class="label">technology initiatives launched</div></div>
      <div class="impact-item"><div class="num">30+</div><div class="label">co-authored books &amp; publications</div></div>
      <div class="impact-item"><div class="num">15+</div><div class="label">competitions &amp; challenges entered</div></div>
    </div>
  </div>
</section>

<section class="section" aria-label="MahaSangram">
  <div class="container about-grid">
    <div>
      <p class="eyebrow">The Venture</p>
      <h2 style="margin-top:14px;">MahaSangram — the thread behind this work.</h2>
    </div>
    <div class="about-body">
      <p>Everything on this site — AgriSmart, FoodBank, ASGT, SmartVillages, BREATHE and the AI Content Moderation research — is built under <strong>MahaSangram Private Limited</strong>, the company I've run as Founder &amp; CEO since 2019. It's the entrepreneurial anchor connecting AI, agriculture, civic systems and social impact into one body of work rather than a list of unrelated side-projects.</p>
      <a href="/about/" class="btn btn-outline" style="margin-top:8px;">More about the founder story →</a>
    </div>
  </div>
</section>

<section class="section">
  <div class="container">
    <div class="section-head">
      <p class="eyebrow">What I Build</p>
      <h2>Six areas, one thread: technology that reaches people.</h2>
    </div>
    <div class="skills-grid">
      <div class="skill-cat"><h4>01 · Intelligent Systems</h4><p style="color:var(--fg-dim);font-size:14.5px;">ML pipelines, classifiers and advisory engines built for real deployment.</p></div>
      <div class="skill-cat"><h4>02 · AI &amp; Responsible Moderation</h4><p style="color:var(--fg-dim);font-size:14.5px;">NLP + computer vision for safer digital spaces — research featured via IndiaAI.</p></div>
      <div class="skill-cat"><h4>03 · AgriTech &amp; Rural Technology</h4><p style="color:var(--fg-dim);font-size:14.5px;">Crop advisory, soil intelligence and rural e-commerce for farming communities.</p></div>
      <div class="skill-cat"><h4>04 · Civic &amp; Smart-City Technology</h4><p style="color:var(--fg-dim);font-size:14.5px;">Adaptive traffic systems and municipal data dashboards.</p></div>
      <div class="skill-cat"><h4>05 · Geospatial Systems</h4><p style="color:var(--fg-dim);font-size:14.5px;">Google Earth Engine and remote-sensing data for on-ground decisions.</p></div>
      <div class="skill-cat"><h4>06 · Technology for Social Impact</h4><p style="color:var(--fg-dim);font-size:14.5px;">Food redistribution and community carbon tracking.</p></div>
    </div>
  </div>
</section>

<section class="section" id="projects-preview">
  <div class="container">
    <div class="section-head">
      <p class="eyebrow">Flagship Project</p>
      <h2>AgriSmart — AI, agriculture and geospatial data, together.</h2>
    </div>
    <a class="project-card" href="/projects/agrismart/" style="display:block;padding:44px;border:1px solid var(--line);margin-bottom:1px;">
      <span class="pnum">01 · Flagship</span>
      <h3 style="font-size:28px;margin-top:12px;">AgriSmart</h3>
      <span class="ptag">AI Crop Advisory System</span>
      <p style="max-width:600px;">Crop-disease detection, soil-health analysis and multilingual advisory for farmers, integrating Google Earth Engine satellite data — selected for BIRAC's National Bio-Entrepreneurship Programme and onboarded to IBM Cloud Startup Programme and Google Cloud for Startups.</p>
      <div class="stack"><span class="chip">Python</span><span class="chip">TensorFlow</span><span class="chip">IoT</span><span class="chip">Google Earth Engine</span><span class="chip">Firebase</span></div>
      <span class="viewlink">View full case study →</span>
    </a>

    <p class="eyebrow" style="margin:48px 0 24px;">Selected Work</p>
    <div class="project-grid">
      <a class="project-card" href="/projects/ai-content-moderation/">
        <span class="pnum">02</span><h3>AI Content Moderation Tool</h3><span class="ptag">NLP · Computer Vision</span>
        <p>Multilingual harmful-content classifier — research featured via IndiaAI, Government of India, 2024.</p>
        <span class="viewlink">View case study →</span>
      </a>
      <a class="project-card" href="/projects/asgt/">
        <span class="pnum">03</span><h3>ASGT</h3><span class="ptag">AI + IoT · Smart Cities</span>
        <p>Real-time adaptive traffic signal control with emergency-vehicle priority routing.</p>
        <span class="viewlink">View case study →</span>
      </a>
      <a class="project-card" href="/projects/foodbank/">
        <span class="pnum">04</span><h3>FoodBank</h3><span class="ptag">Food Security · Social Technology</span>
        <p>Hyperlocal food redistribution connecting surplus donors with communities in need.</p>
        <span class="viewlink">View case study →</span>
      </a>
    </div>
    <div style="margin-top:32px;"><a href="/projects/" class="btn btn-outline">See all 7 projects →</a></div>
  </div>
</section>

<section class="section" style="border-bottom:none;">
  <div class="container contact-wrap">
    <div>
      <p class="eyebrow">Let's Connect</p>
      <h2 style="margin-top:14px;">Building something worth building?</h2>
      <p class="contact-note" style="margin-top:18px;">Open to conversations with technology teams, founders, researchers, mentors and public-sector collaborators.</p>
    </div>
    <div class="contact-links">
      <a href="mailto:sangramsalgar204@gmail.com">Email <span class="arrow">→</span></a>
      <a href="https://www.linkedin.com/in/sangramsalgar/" target="_blank" rel="noopener">Connect on LinkedIn ↗</a>
      <a href="/resume/">Résumé &amp; CV <span class="arrow">→</span></a>
    </div>
  </div>
</section>
"""

page("/",
     "Sangram Santosh Salgar | Computer Engineer, Founder & AI Innovator",
     "Er. Sangram Salgar — Computer Engineer (SPPU) and Founder & CEO of MahaSangram Pvt. Ltd. Building AI, IoT and full-stack systems for agriculture, food security, civic technology and public-interest research from Pune, India.",
     "/", CONTENT, jsonld=PERSON_JSONLD + WEBSITE_JSONLD)
