import math, os, html as H
OUT = os.environ.get('OUT', '/home/claude/site2/out')
os.makedirs(OUT + '/assets', exist_ok=True)
e = H.escape

NAV = [('index.html', 'Home'), ('about.html', 'About'), ('books.html', 'Books'), ('research.html', 'Research'),
       ('legal.html', 'Legal'), ('credentials.html', 'Credentials'), ('ventures.html', 'Ventures'), ('contact.html', 'Contact')]
ARROW = '<svg aria-hidden="true" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"><path d="M5 12h14"/><path d="M13 6l6 6-6 6"/></svg>'
OUT_ARROW = '<svg aria-hidden="true" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"><path d="M7 17L17 7"/><path d="M8 7h9v9"/></svg>'
LI = 'https://www.linkedin.com/in/subhadeep-aditya-080970145/'
RG = 'https://www.researchgate.net/profile/Subhadeep-Aditya'
GH = 'https://github.com/Subhadeep998'
BOOKS = {'hc': 'https://www.amazon.in/dp/B0HD9SY43K', 'varah': 'https://www.amazon.in/dp/B0FL3S14H6', 'memory': 'https://www.amazon.in/dp/B0G4KL9H5B'}


def layout(fname, title, desc, body):
    items = ''.join(
        f'<li><a href="{h}"{" aria-current=\"page\"" if h == fname else ""}>{t}</a></li>' for h, t in NAV)
    foot = ''.join(f'<a href="{h}">{t}</a>' for h, t in NAV)
    return f'''<!doctype html>
<html lang="en">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width, initial-scale=1">
<title>{e(title)}</title>
<meta name="description" content="{e(desc)}">
<meta property="og:title" content="{e(title)}">
<meta property="og:description" content="{e(desc)}">
<meta property="og:type" content="website">
<meta property="og:image" content="https://www.subhadeepaditya.in/assets/og.png">
<meta name="theme-color" content="#0D0F12">
<script>try{{var t=localStorage.getItem("theme");if(t!=="light"&&t!=="dark")t=(window.matchMedia&&matchMedia("(prefers-color-scheme: light)").matches)?"light":"dark";document.documentElement.setAttribute("data-theme",t);}}catch(e){{}}</script>
<link rel="icon" href="assets/favicon.png">
<link rel="apple-touch-icon" href="assets/favicon.png">
<link rel="canonical" href="https://www.subhadeepaditya.in/{"" if fname=="index.html" else fname}">{"<base href=\"/\">" if fname=="404.html" else ""}
<link rel="preconnect" href="https://fonts.googleapis.com">
<link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
<link href="https://fonts.googleapis.com/css2?family=Space+Grotesk:wght@400;500;600;700&family=Instrument+Serif:ital@0;1&family=JetBrains+Mono:wght@400;500&family=Cinzel:wght@600;800&display=swap" rel="stylesheet">
<link rel="stylesheet" href="assets/style.css">
</head>
<body>
<a class="skip" href="#main">Skip to content</a>
<header class="site-head">
<div class="wrap" style="position:relative">
<a class="brand" href="index.html"><img class="logo-d" src="assets/logo-dark.png" alt="SAditya logo" width="62" height="50"><img class="logo-l" src="assets/logo-light.png" alt="SAditya logo" width="62" height="50"><span><b>Subhadeep Aditya</b><small>tech.health.law</small></span></a>
<nav aria-label="Main"><ul class="menu" id="menu">{items}</ul></nav>
<div class="head-ctrls">
<button class="theme-btn" type="button" aria-label="Switch to light mode" title="Switch to light mode"><svg class="i-sun" aria-hidden="true" width="20" height="20" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round"><circle cx="12" cy="12" r="4.5"/><path d="M12 2v2.5M12 19.5V22M2 12h2.5M19.5 12H22M4.9 4.9l1.8 1.8M17.3 17.3l1.8 1.8M4.9 19.1l1.8-1.8M17.3 6.7l1.8-1.8"/></svg><svg class="i-moon" aria-hidden="true" width="20" height="20" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"><path d="M20.5 14.5A8.5 8.5 0 0 1 9.5 3.5a8.5 8.5 0 1 0 11 11z"/></svg><span class="theme-label">Light</span></button>
<button class="menu-btn" type="button" aria-expanded="false" aria-controls="menu" aria-label="Open menu"><svg aria-hidden="true" width="22" height="22" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round"><path d="M4 7h16M4 12h16M4 17h16"/></svg></button>
</div>
</div>
</header>
<main id="main">
{body}
</main>
<footer class="site-foot">
<div class="logo"><img class="logo-d" src="assets/logo-dark.png" alt="SAditya — tech.health.law"><img class="logo-l" src="assets/logo-light.png" alt="SAditya — tech.health.law"></div>
<div aria-hidden="true" class="big outline">Subhadeep Aditya</div>
<div class="wrap foot-grid">
<nav aria-label="Footer">{foot}</nav>
<nav aria-label="More"><a href="chobighor.html">ChobiGhor gallery</a></nav>
<nav aria-label="Profiles"><a href="{LI}">LinkedIn</a><a href="{RG}">ResearchGate</a><a href="{GH}">GitHub</a><a href="mailto:info@subhadeepaditya.in">info@subhadeepaditya.in</a></nav>
</div>
<div class="wrap foot-small"><span>© <span id="year">2026</span> Subhadeep Aditya · Kolkata, India</span><span>Views on this site are personal and not legal advice.</span></div>
</footer>
<script src="assets/main.js"></script>
</body>
</html>
'''


def page_hero(crumb, eyebrow, title_html, lede, extra=''):
    return f'''<div class="page-hero dots"><div class="wrap">
<p class="crumbs"><a href="index.html">Home</a> / {crumb}</p>
<p class="eyebrow">{eyebrow}</p>
<h1 class="h-page">{title_html}</h1>
<p class="lede">{lede}</p>
{extra}
</div></div>'''


def sec_head(eyebrow, title_html, side=''):
    s = f'<p>{side}</p>' if side else ''
    return f'<div class="sec-head"><div><p class="eyebrow">{eyebrow}</p><h2 class="h-sec">{title_html}</h2></div>{s}</div>'


# ---------------- data ----------------
TOPICS = ['Cancer Genomics', 'Precision Medicine', 'Artificial Intelligence', 'Healthcare Systems', 'Intellectual Property', 'Technology Regulation']

JOBS = [
    ('Ongoing', 'LAW', 'LL.B. (three-year programme)', 'Techno India University, Kolkata',
     'Studying the law that will govern biology, data and AI.',
     ['Semester I: criminal law, law of contract, jurisprudence, Hindu family law and constitutional law',
      'Focus areas: healthcare law, intellectual property and AI governance',
      'Member, American Bar Association (2026)']),
    ('11/2024 — 03/2025', 'DATA', 'Data Specialist', 'GHX India Pvt Ltd, Hyderabad',
     'Medical-surgical device and supply data; product data operations and product information management.',
     ['Managed large-scale medical supply databases for accuracy, structure and integrity',
      'Trend analysis and competitor mapping for surgical and diagnostic equipment',
      'Client-facing intelligence reports supporting product decisions and market positioning']),
    ('06/2024 — 10/2024', 'RESEARCH', 'Healthcare Analyst', 'Vatrix Healthcare Data India Pvt Ltd, Hyderabad',
     'Market and competitor research for healthcare clients.',
     ['Research using Factiva, ECRI and Sigma',
      'Authored whitepapers and reports with SEO and keyword strategy',
      'Data-driven storytelling and operational improvements in cross-functional teams']),
    ('03/2022 — 05/2024', 'INTELLIGENCE', 'Associate Healthcare Analyst', 'GlobalData PLC, Hyderabad',
     'Secondary research and SKU intelligence across medical devices and therapies.',
     ['Trackers for neuromodulation devices, diagnostic catheters, ligation devices, peripheral nerve repair and human growth hormone',
      'Cut turnaround time by 20% through workflow optimisation and automation',
      'Improved regulatory tracking for product databases; mentored new analysts']),
    ('2022', 'SCIENCE', 'M.Sc. Biotechnology', 'Amity Institute of Biotechnology, Amity University Kolkata',
     'Dissertation on Replication Factor C-like complexes and genome stability in yeast.', []),
    ('2020', 'SCIENCE', 'B.Sc. (Hons.) Biotechnology', 'Adamas University, Kolkata',
     'Dissertation on targeting quorum sensing in Vibrio cholerae. Chancellor’s Scholarship (2018).', []),
]

