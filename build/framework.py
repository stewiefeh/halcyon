# HALCYON build framework: shared layout + SVG art generators
import html as _h

CANON = "https://halcyon-dqd.pages.dev"   # placeholder, corrected to real subdomain in v1.0.1
VER = "1.0.0"
NAME = "Halcyon Stereo"
TAG = "Vintage Hi-Fi & Records, Portland OR"

NAV = [
    ("index.html", "Home"),
    ("inventory.html", "Inventory"),
    ("records.html", "Records"),
    ("service.html", "Service"),
    ("events.html", "Events"),
    ("journal.html", "Journal"),
    ("contact.html", "Visit"),
]

LOGO = '''<svg viewBox="0 0 48 48" aria-hidden="true"><circle cx="24" cy="24" r="21" fill="var(--ink)"/><circle cx="24" cy="24" r="20" fill="none" stroke="var(--mustard)" stroke-width="2.5"/><circle cx="24" cy="24" r="15.5" fill="none" stroke="var(--paper)" stroke-opacity=".5" stroke-width="1.2"/><circle cx="24" cy="24" r="11.5" fill="none" stroke="var(--paper)" stroke-opacity=".5" stroke-width="1.2"/><circle cx="24" cy="24" r="8.5" fill="var(--orange)"/><circle cx="24" cy="24" r="2.4" fill="var(--paper)"/><path d="M15 20h4l2 8h2l2-8h4" fill="none" stroke="var(--ink)" stroke-width="2.4" stroke-linecap="round" stroke-linejoin="round"/></svg>'''

def esc(s): return _h.escape(str(s), quote=True)

def head(title, desc, path, extra=""):
    url = f"{CANON}/{path}"
    ogtype = "website" if path == "index.html" else "article"
    return f'''<!doctype html>
<html lang="en">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width, initial-scale=1">
<title>{esc(title)} | {NAME}</title>
<meta name="description" content="{esc(desc)}">
<link rel="canonical" href="{url}">
<meta name="theme-color" content="#e0862f">
<meta property="og:site_name" content="{NAME}">
<meta property="og:title" content="{esc(title)}">
<meta property="og:description" content="{esc(desc)}">
<meta property="og:type" content="{ogtype}">
<meta property="og:url" content="{url}">
<meta name="twitter:card" content="summary">
<link rel="icon" href="assets/img/favicon.svg" type="image/svg+xml">
<link rel="preload" href="assets/fonts/anybody-var.woff2" as="font" type="font/woff2" crossorigin>
<link rel="preload" href="assets/fonts/figtree-var.woff2" as="font" type="font/woff2" crossorigin>
<link rel="stylesheet" href="assets/css/main.css?v={VER}">
{extra}
</head>'''

def header(path):
    items = []
    for href, label in NAV:
        cur = ' aria-current="page"' if href == path else ""
        items.append(f'<li><a href="{href}"{cur}>{label}</a></li>')
    nav = "\n".join(items)
    return f'''
<a class="skip-link" href="#main">Skip to content</a>
<div class="progress-rail" aria-hidden="true"><div class="progress-bar"></div></div>
<header class="site-header">
  <div class="container">
    <a class="brand" href="index.html" aria-label="Halcyon Stereo, home">
      {LOGO}
      <span>Halcyon<small>Stereo · est. 1974</small></span>
    </a>
    <nav class="site-nav" id="site-nav" aria-label="Main">
      <ul>{nav}</ul>
    </nav>
    <button class="nav-toggle" aria-expanded="false" aria-controls="site-nav">Menu</button>
    <button class="lamp" id="lamp" aria-label="Toggle evening mode" title="Lamp switch">
      <svg class="ico-day" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" aria-hidden="true"><circle cx="12" cy="12" r="4.5"/><path d="M12 2v3M12 19v3M2 12h3M19 12h3M4.9 4.9l2.1 2.1M17 17l2.1 2.1M19.1 4.9L17 7M7 17l-2.1 2.1"/></svg>
      <svg class="ico-evening" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" aria-hidden="true"><path d="M20 14.5A8.5 8.5 0 1 1 9.5 4a7 7 0 0 0 10.5 10.5Z"/></svg>
    </button>
  </div>
</header>'''

