# -*- coding: utf-8 -*-
"""English landing page for vione.app/en/ (hreflang alternate of /)."""
SITE = 'https://vione.app'
MOD = '2026-09-02'

def pic(name, alt, w=300):
    return f'<picture><source srcset="/assets/img/{name}.webp" type="image/webp"><img src="/assets/img/{name}.png" alt="{alt}" width="{w}" loading="lazy"></picture>'

FAQ_EN = [
    ("What is VI One?", "VI One (브이원) is an AI CRM app for small business owners such as salons, nail studios, cafes and restaurants in Korea. It combines booking management, customer management (automatic VIP / regular / new / no-show tags), quick sales logging, customer messaging over SMS, KakaoTalk and WhatsApp, and an AI FAQ auto-reply (Pro) in one iPhone app."),
    ("How much does it cost?", "Starter is free (bookings, customers, quick sales logs, messaging). Pro is ₩39,000 per month or ₩249,000 per year and adds the AI FAQ draft and auto-reply. There is no free trial period; subscriptions are handled through Apple in-app purchase."),
    ("How does the AI reply work?", "You fill in your shop's FAQ (hours, parking, booking, prices, location). When a customer asks, the AI drafts an answer from the closest FAQ entry and you review it before sending. If the question is not in your FAQ, the AI does not make anything up — it hands the question to you, and your answer becomes a new FAQ entry."),
    ("Which channels are supported?", "From a customer's profile you can contact them by SMS, WhatsApp, KakaoTalk (copy-and-paste, since KakaoTalk has no public deep link to open a chat by phone number) and phone. Sent messages are logged in the customer's communication history. Inbound SMS/WhatsApp can be collected in the Communication tab once an inbound number is connected."),
    ("Is my data safe?", "Each shop's data is stored in isolation from other shops, and you can delete your account and data at any time from Settings inside the app."),
    ("Which devices?", "iPhone (iOS) via the App Store, in Korean and English. Android is under review."),
]

def faq_ld(items):
    return {"@context": "https://schema.org", "@type": "FAQPage", "mainEntity": [{"@type": "Question", "name": q, "acceptedAnswer": {"@type": "Answer", "text": a}} for q, a in items]}

def pages(cta):
    faq = ''.join(f'<details><summary>{q}</summary><div class="a">{a}</div></details>' for q, a in FAQ_EN)
    return [dict(path='/en/', lang='en', priority=0.8, modified=MOD, alt=[('ko', '/'), ('en', '/en/')], ld=[faq_ld(FAQ_EN)],
        title='VI One — AI CRM for Small Business Owners in Korea',
        desc='iPhone AI CRM for Korean salons, cafes and restaurants: bookings, VIP/regular/no-show tags, sales logs, SMS·KakaoTalk·WhatsApp messaging, human-in-the-loop AI FAQ replies. Free Starter.',
        body=f"""
<section class="hero"><div class="wrap">
  <div>
    <span class="kicker">AI CRM for small business · iPhone · Korea</span>
    <h1>You serve the guest.<br><span class="em">AI handles the repeat questions.</span></h1>
    <p class="lede"><strong>VI One (브이원)</strong> is an AI CRM built for salons, nail studios, cafes and restaurants where one owner handles bookings, customers and every message. Bookings, customer history, quick sales logs, SMS / KakaoTalk / WhatsApp messaging, and an AI FAQ auto-reply (Pro) — in one app.</p>
    <div class="cta-row">{cta('btn primary', 'Download on the App Store', 'Get the launch email', 'en')}<a class="btn ghost" href="/features/">Features (Korean)</a></div>
    <p class="note">Starter free · Pro ₩39,000/month or ₩249,000/year · AI replies are for reference; the owner decides</p>
  </div>
  <div class="phone">{pic('screen-dash', "VI One dashboard — today's bookings, customers, monthly sales, insights", 330)}</div>
</div></section>

<section><div class="wrap">
  <h2>What VI One does</h2>
  <p class="def"><strong>VI One is a Korean-first AI CRM for owner-operated shops.</strong> It records bookings that arrive by phone, text or KakaoTalk; tags customers automatically as VIP, regular, new or no-show risk; logs payments in a few taps; and lets the owner message customers over SMS, KakaoTalk or WhatsApp with ready-made templates. On the Pro plan, the AI drafts replies to repeat questions (hours, parking, prices, bookings, directions) strictly from the shop's own FAQ, and hands anything it doesn't know back to the owner. Human review is the default.</p>
  <div class="grid3" style="margin-top:28px">
    <div class="card"><div class="ic">📅</div><h3>Bookings</h3><p>List and weekly views, request → confirmed → done, no-show marking, create a booking straight from a conversation.</p></div>
    <div class="card"><div class="ic">👑</div><h3>Customers</h3><p>Automatic VIP / regular / new / caution (2+ no-shows) tags, notes, visit, payment and message history in one profile.</p></div>
    <div class="card"><div class="ic">💳</div><h3>Quick sales log</h3><p>Item, quantity, amount and payment method — rolls up into per-customer history and monthly sales.</p></div>
    <div class="card"><div class="ic">💬</div><h3>Messaging</h3><p>SMS, KakaoTalk, WhatsApp and phone from the customer profile; reminder, thank-you, no-show check and review templates; every send is logged.</p></div>
    <div class="card"><div class="ic">✨</div><h3>AI FAQ auto-reply (Pro)</h3><p>AI drafts from your FAQ only, you approve before sending; unknown questions go to an "owner to answer" queue and become new FAQ entries.</p></div>
    <div class="card"><div class="ic">🔒</div><h3>Built to trust</h3><p>Per-shop data isolation, in-app account and data deletion, Apple in-app subscriptions you can cancel in iPhone Settings.</p></div>
  </div>
</div></section>

<section class="soft"><div class="wrap">
  <div class="sec-h"><h2>Pricing</h2><p>Start free; upgrade when you want the AI to handle repeat questions. No trial period — Starter is simply free.</p></div>
  <div class="plans">
    <div class="plan"><h3>Starter</h3><div class="price">Free</div><ul><li>Bookings</li><li>Customers with automatic tags</li><li>Quick sales log</li><li>SMS / KakaoTalk / WhatsApp messaging + history</li><li class="x">AI FAQ auto-reply</li></ul>{cta('btn', 'Download on the App Store', 'Get the launch email', 'en')}</div>
    <div class="plan hot"><span class="badge">Includes AI</span><h3>Pro</h3><div class="price">₩39,000<small>/month · or ₩249,000/year</small></div><ul><li>Everything in Starter</li><li>AI reply drafts + FAQ auto-reply</li><li>Unknown questions → owner queue → new FAQ</li><li>Apple in-app purchase, cancel anytime in Settings</li></ul>{cta('btn blue', 'Download on the App Store', 'Get the launch email', 'en')}</div>
  </div>
</div></section>

<section><div class="wrap"><div class="sec-h"><h2>FAQ</h2></div><div class="faq">{faq}</div></div></section>

<section class="cta-band"><div class="wrap"><h2>Missed calls happen. Missed bookings shouldn't.</h2><p>VI One — from booking to reply, in one app. Starter is free.</p>{cta('btn primary', 'Download on the App Store', 'Get the launch email', 'en')}<p class="notice" style="color:rgba(255,255,255,.7)">hello@vione.app · Seoul, Korea</p></div></section>
""")]