TRACKERS = [('Ligation Devices SKU Tracker', 'Medtronic PLC'), ('Peripheral Nerve Repair Tracker', 'Nephron'),
            ('Neuromodulation Devices Tracker', 'Wells Fargo & Nephron Research'), ('Diagnostic Catheters Tracker', 'Bloomberg'),
            ('Human Growth Hormone Tracker', 'Market intelligence')]

TOOLS = ['Excel', 'Power Query', 'Power BI', 'Tableau', 'Python', 'SAP S/4HANA (MM)', 'Asana', 'Miro', 'SharePoint', 'Factiva', 'ECRI', 'Item360', 'Claude', 'Generative AI']

PUBS = [
    ('Mar 2026', 'The Kidney as a Master Regulator of Blood Pressure and Cardiac Function: A Comprehensive Review', 'International Journal of Science and Research (IJSR)', 'https://www.ijsr.net/getabstract.php?paperid=SR26303231817',
     'Narrative review',
     ['Background: the kidneys sit at the centre of cardiovascular homeostasis through fluid and electrolyte regulation, hormonal signalling and sympathetic modulation; renal dysfunction is among the strongest independent predictors of hypertension and adverse cardiac outcomes.',
      'Methods: a synthesis of original research, systematic reviews and meta-analyses published 2000–2024 in PubMed, MEDLINE and Cochrane.',
      'Findings: the kidney regulates blood pressure through sodium handling, the renin–angiotensin–aldosterone system (RAAS), tubuloglomerular feedback and renal sympathetic innervation. Cardiorenal syndrome describes the two-way damage between heart and kidney, mediated by angiotensin II, aldosterone, erythropoietin, FGF-23 and natriuretic peptides.',
      'Conclusion: integrated strategies targeting RAAS, sympathetic activity and sodium balance offer cardiovascular and renoprotective benefits for hypertension, heart failure and chronic kidney disease.']),
    ('Oct 2025', 'Redefining Alzheimer’s Treatment in 2025: New Drug Breakthroughs and Next-Generation Diagnostics', 'Academia · Figshare (poster)', 'https://figshare.com/articles/poster/Redefining_Alzheimer_s_Treatment_in_2025_New_Drug_Breakthroughs_and_Next-Generation_Diagnostics/30340270',
     'Poster',
     ['How 2025 changed Alzheimer’s disease care: blood-based biomarker tests such as PrecivityAD2 and Elecsys pTau217 now detect Alzheimer’s pathology with accuracy rivalling PET scans.',
      'Earlier, cheaper diagnosis identifies patients for early intervention — the window where new disease-modifying therapies are most effective.']),
    ('Aug 2025', 'The Varah Files: Dashavatara Reimagined', 'Amazon Kindle', BOOKS['varah'], 'Novel',
     ['A mythic techno-thriller fusing India’s ten avatars with espionage, biotechnology and cyber warfare.']),
    ('Aug 2021', 'A Comparative Study on COVID-19 Coronavirus Variants: Alpha, Beta, Gamma, Delta', 'IJRASET', RG, 'Study',
     ['A comparison of the major SARS-CoV-2 variants of concern.']),
]

PROJECTS = [
    ('Oct 2026 — Present', 'ONGOING', True, 'OncoGenome: Cancer Genomics Research', 'NextLeap Advisory',
     'A scientific research project exploring cancer-associated genomic alterations, molecular biomarkers and emerging applications of precision oncology through literature analysis.'),
    ('May 2021 — Jul 2021', 'M.SC. PROJECT', False, 'Role of Replication Factor C-Like Complexes (RLCs) in Maintaining Genome Stability', 'Amity University Kolkata',
     'Lessons learnt from budding yeast and fission yeast on how RFC-like complexes protect the genome.'),
    ('Jul 2019 — Jul 2020', 'B.SC. PROJECT', False, 'Targeting Quorum Sensing in Vibrio cholerae', 'Adamas University',
     'Investigating bacterial quorum sensing as a target against the cholera pathogen.'),
]

HONORS = [('MEMBER', 'Oct 2026', 'American Bar Association', 'Associated with Techno India University'),
          ('MEMBER', 'Feb 2026', 'World Society for Virology', 'WSV'),
          ('CONTRIBUTING MEMBER', '2024', 'Global Outreach — American Society for Microbiology', 'ASM'),
          ('AFFILIATE MEMBER', 'Sep 2020', 'Microbiology Society, UK', 'Associated with Amity University Kolkata'),
          ('SCHOLARSHIP', 'Oct 2018', 'Chancellor’s Scholarship', 'Adamas University'),
          ('AWARD', 'Oct 2017', 'Infinity Merit Award', 'Infinity Educare')]

CREDS = [
    ('Law & Policy', 'Fundamentals of Medical Laws in India', 'Manupatra Academy', 'Oct 2026'),
    ('Law & Policy', 'AI, Justice and Rule of Law', 'Faculty of Law, University of Oxford', 'Sep 2026'),
    ('AI', 'Claude Academy: AI Fluency — Framework & Foundations', 'Anthropic', 'Sep 2026'),
    ('AI', 'Claude Academy: Claude Code in Action', 'Anthropic', 'Sep 2026'),
    ('AI', 'Agents and Workflows', 'OpenAI Academy', 'Sep 2026'),
    ('AI', 'Large Language Models (LLMs) Concepts', 'DataCamp', 'Nov 2025'),
    ('AI', 'Generative AI Foundations', 'upGrad', 'Sep 2025'),
    ('AI', 'Introduction to Machine Learning on AWS', 'Amazon Web Services', 'May 2023'),
    ('Data & Business', 'SAP MM Module — SAP S/4HANA Enterprise Package', 'EME Academy', 'Aug 2026'),
    ('Data & Business', 'Internal Audit Job Simulation', 'Goldman Sachs · Forage', 'Jul 2025'),
    ('Data & Business', 'McKinsey.org Forward Program', 'McKinsey & Company', 'Jul 2025'),
    ('Data & Business', 'Data Analytics Job Simulation', 'Deloitte Australia · Forage', 'Jun 2025'),
    ('Data & Business', 'Healthcare Supply Chain 101', 'GHX', 'Mar 2025'),
    ('Data & Business', 'Introduction to Business Intelligence', 'Infosys Springboard', 'Apr 2024'),
    ('Data & Business', 'Fundamentals of Data Analysis in Excel', 'Corporate Finance Institute', 'Apr 2024'),
    ('Data & Business', 'Excel Modeling Tips and Tricks', 'LinkedIn Learning', 'Jan 2024'),
    ('Data & Business', 'Python Foundations for Data Analysis & BI', 'Udemy', 'Apr 2023'),
    ('Data & Business', 'Foundations: Data, Data, Everywhere', 'Google', 'Apr 2023'),
    ('Project & Quality', 'Six Sigma Green Belt (CSSGB)', 'IIBA', 'Sep 2026'),
    ('Project & Quality', 'Six Sigma White Belt', 'Council for Six Sigma Certification', 'Dec 2024'),
    ('Project & Quality', 'Workflow Specialist', 'Asana', 'Nov 2024'),
    ('Project & Quality', 'Cert Prep: PMI Agile Certified Practitioner (PMI-ACP)', 'LinkedIn Learning', 'Sep 2024'),
    ('Project & Quality', 'Google Project Management Professional Certificate', 'Google', 'May 2023'),
    ('Project & Quality', 'Miro Essentials', 'Miro', 'Feb 2022'),
    ('Life Sciences', 'Understanding Cancer Metastasis', 'Johns Hopkins University', 'Jun 2021'),
    ('Life Sciences', 'Introduction to Bioinformatics', 'OmicsLogic', 'Oct 2020'),
    ('Life Sciences', 'Virus Replication Centers during Murine Polyomavirus Infection', 'LabRoots BioConference Live', 'Oct 2020'),
    ('Life Sciences', 'The Art and Science of Haematology Morphology', 'LabRoots BioConference Live', 'Oct 2020'),
    ('Life Sciences', 'Introduction to Indoor Air Quality', 'HKUST', 'Jul 2020'),
    ('Life Sciences', 'Emerging Respiratory Viruses, incl. COVID-19', 'World Health Organization', 'Apr 2020'),
    ('Life Sciences', 'Infection Prevention and Control for Novel Coronavirus', 'World Health Organization', 'Apr 2020'),
    ('Life Sciences', 'Human Health and Climate Change', 'UNITAR', 'Apr 2020'),
    ('Life Sciences', 'Genomics: Decoding the Universal Language of Life', 'University of Illinois Urbana-Champaign', 'Coursera'),
    ('Life Sciences', 'Impact of Microbes on Environment and Society', 'Microbiology Society', 'Apr 2018'),
]

