from build import page, breadcrumb_jsonld, webpage_jsonld

CONTENT = """
<section class="section" style="padding-top:56px;border-bottom:none;">
  <div class="container">
    <div class="section-head">
      <p class="eyebrow">Research &amp; Publications</p>
      <h2>Writing that sits alongside the code.</h2>
    </div>

    <div class="pd-block" style="max-width:760px;">
      <h2 style="font-size:13px;">Featured</h2>
      <div style="border:1px solid var(--line);padding:28px;border-radius:var(--radius);background:var(--bg-card);margin-top:8px;">
        <span class="pd-tag">2024 · IndiaAI</span>
        <h3 style="font-size:22px;margin-top:10px;">AI-Powered Content Moderation for Responsible Digital Ecosystems</h3>
        <p style="color:var(--fg-dim);margin-top:12px;font-size:16px;">Featured / published through <strong>IndiaAI</strong>, a Government of India AI initiative platform — a publication credit, not a government research position or endorsement. The work underlies the <a href="/projects/ai-content-moderation/" style="color:var(--accent-2);">AI Content Moderation Tool</a>, describing a multilingual NLP + computer-vision approach to real-time harmful-content detection, with attention to transparency and adjustable sensitivity thresholds.</p>
      </div>
    </div>

    <div class="card-list" style="margin-top:44px;">
      <div class="card-row">
        <div class="crlabel">Ongoing</div>
        <div>
          <h4>Co-authored collaborative publications</h4>
          <p>Contributing chapters across 30+ self-published/co-authored collections spanning technology, youth leadership, women's rights and space exploration. Publisher and edition details available on request.</p>
        </div>
      </div>
      <div class="card-row">
        <div class="crlabel">Ongoing</div>
        <div>
          <h4>Blog &amp; commentary</h4>
          <p>Regular contributor on personal Blogspot and WordPress channels covering AI, agriculture technology, sustainability and entrepreneurship. Author: Sangram Santosh Salgar.</p>
        </div>
      </div>
    </div>
  </div>
</section>
"""

trail = [("Home", "/"), ("Research", None)]
page("/research/", "Research & Publications | Sangram Santosh Salgar",
     "Research on AI-powered content moderation featured via IndiaAI, plus co-authored collaborative publications and ongoing writing on technology and public impact.",
     "/research/", CONTENT, breadcrumb_trail=trail,
     jsonld=breadcrumb_jsonld(trail) + webpage_jsonld("/research/", "Research & Publications", "Published research and writing."))
