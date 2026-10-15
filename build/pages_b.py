# HALCYON pages part B: about, inventory, gear details
import sys, os
sys.path.insert(0, os.path.dirname(__file__))
from framework import write, esc
from pages_a import INVENTORY, ART, inv_card
from framework import art_turntable, art_receiver, art_speakers

# ---------------- ABOUT ----------------
body = '''
<section class="page-head">
  <div class="container">
    <p class="crumbs"><a href="index.html">Home</a> / About</p>
    <h1>Same block, 54 years</h1>
    <p class="lede">A hi-fi shop that survived the CD era, the streaming era, and three economic catastrophes by doing one simple thing: never selling anything broken.</p>
  </div>
</section>
<section class="section">
  <div class="container">
    <div class="grid" style="grid-template-columns:1fr">
      <div class="prose">
        <p>Gus Halvorsen opened Halcyon Stereo in the spring of 1974, in a former upholstery shop on Ankeny Street, with four shelves of receivers, a workbench he built himself, and a firm belief that a receiver should be repaired, not replaced. He was opinionated about capacitors. He was right about most things.</p>
        <p>The shop grew the way good shops do: slowly, by reputation. Gus serviced the gear other stores wouldn&rsquo;t touch. He taught half the stereo technicians in Portland how to set a cartridge. He kept the listening room open to anyone who wanted to sit and actually hear a system before buying it, which in 1978 was a radical idea and today is still rare enough to be one.</p>
        <p>June Halvorsen took over in 2009 after twenty years at the bench. She kept every rule and added exactly one: every unit gets a written condition report, flaws and all, posted right on the tag. &ldquo;Surprise is for birthday parties,&rdquo; she says, &ldquo;not for amplifiers.&rdquo;</p>
        <blockquote>&ldquo;A good receiver isn&rsquo;t nostalgia. It&rsquo;s engineering that was finished on the first try.&rdquo;<br><span style="font-style:normal;font-size:.9rem">— Gus Halvorsen, shop sign, 1974-present</span></blockquote>
      </div>
    </div>
  </div>
</section>
<section class="section section--sunk">
  <div class="container">
    <div class="section-head">
      <p class="eyebrow">The long version</p>
      <h2>Five decades, condensed</h2>
    </div>
    <ul class="timeline">
      <li class="reveal">
        <span class="t-year">1974</span>
        <h3>Gus opens the doors</h3>
        <p>Four shelves of receivers, one workbench, and the first customer, a violinist who stayed for three hours listening to two speakers she could not afford. She bought them anyway. She still comes in.</p>
      </li>
      <li class="reveal">
        <span class="t-year">1983</span>
        <h3>The CD scare</h3>
        <p>Half the industry said analog was finished. Gus rented the vacant storefront next door and doubled his service capacity instead. The bet paid for the whole block by 1986.</p>
      </li>
      <li class="reveal">
        <span class="t-year">1998</span>
        <h3>The listening room</h3>
        <p>The upstairs office became a proper listening room: eleven seats, acoustic panels June&rsquo;s mother upholstered, and the big system that has anchored every Friday night since.</p>
      </li>
      <li class="reveal">
        <span class="t-year">2009</span>
        <h3>June takes over</h3>
        <p>Second-generation ownership. Written condition reports become policy, the trade-in desk opens, and the first Saturday clinic runs out of seats in an hour.</p>
      </li>
      <li class="reveal">
        <span class="t-year">2026</span>
        <h3>The long boom</h3>
        <p>Vintage hi-fi is mainstream again and the bench is busier than it has ever been. We are hiring a third technician and the waiting list for tube amps is honest about being a waiting list.</p>
      </li>
    </ul>
  </div>
</section>
<section class="section">
  <div class="container">
    <div class="section-head">
      <p class="eyebrow">The people at the bench</p>
      <h2>Who you&rsquo;ll actually meet</h2>
    </div>
    <div class="grid grid-3">
      <div class="card team-card reveal">
        <div class="avatar" style="background:var(--mustard)">JH</div>
        <h3>June Halvorsen</h3>
        <div class="role">Owner · second generation</div>
        <p>Started sweeping the floor in 1989, rebuilt her first amplifier at nineteen. Will absolutely tell you when the cheap option is the right one.</p>
      </div>
      <div class="card team-card reveal reveal-d1">
        <div class="avatar" style="background:var(--orange)">MO</div>
        <h3>Marcus Okafor</h3>
        <div class="role">Head of service</div>
        <p>Fifteen years on the bench, specialist in tape machines and anything with a VU meter. Answers &ldquo;is it fixable&rdquo; in under a day.</p>
      </div>
      <div class="card team-card reveal reveal-d2">
        <div class="avatar" style="background:var(--avocado);color:var(--cream-hi)">RT</div>
        <h3>Rosa Trevino</h3>
        <div class="role">Records &amp; events</div>
        <p>Curates the crates and books the Friday nights. Knows what you&rsquo;ll like better than you do; has never once been wrong about ambient.</p>
      </div>
    </div>
  </div>
</section>
<section class="cta-band">
  <div class="container">
    <h2>Fifty-four years in, still turning knobs</h2>
    <p>The shop is open six days a week and the bench takes walk-in estimates free.</p>
    <div class="row">
      <a class="btn btn--cream" href="contact.html">Visit us</a>
      <a class="btn btn--ghost" href="inventory.html" style="border-color:var(--ink)">See what&rsquo;s on the floor</a>
    </div>
  </div>
</section>'''
write("about.html", "About Us", "The story of Halcyon Stereo, a fictional Portland vintage hi-fi shop open since 1974, and the people who run the bench.", body)

