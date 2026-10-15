# HALCYON pages part E: trade-in, contact, faq, privacy, terms, 404
import sys, os
sys.path.insert(0, os.path.dirname(__file__))
from framework import write

# ---------------- TRADE-IN ----------------
body = '''
<section class="page-head">
  <div class="container">
    <p class="crumbs"><a href="index.html">Home</a> / Trade-In</p>
    <h1>Sell or trade</h1>
    <p class="lede">The trade-in desk is open every day we are. Bring the gear, get a real number in minutes, choose cash or credit, and keep the story alive somewhere it gets played.</p>
  </div>
</section>
<section class="section">
  <div class="container">
    <div class="grid grid-2">
      <div>
        <h2 style="margin-bottom:var(--sp-3)">What we&rsquo;re hunting</h2>
        <ul class="svc-list">
          <li>1970s receivers, any condition<span class="svc-price">Always</span></li>
          <li>Turntables with original tonearms<span class="svc-price">Always</span></li>
          <li>Large floorstanding speakers<span class="svc-price">Usually</span></li>
          <li>Tube amplifiers and preamps<span class="svc-price">Always</span></li>
          <li>Cassette and reel decks<span class="svc-price">Usually</span></li>
          <li>Record collections, any size<span class="svc-price">Tue &amp; Sat</span></li>
          <li>Home theater-in-a-box systems<span class="svc-price">No</span></li>
          <li>Crosswalk-era boomboxes<span class="svc-price">Ask anyway</span></li>
        </ul>
      </div>
      <div>
        <h2 style="margin-bottom:var(--sp-3)">How the math works</h2>
        <ul class="svc-list">
          <li>Five minutes at the counter<span class="svc-price">Free</span></li>
          <li>Cash offer, on the spot<span class="svc-price">Fair</span></li>
          <li>Store credit, same offer<span class="svc-price">+20%</span></li>
          <li>Anything we can&rsquo;t buy<span class="svc-price">Told kindly</span></li>
        </ul>
        <p class="form-note">We buy gear to restore and resell it. That means we price against the bench cost of putting it right, which is why a dead receiver still has real value here and nowhere else.</p>
      </div>
    </div>
  </div>
</section>
<section class="section section--sunk">
  <div class="container">
    <div class="section-head">
      <p class="eyebrow">Skip the counter queue</p>
      <h2>Get a heads-up number first</h2>
      <p class="lede">Fill this in and Marcus will come in with expectations set. You still get the counter offer in person; this just starts the conversation with the facts on the table.</p>
    </div>
    <div class="card" style="max-width:40rem">
      <div class="card__body">
        <form data-demo="trade" novalidate>
          <div class="form-grid">
            <div class="field">
              <label for="tr-name">Your name</label>
              <input type="text" id="tr-name" name="name" required autocomplete="name">
            </div>
            <div class="field">
              <label for="tr-email">Email</label>
              <input type="email" id="tr-email" name="email" required autocomplete="email">
            </div>
            <div class="field">
              <label for="tr-item">What are you selling?</label>
              <input type="text" id="tr-item" name="item" placeholder="e.g. 1977 receiver, Marantz-looking, powers on" required>
            </div>
            <div class="field">
              <label for="tr-cond">Condition</label>
              <select id="tr-cond" name="condition">
                <option>Works, all original</option>
                <option>Works with issues</option>
                <option>Powers on, no sound</option>
                <option>Dead but complete</option>
                <option>Parts only</option>
              </select>
            </div>
          </div>
          <div class="field" style="margin-top:var(--sp-3)">
            <label for="tr-notes">Anything we should know</label>
            <textarea id="tr-notes" name="notes" placeholder="The full story: where it lived, what happened, whether the lamps glow."></textarea>
          </div>
          <div class="row" style="margin-top:var(--sp-4)">
            <button class="btn btn--primary" type="submit">Send it to the bench</button>
          </div>
          <p class="form-success">Thanks. This demo form doesn&rsquo;t send anything anywhere, but on the real shop floor Marcus reads these every morning.</p>
        </form>
      </div>
    </div>
  </div>
</section>
<section class="cta-band">
  <div class="container">
    <h2>One owner&rsquo;s upgrade is another&rsquo;s first system</h2>
    <p>Everything you sell goes on the floor restored, warranted, and loved. That&rsquo;s the deal.</p>
    <div class="row"><a class="btn btn--cream" href="inventory.html">See where it ends up</a></div>
  </div>
</section>'''
write("trade-in.html", "Sell or Trade", "Trade-in details for Halcyon Stereo: what we buy, how cash or store credit works, and a heads-up form for the bench. Fictional portfolio piece.", body)

