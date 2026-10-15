# HALCYON pages part F: faq, privacy, terms, 404
import sys, os
sys.path.insert(0, os.path.dirname(__file__))
from framework import write

FAQ = [
    ("Do I need an appointment to listen to gear?",
     "No. Walk in, tell us what you listen to, and we&rsquo;ll set something up. The listening room is first-come unless a listening night is running upstairs."),
    ("Is your gear really all restored?",
     "Every unit on the floor went through the bench before it was priced. The tag lists exactly what was done, part by part, and any remaining flaws."),
    ("What does the 90-day warranty cover?",
     "Parts and labor on anything we serviced, in-store. If it fails, bring it back and it goes to the front of the bench. We&rsquo;ve honored maybe a dozen claims in five years."),
    ("Can I trade in gear I haven&rsquo;t tested?",
     "Yes. Dead units still have real value here because we can restore them. The offer reflects the bench cost of putting it right, which we&rsquo;ll walk you through."),
    ("Do you ship?",
     "Speakers and turntables we prefer to hand you in person, because freight companies have opinions about vintage walnut. Small units ship anywhere in the US, double-boxed, fully insured."),
    ("Do you buy record collections?",
     "Tuesdays and Saturdays. Under fifty records needs no appointment; above that, call Rosa first so she can clear a table and a morning."),
    ("How much is my receiver worth?",
     "Depends on model, condition, and whether the lamps still glow. Photos and a model number by email gets a rough range the same day; the real number happens at the counter."),
    ("Can you service something I bought somewhere else?",
     "Yes, that&rsquo;s most of the bench&rsquo;s work. Published rates apply, the estimate is free, and we&rsquo;ll tell you honestly when a unit isn&rsquo;t worth fixing."),
    ("Do you sell new equipment?",
     "A short shelf of cartridges, styli, belts, cleaning supplies, and sleeves. Everything else is vintage, because that&rsquo;s the whole point of the building."),
    ("Is the $5 crate really $5?",
     "Everything in it is five dollars or less, always. It restocks constantly and the good ones go fast. This is public information and we are not taking it back."),
    ("Can I bring my own record to test a system?",
     "Please do. It is the single best way to buy hi-fi and we wish everyone did it. Bring three or four you know by heart."),
    ("Do listening nights sell out?",
     "Regularly. Eleven seats is eleven seats. Call the shop that week; if it&rsquo;s full we&rsquo;ll put you on the next one&rsquo;s list and slip you a preview of the setlist."),
    ("What payments do you take?",
     "Cash, cards, and store credit. Layaway exists for pieces over $500: a third down, ninety days to finish, and we keep it safe and played on the bench."),
    ("Why should I buy 50-year-old electronics?",
     "Because it was built to be repaired, by people who assumed you would repair it. The good 1970s units outperform new gear at the same price and will still be here in 2076."),
]
faq_items = []
for i, (q, a) in enumerate(FAQ):
    faq_items.append(f'''
      <div class="faq-item">
        <h3><button class="faq-q" aria-expanded="{'true' if i == 0 else 'false'}" aria-controls="faq-a{i}" id="faq-q{i}">{q}<span class="chev" aria-hidden="true">+</span></button></h3>
        <div class="faq-a" id="faq-a{i}" role="region" aria-labelledby="faq-q{i}"{' hidden' if i else ''}>{a}</div>
      </div>''')
faq_html = "".join(faq_items)

body = f'''
<section class="page-head">
  <div class="container">
    <p class="crumbs"><a href="index.html">Home</a> / FAQ</p>
    <h1>Questions, answered</h1>
    <p class="lede">The fourteen things people ask most at the counter, answered the way we answer them at the counter.</p>
  </div>
</section>
<section class="section">
  <div class="container" style="max-width:52rem">
{faq_html}
  </div>
</section>
<section class="cta-band">
  <div class="container">
    <h2>Something we missed?</h2>
    <p>Call the shop. A human who owns the answers picks up.</p>
    <div class="row"><a class="btn btn--cream" href="contact.html">Contact details</a></div>
  </div>
</section>'''
write("faq.html", "Frequently Asked Questions", "The fourteen most common questions at Halcyon Stereo, answered plainly: restoration, warranty, trade-ins, shipping, the $5 crate, and listening nights.", body)