EMAILS = [('GENERAL', 'info@subhadeepaditya.in', 'Anything at all — start here.'),
          ('RESEARCH', 'research@subhadeepaditya.in', 'Collaborations, papers, OncoGenome.'),
          ('SAY HELLO', 'hello@subhadeepaditya.in', 'Books, readers, ChobiGhor, a friendly note.'),
          ('LEGAL', 'legal@subhadeepaditya.in', 'Internships, legal research, writing on law.')]


# ---------------- shared pieces ----------------
def book_cover(k):
    if k == 'hc':
        return '''<div class="book b1"><div class="ring" aria-hidden="true"></div>
<span style="font-family:var(--mono);font-size:10px;letter-spacing:2px;color:var(--accent);position:relative">VOLUME I</span>
<div style="position:relative;display:flex;flex-direction:column;gap:10px"><span style="font-size:31px;font-weight:700;line-height:.95;letter-spacing:-1px">Healthcare Consulting</span><span style="font-size:12px;line-height:1.35;color:var(--soft)">Foundations, Frameworks &amp; Industry Insights</span></div>
<span style="font-size:11px;letter-spacing:2px;color:var(--soft);position:relative">SUBHADEEP ADITYA</span></div>'''
    if k == 'varah':
        return '''<div class="book b2"><span style="font-size:10px;letter-spacing:3px;position:relative">DASHAVATARA REIMAGINED</span>
<div class="sun" aria-hidden="true"><i></i></div>
<div style="display:flex;flex-direction:column;gap:6px;position:relative"><span style="font-size:14px;letter-spacing:4px">THE</span><span style="font-size:34px;font-weight:800;line-height:.95;letter-spacing:1px">VARAH FILES</span></div>
<span style="font-size:10px;letter-spacing:3px;position:relative">SUBHADEEP ADITYA</span></div>'''
    dots = ''.join(f'<i style="opacity:{1 - (i / 24) * 0.9:.2f}"></i>' for i in range(25))
    return f'''<div class="book b3"><div class="fd" aria-hidden="true">{dots}</div>
<div style="display:flex;flex-direction:column;margin-top:100px;position:relative;font-family:var(--serif);font-size:46px;line-height:.92"><span>When</span><span style="opacity:.8">Memory</span><span style="opacity:.6;font-style:italic">Fades</span></div>
<span style="font-size:11px;letter-spacing:2px;position:relative">SUBHADEEP ADITYA</span></div>'''


def helix():
    out = []
    for i in range(22):
        p = i * 0.5; s = math.sin(p); c = math.cos(p); y = 12 + i * 22
        ax = 160 + 120 * s; bx = 160 - 120 * s; hot = i % 4 == 1
        ad = 9 + 4 * c; bd = 9 - 4 * c
        col = 'var(--accent)' if hot else 'var(--line-2)'
        out.append(f'<i style="left:{min(ax, bx):.1f}px;top:{y - 1 if hot else y}px;width:{max(2, abs(ax - bx)):.1f}px;height:{4 if hot else 2}px;background:{col};border-radius:2px"></i>')
        out.append(f'<i style="left:{ax - ad / 2:.1f}px;top:{y + 1 - ad / 2:.1f}px;width:{ad:.1f}px;height:{ad:.1f}px;border-radius:50%;background:var(--paper);opacity:{0.45 + 0.5 * (c + 1) / 2:.2f}"></i>')
        out.append(f'<i style="left:{bx - bd / 2:.1f}px;top:{y + 1 - bd / 2:.1f}px;width:{bd:.1f}px;height:{bd:.1f}px;border-radius:50%;background:var(--accent);opacity:{0.45 + 0.5 * (1 - c) / 2:.2f}"></i>')
    return f'''<div class="helix-box" aria-hidden="true"><div class="helix"><div class="h">{"".join(out)}</div>
<div class="tag" style="right:-10px;top:90px">GENOME</div><div class="tag" style="left:-14px;top:250px">DATA</div><div class="tag" style="right:6px;top:420px">LAW</div>
<div class="badge"><svg width="132" height="132" viewBox="0 0 132 132"><defs><path id="bc" d="M66,66 m-48,0 a48,48 0 1,1 96,0 a48,48 0 1,1 -96,0"/></defs><text style="font-family:var(--mono);font-size:9.5px;font-weight:600;fill:#0D0F12"><textPath href="#bc" textLength="300" lengthAdjust="spacing">AUTHOR · ANALYST · RESEARCHER · LAW · </textPath></text></svg><span>SA</span></div>
</div></div>'''


def marquee():
    t1 = ''.join(f'<span>{t}</span>' for t in TOPICS * 2)
    t2 = ''.join(f'<span>{t}</span>' for t in ['Author', 'Analyst', 'Researcher', 'Consultant', 'Law student', 'Founder'] * 4)
    return f'<div class="marquee"><div class="track">{t1}</div><div class="track rev" aria-hidden="true">{t2}</div></div>'


def cta(title_html='Let’s build something <span class="it red">worth regulating.</span>'):
    mails = ''.join(f'<a class="mail" href="mailto:{a}"><span class="kicker">{l}</span><b>{a}</b><p>{d}</p></a>' for l, a, d in EMAILS)
    return f'''<section><div class="wrap"><div class="big-cta dots">
<div style="display:flex;flex-direction:column;gap:16px"><p class="eyebrow">Get in touch</p><h2 class="h-page" style="font-size:clamp(40px,6.2vw,92px)">{title_html}</h2></div>
<div class="grid g4">{mails}</div>
<div class="btns"><a class="btn btn-ghost" href="{LI}">LinkedIn {OUT_ARROW}</a><a class="btn btn-ghost" href="{RG}">ResearchGate {OUT_ARROW}</a><a class="btn btn-ghost" href="{GH}">GitHub {OUT_ARROW}</a></div>
</div></div></section>'''


def stats():
    return f'''<div class="stats"><div><b>3</b><span>books on Amazon Kindle</span></div><div><b>4</b><span>research publications</span></div><div><b>3+</b><span>years in healthcare intelligence</span></div><div><b>{len(CREDS)}</b><span>certifications, from Oxford Law to WHO</span></div></div>'''