# ---------------- INVENTORY ----------------
inv_cards = "".join(inv_card(item, i) for i, item in enumerate(INVENTORY))
body = f'''
<section class="page-head">
  <div class="container">
    <p class="crumbs"><a href="index.html">Home</a> / Inventory</p>
    <h1>The floor</h1>
    <p class="lede">Everything here is restored, tested, warranted for 90 days, and hooked up. The list updates when the bench ships something new, which is most weeks.</p>
  </div>
</section>
<section class="section">
  <div class="container">
    <div class="inv-layout">
      <aside class="filters" aria-label="Inventory filters">
        <h2>Filter</h2>
        <div class="filter-group">
          <label class="filter-label" for="inv-search">Search</label>
          <input type="search" id="inv-search" placeholder="Try &lsquo;turntable&rsquo; or &lsquo;1977&rsquo;">
        </div>
        <fieldset class="filter-group">
          <legend>Type</legend>
          <label class="check"><input type="checkbox" value="turntable"> Turntables</label>
          <label class="check"><input type="checkbox" value="receiver"> Receivers &amp; tuners</label>
          <label class="check"><input type="checkbox" value="speakers"> Speakers</label>
          <label class="check"><input type="checkbox" value="amp"> Amps</label>
          <label class="check"><input type="checkbox" value="deck"> Cassette decks</label>
        </fieldset>
        <fieldset class="filter-group">
          <legend>Sort</legend>
          <label class="filter-label" for="inv-sort" style="display:none">Sort</label>
          <select id="inv-sort">
            <option value="featured">Featured first</option>
            <option value="price-asc">Price: low to high</option>
            <option value="price-desc">Price: high to low</option>
          </select>
        </fieldset>
        <p class="range-note">Prices include the full service and the 90-day warranty. Every unit is priced with its story attached, flaws included.</p>
      </aside>
      <div>
        <p class="inv-count" data-inv-count>{len(INVENTORY)} of {len(INVENTORY)} pieces</p>
        <div class="inv-grid" data-inventory>
{inv_cards}
        </div>
        <div class="inv-empty" hidden>
          <p>Nothing matches that combination right now.</p>
          <p>Clear a filter, or call the shop: the good stuff often moves before it photographs.</p>
        </div>
      </div>
    </div>
  </div>
</section>
<section class="cta-band">
  <div class="container">
    <h2>Looking for something specific?</h2>
    <p>Tell the bench what you&rsquo;re hunting. We get trade-ins weekly and regulars get first calls.</p>
    <div class="row"><a class="btn btn--cream" href="trade-in.html">Request a want-list</a></div>
  </div>
</section>'''
write("inventory.html", "Current Inventory", "Fully restored vintage turntables, receivers, speakers, amps, and cassette decks. Every unit serviced, tested, and honestly described.", body)