def footer():
    return '''
<footer class="site-footer">
  <div class="container">
    <div class="footer-grid">
      <div class="footer-brand">
        <a class="brand" href="index.html" style="color:inherit">
          <svg viewBox="0 0 48 48" aria-hidden="true"><circle cx="24" cy="24" r="21" fill="var(--mustard)"/><circle cx="24" cy="24" r="20" fill="none" stroke="var(--ink)" stroke-width="2.5"/><circle cx="24" cy="24" r="8.5" fill="var(--ink)"/><circle cx="24" cy="24" r="2.4" fill="var(--mustard)"/></svg>
          <span>Halcyon<small style="color:inherit">Stereo · est. 1974</small></span>
        </a>
        <p>Two floors of restored hi-fi, a listening room that seats eleven, and several thousand records. Family run since 1974.</p>
      </div>
      <div>
        <h3>Explore</h3>
        <ul>
          <li><a href="inventory.html">Current inventory</a></li>
          <li><a href="records.html">Record crates</a></li>
          <li><a href="service.html">Service bench</a></li>
          <li><a href="events.html">Listening nights</a></li>
          <li><a href="journal.html">The Journal</a></li>
        </ul>
      </div>
      <div>
        <h3>The Shop</h3>
        <ul>
          <li><a href="about.html">Our story</a></li>
          <li><a href="trade-in.html">Sell or trade</a></li>
          <li><a href="faq.html">Questions</a></li>
          <li><a href="contact.html">Visit us</a></li>
          <li><a href="privacy.html">Privacy</a></li>
          <li><a href="terms.html">Terms</a></li>
        </ul>
      </div>
      <div>
        <h3>Hours &amp; Address</h3>
        <ul>
          <li>Tue&ndash;Sat 10&ndash;6, Sun 12&ndash;5</li>
          <li>Closed Mondays (bench day)</li>
          <li>2114 SE Ankeny St<br>Portland, OR 97214</li>
          <li><a href="tel:+15035550174">(503) 555-0174</a></li>
          <li><a href="mailto:hello@halcyon.example">hello@halcyon.example</a></li>
        </ul>
      </div>
    </div>
    <div class="footer-note">
      <span>&copy; <span data-year>2026</span> Halcyon Stereo. A fictional shop for a portfolio piece.</span>
      <span>Spin responsibly.</span>
    </div>
  </div>
</footer>
<script src="assets/js/main.js?v=VERPLACE" defer></script>
</body>
</html>'''

FOOTER = footer().replace("VERPLACE", VER)

def write(path_str, title, desc, body, extra=""):
    doc = head(title, desc, path_str, extra) + "\n" + header(path_str) + '\n<main id="main">\n' + body + "\n</main>\n" + FOOTER
    with open(path_str, "w") as f:
        f.write(doc)
    print(f"wrote {path_str} ({doc.count(chr(10))+1} lines)")

# ---------------- SVG art generators ----------------
WOOD = '''<defs><linearGradient id="woodgrad" x1="0" y1="0" x2="0" y2="1"><stop offset="0" stop-color="#7a4a26"/><stop offset=".25" stop-color="#8a5628"/><stop offset=".5" stop-color="#6f421f"/><stop offset=".75" stop-color="#8a5628"/><stop offset="1" stop-color="#5f3718"/></linearGradient></defs>'''