# ---------------- ESSAYS ----------------
ESSAY_META = [
    ('The Ayodhya Verdict (2019)', 'ayodhya-verdict', 'Constitutional law'),
    ('Decriminalisation of Adultery', 'decriminalisation-of-adultery', 'Constitutional law'),
    ('Recognition of Digital Privacy in India', 'digital-privacy-india', 'Privacy & technology'),
    ('The Supreme Court\'s Contemporary Constitutional Jurisprudence', 'supreme-court-progressive-judgments', 'Constitutional law'),
    ('Justice Beyond Judgments', 'ipr-justice-beyond-judgments', 'Intellectual property'),
    ('The Sanctity of the Robes', 'legal-advertising-india', 'Legal profession'),
]
H2S = {'The Statutory Framework: Rule 36', 'The Jurisprudential Rationale: Why the Embargo?', 'The 2008 Amendment: A Cautious Relaxation', 'Penalties for Contravention'}
def load_essays():
    raw = [l.strip() for l in open('/home/claude/site2/essays.txt', encoding='utf-8').read().split('\n')]
    lines = [l for l in raw if l]
    starts = []
    for i, l in enumerate(lines):
        for k, (prefix, slug, cat) in enumerate(ESSAY_META):
            if l.startswith(prefix) and len(l) < 160 and not any(st[1] == k for st in starts):
                starts.append((i, k))
    starts.sort()
    essays = []
    for n, (i, k) in enumerate(starts):
        end = starts[n + 1][0] if n + 1 < len(starts) else len(lines)
        title = lines[i]
        body = lines[i + 1:end]
        blocks = []; j = 0
        while j < len(body):
            l = body[j]
            if l in H2S:
                blocks.append(('h2', l)); j += 1; continue
            if l.endswith(':') and j + 1 < len(body):
                blocks.append(('p', l)); j += 1; items = []
                while j < len(body) and body[j] not in H2S and (len(body[j]) < 120 or body[j].startswith('Removal from the State Roll')):
                    items.append(body[j]); j += 1
                blocks.append(('ul', items)); continue
            if l.endswith('Joshi v. Union of India'):
                l += '.'
            blocks.append(('p', l)); j += 1
        words = sum(len((b[1] if isinstance(b[1], str) else ' '.join(b[1])).split()) for b in blocks)
        first = next(b[1] for b in blocks if b[0] == 'p')
        ex = ' '.join(first.split()[:34]).rstrip(',.;:') + '…'
        prefix, slug, cat = ESSAY_META[k]
        essays.append(dict(title=title, slug=slug, cat=cat, blocks=blocks, mins=max(1, round(words / 200)), excerpt=ex))
    return essays
ESSAYS = load_essays()
assert len(ESSAYS) == 6, [x['title'] for x in ESSAYS]

def inline(t):
    t = e(t)
    if ':' in t[:48] and not t.startswith(('The ', 'A ', 'In ', 'This ')):
        lead, rest = t.split(':', 1)
        return f'<b>{lead}:</b>{rest}'
    return t

def render_blocks(blocks):
    out = []
    for kind, v in blocks:
        if kind == 'h2': out.append(f'<h2>{e(v)}</h2>')
        elif kind == 'ul': out.append('<ul>' + ''.join(f'<li>{inline(x)}</li>' for x in v) + '</ul>')
        else: out.append(f'<p>{inline(v)}</p>')
    return '\n'.join(out)

pages = {}

# ---------------- HOME ----------------
lens = ''.join(f'<button type="button" class="toggle" data-lens="{k}" aria-pressed="{"true" if k == "scientist" else "false"}">{v}</button>'
               for k, v in [('scientist', 'Scientist'), ('analyst', 'Analyst'), ('author', 'Author'), ('legal', 'Legal mind')])
strands = [('i.', 'SCIENCE', 'The Scientist', 'M.Sc. and B.Sc. (Hons.) in Biotechnology, with research on genome stability and bacterial quorum sensing.', 'research.html', 'Research'),
           ('ii.', 'DATA', 'The Analyst', '3+ years in healthcare intelligence at GlobalData, Vatrix Healthcare and GHX.', 'about.html', 'Experience'),
           ('iii.', 'STORIES', 'The Author', 'Three books spanning healthcare consulting, mythic fiction and the science of Alzheimer’s.', 'books.html', 'Books'),
           ('iv.', 'LAW', 'The Legal Mind', 'LL.B. at Techno India University — healthcare law, IP and AI governance.', 'legal.html', 'Legal analysis')]
strand_html = ''.join(f'<a class="card" href="{h}"><div style="display:flex;justify-content:space-between;align-items:center"><span class="num">{n}</span><span class="kicker">{t}</span></div><h3 class="h-card">{ti}</h3><p>{d}</p><span class="foot">{lk} →</span></a>' for n, t, ti, d, h, lk in strands)
home_books = ''.join(f'<a class="card flat" href="books.html#{k}" style="align-items:center;gap:20px"><div class="shelf" style="height:330px;width:100%;transform:scale(.82)">{book_cover(k)}</div><b style="font-size:19px;text-align:center;line-height:1.25">{t}</b></a>'
                     for k, t in [('hc', 'Healthcare Consulting, Vol. I'), ('varah', 'The Varah Files'), ('memory', 'When Memory Fades')])
pages['index.html'] = ('Subhadeep Aditya — Where genomes meet governance',
  'Subhadeep Aditya: biotechnologist, healthcare data analyst, author, researcher and LL.B. student in Kolkata. tech.health.law',
  f'''<div class="hero dots"><div class="wrap">
<div class="copy">
<div class="now"><span class="blink"></span>Now: LL.B. student · ABA member · open to law-firm internships</div>
<p class="it" style="font-size:clamp(24px,2.4vw,32px);color:var(--body)">Hi, I’m Subhadeep Aditya — <span style="font-family:var(--mono);font-style:normal;font-size:.6em;letter-spacing:1px;color:var(--accent)">tech.health.law</span></p>
<h1 class="display">Where genomes <span class="it red">meet</span> <span class="outline">governance.</span></h1>
<div style="display:flex;flex-direction:column;gap:14px"><p class="kicker">View me as</p><div class="chips" role="group" aria-label="Choose a lens">{lens}</div>
<p id="lensText" class="lede" aria-live="polite" style="min-height:70px">Trained in biotechnology and drawn to cancer genomics and precision medicine — curious about what our genes can tell medicine next.</p></div>
<div class="btns"><a class="btn btn-red" href="books.html">Explore my books {ARROW}</a><a class="btn btn-ghost" href="legal.html">Read legal analysis</a></div>
</div>
{helix()}
</div></div>
{marquee()}
<section><div class="wrap">
{sec_head('01 / Who I am', 'Four strands, <span class="it">one</span> helix.', 'Biotechnology postgraduate, healthcare data analyst, consultant, author and independent researcher — now studying law to work where science, technology and regulation collide.')}
<div class="grid g4">{strand_html}</div>
<div style="margin-top:20px">{stats()}</div>
</div></section>
<section><div class="wrap">
{sec_head('02 / The bookshelf', 'Three books. <span class="it">Three</span> worlds.', 'A practitioner’s handbook, a mythic techno-thriller and a journey through Alzheimer’s disease.')}
<div class="grid g3">{home_books}</div>
</div></section>
<section><div class="wrap">
{sec_head('03 / Latest research', 'Questions I keep <span class="it">returning</span> to.')}
<div class="rows">{''.join(f'<a class="row" href="research.html"><span class="d">{d}</span><span class="t"><b>{e(t)}</b></span><span class="v">{e(v)}</span></a>' for d, t, v, u, k, a in PUBS[:2])}
<a class="row" href="research.html#projects"><span class="d">Ongoing</span><span class="t"><b>OncoGenome: Cancer Genomics Research</b></span><span class="v">NextLeap Advisory</span></a></div>
<div class="btns" style="margin-top:28px"><a class="btn btn-ghost" href="research.html">All research {ARROW}</a></div>
</div></section>
<section><div class="wrap"><div class="split" style="align-items:center">
<div class="main" style="display:flex;flex-direction:column;gap:20px"><p class="eyebrow">04 / Legal analysis &amp; opinions</p><h2 class="h-sec">A scientist’s eye on <span class="it red">the law.</span></h2>
<p class="lede">Essays on the Constitution, privacy, intellectual property and the legal profession — written from the bench of a biotech lab and the desk of a law student.</p>
<div class="btns"><a class="btn btn-red" href="legal.html">Read all {len(ESSAYS)} essays {ARROW}</a></div></div>
<div class="side" style="flex:1 1 440px"><div class="rows">{''.join(f'<a class="row" href="{x["slug"]}.html" style="padding:20px 0"><span class="t"><span class="kicker" style="color:var(--accent)">{e(x["cat"])} · {x["mins"]} min</span><b style="font-size:20px">{e(x["title"])}</b></span></a>' for x in ESSAYS[:4])}</div></div></div>
</div></div></section>
<section><div class="wrap">
{sec_head('05 / ChobiGhor Studios', 'Kolkata, one <span class="it">frame</span> at a time.', 'Heritage photography — lanes, trams, old houses and everyday life.')}
<div class="strip">{''.join(f'<a class="strip-ph" href="chobighor.html"><img src="assets/chobighor/{x}-sm.jpg" alt="ChobiGhor photograph" loading="lazy"></a>' for x in ['inside-the-tram','red-stairs','checkered-corridor','ma-kali'])}</div>
<div class="btns" style="margin-top:24px"><a class="btn btn-ghost" href="chobighor.html">Open the gallery {ARROW}</a></div>
</div></section>
{cta()}''')

