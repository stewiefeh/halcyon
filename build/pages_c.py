# HALCYON pages part C: records, service, events
import sys, os
sys.path.insert(0, os.path.dirname(__file__))
from framework import write, esc, record_sleeve

# ---------------- RECORDS ----------------
crates = [
    ("Crate: New Arrivals", "Restocked every Thursday morning. Roughly 200 records hit the wall weekly: collections, estate buys, and the boxes from Tuesday's trade-ins.", [
        ("Second Sun", "Atlas Motel", "oklch(66% 0.2 42)", "oklch(90% 0.04 88)", "oklch(32% 0.08 40)", "$38", "NM"),
        ("Golden Hour Radio", "Marisol Vega", "oklch(80% 0.12 88)", "oklch(64% 0.18 45)", "oklch(30% 0.06 50)", "$32", "NM"),
        ("Harbor Lights", "Slow Water", "oklch(60% 0.09 220)", "oklch(88% 0.05 85)", "oklch(27% 0.05 240)", "$26", "VG+"),
    ]),
    ("Crate: $5 and Under", "The honesty crate. Play-graded, priced to move, and absolutely loved by somebody once. Some of the best records in the building live here.", [
        ("County Fair '68", "The Vernelle County Players", "oklch(70% 0.14 100)", "oklch(88% 0.05 85)", "oklch(40% 0.09 45)", "$5", "VG"),
        ("Dance Party at the Armory", "Doc Hollis Band", "oklch(62% 0.16 30)", "oklch(84% 0.1 85)", "oklch(34% 0.08 40)", "$4", "VG"),
        ("Sunday Kitchen Radio", "Hattie Blue", "oklch(75% 0.1 60)", "oklch(30% 0.05 45)", "oklch(90% 0.03 85)", "$5", "VG+"),
    ]),
    ("Crate: Deep Cuts", "Staff picks that aren't famous and should be. Rosa's shelf. If you buy one, she will talk to you about it, and you will not regret it.", [
        ("The Long Room", "Quarry Choir", "oklch(38% 0.06 50)", "oklch(78% 0.13 85)", "oklch(90% 0.03 85)", "$30", "NM"),
        ("Basement Tapes Vol. 3", "Cedar & Rust", "oklch(58% 0.1 128)", "oklch(92% 0.03 85)", "oklch(28% 0.05 45)", "$28", "EX"),
        ("Midnight Orchard", "The Field Years", "oklch(62% 0.16 45)", "oklch(80% 0.13 88)", "oklch(28% 0.05 45)", "$24", "NM"),
    ]),
]
crate_sections = []
for title, blurb, recs in crates:
    cards = []
    for i, (t, a, c1, c2, c3, p, grade) in enumerate(recs):
        dly = f" reveal-d{(i % 3) + 1}"
        cards.append(f'''<a class="record-card reveal{dly}" href="contact.html">
  <figure style="margin:0">
    <div class="record-sleeve">{record_sleeve(i, t, a, c1, c2, c3)}</div>
    <figcaption>
      <div class="rec-artist">{esc(a)}</div>
      <div class="rec-title">{esc(t)}</div>
      <div class="card__meta"><span class="rec-price">{p}</span><span class="badge">{grade}</span></div>
    </figcaption>
  </figure>
</a>''')
    crate_sections.append(f'''
<section class="section {'section--sunk' if len(crate_sections) % 2 else ''}">
  <div class="container">
    <div class="section-head">
      <h2 style="font-stretch:108%">{esc(title)}</h2>
      <p class="lede">{blurb}</p>
    </div>
    <div class="inv-grid">{"".join(cards)}</div>
  </div>
</section>''')

