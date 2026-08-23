from build import page, breadcrumb_jsonld, webpage_jsonld

# --- Resume ---
resume_content = """
<section class="section" style="padding-top:56px;border-bottom:none;">
  <div class="container">
    <div class="section-head">
      <p class="eyebrow">Résumé — Technology / Industry</p>
      <h2>For technology, startups &amp; engineering opportunities.</h2>
      <p>A one-page, technology-industry-focused résumé — summary, experience, projects and skills.</p>
    </div>
    <div class="hero-ctas">
      <a href="/assets/Sangram_Salgar_Resume.pdf" class="btn btn-primary" download>Download PDF Résumé</a>
      <a href="/cv/" class="btn btn-outline">Looking for the academic / public-service CV? →</a>
    </div>

    <div class="about-facts" style="margin-top:44px;max-width:760px;">
      <dl>
        <dt>Summary</dt>
        <dd>Computer Engineer (SPPU, 2026) and Founder &amp; CEO with 6 years building AI, full-stack and IoT-driven products. Shipped 10+ initiatives across AgriTech, food security, smart traffic and NLP content safety. Research featured via IndiaAI, Government of India.</dd>
        <dt>Education</dt>
        <dd>B.E. Computer Engineering, Smt. Kashibai Navale College of Engineering (SPPU) — CGPA 8.46/10.0, Nov 2022–Apr 2026</dd>
        <dt>Core stack</dt>
        <dd>Python, TensorFlow, Scikit-Learn, NLP, Computer Vision, GCP, IBM Cloud, AWS, Firebase, Google Earth Engine, IoT (Arduino / Raspberry Pi)</dd>
        <dt>Full detail</dt>
        <dd>See <a href="/projects/" style="color:var(--accent-2);">Projects</a>, <a href="/experience/" style="color:var(--accent-2);">Experience</a> and <a href="/achievements/" style="color:var(--accent-2);">Achievements</a> for the complete picture, or download the PDF above.</dd>
      </dl>
    </div>
  </div>
</section>
"""
trail_r = [("Home", "/"), ("Résumé", None)]
page("/resume/", "Résumé | Sangram Santosh Salgar",
     "Technology-industry résumé for Sangram Santosh Salgar — Computer Engineer, Founder & CEO of MahaSangram Pvt. Ltd. For technology, startups and engineering opportunities.",
     "/resume/", resume_content, breadcrumb_trail=trail_r,
     jsonld=breadcrumb_jsonld(trail_r) + webpage_jsonld("/resume/", "Résumé", "Downloadable technology résumé."))

# --- CV ---
cv_content = """
<section class="section" style="padding-top:56px;border-bottom:none;">
  <div class="container">
    <div class="section-head">
      <p class="eyebrow">CV — Academic / Government / Public Service</p>
      <h2>For research, fellowships &amp; public-sector opportunities.</h2>
      <p>A longer-form CV emphasising education, government/civic internships, research and public-service exposure.</p>
    </div>
    <div class="hero-ctas">
      <a href="/assets/Sangram_Salgar_CV.pdf" class="btn btn-primary" download>Download PDF CV</a>
      <a href="/resume/" class="btn btn-outline">Looking for the technology résumé? →</a>
    </div>

    <div class="about-facts" style="margin-top:44px;max-width:760px;">
      <dl>
        <dt>Professional summary</dt>
        <dd>Computer Engineer, entrepreneur and public-service-oriented innovator with experience across AI, civic technology, agriculture and social impact. Founder &amp; CEO of MahaSangram Pvt. Ltd. (est. 2019). Interned with NHRC, Pune Municipal Corporation and UN Volunteers (UNDP). Selected for the MHA National Cybercrime Training Programme (not attended). Research featured via IndiaAI. Recipient of The Young Achiever of the Year 2024.</dd>
        <dt>Government &amp; civic exposure</dt>
        <dd>NHRC India (Aug 2024) · MHA National Cybercrime Training Centre — selected, not attended (Feb–Mar 2025) · UN Volunteers / UNDP (Jun 2024) · Pune Municipal Corporation (Jun–Jul 2024) · MyGov India — registered Changemaker</dd>
        <dt>Full detail</dt>
        <dd>See <a href="/experience/" style="color:var(--accent-2);">Experience</a> and <a href="/achievements/" style="color:var(--accent-2);">Achievements</a> for the complete timeline, or download the PDF above.</dd>
      </dl>
    </div>
  </div>
</section>
"""
trail_c = [("Home", "/"), ("CV", None)]
page("/cv/", "CV | Sangram Santosh Salgar",
     "Academic and public-service CV for Sangram Santosh Salgar, covering government internships, research and civic engagement.",
     "/cv/", cv_content, breadcrumb_trail=trail_c,
     jsonld=breadcrumb_jsonld(trail_c) + webpage_jsonld("/cv/", "CV", "Downloadable academic and public-service CV."))

# --- Contact ---
contact_content = """
<section class="section" style="padding-top:56px;border-bottom:none;">
  <div class="container contact-wrap">
    <div>
      <p class="eyebrow">Contact</p>
      <h2 style="margin-top:14px;">Let's build something meaningful.</h2>
      <p class="contact-note" style="margin-top:20px;">For technology, research, collaboration or speaking opportunities — reach out directly. Open to conversations with technology teams, founders, researchers, mentors and public-sector collaborators working on AI, agriculture, civic technology or social impact.</p>
    </div>
    <div class="contact-links">
      <a href="mailto:sangramsalgar204@gmail.com">Email <span class="arrow">→</span></a>
      <a href="https://www.linkedin.com/in/sangramsalgar/" target="_blank" rel="noopener">Connect on LinkedIn ↗</a>
      <a href="/resume/">Download Résumé <span class="arrow">→</span></a>
      <a href="/cv/">Download CV <span class="arrow">→</span></a>
    </div>
  </div>
</section>
"""
trail_ct = [("Home", "/"), ("Contact", None)]
page("/contact/", "Contact | Sangram Santosh Salgar",
     "Get in touch with Sangram Santosh Salgar for technology collaborations, research, speaking opportunities or hiring.",
     "/contact/", contact_content, breadcrumb_trail=trail_ct,
     jsonld=breadcrumb_jsonld(trail_ct) + webpage_jsonld("/contact/", "Contact", "Get in touch."))

# --- 404 ---
error_content = """
<section class="error-page">
  <div class="container">
    <div class="big">404</div>
    <p>You've reached an unexplored coordinate.</p>
    <a href="/" class="btn btn-primary">Return to base →</a>
  </div>
</section>
"""
page("/404.html", "Page Not Found | Sangram Santosh Salgar",
     "This page doesn't exist. Return to the homepage.",
     "", error_content)