# ---------------- ABOUT ----------------
jobs_html = ''.join(f'''<li><div class="when"><span>{w}</span><span class="pill" style="align-self:flex-start">{tg}</span></div>
<div class="what"><h3>{e(r)}</h3><p class="org">{e(o)}</p><p class="muted">{e(d)}</p>{("<ul>" + "".join(f"<li>{e(b)}</li>" for b in bl) + "</ul>") if bl else ""}</div></li>''' for w, tg, r, o, d, bl in JOBS)
pages['about.html'] = ('About — Subhadeep Aditya', 'Background, experience, education and toolkit of Subhadeep Aditya — biotechnologist, healthcare data analyst, author and law student.',
  page_hero('About', 'About', 'Science, data, stories <span class="it red">&amp;</span> law.',
            'I’m Subhadeep Aditya — a biotechnology postgraduate, healthcare data analyst, consultant, author and independent researcher from Kolkata, now studying law.') + f'''
<section><div class="wrap"><div class="split">
<div class="main prose"><p class="eyebrow" style="margin-bottom:20px">The short version</p>
<p>I trained as a biotechnologist, researching genome stability in yeast and quorum sensing in <i>Vibrio cholerae</i>. I then spent three-plus years in healthcare intelligence — at GlobalData, Vatrix Healthcare and GHX — turning medical-device and market data into clear, decision-ready insight.</p>
<p>Along the way I started writing: a practitioner’s handbook on healthcare consulting, a mythic techno-thriller set in modern India, and a book on Alzheimer’s disease. I founded NextLeap Advisory, an educational consulting platform, and ChobiGhor Studios, which explores Kolkata’s heritage through photography and art.</p>
<p>Today I’m pursuing an LL.B. at Techno India University, because the hardest questions in genomics, health data and AI are increasingly legal ones. My focus is healthcare law, intellectual property and AI governance — and I’m open to law-firm internships.</p></div>
<div class="side"><div class="card"><p class="kicker">At a glance</p>
<p><b style="color:var(--paper)">Based in</b><br>Kolkata, India</p><p><b style="color:var(--paper)">Studying</b><br>LL.B., Techno India University</p><p><b style="color:var(--paper)">Education</b><br>M.Sc. &amp; B.Sc. (Hons.) Biotechnology</p><p><b style="color:var(--paper)">Experience</b><br>3+ years, healthcare intelligence</p><p><b style="color:var(--paper)">Memberships</b><br>ABA · WSV · ASM · Microbiology Society</p>
<a class="btn btn-red" href="contact.html" style="align-self:flex-start;margin-top:8px">Get in touch</a></div></div>
</div></div></section>
<section><div class="wrap">{sec_head('Experience &amp; education', 'The sequence <span class="outline">so far.</span>')}<ol class="timeline">{jobs_html}</ol></div></section>
<section><div class="wrap">{sec_head('Healthcare intelligence', 'Trackers I’ve built.', 'Market-intelligence trackers delivered for clients and research teams.')}
<div class="grid g3">{''.join(f'<div class="card"><span class="kicker">TRACKER</span><h3 class="h-card">{e(t)}</h3><span class="foot">{e(c)}</span></div>' for t, c in TRACKERS)}</div></div></section>
<section><div class="wrap">{sec_head('Toolkit', 'Instruments of the trade.')}<div class="chips">{''.join(f'<span class="chip">{e(t)}</span>' for t in TOOLS)}</div>
<div class="grid g6" style="margin-top:36px">{''.join(f'<div class="card flat" style="min-height:130px;justify-content:space-between"><span class="kicker" style="color:var(--accent)">0{i + 1}</span><b style="font-size:20px;line-height:1.2">{t}</b></div>' for i, t in enumerate(TOPICS))}</div></div></section>
{cta()}''')

# ---------------- BOOKS ----------------
bk = [('hc', 'NON-FICTION · PRACTITIONER HANDBOOK', 'Healthcare Consulting', 'Foundations, Frameworks &amp; Industry Insights — The Complete Practitioner Handbook, Volume I',
       ['A practitioner’s guide to healthcare consulting, drawing on years of work in healthcare intelligence, market research and medical-device data.',
        'It brings together the foundations of the field, the frameworks consultants use, and insights into how the healthcare industry actually works.'],
       ['Volume I', 'Healthcare', 'Consulting', 'Kindle eBook']),
      ('varah', 'FICTION · MYTHIC TECHNO-THRILLER', 'The Varah Files', 'Dashavatara Reimagined — A Mythic Techno-Thriller Across Modern India',
       ['In a world where data is more sacred than scripture, a single data breach at the Port of Kolkata spirals into a national crisis that threatens India’s digital backbone — from land records and pharmaceutical databases to classified defence blueprints.',
        'Arjun Sen, a reluctant RAW operative haunted by personal loss, is pulled into a shadow war where the ancient avatars appear as modern archetypes. From the depths of Matsya to the final reckoning of Kalki, every chapter mirrors a stage of the myth — through political subterfuge, cyber sabotage, neural poisons and bio-surveillance gone rogue.',
        'Part thriller, part prophecy: a call for digital dharma in an age of controlled chaos.'],
       ['Published Aug 2025', 'Dashavatara', 'Espionage', 'Biotech', 'Kindle eBook']),
      ('memory', 'NON-FICTION · SCIENCE &amp; HEALTH', 'When Memory Fades', 'The Silent Epidemic of Alzheimer’s Disease — A Comprehensive Journey Through Science, Suffering, and Hope',
       ['A journey through Alzheimer’s disease: the science of how memory fails, the human cost for patients and families, and the hope offered by new research.',
        'It connects with my research on next-generation Alzheimer’s diagnostics and treatment.'],
       ['Alzheimer’s', 'Neuroscience', 'Public health', 'Kindle eBook'])]
