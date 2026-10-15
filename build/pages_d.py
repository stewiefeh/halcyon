# HALCYON pages part D: journal, trade-in, contact
import sys, os
sys.path.insert(0, os.path.dirname(__file__))
from framework import write

# ---------------- JOURNAL INDEX ----------------
body = '''
<section class="page-head">
  <div class="container">
    <p class="crumbs"><a href="index.html">Home</a> / Journal</p>
    <h1>Notes from the bench</h1>
    <p class="lede">Repair stories, buying advice, and the occasional strong opinion about capacitors. Written by the people who actually do the work.</p>
  </div>
</section>
<section class="section">
  <div class="container">
    <div class="grid" style="grid-template-columns:1fr;gap:var(--sp-3)">
      <a class="card post-card reveal" href="journal-sansui.html" style="text-decoration:none;padding:var(--sp-4)">
        <time datetime="2026-10-06">October 6, 2026 &middot; Repair story</time>
        <h3>The receiver that refused to die</h3>
        <p>A 1974 receiver came in for a blown fuse and stayed for three months. What we found inside, why we replaced half the board, and why the customer was right to insist.</p>
      </a>
      <a class="card post-card reveal reveal-d1" href="journal-care.html" style="text-decoration:none;padding:var(--sp-4)">
        <time datetime="2026-09-22">September 22, 2026 &middot; Guides</time>
        <h3>Vinyl care without the anxiety</h3>
        <p>Heat, sleeves, and gravity ruin records. Inner-sleeve swirl marks and the fear of touching them do not. A calm guide to handling vinyl.</p>
      </a>
      <div class="card post-card reveal reveal-d2" style="padding:var(--sp-4)">
        <time datetime="2026-09-09">September 9, 2026 &middot; Shop policy</time>
        <h3>Why we publish our bench rates</h3>
        <p>Because a surprise repair bill is worse than a scary one you read first. The full rate card lives on the service page and always will.</p>
      </div>
      <div class="card post-card reveal reveal-d3" style="padding:var(--sp-4)">
        <time datetime="2026-08-27">August 27, 2026 &middot; Guides</time>
        <h3>Receiver watts: a field guide to numbers that lie</h3>
        <p>How to read a power spec from 1977 without getting fooled, and why 55 honest watts beats 120 fantasy ones every single time.</p>
      </div>
      <div class="card post-card reveal reveal-d4" style="padding:var(--sp-4)">
        <time datetime="2026-08-12">August 12, 2026 &middot; Repair story</time>
        <h3>The tape deck in the attic</h3>
        <p>A deck that sat in a hot attic for twenty-two years, the belts that were not belts anymore, and the family tape that survived it all.</p>
      </div>
      <div class="card post-card reveal" style="padding:var(--sp-4)">
        <time datetime="2026-07-30">July 30, 2026 &middot; Shop policy</time>
        <h3>What &ldquo;restored&rdquo; means here</h3>
        <p>The exact checklist every unit passes before it reaches the floor, written down so you can argue with it. We welcome the argument.</p>
      </div>
    </div>
  </div>
</section>
<section class="cta-band">
  <div class="container">
    <h2>One entry a month, no newsletter</h2>
    <p>The journal is just here. Check it when you&rsquo;re in the neighborhood, like the shop itself.</p>
    <div class="row"><a class="btn btn--cream" href="service.html">Bench rates</a></div>
  </div>
</section>'''
write("journal.html", "The Journal", "Repair stories and buying guides from the bench at Halcyon Stereo, written by the technicians who do the work. Fictional portfolio piece.", body)