body = f'''
<section class="page-head">
  <div class="container">
    <p class="crumbs"><a href="index.html">Home</a> / Records</p>
    <h1>The crates</h1>
    <p class="lede">Six thousand records, three floors, one rule: nothing goes on the floor until we play it. Grades are honest, prices are fair, and the $5 crate is sacred.</p>
  </div>
</section>
{"".join(crate_sections)}
<section class="section section--panel">
  <div class="container">
    <div class="grid grid-2">
      <div>
        <p class="eyebrow">How we grade</p>
        <h2 style="color:var(--paper);margin-bottom:var(--sp-3)">Play-graded, not eyeballed</h2>
        <p style="color:oklch(88% .03 80 / .85)">Every record that hits the wall gets played on the shop system, front and back, before it gets priced. We grade the record, not the cover, and we tell you what we heard.</p>
      </div>
      <div>
        <div class="table-wrap" style="box-shadow:none">
          <table>
            <thead><tr><th scope="col">Grade</th><th scope="col">What it means here</th></tr></thead>
            <tbody>
              <tr><th scope="row">NM</th><td>Plays clean. Maybe one tick on a bad night. The sleeve would pass a photo shoot.</td></tr>
              <tr><th scope="row">EX</th><td>Light surface sound under the music on quiet passages. Sounds great, not perfect.</td></tr>
              <tr><th scope="row">VG+</th><td>You can hear it has lived, especially between tracks. Still a good record.</td></tr>
              <tr><th scope="row">VG</th><td>Loud and proud with audible wear. Belongs in the $5 crate or priced like it.</td></tr>
            </tbody>
          </table>
        </div>
      </div>
    </div>
  </div>
</section>
<section class="section">
  <div class="container">
    <div class="section-head">
      <p class="eyebrow">Trade day</p>
      <h2>Bring us your crates</h2>
      <p class="lede">We buy records Tuesdays and Saturdays. No appointment needed for under fifty records; above that, call Rosa first so she can clear a table.</p>
    </div>
    <div class="grid grid-3">
      <div class="card reveal"><div class="card__body"><h3>What sells</h3><p>Jazz, soul, funk, reggae, 60s-70s rock, and anything local with a Portland address. Good copies of good records, that&rsquo;s the whole secret.</p></div></div>
      <div class="card reveal reveal-d1"><div class="card__body"><h3>What doesn&rsquo;t</h3><p>Sealed classical box sets from 1987, warped thrift-store specials, and anything with a name written on the label in ballpoint. We&rsquo;ll tell you kindly.</p></div></div>
      <div class="card reveal reveal-d2"><div class="card__body"><h3>How it pays</h3><p>Cash or store credit, your call at the counter. Store credit runs 20% higher and nobody has ever been mad about that math.</p></div></div>
    </div>
  </div>
</section>
<section class="cta-band">
  <div class="container">
    <h2>Thursday is restock day</h2>
    <p>The new arrivals crate goes out at 10am and the serious collectors know it.</p>
    <div class="row"><a class="btn btn--cream" href="contact.html">Get directions</a></div>
  </div>
</section>'''
write("records.html", "Record Crates", "Six thousand play-graded records in three crates: new arrivals, the $5 honesty crate, and staff deep cuts. Honest grades, fair prices, trade-ins welcome.", body)

