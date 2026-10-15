# HALCYON pages part A: home, about, inventory, gear details
import sys, os
sys.path.insert(0, os.path.dirname(__file__))
from framework import (write, esc, art_turntable, art_receiver, art_speakers, art_deck, art_amp,
                       record_sleeve, sunburst_divider, NAME, TAG)

# ---------------- inventory data ----------------
INVENTORY = [
    dict(slug="turntable-tt500.html", name="TT-500 Belt-Drive Turntable", type="turntable",
         year="1976", price=895.0, badge="Restored", art="turntable",
         blurb="Suspended chassis, new belt, rebuilt motor. The one we measure everything else against."),
    dict(slug="receiver-r70.html", name="R-70 AM/FM Receiver", type="receiver",
         year="1974", price=640.0, badge="Bench Fresh", art="receiver",
         blurb="75 honest watts per channel, warm blue dial, every switch cleaned and debossed new."),
    dict(slug="speakers-ls6.html", name="LS-6 Floorstanding Loudspeakers", type="speakers",
         year="1975", price=780.0, badge="Pair", art="speakers",
         blurb="Big cabinets, bigger sound. Re-foamed woofers, recapped crossovers, original grilles."),
    dict(slug=None, name="HA-80 Tube Integrated Amp", type="amp",
         year="1972", price=1150.0, badge="Hero Piece", art="amp",
         blurb="Four EL84s glowing like a porch light. New coupling caps, freshly biased, hum-free."),
    dict(slug=None, name="CD-9 Cassette Deck", type="deck",
         year="1978", price=385.0, badge="Serviced", art="deck",
         blurb="Three heads, dual VU needles, new belts and idler tire. Sounds better than it should."),
    dict(slug=None, name="Mark III Micro Turner Tuner", type="receiver",
         year="1973", price=210.0, badge="Budget", art="receiver",
         blurb="A simple FM tuner that pulls in stations like it has a grudge against static."),
    dict(slug=None, name="Monitor 8 Bookshelf Speakers", type="speakers",
         year="1977", price=295.0, badge="Pair", art="speakers",
         blurb="Small cabinets with serious intent. Perfect for a first system or a small room."),
    dict(slug=None, name="Studio Belt-Drive Turntable", type="turntable",
         year="1979", price=520.0, badge="Restored", art="turntable",
         blurb="Quartz-locked, direct-readout speed. The quiet workhorse of the back wall."),
    dict(slug=None, name="Grand Cassette Deck", type="deck",
         year="1976", price=445.0, badge="Serviced", art="deck",
         blurb="Auto-reverse, orange VUs, wood side panels. Recorded an entire decade on it, probably."),
    dict(slug=None, name="Compact Phono Preamp", type="amp",
         year="1981", price=165.0, badge="Budget", art="amp",
         blurb="A clean little phono stage for receivers without one. Does one job, does it well."),
    dict(slug=None, name="Twin-12 Receiver", type="receiver",
         year="1977", price=820.0, badge="Bench Fresh", art="receiver",
         blurb="Twin VU meters, twin tuning knobs, one giant gold face. Peak 1977 confidence."),
    dict(slug=None, name="Tower 15 Loudspeakers", type="speakers",
         year="1974", price=960.0, badge="Pair", art="speakers",
         blurb="Fifteen-inch woofers that move air like weather. Bring a strong floor."),
]

ART = dict(turntable=art_turntable, receiver=art_receiver, speakers=art_speakers,
           deck=art_deck, amp=art_amp)