# ---------------- JOURNAL POST 1 ----------------
body = '''
<section class="page-head">
  <div class="container">
    <p class="crumbs"><a href="index.html">Home</a> / <a href="journal.html">Journal</a> / The receiver that refused to die</p>
    <h1 style="font-stretch:112%">The receiver that refused to die</h1>
    <p class="lede">Filed under repair stories. October 6, 2026, by Marcus Okafor.</p>
  </div>
</section>
<section class="section">
  <div class="container">
    <div class="prose">
      <p>In late June a man named Dennis carried a 1974 receiver into the shop in a drywall bucket. Not a box, not a blanket: a drywall bucket, handles out, receiver wedged in at an angle that made everyone in the shop wince. The fuse was blown. That was the whole request. He wanted a fuse.</p>
      <p>We get this a lot. The blown fuse looks like the problem because it is the only thing you can see. Dennis had already bought a pack of fuses at the hardware store, put one in, watched it pop, put in another, watched it pop, and correctly stopped at three. Most people stop at one and assume the machine is dead. Stopping at three is the behavior of a man who has fixed things before, and Dennis had, for forty years, on tractors.</p>
      <h2>What the fuse was trying to say</h2>
      <p>A fuse is a messenger. When it pops once, it might just be a fuse doing its job after a power surge. When it pops three times in a row, it is telling you something downstream is drawing current it should not, and the polite thing to do is listen. In Dennis&rsquo;s case the something was a pair of output transistors that had failed short, which means the amp was essentially trying to pass the full power supply through a component the size of a thumbnail. The fuse was the only thing standing between the receiver and a small fire.</p>
      <p>This is why we always say: do not keep replacing fuses. Three is curiosity. Four is a hobby. A fuse costs a dollar and it is protecting a machine that cannot be replaced at any price.</p>
      <h2>The heart transplant</h2>
      <p>Here is where the story stops being a standard repair. Dennis&rsquo;s receiver was a lower-line model from a company whose higher-line models get all the attention. The outputs it needed were no longer made, the modern substitutes had different pinouts, and the standard answer in this situation is: pull the output stage, fit a modern module, call it a day. Most shops would have done that and Dennis would have been happy.</p>
      <p>Except Dennis had owned this receiver since he was twenty-two years old. It was the first thing he bought with his first real paycheck, and the five hundred albums in his garage had all been played on it. He did not want a module. He wanted this receiver.</p>
      <blockquote>&ldquo;I don&rsquo;t need it loud,&rdquo; he said. &ldquo;I need it to be the same one.&rdquo;</blockquote>
      <p>So we did it the long way. Marcus spent a week sourcing genuine NOS (new old stock) output transistors from two suppliers and a forum for people who hoard 1970s semiconductors, which is a real community and honestly a lovely one. He matched the pair within 2%. He recapped the power supply, replaced every solder joint the heat had darkened, and rebuilt the switch contacts. The receiver came off the bench drawing the current it drew in 1974, at the idle bias the manual specifies, which almost none of them still do.</p>
      <h2>The part nobody expects</h2>
      <p>When Dennis picked it up, he brought the bucket back. Not for returns. He said the receiver had come in the bucket and it should leave the same way, because that was how the story went. It played three hours of his first album, a 1971 record with a warped jacket and a perfect pressing, before he carried it out.</p>
      <p>The bill was $340. The fuse was $1. Everything in between was the difference between a working receiver and his receiver. That gap is the whole job.</p>
      <p><em>Thinking about a repair of your own? The <a href="service.html">bench rates</a> are published and the estimate is free.</em></p>
    </div>
  </div>
</section>
<section class="section section--sunk">
  <div class="container">
    <div class="grid grid-3">
      <div class="stat"><div class="n">3</div><div class="l">months on the bench</div></div>
      <div class="stat"><div class="n">2%</div><div class="l">output transistor matching</div></div>
      <div class="stat"><div class="n">1971</div><div class="l">first record back on the platter</div></div>
    </div>
  </div>
</section>
<section class="cta-band">
  <div class="container">
    <h2>Your machine has a story too</h2>
    <p>Bring it in. The estimate is free and the fuse advice is, as ever, stop at three.</p>
    <div class="row"><a class="btn btn--cream" href="service.html">Book the bench</a></div>
  </div>
</section>'''
write("journal-sansui.html", "The receiver that refused to die", "A three-month repair story from the Halcyon Stereo bench: blown fuses, NOS transistors, and why a $1 part was protecting an irreplaceable machine.", body)