def art_turntable():
    return f'''<svg class="gear-art" viewBox="0 0 400 300" role="img" aria-label="Illustration of a vintage belt-drive turntable on a walnut plinth">
{WOOD}
<rect x="18" y="96" width="364" height="160" rx="14" fill="url(#woodgrad)"/>
<rect x="18" y="96" width="364" height="14" rx="7" fill="#00000022"/>
<rect x="30" y="30" width="340" height="72" rx="10" fill="#e8dcc2"/>
<text x="46" y="58" font-family="Anybody, sans-serif" font-weight="800" font-size="17" fill="#3a2a18" letter-spacing="1">HALCYON TT-500</text>
<text x="46" y="80" font-family="Figtree, sans-serif" font-weight="600" font-size="13" fill="#7a6a50">BELT DRIVE &#183; 33/45 &#183; SUSPENDED</text>
<circle cx="286" cy="176" r="92" fill="#22180f"/>
<circle cx="286" cy="176" r="90" fill="none" stroke="#c9b894" stroke-width="2"/>
<g stroke="#ffffff22" stroke-width="1.2">
<circle cx="286" cy="176" r="82" fill="none"/><circle cx="286" cy="176" r="72" fill="none"/><circle cx="286" cy="176" r="62" fill="none"/><circle cx="286" cy="176" r="52" fill="none"/><circle cx="286" cy="176" r="44" fill="none"/>
</g>
<circle cx="286" cy="176" r="34" fill="#e0862f"/>
<circle cx="286" cy="176" r="34" fill="none" stroke="#f4e8cf" stroke-width="3"/>
<circle cx="286" cy="176" r="5" fill="#f4e8cf"/>
<text x="286" y="170" text-anchor="middle" font-family="Anybody, sans-serif" font-weight="800" font-size="12" fill="#3a2410">HALCYON</text>
<text x="286" y="190" text-anchor="middle" font-family="Figtree, sans-serif" font-weight="600" font-size="9" fill="#3a2410">SIDE A</text>
<rect x="60" y="150" width="9" height="120" rx="4" fill="#d9cdb6" transform="rotate(24 64 150)"/>
<circle cx="70" cy="146" r="13" fill="#c9b894"/>
<rect x="128" y="238" width="52" height="16" rx="8" fill="#e05a3a"/>
<rect x="196" y="240" width="14" height="12" rx="3" fill="#f4e8cf"/>
<rect x="216" y="240" width="14" height="12" rx="3" fill="#f4e8cf"/>
<text x="196" y="232" font-family="Anybody, sans-serif" font-weight="700" font-size="10" fill="#f4e8cf">STOP</text>
<text x="240" y="232" font-family="Anybody, sans-serif" font-weight="700" font-size="10" fill="#f4e8cf">33</text>
<rect x="18" y="256" width="364" height="0" fill="none"/>
</svg>'''

def art_receiver():
    return f'''<svg class="gear-art" viewBox="0 0 400 300" role="img" aria-label="Illustration of a 1970s brushed-silver stereo receiver with warm dial glow">
{WOOD}
<rect x="30" y="40" width="340" height="220" rx="12" fill="url(#woodgrad)"/>
<rect x="52" y="58" width="296" height="184" rx="8" fill="#b9b3a4"/>
<rect x="52" y="58" width="296" height="184" rx="8" fill="none" stroke="#8f8a7d" stroke-width="2"/>
<rect x="66" y="72" width="150" height="64" rx="6" fill="#1d2318"/>
<text x="74" y="98" font-family="Anybody, sans-serif" font-weight="800" font-size="14" fill="#e8c76a">103.3</text>
<text x="74" y="118" font-family="Figtree, sans-serif" font-weight="600" font-size="11" fill="#9fb08a">MHz &#183; STEREO</text>
<g stroke="#e8c76a" stroke-width="2"><line x1="150" y1="80" x2="158" y2="88"/><line x1="150" y1="96" x2="158" y2="104"/><line x1="150" y1="112" x2="158" y2="120"/></g>
<circle cx="300" cy="104" r="30" fill="#8f8a7d"/><circle cx="300" cy="104" r="24" fill="#6b665c"/><rect x="298" y="82" width="4" height="16" rx="2" fill="#e8dcc2"/>
<circle cx="300" cy="176" r="30" fill="#8f8a7d"/><circle cx="300" cy="176" r="24" fill="#6b665c"/><rect x="298" y="154" width="4" height="16" rx="2" fill="#e8dcc2"/>
<rect x="70" y="150" width="180" height="70" rx="6" fill="#8f8a7d"/>
<text x="78" y="168" font-family="Anybody, sans-serif" font-weight="700" font-size="10" fill="#3f3b34">PHONO</text><text x="78" y="188" font-family="Anybody, sans-serif" font-weight="700" font-size="10" fill="#3f3b34">TUNER</text><text x="78" y="208" font-family="Anybody, sans-serif" font-weight="700" font-size="10" fill="#3f3b34">AUX</text>
<rect x="150" y="162" width="80" height="10" rx="5" fill="#4a463e"/><rect x="150" y="178" width="60" height="10" rx="5" fill="#4a463e"/><rect x="150" y="194" width="70" height="10" rx="5" fill="#4a463e"/>
<circle cx="196" cy="252" r="3.4" fill="#e05a3a"/><circle cx="212" cy="252" r="3.4" fill="#e8c76a"/>
</svg>'''

