from build import page, breadcrumb_jsonld, webpage_jsonld

CONTENT = """
<section class="section" style="padding-top:56px;">
  <div class="container about-grid">
    <div>
      <p class="eyebrow">About</p>
      <h2 style="margin-top:14px;">Founder &amp; CEO, MahaSangram. Engineer by training.</h2>
      <div class="about-facts" style="margin-top:32px;">
        <dl>
          <dt>Education</dt>
          <dd>B.E. Computer Engineering, Smt. Kashibai Navale College of Engineering — Savitribai Phule Pune University · CGPA 8.46/10.0 · Nov 2022 – Apr 2026</dd>
          <dt>Base</dt>
          <dd>Pune, Maharashtra, India</dd>
          <dt>Current focus</dt>
          <dd>MahaSangram Pvt. Ltd. — AgriSmart, FoodBank, ASGT, SmartVillages, BREATHE</dd>
          <dt>Contact</dt>
          <dd>sangramsalgar204@gmail.com</dd>
        </dl>
      </div>
    </div>
    <div class="about-body">
      <p>I started building <strong>MahaSangram</strong> in 2019, well before finishing my engineering degree — first as an attempt to make agricultural knowledge more accessible to farming communities, and gradually into a small studio of AI, IoT and full-stack products aimed at practical, public-facing problems. MahaSangram is the entrepreneurial thread running through everything else on this site.</p>
      <p>That work now spans <strong>crop advisory and soil intelligence</strong> (AgriSmart), <strong>food redistribution</strong> (FoodBank), <strong>adaptive traffic management</strong> (ASGT), <strong>rural e-commerce</strong> (SmartVillages) and a <strong>multilingual content-safety classifier</strong> whose underlying research was featured via IndiaAI, a Government of India AI initiative.</p>
      <p>Alongside the company, I've worked inside public institutions to understand how technology actually meets policy — a research internship at the <strong>National Human Rights Commission</strong>, a civic-data role at the <strong>Pune Municipal Corporation</strong>, and a volunteering stint with <strong>UN Volunteers / UNDP</strong> on SDG-aligned community development.</p>
      <p>I'm finishing my B.E. in Computer Engineering at SPPU in 2026. Everything on this site is drawn directly from that work — what I built, what I was selected for, and what's still in progress. See the <a href="/experience/" style="color:var(--accent-2);">full experience timeline</a> or the <a href="/projects/" style="color:var(--accent-2);">project case studies</a>.</p>
    </div>
  </div>
</section>

<section class="section" style="border-bottom:none;">
  <div class="container">
    <div class="section-head">
      <p class="eyebrow">Selected Technologies</p>
      <h2>Tools behind the work — attached to real projects, not just listed.</h2>
    </div>
    <div class="skills-grid">
      <div class="skill-cat"><h4>Engineering</h4><span class="chip">Python</span><span class="chip">Java</span><span class="chip">C++</span><span class="chip">JavaScript</span><span class="chip">SQL</span><span class="chip">Kotlin</span></div>
      <div class="skill-cat"><h4>AI</h4><span class="chip">TensorFlow</span><span class="chip">Scikit-Learn</span><span class="chip">PyTorch (basics)</span><span class="chip">NLP</span><span class="chip">Computer Vision</span><span class="chip">Transformers</span></div>
      <div class="skill-cat"><h4>Cloud</h4><span class="chip">Google Cloud Platform</span><span class="chip">IBM Cloud</span><span class="chip">AWS</span><span class="chip">Firebase</span></div>
      <div class="skill-cat"><h4>Geospatial</h4><span class="chip">Google Earth Engine</span><span class="chip">NASA Remote Sensing APIs</span><span class="chip">IIRS-ISRO Platforms</span></div>
      <div class="skill-cat"><h4>IoT &amp; Systems</h4><span class="chip">Arduino</span><span class="chip">Raspberry Pi</span><span class="chip">Sensor Integration</span><span class="chip">Edge Computing</span></div>
      <div class="skill-cat"><h4>Data &amp; Tools</h4><span class="chip">MySQL</span><span class="chip">PostgreSQL</span><span class="chip">Firestore</span><span class="chip">Git / GitHub</span><span class="chip">Docker (basics)</span></div>
    </div>
    <p style="color:var(--fg-faint);font-family:var(--mono);font-size:12px;margin-top:20px;">Listed by category, not proficiency score — the <a href="/projects/" style="color:var(--accent-2);">project case studies</a> show how each is actually used.</p>
  </div>
</section>
"""

trail = [("Home", "/"), ("About", None)]
page("/about/",
     "About | Sangram Santosh Salgar",
     "Computer Engineer and Founder & CEO of MahaSangram Pvt. Ltd. — the story behind the AI, agriculture, civic and social-impact work.",
     "/about/", CONTENT, breadcrumb_trail=trail,
     jsonld=breadcrumb_jsonld(trail) + webpage_jsonld("/about/", "About Sangram Santosh Salgar", "The founder story behind MahaSangram."))