# ---------------- GEAR DETAIL PAGES ----------------
def detail_page(slug, name, meta_desc, hero_blurb, specs_rows, story, bench_notes, price, year, art_fn, badge):
    rows = "\n".join(f"<tr><th scope='row'>{esc(k)}</th><td>{esc(v)}</td></tr>" for k, v in specs_rows)
    notes = "\n".join(f"<li>{n}</li>" for n in bench_notes)
    body = f'''
<section class="page-head">
  <div class="container">
    <p class="crumbs"><a href="index.html">Home</a> / <a href="inventory.html">Inventory</a> / {esc(name)}</p>
    <h1 style="font-stretch:108%">{esc(name)}</h1>
    <p class="lede">{hero_blurb}</p>
  </div>
</section>
<section class="section">
  <div class="container">
    <div class="grid" style="grid-template-columns:1fr">
      <div class="card reveal" style="max-width:44rem;margin-inline:auto;width:100%">
        <div class="card__media">{art_fn()}</div>
      </div>
      <div class="row" style="justify-content:center;margin-top:var(--sp-3)">
        <span class="badge badge--orange">{esc(badge)}</span>
        <span class="badge">{esc(year)}</span>
        <span class="price" style="font-size:1.5rem">${price:,.0f}</span>
      </div>
    </div>
  </div>
</section>
<section class="section section--sunk">
  <div class="container">
    <div class="grid grid-2">
      <div>
        <h2 style="margin-bottom:var(--sp-3)">Specifications</h2>
        <div class="table-wrap"><table><tbody>
{rows}
        </tbody></table></div>
      </div>
      <div>
        <h2 style="margin-bottom:var(--sp-3)">On the bench</h2>
        <ul class="svc-list">
{notes}
        </ul>
        <div class="row" style="margin-top:var(--sp-4)">
          <a class="btn btn--primary" href="contact.html">Reserve for in-store pickup</a>
          <a class="btn btn--ghost" href="records.html">Pair it with a record</a>
        </div>
        <p class="form-note">Reservations hold for five days, no deposit. Phone is faster: (503) 555-0174.</p>
      </div>
    </div>
  </div>
</section>
<section class="section">
  <div class="container">
    <div class="prose">
      <h2>The story</h2>
      {story}
    </div>
  </div>
</section>
<section class="cta-band">
  <div class="container">
    <h2>Hear it before you haul it</h2>
    <p>Every unit stays hooked up in the shop until it leaves with you.</p>
    <div class="row"><a class="btn btn--cream" href="contact.html">Plan a visit</a></div>
  </div>
</section>'''
    write(slug, name, meta_desc, body)

detail_page(
    "turntable-tt500.html", "TT-500 Belt-Drive Turntable",
    "A 1976 suspended-chassis belt-drive turntable, fully restored with new belt, rebuilt motor, and aligned tonearm. Fictional portfolio piece.",
    "The suspended chassis that made 1976 worth remembering. Floating suspension, new belt, rebuilt motor, and a tonearm aligned to within a hair.",
    [("Year", "1976"), ("Drive", "Belt, new rubber, correct OEM spec"), ("Speeds", "33 1/3 and 45 rpm, quartz-checked"),
     ("Tonearm", "9-inch static-balance, aligned with protractor"), ("Cartridge", "New MM cartridge fitted and aligned"),
     ("Suspension", "Re-tuned, level checked on a calibrated bubble"), ("Plinth", "Original walnut veneer, minor honest wear"),
     ("Dust cover", "Original, one small repaired crack at the rear edge"), ("Warranty", "90 days, parts and labor, in-store")],
    '''<p>The TT-500 was the receiver of the turntable world: not the most exotic name, but the one that showed up in every decent system between 1975 and 1980 and simply worked. This one spent its first life in a southeast Portland living room and its second in a garage, which is where garage finds usually go to die.</p>
<p>Instead it came to us with a dead motor bearing and twenty-eight years of dust. The motor came apart cleanly, the bearing got repacked, the belt got replaced with the correct profile, and the suspension was re-tuned until the plinth floated the way the factory intended. It now measures wow and flutter inside original spec, which is the kind of sentence that makes Marcus unreasonably happy.</p>''',
    ["Motor rebuilt, bearing repacked, new OEM-spec belt", "Tonearm aligned with a two-point protractor",
     "New moving-magnet cartridge fitted and set", "Speed checked at 33 1/3 and 45 with a strobe",
     "Suspension re-tuned and leveled", "RCA grounds replaced; hum verified silent at volume"],
    895.0, "1976", art_turntable, "Restored")