book_rows = ''.join(f'''<article class="book-row" id="{k}"><div class="shelf">{book_cover(k)}</div>
<div class="info"><span class="kicker">{tag}</span><h2 class="h-sec" style="font-size:clamp(34px,4vw,56px)">{t}</h2><p style="font-size:19px;color:var(--muted)">{sub}</p>
<div class="prose">{''.join(f"<p>{p}</p>" for p in ps)}</div>
<div class="facts">{''.join(f"<span>{f}</span>" for f in facts)}</div>
<div class="btns"><a class="btn btn-red" href="{BOOKS[k]}">Read on Kindle {OUT_ARROW}</a></div></div></article>''' for k, tag, t, sub, ps, facts in bk)
pages['books.html'] = ('Books — Subhadeep Aditya', 'Three books by Subhadeep Aditya: Healthcare Consulting (Vol. I), The Varah Files, and When Memory Fades. Available on Amazon Kindle.',
  page_hero('Books', 'The bookshelf', 'Three books. <span class="it red">Three</span> worlds.', 'A practitioner’s handbook, a mythic techno-thriller and a journey through Alzheimer’s disease — all on Amazon Kindle.') +
  f'<section class="light" style="margin-top:48px;padding:40px 0 80px"><div class="wrap">{book_rows}</div></section>' + cta('Read one? <span class="it red">Tell me.</span>'))

# ---------------- RESEARCH ----------------
pub_html = ''.join(f'''<article class="card" style="gap:16px"><div style="display:flex;flex-wrap:wrap;gap:10px;justify-content:space-between;align-items:center"><span class="pill" style="color:var(--accent);border-color:var(--accent)">{d} · {k}</span><span class="kicker">{e(v)}</span></div>
<h3 class="h-card" style="font-size:clamp(22px,2.4vw,30px)">{e(t)}</h3><div class="prose" style="font-size:16px">{''.join(f"<p>{e(x)}</p>" for x in a)}</div>
<a class="btn btn-ghost" style="align-self:flex-start" href="{u}">Read {OUT_ARROW}</a></article>''' for d, t, v, u, k, a in PUBS)
proj_html = ''.join(f'''<article class="card"><div style="display:flex;flex-wrap:wrap;gap:8px;justify-content:space-between;align-items:center"><span class="kicker">{w}</span><span class="pill" style="{"background:var(--accent);color:var(--ink);border-color:var(--accent)" if on else ""}">{s}</span></div>
<h3 class="h-card">{e(t)}</h3><p>{e(d)}</p><span class="foot">{e(o)}</span></article>''' for w, s, on, t, o, d in PROJECTS)
pages['research.html'] = ('Research — Subhadeep Aditya', 'Publications and research projects by Subhadeep Aditya: cardiorenal physiology, Alzheimer’s diagnostics, COVID-19 variants, cancer genomics (OncoGenome).',
  page_hero('Research', 'Research', 'Questions I keep <span class="it red">returning</span> to.', 'Cancer genomics, precision medicine, healthcare systems, AI, intellectual property and technology regulation.',
            f'<div class="btns"><a class="btn btn-red" href="{RG}">Papers on ResearchGate {OUT_ARROW}</a></div>') + f'''
<section><div class="wrap"><div class="grid g6">{''.join(f'<div class="card flat" style="min-height:130px;justify-content:space-between"><span class="kicker" style="color:var(--accent)">0{i + 1}</span><b style="font-size:20px;line-height:1.2">{t}</b></div>' for i, t in enumerate(TOPICS))}</div></div></section>
<section><div class="wrap">{sec_head('Publications', 'On the record.', f'{len(PUBS)} publications across nephrology, neurology, virology and fiction.')}<div class="grid" style="gap:20px">{pub_html}</div></div></section>
<section id="projects"><div class="wrap">{sec_head('Research projects', 'In the lab &amp; the library.')}<div class="grid g3">{proj_html}</div></div></section>
{cta('Collaborate on <span class="it red">research.</span>')}''')

# ---------------- LEGAL ----------------

ecats = ['All'] + sorted({x['cat'] for x in ESSAYS}, key=lambda c: ['Constitutional law', 'Privacy & technology', 'Intellectual property', 'Legal profession'].index(c))
efilters = ''.join(f'<button type="button" class="toggle" data-filter="{e(c)}" aria-pressed="{"true" if c == "All" else "false"}">{e(c)}<span class="n">{len(ESSAYS) if c == "All" else sum(1 for x in ESSAYS if x["cat"] == c)}</span></button>' for c in ecats)
ecards = ''.join(f'<a class="card essay-card" data-group="{e(x["cat"])}" href="{x["slug"]}.html"><div style="display:flex;justify-content:space-between;gap:10px;flex-wrap:wrap"><span class="kicker" style="color:var(--accent)">{e(x["cat"])}</span><span class="kicker">{x["mins"]} min read</span></div><h3 class="h-card" style="font-size:clamp(21px,2.1vw,26px)">{e(x["title"])}</h3><p>{e(x["excerpt"])}</p><span class="foot">Read the essay →</span></a>' for x in ESSAYS)
essay_list = f'<div class="chips" role="group" aria-label="Filter essays" data-filter-group="essays" style="margin-bottom:8px">{efilters}</div><div class="grid" id="essays" style="grid-template-columns:repeat(auto-fill,minmax(300px,1fr));gap:16px">{ecards}</div>'
focus = [('§1', 'Healthcare &amp; medical law', 'Medical negligence, patient rights, clinical trials, drug and device regulation in India — grounded in Manupatra’s Fundamentals of Medical Laws in India.'),
         ('§2', 'Intellectual property &amp; biotechnology', 'Patents on genes, diagnostics and biologics; trade secrets in health data; how IP shapes access to medicine.'),
         ('§3', 'AI, justice &amp; the rule of law', 'Accountability, bias and due process when algorithms make or inform decisions — building on Oxford’s AI, Justice and Rule of Law.'),
         ('§4', 'Data protection &amp; technology regulation', 'Health and genomic data, consent, and how India’s data-protection regime meets biotechnology and AI.')]
focus_html = ''.join(f'<article class="card"><span class="num">{n}</span><h3 class="h-card">{t}</h3><p>{d}</p></article>' for n, t, d in focus)
pages['legal.html'] = ('Legal Analysis & Opinions — Subhadeep Aditya', 'Legal analysis and opinions by Subhadeep Aditya on healthcare law, intellectual property, AI governance and technology regulation in India.',
  page_hero('Legal', 'Legal analysis &amp; opinions', 'A scientist’s eye on <span class="it red">the law.</span>',
            'Analysis of healthcare law, intellectual property and AI governance — from someone who has worked inside biotech labs and health-data teams, and now studies the law that governs them.') + f'''
<section><div class="wrap">{sec_head('Focus areas', 'Where I write.')}<div class="grid g4">{focus_html}</div></div></section>
<section><div class="wrap"><div class="split" style="flex-direction:column">
<div class="main" style="display:flex;flex-direction:column;gap:20px">
{sec_head('Analysis &amp; opinions', 'The casebook.', f'{len(ESSAYS)} essays on the Constitution, privacy, intellectual property and the legal profession.')}
{essay_list}</div>
</div>
<div class="side grid g2" style="gap:16px">
<div class="card"><p class="kicker">Grounding</p>
<p><b style="color:var(--paper)">LL.B.</b> — Techno India University, Kolkata</p>
<p><b style="color:var(--paper)">AI, Justice and Rule of Law</b> — Faculty of Law, University of Oxford (2026)</p>
<p><b style="color:var(--paper)">Fundamentals of Medical Laws in India</b> — Manupatra Academy (2026)</p>
<p><b style="color:var(--paper)">Member</b> — American Bar Association (2026)</p></div>
<div class="card"><p class="kicker">Currently studying</p><div class="chips">{''.join(f'<span class="chip" style="font-size:14px">{t}</span>' for t in ['Criminal law', 'Law of contract', 'Jurisprudence', 'Hindu family law', 'Constitutional law'])}</div></div>
</div></div></div></section>
<section><div class="wrap"><div class="note"><b>Disclaimer.</b> Everything on this page is academic analysis and personal opinion written by a law student. It is not legal advice and does not create a lawyer–client relationship. For advice on your situation, consult a qualified advocate.</div></div></section>
{cta('Internships &amp; <span class="it red">legal research.</span>')}''')