# ---------------- SERVICE ----------------
body = '''
<section class="page-head">
  <div class="container">
    <p class="crumbs"><a href="index.html">Home</a> / Service</p>
    <h1>The service bench</h1>
    <p class="lede">Same bench since 1974, now staffed by two full-time technicians and one very opinionated parts wall. Free written estimates, honest turnaround times, published rates.</p>
  </div>
</section>
<section class="section">
  <div class="container">
    <div class="section-head">
      <p class="eyebrow">Published rates</p>
      <h2>Every price, up front</h2>
      <p class="lede">Repair quotes surprise people, so we stopped making them surprising. These are our standard bench rates; if your unit needs more, you get a written estimate before we touch another screw.</p>
    </div>
    <div class="table-wrap reveal">
      <table>
        <thead><tr><th scope="col">Service</th><th scope="col">Typical range</th><th scope="col">Turnaround</th><th scope="col">What it covers</th></tr></thead>
        <tbody>
          <tr><th scope="row">Turntable setup &amp; alignment</th><td>$60&ndash;120</td><td>Same day</td><td>Cartridge alignment, tracking force, anti-skate, speed check, level</td></tr>
          <tr><th scope="row">Turntable full service</th><td>$120&ndash;240</td><td>3&ndash;7 days</td><td>Everything above plus belt, motor, bearing service, suspension check</td></tr>
          <tr><th scope="row">Receiver or amplifier service</th><td>$180&ndash;320</td><td>5&ndash;10 days</td><td>Full clean, deox, recapping as needed, output check on both channels</td></tr>
          <tr><th scope="row">Speaker re-foam</th><td>$140&ndash;200 per pair</td><td>2&ndash;4 days</td><td>New surrounds, driver check, crossover inspection</td></tr>
          <tr><th scope="row">Cassette deck overhaul</th><td>$150&ndash;260</td><td>4&ndash;8 days</td><td>New belts and idler, head clean and demagnetize, speed calibration</td></tr>
          <tr><th scope="row">Tube amp re-cap &amp; bias</th><td>$260&ndash;420</td><td>1&ndash;2 weeks</td><td>Full electrolytic replacement, tube testing, bias set, burn-in</td></tr>
          <tr><th scope="row">Diagnosis &amp; written estimate</th><td>Free</td><td>1&ndash;2 days</td><td>What&rsquo;s wrong, what it costs, and whether it&rsquo;s worth doing. In writing.</td></tr>
        </tbody>
      </table>
    </div>
    <p class="form-note" style="margin-top:var(--sp-2)">Rush service is available at +50% when the bench has room. It usually doesn&rsquo;t, so plan ahead and we&rsquo;ll be nice about it.</p>
  </div>
</section>
<section class="section section--sunk">
  <div class="container">
    <div class="section-head">
      <p class="eyebrow">How a repair runs</p>
      <h2>No mystery, no surprise calls</h2>
    </div>
    <div class="grid grid-2">
      <div class="card reveal"><div class="card__body">
        <span class="badge badge--orange">Step 1</span>
        <h3 style="margin-top:.7rem">Intake</h3>
        <p>Bring it in or ship it to us. You get a ticket number and a technician&rsquo;s name. The estimate visit is free and usually takes a day or two.</p>
      </div></div>
      <div class="card reveal reveal-d1"><div class="card__body">
        <span class="badge badge--mustard">Step 2</span>
        <h3 style="margin-top:.7rem">The written estimate</h3>
        <p>What&rsquo;s wrong, what it costs, what it&rsquo;s worth. If the repair costs more than the unit, we say so plainly and hand it back with the diagnosis.</p>
      </div></div>
      <div class="card reveal reveal-d2"><div class="card__body">
        <span class="badge badge--avocado">Step 3</span>
        <h3 style="margin-top:.7rem">The bench</h3>
        <p>Approved work happens in order. You get one honest progress call, not five vague ones. Parts substitutions get approved by you first.</p>
      </div></div>
      <div class="card reveal reveal-d3"><div class="card__body">
        <span class="badge badge--orange">Step 4</span>
        <h3 style="margin-top:.7rem">Burn-in &amp; pickup</h3>
        <p>Every repair runs a minimum 24-hour burn-in on the bench before it goes home. You leave with a written work order and a 90-day warranty.</p>
      </div></div>
    </div>
  </div>
</section>
<section class="section">
  <div class="container">
    <div class="grid grid-2">
      <div>
        <h2 style="margin-bottom:var(--sp-3)">What we service</h2>
        <ul class="svc-list">
          <li>Turntables, all belt and direct drive<span class="svc-price">Yes</span></li>
          <li>Receivers and integrated amps<span class="svc-price">Yes</span></li>
          <li>Tube amplifiers<span class="svc-price">Yes</span></li>
          <li>Cassette decks<span class="svc-price">Yes</span></li>
          <li>Reel-to-reel machines<span class="svc-price">Select models</span></li>
          <li>8-track players<span class="svc-price">Ask Marcus</span></li>
          <li>Bluetooth speakers, phones, laptops<span class="svc-price">No</span></li>
        </ul>
      </div>
      <div>
        <h2 style="margin-bottom:var(--sp-3)">The honest fine print</h2>
        <ul class="svc-list">
          <li>Estimates are free and written<span class="svc-price">Always</span></li>
          <li>90-day warranty on repairs<span class="svc-price">Standard</span></li>
          <li>We use original parts when they exist<span class="svc-price">Preference</span></li>
          <li>Unclaimed units after 90 days<span class="svc-price">We call twice first</span></li>
          <li>Ship-ins from anywhere in the US<span class="svc-price">Welcome</span></li>
        </ul>
        <div class="row" style="margin-top:var(--sp-4)">
          <a class="btn btn--primary" href="contact.html">Book a bench slot</a>
          <a class="btn btn--ghost" href="faq.html">Common questions</a>
        </div>
      </div>
    </div>
  </div>
</section>
<section class="cta-band">
  <div class="container">
    <h2>Dead receiver? Bring the patient in.</h2>
    <p>Free estimates, written diagnoses, and a bench that&rsquo;s seen everything twice.</p>
    <div class="row"><a class="btn btn--cream" href="contact.html">Get directions</a></div>
  </div>
</section>'''
write("service.html", "Service & Repairs", "Published bench rates, free written estimates, and a 90-day repair warranty from a bench that has run since 1974. Fictional portfolio piece.", body)