detail_page(
    "receiver-r70.html", "R-70 AM/FM Receiver",
    "A 1974 75-watt vintage stereo receiver, fully serviced with cleaned switches, new dial lamps, and recapped power supply. Fictional portfolio piece.",
    "Seventy-five honest watts, a warm blue dial, and switches that feel like they mean it. The definitive 1974 living-room centerpiece.",
    [("Year", "1974"), ("Power", "75 watts per channel into 8 ohms, both channels driven"),
     ("Tuner", "Analog AM/FM, aligned and sensitive"), ("Phono stage", "MM input, recapped and verified flat"),
     ("Switches", "All deoxed and cycled; no crackle at any position"), ("Lamps", "Dial and meters re-lamped, warm white"),
     ("Faceplate", "Original brushed silver, light honest patina"), ("Warranty", "90 days, parts and labor, in-store")],
    '''<p>Seventy-four was the year receiver design got generous. Everything got bigger: the dial, the heat sinks, the knobs, the optimism. The R-70 is that moment in a box, and this particular box arrived with a dead channel and a story about a New Year&rsquo;s party nobody wanted to detail.</p>
<p>The dead channel turned out to be a cracked solder joint and one leaky coupling capacitor. Everything else was tired rather than broken: every switch got cleaned and cycled until it clicked like new, the power supply got fresh capacitors, and the dial lamps were replaced with warm whites so the blue dial reads like dusk instead of surgery. It has been playing the shop floor for six weeks straight now, which is our actual burn-in policy.</p>''',
    ["Both channels verified at rated power into 8 ohms", "Every switch and control deoxed and cycled",
     "Power supply recapped with modern equivalents", "Tuner aligned for sensitivity and stereo separation",
     "Phono stage recapped and RIAA-verified", "New warm-white dial and meter lamps"],
    640.0, "1974", art_receiver, "Bench Fresh")

detail_page(
    "speakers-ls6.html", "LS-6 Floorstanding Loudspeakers",
    "A restored pair of 1975 floorstanding loudspeakers with re-foamed woofers, recapped crossovers, and original grilles. Fictional portfolio piece.",
    "Big cabinets with bigger manners. Re-foamed woofers, recapped crossovers, original grilles, and bass you feel in the floorboards.",
    [("Year", "1975"), ("Configuration", "3-way, 15-inch woofer, midrange dome, cone tweeter"),
     ("Sensitivity", "91 dB, easy load for any honest receiver"), ("Impedance", "8 ohms nominal"),
     ("Woofers", "Professional re-foam, both drivers"), ("Crossovers", "Recapped, matched within 0.5 dB"),
     ("Cabinets", "Original veneer, re-oiled, one repaired corner"), ("Grilles", "Original cloth, intact"),
     ("Warranty", "90 days, parts and labor, in-store")],
    '''<p>Fifteen-inch woofers went out of fashion for reasons that had nothing to do with how they sound. They move air the way a church door moves air, and the LS-6 was designed by people who understood that and built the cabinet to survive it.</p>
<p>This pair came out of a church basement rec hall, where they had faithfully played every potluck and wedding since the Carter administration. The surrounds were dust, the crossovers were drifting, and the cabinets were filthy but fundamentally perfect. Re-foamed, recapped, re-oiled, and matched, they now do the thing big speakers do: make a room feel like a room. Not subtle. Correct.</p>''',
    ["Both woofers professionally re-foamed", "Crossover capacitors replaced, pairs matched",
     "Drivers verified and paired within 0.5 dB", "Cabinets re-oiled, one corner professionally repaired",
     "Original grilles cleaned and intact", "Bass port damping renewed"],
    780.0, "1975", art_speakers, "Pair")