# ---------------- CONTACT ----------------
body = '''
<section class="page-head">
  <div class="container">
    <p class="crumbs"><a href="index.html">Home</a> / Visit</p>
    <h1>Come sit down</h1>
    <p class="lede">Two floors on Ankeny Street, the kettle always on, and no pressure to buy anything. Parking is street and honest; the good spot is usually across from the blue door.</p>
  </div>
</section>
<section class="section">
  <div class="container">
    <div class="grid grid-2">
      <div>
        <h2 style="margin-bottom:var(--sp-3)">Hours &amp; address</h2>
        <div class="table-wrap"><table><tbody>
          <tr><th scope="row">Tuesday &ndash; Saturday</th><td>10:00 am &ndash; 6:00 pm</td></tr>
          <tr><th scope="row">Sunday</th><td>12:00 pm &ndash; 5:00 pm</td></tr>
          <tr><th scope="row">Monday</th><td>Closed. Bench day.</td></tr>
          <tr><th scope="row">Address</th><td>2114 SE Ankeny St, Portland, OR 97214</td></tr>
          <tr><th scope="row">Phone</th><td><a href="tel:+15035550174">(503) 555-0174</a></td></tr>
          <tr><th scope="row">Email</th><td><a href="mailto:hello@halcyon.example">hello@halcyon.example</a></td></tr>
        </tbody></table></div>
        <div class="card" style="margin-top:var(--sp-4)">
          <div class="card__body">
            <h3 style="margin-bottom:.4rem">Getting here</h3>
            <p style="font-size:var(--step--1)">Two blocks off the Burnside bridgehead, street parking on Ankeny and Grand. The #4 bus stops at the corner. Bike parking out front, obviously, it&rsquo;s Portland.</p>
          </div>
        </div>
      </div>
      <div>
        <h2 style="margin-bottom:var(--sp-3)">Say something first</h2>
        <div class="card"><div class="card__body">
          <form data-demo="contact" novalidate>
            <div class="form-grid">
              <div class="field">
                <label for="ct-name">Name</label>
                <input type="text" id="ct-name" required autocomplete="name">
              </div>
              <div class="field">
                <label for="ct-email">Email</label>
                <input type="email" id="ct-email" required autocomplete="email">
              </div>
            </div>
            <div class="field" style="margin-top:var(--sp-3)">
              <label for="ct-topic">What&rsquo;s this about?</label>
              <select id="ct-topic">
                <option>General question</option>
                <option>Hold a piece from inventory</option>
                <option>Repair / bench question</option>
                <option>Trade-in heads-up</option>
                <option>Listening night seats</option>
                <option>Records</option>
              </select>
            </div>
            <div class="field" style="margin-top:var(--sp-3)">
              <label for="ct-msg">Message</label>
              <textarea id="ct-msg" placeholder="The more detail, the better the answer."></textarea>
            </div>
            <div class="row" style="margin-top:var(--sp-4)">
              <button class="btn btn--primary" type="submit">Send</button>
            </div>
            <p class="form-success">Drafted. Demo note: this form doesn&rsquo;t send anywhere, but the phone number up top is real in spirit.</p>
          </form>
        </div></div>
      </div>
    </div>
  </div>
</section>
<section class="section section--sunk">
  <div class="container">
    <div class="section-head"><p class="eyebrow">First visit?</p><h2>What happens when you walk in</h2></div>
    <div class="grid grid-3">
      <div class="card reveal"><div class="card__body"><h3>You&rsquo;ll be greeted</h3><p>By Rosa or June, offered tea or coffee, and then left alone. Hovering is against shop policy and shop personality.</p></div></div>
      <div class="card reveal reveal-d1"><div class="card__body"><h3>You&rsquo;ll be asked one question</h3><p>&ldquo;What do you listen to?&rdquo; Answer it honestly and the next forty minutes get very good. Everyone&rsquo;s taste is right for something on the floor.</p></div></div>
      <div class="card reveal reveal-d2"><div class="card__body"><h3>You&rsquo;ll get to listen</h3><p>Anything can be hooked up. Bring a record or borrow one. There are two chairs, one beanbag, and a strict rule that you may stay as long as you like.</p></div></div>
    </div>
  </div>
</section>
<section class="cta-band">
  <div class="container">
    <h2>See you on Ankeny Street</h2>
    <p>Tuesday through Saturday, ten to six. Sundays noon to five. Mondays the bench dreams of capacitors.</p>
    <div class="row"><a class="btn btn--cream" href="inventory.html">Preview the floor first</a></div>
  </div>
</section>'''
write("contact.html", "Visit Us", "Hours, address, directions, and contact details for Halcyon Stereo, plus what to expect on your first visit. Fictional portfolio piece.", body)