def inv_card(item, i=0):
    art_fn = ART[item["art"]]
    dly = f" reveal-d{(i % 4) + 1}" if i else ""
    link = item["slug"] or "inventory.html"
    href = f'href="{link}"' if item["slug"] else ""
    tag = item["slug"] and "a" or "div"
    inner = f'''
      <div class="card__media">{art_fn()}</div>
      <div class="card__body">
        <span class="badge badge--{'orange' if item['badge'] in ('Restored','Bench Fresh') else 'mustard'}">{esc(item["badge"])}</span>
        <span class="badge">{'1970s'}</span>
        <h3 style="margin-top:.6rem">{esc(item["name"])}</h3>
        <p>{esc(item["blurb"])}</p>
        <div class="card__meta">
          <span class="price">${item["price"]:,.0f}</span>
          <span class="badge">{esc(item["year"])}</span>
        </div>
      </div>'''
    if item["slug"]:
        return f'<a class="card inv-card reveal{dly}" {href} data-type="{item["type"]}" data-price="{item["price"]}">{inner}</a>'
    return f'<div class="card inv-card reveal{dly}" data-type="{item["type"]}" data-price="{item["price"]}">{inner}</div>'

# ---------------- HOME ----------------
records_row = [
    ("Midnight Orchard", "The Field Years", "oklch(62% 0.16 45)", "oklch(80% 0.13 88)", "oklch(28% 0.05 45)", "$24"),
    ("Golden Hour Radio", "Marisol Vega", "oklch(80% 0.12 88)", "oklch(64% 0.18 45)", "oklch(30% 0.06 50)", "$32"),
    ("Basement Tapes Vol. 3", "Cedar & Rust", "oklch(58% 0.1 128)", "oklch(92% 0.03 85)", "oklch(28% 0.05 45)", "$28"),
    ("Slow Water", "Harbor Lights", "oklch(60% 0.09 220)", "oklch(88% 0.05 85)", "oklch(27% 0.05 240)", "$26"),
    ("Second Sun", "Atlas Motel", "oklch(66% 0.2 42)", "oklch(90% 0.04 88)", "oklch(32% 0.08 40)", "$38"),
    ("The Long Room", "Quarry Choir", "oklch(38% 0.06 50)", "oklch(78% 0.13 85)", "oklch(90% 0.03 85)", "$30"),
]
rec_html = []
for i, (t, a, c1, c2, c3, p) in enumerate(records_row):
    rec_html.append(f'''<a class="record-card" href="records.html">
  <figure style="margin:0">
    <div class="record-sleeve">{record_sleeve(i, t, a, c1, c2, c3)}</div>
    <figcaption>
      <div class="rec-artist">{esc(a)}</div>
      <div class="rec-title">{esc(t)}</div>
      <div class="rec-price">{p}</div>
    </figcaption>
  </figure>
</a>''')
records_row_html = "\n".join(rec_html)

featured = "".join(inv_card(item, i) for i, item in enumerate(INVENTORY[:4]))