# ---------------- CREDENTIALS ----------------
cats = ['All', 'Law & Policy', 'AI', 'Data & Business', 'Project & Quality', 'Life Sciences']
filters = ''.join(f'<button type="button" class="toggle" data-filter="{e(c)}" aria-pressed="{"true" if c == "All" else "false"}">{e(c)}<span class="n">{len(CREDS) if c == "All" else sum(1 for x in CREDS if x[0] == c)}</span></button>' for c in cats)
cred_html = ''.join(f'<div class="card" data-group="{e(g)}" style="padding:20px;gap:10px;min-height:130px"><div style="display:flex;justify-content:space-between;gap:10px"><span class="kicker" style="color:var(--accent)">{e(g)}</span><span class="kicker">{e(w)}</span></div><b style="font-size:17px;line-height:1.3">{e(t)}</b><p style="margin-top:auto;font-size:14px">{e(o)}</p></div>' for g, t, o, w in CREDS)
hon_html = ''.join(f'<div class="card" style="flex-direction:row;gap:16px;align-items:flex-start"><span style="flex:0 0 48px;width:48px;height:48px;border-radius:50%;border:1.5px solid var(--accent);display:flex;align-items:center;justify-content:center"><svg aria-hidden="true" width="22" height="22" viewBox="0 0 24 24" fill="none" stroke="#F2463A" stroke-width="1.8" stroke-linecap="round" stroke-linejoin="round"><circle cx="12" cy="9" r="6"/><path d="M8.5 14L7 22l5-3 5 3-1.5-8"/></svg></span><span style="display:flex;flex-direction:column;gap:6px"><span class="kicker">{k} · {w}</span><b style="font-size:18px;line-height:1.25">{e(t)}</b><span class="muted" style="font-size:14px">{e(o)}</span></span></div>' for k, w, t, o in HONORS)
pages['credentials.html'] = ('Credentials — Subhadeep Aditya', f'{len(CREDS)} certifications and six honours and memberships held by Subhadeep Aditya — Oxford Law, Johns Hopkins, WHO, Anthropic, OpenAI and more.',
  page_hero('Credentials', 'Credentials', 'A lifelong <span class="it red">learner,</span> on record.', f'From Oxford’s Faculty of Law to Johns Hopkins, WHO, Anthropic and OpenAI — {len(CREDS)} certifications across law, AI, data and the life sciences.') + f'''
<section><div class="wrap">{sec_head('Honours &amp; memberships', 'Recognised by.')}<div class="grid g3">{hon_html}</div></div></section>
<section><div class="wrap">{sec_head('Certifications', 'Filter by field.')}
<div class="chips" role="group" aria-label="Filter certifications" data-filter-group="creds" style="margin-bottom:24px">{filters}</div>
<div class="grid" id="creds" style="grid-template-columns:repeat(auto-fill,minmax(270px,1fr));gap:12px">{cred_html}</div></div></section>
{cta()}''')

# ---------------- VENTURES ----------------
pages['ventures.html'] = ('Ventures — NextLeap Advisory & ChobiGhor Studios', 'NextLeap Advisory, an educational consulting platform, and ChobiGhor Studios, exploring Kolkata heritage through photography and art — founded by Subhadeep Aditya.',
  page_hero('Ventures', 'Ventures', 'Things I’ve <span class="it red">started.</span>', 'An educational consulting platform and a photography-and-art initiative rooted in Kolkata.') + f'''
<section><div class="wrap"><div class="card" style="background:var(--accent);color:var(--ink);border:0;padding:clamp(28px,5vw,64px);gap:28px">
<span class="kicker" style="color:var(--ink)">FOUNDER · EDUCATIONAL CONSULTING</span>
<h2 class="h-page" style="font-size:clamp(44px,6.4vw,96px)">NextLeap Advisory</h2>
<p style="font-size:clamp(19px,1.9vw,23px);max-width:760px;color:var(--ink)">An educational consulting platform — guiding learners and professionals toward their next leap in biology, healthcare and research careers.</p>
<div class="grid g3">
<div class="card" style="background:var(--ink);color:var(--paper);border:0"><span class="kicker" style="color:var(--accent)">RESEARCH</span><h3 class="h-card">OncoGenome</h3><p>Cancer genomics research: genomic alterations, biomarkers and precision oncology. Ongoing since Oct 2026.</p></div>
<a class="card" href="https://github.com/Subhadeep998/NextLeap-Advisory---Biology-leaning-app" style="background:var(--ink);color:var(--paper);border:0"><span class="kicker" style="color:var(--accent)">APP</span><h3 class="h-card">Biology learning app</h3><p>An Android app for learning biology, built in Kotlin.</p><span class="foot">View on GitHub →</span></a>
<div class="card" style="background:var(--ink);color:var(--paper);border:0"><span class="kicker" style="color:var(--accent)">PUBLISHING</span><h3 class="h-card">Practitioner handbooks</h3><p>Healthcare Consulting: Foundations, Frameworks &amp; Industry Insights, Volume I.</p></div>
</div>
<div class="btns"><a class="btn btn-ink" href="mailto:info@subhadeepaditya.in?subject=NextLeap%20Advisory">Work with NextLeap</a></div>
</div></div></section>
<section><div class="wrap"><div class="card" style="padding:clamp(28px,5vw,64px);gap:28px">
<span class="kicker">FOUNDER · PHOTOGRAPHY &amp; ART</span>
<h2 class="h-page" style="font-size:clamp(44px,6.4vw,96px)">ChobiGhor <span class="it red">Studios</span></h2>
<p class="lede">Exploring Kolkata’s heritage through photography and art — the city’s lanes, facades and stories, one frame at a time.</p>
<div class="strip">{''.join(f'<a class="strip-ph" href="chobighor.html"><img src="assets/chobighor/{x}-sm.jpg" alt="ChobiGhor photograph" loading="lazy"></a>' for x in ['the-courtyard','tram-238-monochrome','green-shutters-lane','his-masters-voice'])}</div>
<p class="muted" style="font-size:14px">© ChobiGhor Studios · photographs by Subhadeep Aditya</p>
<div class="btns"><a class="btn btn-red" href="chobighor.html">View the gallery {ARROW}</a><a class="btn btn-ghost" href="mailto:hello@subhadeepaditya.in?subject=ChobiGhor%20Studios">Say hello to ChobiGhor</a></div>
</div></div></section>
{cta()}''')