# ---------------- EVENTS ----------------
events = [
    ("Fri", "17", "Oct", "African Hi-Fi Migrations", "Listening Night", "Ghanaian highlife into 80s boogie into Congolese rumba, played properly loud on the big system. $5 at the door, tea included, eleven seats, arrive early.", "7:00 pm"),
    ("Sat", "18", "Oct", "Clinic: Belt &amp; stylus basics", "Free Clinic", "Thirty minutes on the three things that ruin turntables and how to catch them early. Bring questions; leave with a checklist.", "11:00 am"),
    ("Fri", "24", "Oct", "Blue Note Deep Cuts", "Listening Night", "The famous albums everyone knows and the sessions two people bought in 1964. Hosted by Marcus, who has opinions.", "7:00 pm"),
    ("Sat", "25", "Oct", "Clinic: Setting up your first system", "Free Clinic", "Speaker placement, receiver matching, and the budget traps. Aimed at people starting out; veterans welcome anyway.", "11:00 am"),
    ("Fri", "31", "Oct", "Halloween: Horror Soundtracks on Vinyl", "Listening Night", "Goblin, John Carpenter, Ennio Morricone at his scariest. Costumes encouraged, candles provided, jump scares not.", "8:00 pm"),
    ("Sat", "1", "Nov", "Trade Day Super Session", "Trade Day", "Double-length trade day with two buyers on the floor. Bring the crates you&rsquo;ve been meaning to bring for a year.", "10:00 am"),
]
event_rows = []
for i, (dw, d, mon, title, kind, desc, time) in enumerate(events):
    dly = f" reveal-d{(i % 3) + 1}"
    event_rows.append(f'''
      <div class="card event-card reveal{dly}">
        <div class="event-date"><div class="d-day">{d}</div><div class="d-mon">{mon}</div></div>
        <div class="card__body" style="padding:0">
          <p style="margin:0 0 .3rem"><span class="badge badge--{'orange' if kind == 'Listening Night' else 'avocado'}">{kind}</span> <strong>{dw} &middot; {time}</strong></p>
          <h3>{title}</h3>
          <p style="color:var(--ink-soft);font-size:var(--step--1)">{desc}</p>
        </div>
      </div>''')
events_html = "".join(event_rows)

body = f'''
<section class="page-head">
  <div class="container">
    <p class="crumbs"><a href="index.html">Home</a> / Events</p>
    <h1>Upstairs calendar</h1>
    <p class="lede">Eleven seats, one very good system, and a strict no-phones rule during playback. Listening nights are $5 with tea; clinics are free; everybody leaves with something to listen to.</p>
  </div>
</section>
<section class="section">
  <div class="container">
    <div class="section-head">
      <p class="eyebrow">Next six weeks</p>
      <h2>What&rsquo;s on</h2>
    </div>
    <div class="grid" style="grid-template-columns:1fr;gap:var(--sp-3)">
{events_html}
    </div>
  </div>
</section>
<section class="section section--sunk">
  <div class="container">
    <div class="grid grid-2">
      <div class="ticket reveal">
        <p class="eyebrow">House rules</p>
        <h3 style="margin-top:.5rem">The listening room contract</h3>
        <p style="color:var(--ink-soft);margin-top:.6rem">Phones away during playback. Talk between sides, not over them. Applause is permitted and encouraged after side twos. The host picks the volume; arguments are part of the event.</p>
      </div>
      <div class="ticket reveal reveal-d1">
        <p class="eyebrow">Reserving</p>
        <h3 style="margin-top:.5rem">How seats work</h3>
        <p style="color:var(--ink-soft);margin-top:.6rem">Eleven seats go fast. Call the shop or ask at the counter; we don&rsquo;t take online reservations for listening nights because half the regulars refuse to use the internet and we love them.</p>
      </div>
    </div>
  </div>
</section>
<section class="cta-band">
  <div class="container">
    <h2>Friday nights are for listening</h2>
    <p>Call the shop to grab a seat. Tea&rsquo;s on, lights are low, phones are in the basket by the door.</p>
    <div class="row"><a class="btn btn--cream" href="contact.html">Call for seats</a></div>
  </div>
</section>'''
write("events.html", "Listening Nights & Clinics", "The upstairs calendar at Halcyon Stereo: $5 listening nights, free Saturday clinics, and trade days. Fictional portfolio piece.", body)