# ---------------- JOURNAL POST 2 ----------------
body = '''
<section class="page-head">
  <div class="container">
    <p class="crumbs"><a href="index.html">Home</a> / <a href="journal.html">Journal</a> / Vinyl care without the anxiety</p>
    <h1 style="font-stretch:112%">Vinyl care without the anxiety</h1>
    <p class="lede">Filed under guides. September 22, 2026, by Rosa Trevino.</p>
  </div>
</section>
<section class="section">
  <div class="container">
    <div class="prose">
      <p>Every week somebody handles a record at my counter like it is made of soap bubbles and ancient prophecy. And every week the same person asks whether the faint marks in the light are scratches. They are usually not scratches. They are almost never scratches. Let&rsquo;s fix the fear first, then the records.</p>
      <h2>The three things that actually ruin records</h2>
      <p>Short list, because the real list is short.</p>
      <ul>
        <li><strong>Heat.</strong> A record on a car dashboard in July is a record that will never be flat again. Vinyl warps around 140&deg;F and it does not ask permission first.</li>
        <li><strong>Sleeves.</strong> Paper inner sleeves shed and scuff. Every year of storage in a rough paper sleeve does more damage than a hundred careful plays.</li>
        <li><strong>Gravity and pressure.</strong> Records stacked flat bend. Records stored leaning warp. Upright and snug, like books, is the whole secret.</li>
      </ul>
      <p>That is it. Dust is manageable, fingerprints wash off, and the marks that scare you in raking light are usually sleeve scuffs that do not reach the groove walls at all.</p>
      <h2>What you can stop worrying about</h2>
      <p><strong>Touching the surface.</strong> Holding a record by edge and label is good practice, but a thumbprint on the playing surface washes off with a record brush and cleaner. It is not a wound. It is a smudge.</p>
      <p><strong>Inner-sleeve swirl.</strong> Those fine marks under a bright bulb look devastating and usually inaudible. The groove is deeper than the scuff. Play the record. If you cannot hear it over the music, it does not exist.</p>
      <p><strong>Playing a VG record.</strong> A visually worn record that plays fine is fine. Grades describe how it sounds to us, not a moral judgment about how you treat your things.</p>
      <p><strong>Playing it &ldquo;too much.&rdquo;</strong> A well-adjusted stylus on a clean record takes thousands of plays to show wear. The records that die young die from bad needles, not from love.</p>
      <h2>The five-minute routine worth doing</h2>
      <ol style="padding-left:1.3rem">
        <li>Carbon-fiber brush before every play. Three spins, light pressure. This is the whole daily routine.</li>
        <li>Change paper inners for poly-lined sleeves as you touch each record. Do it gradually, crate by crate.</li>
        <li>Store everything upright. Full shelves, no leaning, away from radiators and sunny windows.</li>
        <li>Deep-clean a record only when it is visibly dirty or audibly noisy. Wet cleaning is a tool, not a religion.</li>
        <li>Replace your stylus on schedule. A worn stylus is the single most destructive object in your house and it costs $30 to retire.</li>
      </ol>
      <blockquote>The stylus thing bears repeating: a worn needle grinding through a groove is the only way a careful listener destroys their records. Check it yearly.</blockquote>
      <h2>What we do at the counter</h2>
      <p>Every used record that goes on our wall gets played, front and back, before it gets graded. If we hear a tick on track three, the tag says so. The grade is the record&rsquo;s report card, not its eulogy, and it is written by people who genuinely want you to play this thing every Sunday for thirty years.</p>
      <p><em>Want your crates graded, priced, or rescued? <a href="trade-in.html">Trade day details are here.</a></em></p>
    </div>
  </div>
</section>
<section class="section section--sunk">
  <div class="container">
    <div class="grid grid-3">
      <div class="stat"><div class="n">3</div><div class="l">things that actually ruin vinyl</div></div>
      <div class="stat"><div class="n">$30</div><div class="l">cost of retiring a worn stylus</div></div>
      <div class="stat"><div class="n">1000s</div><div class="l">of plays a clean record can take</div></div>
    </div>
  </div>
</section>
<section class="cta-band">
  <div class="container">
    <h2>Play the records</h2>
    <p>They were pressed to be played. Everything else is housekeeping.</p>
    <div class="row"><a class="btn btn--cream" href="records.html">See the crates</a></div>
  </div>
</section>'''
write("journal-care.html", "Vinyl care without the anxiety", "A calm guide to vinyl care: the three things that actually ruin records, the fears you can drop, and the five-minute routine worth keeping.", body)