# ---------------- ARTICLES ----------------
for n, x in enumerate(ESSAYS):
    prev = ESSAYS[n - 1] if n > 0 else None
    nxt = ESSAYS[n + 1] if n + 1 < len(ESSAYS) else None
    pn = ''
    if prev: pn += f'<a class="card" href="{prev["slug"]}.html"><span class="kicker">← Previous</span><b style="font-size:19px;line-height:1.3">{e(prev["title"])}</b></a>'
    else: pn += '<span></span>'
    if nxt: pn += f'<a class="card" href="{nxt["slug"]}.html" style="text-align:right"><span class="kicker">Next →</span><b style="font-size:19px;line-height:1.3">{e(nxt["title"])}</b></a>'
    first_p = next(b[1] for b in x['blocks'] if b[0] == 'p')
    pages[x['slug'] + '.html'] = (f'{x["title"]} — Subhadeep Aditya', ' '.join(first_p.split()[:30]) + '…', f'''<div class="page-hero dots"><div class="wrap" style="max-width:900px">
<p class="crumbs"><a href="index.html">Home</a> / <a href="legal.html">Legal</a> / {e(x["cat"])}</p>
<div style="display:flex;flex-wrap:wrap;gap:10px"><span class="pill" style="color:var(--accent);border-color:var(--accent)">{e(x["cat"])}</span><span class="pill">{x["mins"]} min read</span><span class="pill">Essay</span></div>
<h1 class="h-page" style="font-size:clamp(36px,5vw,68px);letter-spacing:-1.5px;line-height:1.02">{e(x["title"])}</h1>
<div class="byline"><img src="assets/favicon.png" alt="" width="44" height="44"><span><b>Subhadeep Aditya</b><small>LL.B. student · Techno India University, Kolkata</small></span></div>
</div></div>
<article class="article wrap">
{render_blocks(x["blocks"])}
<div class="note" style="margin-top:48px"><b>Disclaimer.</b> This essay is academic analysis and personal opinion written by a law student. It is not legal advice.</div>
<div class="share"><span class="kicker">Share</span><a class="btn btn-ghost" href="https://www.linkedin.com/sharing/share-offsite/?url=https://www.subhadeepaditya.in/{x["slug"]}.html">LinkedIn {OUT_ARROW}</a><a class="btn btn-ghost" href="mailto:?subject={e(x["title"])}&amp;body=https://www.subhadeepaditya.in/{x["slug"]}.html">Email</a><a class="btn btn-ghost" href="legal.html">All essays</a></div>
</article>
<section style="padding-top:48px"><div class="wrap" style="max-width:900px"><div class="grid g2">{pn}</div></div></section>
{cta('Discuss this <span class="it red">essay.</span>')}''')


# ---------------- CHOBIGHOR GALLERY ----------------
import json as _json
PHOTOS = _json.load(open('/home/claude/photos/meta.json'))
PCATS = ['All'] + [c for c in ['Streets','Trams','Interiors','Objects','Street life','Devotion','Skyline'] if any(x['cat']==c for x in PHOTOS)]
pfilters = ''.join(f'<button type="button" class="toggle" data-filter="{e(c)}" aria-pressed="{"true" if c == "All" else "false"}">{e(c)}<span class="n">{len(PHOTOS) if c == "All" else sum(1 for x in PHOTOS if x["cat"] == c)}</span></button>' for c in PCATS)
ptiles = ''.join(f'<figure class="ph" data-group="{e(x["cat"])}"><button type="button" class="ph-open" data-i="{i}" aria-label="Open photo: {e(x["title"])}"><img src="assets/chobighor/{x["slug"]}-sm.jpg" width="{x["tw"]}" height="{x["th"]}" alt="{e(x["title"])} — {e(x["cap"])}" loading="lazy" decoding="async"></button><figcaption><b>{e(x["title"])}</b><span>{e(x["cat"])}</span></figcaption></figure>' for i, x in enumerate(PHOTOS))
pdata = _json.dumps([dict(src=f'assets/chobighor/{x["slug"]}.jpg', t=x['title'], c=x['cap'], k=x['cat']) for x in PHOTOS], ensure_ascii=False).replace('</', '<\\/')
pages['chobighor.html'] = ('ChobiGhor Studios — Kolkata heritage photography by Subhadeep Aditya',
  'ChobiGhor Studios: photographs of Kolkata’s heritage — lanes, trams, old houses and everyday life — by Subhadeep Aditya.',
  page_hero('<a href="ventures.html">Ventures</a> / ChobiGhor', 'ChobiGhor Studios · ছবিঘর', 'Kolkata, one <span class="it red">frame</span> at a time.',
            'Lanes, trams, old houses and the small things that hold a city’s memory — photographed by Subhadeep Aditya.') + f'''
<section style="padding-top:40px"><div class="wrap">
<div class="chips" role="group" aria-label="Filter photographs" data-filter-group="gallery" style="margin-bottom:28px">{pfilters}</div>
<div class="gallery" id="gallery">{ptiles}</div>
<p class="note" style="margin-top:40px"><b>© 2026 ChobiGhor Studios · Subhadeep Aditya. All rights reserved.</b> Every photograph on this page was taken by Subhadeep Aditya. Please don’t download, reuse or republish them without written permission — write to <a href="mailto:hello@subhadeepaditya.in?subject=ChobiGhor%20photo%20permission">hello@subhadeepaditya.in</a> for licensing or prints.</p>
</div></section>
<dialog class="lb" id="lb" aria-label="Photo viewer">
<div class="lb-inner">
<img id="lb-img" alt="">
<div class="lb-bar"><div class="lb-text"><b id="lb-title"></b><span id="lb-cap"></span><small>© ChobiGhor Studios · Subhadeep Aditya</small></div>
<div class="lb-ctrls"><button type="button" class="lb-btn" id="lb-prev" aria-label="Previous photo">←</button><span id="lb-count" class="kicker"></span><button type="button" class="lb-btn" id="lb-next" aria-label="Next photo">→</button><button type="button" class="lb-btn" id="lb-close" aria-label="Close viewer">✕</button></div></div>
</div>
</dialog>
<script>window.CHOBI={pdata};</script>
{cta('Prints &amp; <span class="it red">collaborations.</span>')}''')

# ---------------- CONTACT ----------------
pages['contact.html'] = ('Contact — Subhadeep Aditya', 'Contact Subhadeep Aditya for research collaboration, legal internships, consulting, books and photography.',
  page_hero('Contact', 'Contact', 'Let’s <span class="it red">talk.</span>', 'Pick the address that fits — every message reaches me.') + f'''
<section style="padding-top:48px"><div class="wrap"><div class="grid g4">{''.join(f'<a class="mail" href="mailto:{a}" style="min-height:180px"><span class="kicker">{l}</span><b style="font-size:19px">{a}</b><p>{d}</p></a>' for l, a, d in EMAILS)}</div></div></section>
<section><div class="wrap">{sec_head('Elsewhere', 'Find me online.')}
<div class="grid g3">
<a class="card" href="{LI}"><span class="kicker">PROFESSIONAL</span><h3 class="h-card">LinkedIn</h3><p>Experience, certifications and updates.</p><span class="foot">Connect →</span></a>
<a class="card" href="{RG}"><span class="kicker">ACADEMIC</span><h3 class="h-card">ResearchGate</h3><p>Papers, posters and research projects.</p><span class="foot">View papers →</span></a>
<a class="card" href="{GH}"><span class="kicker">CODE</span><h3 class="h-card">GitHub</h3><p>This website and the NextLeap biology app.</p><span class="foot">View GitHub →</span></a>
</div>
<div class="note" style="margin-top:32px"><b>Based in Kolkata, India.</b> Open to law-firm internships, research collaborations and consulting engagements.</div>
</div></section>''')

# ---------------- 404 ----------------
pages['404.html'] = ('Page not found — Subhadeep Aditya', 'Page not found.',
  page_hero('404', 'Error 404', 'This page has <span class="it red">faded.</span>', 'The page you were looking for isn’t here. Try the home page instead.',
            f'<div class="btns"><a class="btn btn-red" href="index.html">Back to home {ARROW}</a></div>'))

import re as _re
def _ext(m):
    tag = m.group(0)
    href = _re.search(r'href="([^"]*)"', tag).group(1)
    if 'target=' in tag or _re.match(r'https?://(www\.)?subhadeepaditya\.in', href): return tag
    return tag[:-1] + ' target="_blank" rel="noopener">'
for fname, (title, desc, body) in pages.items():
    html = layout(fname, title, desc, body)
    html = _re.sub(r'<a\b[^>]*href="https?://[^"]*"[^>]*>', _ext, html)
    open(f'{OUT}/{fname}', 'w').write(html)
print('pages:', ', '.join(pages))
