from build import page, breadcrumb_jsonld, webpage_jsonld

def meta(role_type, dates, location):
    return f'<div class="tl-org" style="opacity:.8;">{role_type} · {dates} · {location}</div>'

CONTENT = """
<section class="section" style="padding-top:56px;border-bottom:none;">
  <div class="container">
    <div class="section-head">
      <p class="eyebrow">Experience</p>
      <h2>Where engineering has met public institutions.</h2>
      <p>Employment, internships, fellowships and programme selections — kept clearly distinct. Read top to bottom, most recent first.</p>
    </div>

    <div class="tl-year">2026</div>
    <div class="timeline">
      <div class="tl-item">
        <div class="tl-date">Apr 2026 (expected)</div>
        <h3>B.E. Computer Engineering — completion</h3>
        <div class="tl-org">Education · Savitribai Phule Pune University · Pune</div>
        <p>Wrapping up the degree alongside ongoing MahaSangram work.</p>
      </div>
    </div>

    <div class="tl-year">2025</div>
    <div class="timeline">
      <div class="tl-item">
        <div class="tl-date">Dec 2025</div>
        <h3>Agriculture Research Fellow</h3>
        <div class="tl-org">Fellowship · Sharad Pawar Inspire Fellowship</div>
        <p>Field research on sustainable agriculture and rural development practices.</p>
      </div>
      <div class="tl-item">
        <div class="tl-date">Feb — Mar 2025</div>
        <h3>Selected — National Cybercrime Training Cohort</h3>
        <div class="tl-org">Programme selection · Ministry of Home Affairs, Government of India</div>
        <p>Competitively selected for the GOI's national cybercrime training programme.</p>
        <span class="tl-note">Selected · training not attended</span>
      </div>
      <div class="tl-item">
        <div class="tl-date">Jan — Mar 2025</div>
        <h3>International Intern</h3>
        <div class="tl-org">Internship · India International Model United Nations (IMUN)</div>
        <p>Participated in international diplomacy simulations and multilateral policy dialogues on global governance issues.</p>
      </div>
    </div>

    <div class="tl-year">2024</div>
    <div class="timeline">
      <div class="tl-item">
        <div class="tl-date">Aug 2024</div>
        <h3>Research Intern</h3>
        <div class="tl-org">Internship · National Human Rights Commission (NHRC) of India · New Delhi</div>
        <p>Researched the application of AI and ML in human rights monitoring; contributed to internal policy documentation and case-study analysis.</p>
      </div>
      <div class="tl-item">
        <div class="tl-date">Jun — Jul 2024</div>
        <h3>Technical Intern — Computer Operator</h3>
        <div class="tl-org">Internship · Pune Municipal Corporation (PMC) · Pune</div>
        <p>Managed civic data pipelines and built visualisation dashboards supporting urban planning and administrative decision-making.</p>
      </div>
      <div class="tl-item">
        <div class="tl-date">Jun 2024</div>
        <h3>UN Volunteer</h3>
        <div class="tl-org">Volunteering · United Nations Volunteers (UNV) / UNDP · Remote</div>
        <p>Contributed to UNDP-led SDG community-development initiatives, supporting data collection and reporting.</p>
      </div>
      <div class="tl-item">
        <div class="tl-date">2024</div>
        <h3>Research featured — AI Content Moderation</h3>
        <div class="tl-org">Publication · IndiaAI, Government of India</div>
        <p>Research on AI-powered content moderation for responsible digital ecosystems featured on IndiaAI.</p>
      </div>
    </div>

    <div class="tl-year">2022 — 2019</div>
    <div class="timeline">
      <div class="tl-item">
        <div class="tl-date">Nov 2022</div>
        <h3>B.E. Computer Engineering — begins</h3>
        <div class="tl-org">Education · Smt. Kashibai Navale College of Engineering, SPPU · Pune</div>
        <p>Started the engineering degree while continuing to build MahaSangram.</p>
      </div>
      <div class="tl-item">
        <div class="tl-date">Sept 2019 — Present</div>
        <h3>Founder &amp; CEO</h3>
        <div class="tl-org">Entrepreneurship · MahaSangram Private Limited · Pune</div>
        <p>Leading strategy, product and R&amp;D across 10+ initiatives in AgriTech, food security, civic infrastructure and climate resilience.</p>
      </div>
    </div>
  </div>
</section>
"""

trail = [("Home", "/"), ("Experience", None)]
page("/experience/", "Experience | Sangram Santosh Salgar",
     "Founder & CEO of MahaSangram since 2019, with research and civic internships at NHRC, PMC and UN Volunteers, and a selection for the MHA National Cybercrime Training Programme.",
     "/experience/", CONTENT, breadcrumb_trail=trail,
     jsonld=breadcrumb_jsonld(trail) + webpage_jsonld("/experience/", "Experience", "Career and civic-engagement timeline."))
