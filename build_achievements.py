from build import page, breadcrumb_jsonld, webpage_jsonld

CONTENT = """
<section class="section" style="padding-top:56px;">
  <div class="container">
    <div class="section-head">
      <p class="eyebrow">Awards</p>
      <h2>Awards received.</h2>
    </div>
    <div class="card-list">
      <div class="card-row"><div class="crlabel">2024</div><div><h4>The Young Achiever of the Year</h4><p>National-level recognition for technology and social entrepreneurship.</p></div></div>
      <div class="card-row"><div class="crlabel">2021 · 2023 · 2024</div><div><h4>Global Youth Leadership Award</h4><p>Global Youth Parliament, Nepal.</p></div></div>
    </div>
  </div>
</section>

<section class="section">
  <div class="container">
    <div class="section-head">
      <p class="eyebrow">Recognition</p>
      <h2>Institutional and public recognition.</h2>
      <p>Recognition of work or research — distinct from a formal award or an institutional endorsement.</p>
    </div>
    <div class="card-list">
      <div class="card-row"><div class="crlabel">2024</div><div><h4>Recognised — World Food India</h4><p>Ministry of Food Processing Industries, Government of India, for the FoodBank initiative.</p></div></div>
      <div class="card-row"><div class="crlabel">2024</div><div><h4>Research featured — IndiaAI</h4><p>Research featured on IndiaAI, a Government of India AI initiative platform — a publication credit, not government employment.</p></div></div>
      <div class="card-row"><div class="crlabel">—</div><div><h4>ISRO–IIRS Geospatial &amp; Remote Sensing Training</h4><p>Completed remote-sensing and geospatial coursework through IIRS-ISRO (see Certifications below for the specific courses).</p></div></div>
    </div>
  </div>
</section>

<section class="section">
  <div class="container">
    <div class="section-head">
      <p class="eyebrow">Government &amp; Civic Engagement</p>
      <h2>Technology alongside public service.</h2>
    </div>
    <div class="card-list">
      <div class="card-row"><div class="crlabel">NHRC</div><div><p>AI &amp; human-rights policy research internship, Aug 2024.</p></div></div>
      <div class="card-row"><div class="crlabel">MHA</div><div><p>Selected for the National Cybercrime Training Centre cohort, Feb–Mar 2025 (not attended).</p></div></div>
      <div class="card-row"><div class="crlabel">PMC</div><div><p>Civic data management and urban-planning visualisation, Jun–Jul 2024.</p></div></div>
      <div class="card-row"><div class="crlabel">UNV / UNDP</div><div><p>SDG-aligned community-development contribution, Jun 2024.</p></div></div>
      <div class="card-row"><div class="crlabel">MyGov India</div><div><p>Registered Changemaker; contributor to national civic-innovation campaigns.</p></div></div>
    </div>
  </div>
</section>

<section class="section">
  <div class="container">
    <div class="section-head">
      <p class="eyebrow">Competitions</p>
      <h2>15+ national &amp; international competitions.</h2>
      <p>Selection or participation status — see individual project pages for anything that resulted in a shipped outcome.</p>
    </div>
    <div class="filter-bar" role="tablist" aria-label="Filter competitions">
      <button class="filter-btn active" data-filter="all" aria-selected="true">All</button>
      <button class="filter-btn" data-filter="space" aria-selected="false">Space</button>
      <button class="filter-btn" data-filter="gov" aria-selected="false">Government</button>
      <button class="filter-btn" data-filter="social" aria-selected="false">Social Impact</button>
      <button class="filter-btn" data-filter="software" aria-selected="false">Software</button>
    </div>
    <div class="comp-grid">
      <div class="comp-item" data-cat="space"><span class="ctag">Space</span><h4>ISRO Bharatiya Antariksha Hackathon 2024</h4></div>
      <div class="comp-item" data-cat="space"><span class="ctag">Space</span><h4>NASA International Space Apps Challenge 2024</h4></div>
      <div class="comp-item" data-cat="gov"><span class="ctag">Government</span><h4>Supreme Court of India Hackathon 2024</h4></div>
      <div class="comp-item" data-cat="software"><span class="ctag">Software</span><h4>Contract Risk Assessment Hackathon — IIT Madras</h4></div>
      <div class="comp-item" data-cat="social"><span class="ctag">Social Impact</span><h4>BIRAC National Bio-Entrepreneurship Competition, 2024 &amp; 2025</h4></div>
      <div class="comp-item" data-cat="software"><span class="ctag">Software</span><h4>Flipkart GRiD 6.0</h4></div>
      <div class="comp-item" data-cat="software"><span class="ctag">Software</span><h4>GDG Solution Challenge (Google), 2024 &amp; 2025</h4></div>
      <div class="comp-item" data-cat="gov"><span class="ctag">Government</span><h4>Code for GovTech (C4GT)</h4></div>
      <div class="comp-item" data-cat="gov"><span class="ctag">Government</span><h4>OGD India Hackathon</h4></div>
    </div>
  </div>
</section>

<section class="section" style="border-bottom:none;">
  <div class="container">
    <div class="section-head">
      <p class="eyebrow">Certifications</p>
      <h2>Documented coursework, by category.</h2>
    </div>
    <div>
      <div class="acc-item">
        <button class="acc-btn" aria-expanded="false">Geospatial · ISRO / IIRS <span class="plus">+</span></button>
        <div class="acc-panel"><div class="acc-panel-inner">Geodata Processing using Python · Remote Sensing of Soils · Exploring Earth's Moon through Chandrayaan · Integration of EO Data for Geological Applications — all IIRS-ISRO.</div></div>
      </div>
      <div class="acc-item">
        <button class="acc-btn" aria-expanded="false">Cloud &amp; Developer Ecosystem <span class="plus">+</span></button>
        <div class="acc-panel"><div class="acc-panel-inner">Google Developer Program · Google Cloud Innovator · Google Maps Platform Innovator · Google Earth Engine Developer.</div></div>
      </div>
      <div class="acc-item">
        <button class="acc-btn" aria-expanded="false">AI &amp; Entrepreneurship <span class="plus">+</span></button>
        <div class="acc-panel"><div class="acc-panel-inner">AI for India 2.0 — Guvi / IIT Madras &amp; Google · Y Combinator Startup School, Founder Track (2025).</div></div>
      </div>
      <div class="acc-item">
        <button class="acc-btn" aria-expanded="false">Other documented certifications <span class="plus">+</span></button>
        <div class="acc-panel"><div class="acc-panel-inner">20+ additional certifications across AI, Cloud, Cybercrime and Geospatial Technology. Full certificate list available on request — this figure reflects only what's independently listed in source documents (an earlier draft cited "500+," which the underlying documents don't support).</div></div>
      </div>
    </div>
  </div>
</section>
"""

trail = [("Home", "/"), ("Achievements", None)]
page("/achievements/", "Achievements | Sangram Santosh Salgar",
     "Awards, public recognition, government & civic engagement, competitions and certifications for Sangram Santosh Salgar.",
     "/achievements/", CONTENT, breadcrumb_trail=trail,
     jsonld=breadcrumb_jsonld(trail) + webpage_jsonld("/achievements/", "Achievements", "Awards, recognition and certifications."))