# ---------------- PRIVACY ----------------
body = '''
<section class="page-head">
  <div class="container">
    <p class="crumbs"><a href="index.html">Home</a> / Privacy</p>
    <h1>Privacy</h1>
    <p class="lede">Short version: this site collects nothing, stores nothing, and phones nobody. The longer version is barely longer.</p>
  </div>
</section>
<section class="section">
  <div class="container">
    <div class="prose">
      <h2>What this site collects</h2>
      <p>Nothing. There are no analytics scripts, no advertising trackers, no cookies, no sign-in, no third-party embeds. The site is static files served by a content delivery network.</p>
      <h2>The forms</h2>
      <p>The forms on this site are demonstration forms. You can type into them and press send, and nothing leaves your browser: no data is transmitted, stored, or seen by anyone. They exist to show how the real shop&rsquo;s forms would work.</p>
      <h2>The theme toggle</h2>
      <p>The lamp switch remembers your choice using your browser&rsquo;s local storage on your own device. It never leaves your device, and clearing your browser data clears it.</p>
      <h2>Fonts and images</h2>
      <p>Fonts and artwork are served from this site itself, so your browser talks to exactly one server: ours. Nothing is fetched from a font CDN or an ad network.</p>
      <h2>If you contact the real shop</h2>
      <p>Halcyon Stereo is a fictional business created as a portfolio piece. On a real shop&rsquo;s site, this section would describe how phone calls and emails are handled. As written: we don&rsquo;t have a mailing list, we don&rsquo;t sell information, and the only records kept are the repair tickets on work you brought in.</p>
      <h2>Questions</h2>
      <p>About this page or the site, use the contact page. Everything here is fictional and built as a design portfolio piece.</p>
    </div>
  </div>
</section>'''
write("privacy.html", "Privacy Policy", "Privacy details for the Halcyon Stereo demo site: no analytics, no cookies, no trackers, and demonstration forms that transmit nothing.", body)

# ---------------- TERMS ----------------
body = '''
<section class="page-head">
  <div class="container">
    <p class="crumbs"><a href="index.html">Home</a> / Terms</p>
    <h1>Terms of use</h1>
    <p class="lede">The rules for using this website, which are short because the site does very little and does it on purpose.</p>
  </div>
</section>
<section class="section">
  <div class="container">
    <div class="prose">
      <h2>What this site is</h2>
      <p>Halcyon Stereo is a fictional business. The site exists as a design and development portfolio piece. All products, prices, people, events, phone numbers, and history described here are invented. Any resemblance to a real shop on Ankeny Street is the sincerest form of flattery and entirely coincidental.</p>
      <h2>Using the site</h2>
      <p>Browse freely. The pages, code, and artwork were created for this portfolio piece; the design system and illustrations may not be reproduced commercially without permission. Links back and credit are always welcome.</p>
      <h2>The demonstration forms</h2>
      <p>Forms on this site do not transmit information. Submitting one produces a friendly confirmation and no side effects anywhere.</p>
      <h2>Accuracy</h2>
      <p>Prices, hours, and inventory listings are illustrative and may not match anything real, including next week&rsquo;s version of this same fictional shop. The <a href="faq.html">FAQ</a> and <a href="service.html">service pages</a> demonstrate how a real shop would publish this information.</p>
      <h2>Accessibility</h2>
      <p>The site aims for WCAG 2.2 AA: keyboard navigable, screen-reader labeled, high-contrast, and fully functional with animations disabled for visitors who prefer reduced motion. If something doesn&rsquo;t work for you, that&rsquo;s a bug worth knowing about.</p>
      <h2>Contact</h2>
      <p>Use the <a href="contact.html">contact page</a> for any question about this piece.</p>
    </div>
  </div>
</section>'''
write("terms.html", "Terms of Use", "Terms of use for the Halcyon Stereo portfolio site: a fictional shop, demonstration forms, and accessibility commitments.", body)

# ---------------- 404 ----------------
body = '''
<section class="section" style="padding-block:clamp(4rem,12vw,9rem)">
  <div class="container tc">
    <p class="eyebrow">Error 404</p>
    <h1 style="font-stretch:120%">Needle skipped</h1>
    <p class="lede" style="margin:var(--sp-3) auto 0">That page isn&rsquo;t on the shelf. Either it moved, it sold, or the URL has a typo wearing a disguise.</p>
    <div class="row" style="justify-content:center;margin-top:var(--sp-4)">
      <a class="btn btn--primary" href="index.html">Back to the shop floor</a>
      <a class="btn btn--ghost" href="inventory.html">Browse inventory</a>
    </div>
    <p style="margin-top:var(--sp-5);color:var(--ink-faint);font-weight:600">Popular destinations: <a href="records.html">records</a> &middot; <a href="service.html">service</a> &middot; <a href="events.html">events</a> &middot; <a href="faq.html">FAQ</a></p>
  </div>
</section>'''
write("404.html", "Page not found", "The page you were looking for isn't on the shelf. Needle skipped; here's the way back.", body)