def art_speakers():
    return f'''<svg class="gear-art" viewBox="0 0 400 300" role="img" aria-label="Illustration of a pair of large 1970s loudspeakers with cloth grilles">
{WOOD}
<rect x="36" y="30" width="150" height="240" rx="10" fill="url(#woodgrad)"/>
<rect x="214" y="30" width="150" height="240" rx="10" fill="url(#woodgrad)"/>
<rect x="50" y="44" width="122" height="150" rx="8" fill="#4a3520"/>
<rect x="228" y="44" width="122" height="150" rx="8" fill="#4a3520"/>
<g fill="none" stroke="#6b543a" stroke-width="1.4" opacity=".8">
<path d="M54 50h114M54 62h114M54 74h114M54 86h114M54 98h114M54 110h114M54 122h114M54 134h114M54 146h114M54 158h114M54 170h114M54 182h114"/>
</g>
<circle cx="111" cy="86" r="22" fill="#e8dcc2"/><circle cx="111" cy="86" r="8" fill="#3a2a18"/>
<circle cx="289" cy="86" r="22" fill="#e8dcc2"/><circle cx="289" cy="86" r="8" fill="#3a2a18"/>
<circle cx="111" cy="150" r="30" fill="#22180f"/><circle cx="111" cy="150" r="11" fill="#e0862f"/>
<circle cx="289" cy="150" r="30" fill="#22180f"/><circle cx="289" cy="150" r="11" fill="#e0862f"/>
<rect x="54" y="214" width="114" height="42" rx="6" fill="#2f2214"/>
<rect x="228" y="214" width="114" height="42" rx="6" fill="#2f2214"/>
<text x="111" y="238" text-anchor="middle" font-family="Anybody, sans-serif" font-weight="800" font-size="11" fill="#e8dcc2">LS-6</text>
<text x="289" y="238" text-anchor="middle" font-family="Anybody, sans-serif" font-weight="800" font-size="11" fill="#e8dcc2">LS-6</text>
</svg>'''

def art_deck():
    return f'''<svg class="gear-art" viewBox="0 0 400 300" role="img" aria-label="Illustration of a vintage cassette deck with VU meters">
{WOOD}
<rect x="26" y="52" width="348" height="200" rx="12" fill="url(#woodgrad)"/>
<rect x="44" y="68" width="312" height="168" rx="8" fill="#b9b3a4"/>
<circle cx="120" cy="110" r="26" fill="#1d2318"/><circle cx="120" cy="110" r="20" fill="#8f8a7d"/><circle cx="120" cy="110" r="6" fill="#1d2318"/>
<circle cx="200" cy="110" r="26" fill="#1d2318"/><circle cx="200" cy="110" r="20" fill="#8f8a7d"/><circle cx="200" cy="110" r="6" fill="#1d2318"/>
<rect x="236" y="84" width="100" height="52" rx="6" fill="#1d2318"/>
<text x="246" y="106" font-family="Anybody, sans-serif" font-weight="800" font-size="13" fill="#e05a3a">&#9654; REC</text>
<text x="246" y="126" font-family="Figtree, sans-serif" font-weight="600" font-size="10" fill="#9fb08a">CHROME &#183; 90 MIN</text>
<rect x="60" y="152" width="280" height="30" rx="6" fill="#6b665c"/>
<text x="72" y="172" font-family="Anybody, sans-serif" font-weight="700" font-size="12" fill="#e8dcc2">SIDE A</text>
<rect x="60" y="196" width="80" height="24" rx="12" fill="#e05a3a"/><text x="100" y="212" text-anchor="middle" font-family="Anybody, sans-serif" font-weight="700" font-size="11" fill="#1d140c">PLAY</text>
<rect x="152" y="196" width="80" height="24" rx="12" fill="#8f8a7d"/><text x="192" y="212" text-anchor="middle" font-family="Anybody, sans-serif" font-weight="700" font-size="11" fill="#1d140c">STOP</text>
<rect x="244" y="196" width="80" height="24" rx="12" fill="#e8c76a"/><text x="284" y="212" text-anchor="middle" font-family="Anybody, sans-serif" font-weight="700" font-size="11" fill="#1d140c">REW</text>
</svg>'''