body = f'''
<section class="hero">
  <div class="container">
    <div>
      <p class="eyebrow">Vintage Hi-Fi &middot; Records &middot; Portland, Oregon</p>
      <h1 class="hero-title">Warmth you can <em>measure</em></h1>
      <p class="lede">We restore 1970s hi-fi until it outlives us, put it on the floor with the records that deserve it, and let you hear both before you decide anything.</p>
      <div class="hero-cta">
        <a class="btn btn--primary" href="inventory.html">Browse the floor
          <svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2.5" aria-hidden="true"><path d="M5 12h14m-6-6 6 6-6 6"/></svg></a>
        <a class="btn btn--ghost" href="service.html">Service &amp; repairs</a>
      </div>
      <p class="hero-meta"><span>Est. 1974</span><span>3,100+ units restored</span><span>90-day warranty</span></p>
    </div>
    <div class="vinyl-stage">
      <canvas aria-label="Spinning vinyl record illustration. Press Enter to lift the needle." tabindex="0"></canvas>
      <p class="vinyl-caption">Click the plinth: needle up, needle down</p>
    </div>
  </div>
</section>
{sunburst_divider()}
<section class="section">
  <div class="container">
    <div class="stats">
      <div class="stat reveal"><div class="n">54</div><div class="l">years on Ankeny St</div></div>
      <div class="stat reveal reveal-d1"><div class="n">3,100</div><div class="l">pieces restored &amp; counting</div></div>
      <div class="stat reveal reveal-d2"><div class="n">11</div><div class="l">seats in the listening room</div></div>
      <div class="stat reveal reveal-d3"><div class="n">90</div><div class="l">day warranty on everything</div></div>
    </div>
  </div>
</section>
<section class="section section--sunk">
  <div class="container">
    <div class="section-head">
      <p class="eyebrow">The way we do it</p>
      <h2>Bought once, kept for decades</h2>
      <p class="lede">Every piece on the floor went through the bench first. No exceptions, no &ldquo;as-is&rdquo; bargains, no mystery hiss.</p>
    </div>
    <div class="grid grid-3">
      <div class="card reveal">
        <div class="card__body">
          <span class="badge badge--orange">On the bench</span>
          <h3 style="margin-top:.7rem">Fully restored before sale</h3>
          <p>New belts and capacitors, deoxed every switch, stylus and drive aligned, then thirty hours of burn-in with our own ears on it.</p>
        </div>
      </div>
      <div class="card reveal reveal-d1">
        <div class="card__body">
          <span class="badge badge--mustard">Honest paper</span>
          <h3 style="margin-top:.7rem">Every flaw written down</h3>
          <p>Veneer chips, replaced knobs, non-original parts: it all goes on the tag. What you read is what you hear, at full volume.</p>
        </div>
      </div>
      <div class="card reveal reveal-d2">
        <div class="card__body">
          <span class="badge badge--avocado">On our floor</span>
          <h3 style="margin-top:.7rem">Play it before you buy it</h3>
          <p>Bring your own record or borrow one of ours. The listening room is open whenever we are, and no one will hover.</p>
        </div>
      </div>
    </div>
  </div>
</section>
<section class="section">
  <div class="container">
    <div class="section-head row" style="justify-content:space-between">
      <div>
        <p class="eyebrow">Fresh from the bench</p>
        <h2>This week&rsquo;s featured gear</h2>
      </div>
      <a class="btn btn--ghost btn--small" href="inventory.html">See all inventory</a>
    </div>
    <div class="inv-grid">{featured}</div>
  </div>
</section>
<section class="shelf">
  <div class="container" style="padding-bottom:0">
    <div class="section-head" style="margin-bottom:var(--sp-3)">
      <p class="eyebrow">Crate picks</p>
      <h2>Records worth pulling</h2>
    </div>
  </div>
  <div class="shelf__row" aria-label="Featured records, scroll horizontally">
    {records_row_html}
  </div>
</section>
<section class="section section--panel">
  <div class="container">
    <div class="grid" style="grid-template-columns:1fr;gap:var(--sp-5)">
      <div class="section-head" style="margin-bottom:0">
        <p class="eyebrow">The service bench</p>
        <h2 style="color:var(--paper)">Your gear, our bench</h2>
        <p class="lede" style="color:oklch(88% .03 80 / .85)">We service what we sell and a lot of what we don&rsquo;t. Free estimates, real turnaround times, and a bench that&rsquo;s been running since before we had a website.</p>
      </div>
      <div class="grid grid-2">
        <ul class="svc-list">
          <li>Turntable setup &amp; alignment<span class="svc-price">$60&ndash;120</span></li>
          <li>Receiver full service<span class="svc-price">$180&ndash;320</span></li>
          <li>Speaker re-foam (per pair)<span class="svc-price">$140&ndash;200</span></li>
        </ul>
        <ul class="svc-list">
          <li>Cassette deck overhaul<span class="svc-price">$150&ndash;260</span></li>
          <li>Tube amp re-cap &amp; bias<span class="svc-price">$260&ndash;420</span></li>
          <li>Diagnosis &amp; written estimate<span class="svc-price">Free</span></li>
        </ul>
      </div>
      <div class="row">
        <a class="btn btn--cream" href="service.html">Service details &amp; booking</a>
        <a class="btn btn--ghost" href="trade-in.html" style="color:var(--paper);border-color:var(--paper)">Selling something?</a>
      </div>
    </div>
  </div>
</section>
<section class="section">
  <div class="container">
    <div class="section-head row" style="justify-content:space-between">
      <div>
        <p class="eyebrow">Upstairs calendar</p>
        <h2>Listening nights &amp; clinics</h2>
      </div>
      <a class="btn btn--ghost btn--small" href="events.html">Full calendar</a>
    </div>
    <div class="grid grid-2">
      <a class="card event-card reveal" href="events.html" style="text-decoration:none">
        <div class="event-date"><div class="d-day">17</div><div class="d-mon">Oct</div></div>
        <div class="card__body" style="padding:0">
          <h3>Fri night: African Hi-Fi Migrations</h3>
          <p>Ghanaian highlife to 80s boogie, played loud on the big system. $5, tea included.</p>
        </div>
      </a>
      <a class="card event-card reveal reveal-d1" href="events.html" style="text-decoration:none">
        <div class="event-date"><div class="d-day">25</div><div class="d-mon">Oct</div></div>
        <div class="card__body" style="padding:0">
          <h3>Saturday clinic: Belt &amp; stylus basics</h3>
          <p>Free thirty-minute clinic. Bring your turntable questions and a coffee.</p>
        </div>
      </a>
    </div>
  </div>
</section>
<section class="section section--sunk">
  <div class="container">
    <div class="section-head row" style="justify-content:space-between">
      <div>
        <p class="eyebrow">The Journal</p>
        <h2>Notes from the bench</h2>
      </div>
      <a class="btn btn--ghost btn--small" href="journal.html">All entries</a>
    </div>
    <div class="grid grid-3">
      <a class="card post-card reveal" href="journal-sansui.html" style="text-decoration:none;padding:var(--sp-4)">
        <time datetime="2026-10-06">October 6, 2026</time>
        <h3>The receiver that refused to die</h3>
        <p>Three months with a 1974 receiver that came in for a fuse and stayed for a heart transplant.</p>
      </a>
      <a class="card post-card reveal reveal-d1" href="journal-care.html" style="text-decoration:none;padding:var(--sp-4)">
        <time datetime="2026-09-22">September 22, 2026</time>
        <h3>Vinyl care without the anxiety</h3>
        <p>What actually damages records (heat, sleeves, gravity) and what everyone worries about for no reason.</p>
      </a>
      <a class="card post-card reveal reveal-d2" href="journal.html" style="text-decoration:none;padding:var(--sp-4)">
        <time datetime="2026-09-09">September 9, 2026</time>
        <h3>Why we publish our bench rates</h3>
        <p>Because a surprise repair bill is worse than a scary one you read first. Here&rsquo;s every number.</p>
      </a>
    </div>
  </div>
</section>
<section class="cta-band">
  <div class="container">
    <h2>Come make some noise</h2>
    <p>Bring a record, or pick one from the crates. The kettle&rsquo;s always on and nobody&rsquo;s in a hurry.</p>
    <div class="row">
      <a class="btn btn--cream" href="contact.html">Plan your visit</a>
      <a class="btn btn--ghost" href="trade-in.html" style="border-color:var(--ink)">Get a trade-in quote</a>
    </div>
  </div>
</section>'''

jsonld = '''<script type="application/ld+json">
{"@context":"https://schema.org","@type":"Store","name":"Halcyon Stereo","description":"Fictional vintage hi-fi and records shop in Portland, Oregon. Portfolio piece.","address":{"@type":"PostalAddress","streetAddress":"2114 SE Ankeny St","addressLocality":"Portland","addressRegion":"OR","postalCode":"97214","addressCountry":"US"},"telephone":"+1-503-555-0174","openingHours":["Tu-Sa 10:00-18:00","Su 12:00-17:00"],"foundingDate":"1974"}
</script>'''

write("index.html", "Vintage Hi-Fi & Records in Portland", 
      "Halcyon Stereo restores 1970s hi-fi and sells the records that deserve it. Fully serviced gear, honest condition reports, and a listening room that seats eleven.", 
      body, jsonld)