def art_amp():
    return f'''<svg class="gear-art" viewBox="0 0 400 300" role="img" aria-label="Illustration of a vintage integrated amplifier with glowing tubes">
{WOOD}
<rect x="30" y="60" width="340" height="190" rx="12" fill="url(#woodgrad)"/>
<rect x="48" y="78" width="304" height="150" rx="8" fill="#2b2118"/>
<g>
<circle cx="110" cy="120" r="22" fill="#3a2a18" stroke="#e8c76a" stroke-width="2"/>
<circle cx="110" cy="120" r="10" fill="#e8c76a" opacity=".55"/>
<circle cx="170" cy="120" r="22" fill="#3a2a18" stroke="#e8c76a" stroke-width="2"/>
<circle cx="170" cy="120" r="10" fill="#e8c76a" opacity=".55"/>
<circle cx="230" cy="120" r="22" fill="#3a2a18" stroke="#e8c76a" stroke-width="2"/>
<circle cx="230" cy="120" r="10" fill="#e8c76a" opacity=".55"/>
<circle cx="290" cy="120" r="22" fill="#3a2a18" stroke="#e8c76a" stroke-width="2"/>
<circle cx="290" cy="120" r="10" fill="#e8c76a" opacity=".55"/>
</g>
<rect x="70" y="170" width="260" height="40" rx="6" fill="#1d140c"/>
<g stroke="#e0862f" stroke-width="6" stroke-linecap="round">
<line x1="90" y1="204" x2="90" y2="188"/><line x1="110" y1="204" x2="110" y2="182"/><line x1="130" y1="204" x2="130" y2="192"/><line x1="150" y1="204" x2="150" y2="180"/><line x1="170" y1="204" x2="170" y2="190"/><line x1="190" y1="204" x2="190" y2="178"/><line x1="210" y1="204" x2="210" y2="186"/><line x1="230" y1="204" x2="230" y2="182"/><line x1="250" y1="204" x2="250" y2="192"/><line x1="270" y1="204" x2="270" y2="184"/><line x1="290" y1="204" x2="290" y2="190"/><line x1="310" y1="204" x2="310" y2="180"/>
</g>
<text x="200" y="96" text-anchor="middle" font-family="Anybody, sans-serif" font-weight="800" font-size="13" fill="#e8dcc2">HA-80 TUBE INTEGRATED</text>
</svg>'''

def record_sleeve(i, title, artist, c1, c2, c3):
    """Generative 70s record sleeve art."""
    return f'''<svg viewBox="0 0 300 300" role="img" aria-label="Record sleeve art for {esc(title)} by {esc(artist)}">
<rect width="300" height="300" fill="{c1}"/>
<circle cx="150" cy="118" r="86" fill="{c2}"/>
<path d="M0 214h300v86H0z" fill="{c3}"/>
<path d="M0 214c60 0 90-26 150-26s90 26 150 26" fill="none" stroke="{c1}" stroke-width="10"/>
<circle cx="150" cy="118" r="30" fill="{c1}"/>
<circle cx="150" cy="118" r="30" fill="none" stroke="{c3}" stroke-width="6"/>
<circle cx="150" cy="118" r="4" fill="{c3}"/>
<g stroke="{c3}" stroke-width="5" opacity=".85"><path d="M28 262h60M28 276h44"/></g>
<text x="24" y="48" font-family="Anybody, sans-serif" font-weight="800" font-size="26" fill="{c3}" transform="rotate(-4 24 48)">{esc(title[:14].upper())}</text>
<text x="24" y="72" font-family="Figtree, sans-serif" font-weight="700" font-size="13" fill="{c2}">{esc(artist)}</text>
</svg>'''

def sunburst_divider():
    return '''<div class="marquee" aria-hidden="true"><div class="marquee__track"><span>Restored &middot; Warrantied &middot; Played Before It Ships &middot; Honest About Flaws &middot; </span><span>Restored &middot; Warrantied &middot; Played Before It Ships &middot; Honest About Flaws &middot; </span></div></div>'''
