# -*- coding: utf-8 -*-
"""Static site generator for vione.app (GitHub Pages).
Run:  python3 src/build.py   (from the site/ folder)  -> writes HTML into site/ root.
Everything is plain HTML (no client-side rendering) so AI crawlers can read it.
"""
import os, json, datetime, html, shutil
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
SRC = ROOT / 'src'
import sys; sys.path.insert(0, str(SRC))
import content_ko as C
import content_en as CE

# ---------------- config ----------------
SITE = 'https://vione.app'
APP_STORE_URL = 'https://apps.apple.com/kr/app/vi-one/id6774170446'  # 2026-09-05 출시
PLAY_STORE_URL = ''         # <- 안드로이드 출시 후 Google Play URL 입력 (예: https://play.google.com/store/apps/details?id=app.vione)
GA_MEASUREMENT_ID = ''      # <- GA4 측정 ID (예: G-XXXXXXXXXX). 비우면 GA 스니펫 생략
CONTACT = 'hello@vione.app'
LEGAL_TERMS = 'https://hellosangwoo-ctrl.github.io/vione-legal/terms-of-service.html'
LEGAL_PRIVACY = 'https://hellosangwoo-ctrl.github.io/vione-legal/privacy-policy.html'
TODAY = datetime.date.today().isoformat()
BUILD_DATE = TODAY

ORG_LD = {
    "@context": "https://schema.org", "@type": "Organization",
    "@id": SITE + "/#org", "name": "VI One", "alternateName": ["브이원", "VI One (브이원)"],
    "url": SITE, "logo": SITE + "/assets/img/app-icon.svg", "email": CONTACT,
    "description": "소상공인(미용실·네일·카페·식당)을 위한 AI CRM 앱 VI One(브이원)을 만드는 팀. 예약·고객·매출·고객 소통·AI FAQ 응대를 한 앱에 담습니다.",
    "areaServed": "KR", "foundingLocation": {"@type": "Place", "address": {"@type": "PostalAddress", "addressLocality": "Seoul", "addressCountry": "KR"}},
    "contactPoint": [{"@type": "ContactPoint", "email": CONTACT, "contactType": "customer support", "availableLanguage": ["ko", "en"]}],
}
APP_LD = {
    "@context": "https://schema.org", "@type": "SoftwareApplication",
    "@id": SITE + "/#app", "name": "VI One", "alternateName": "브이원",
    "applicationCategory": "BusinessApplication", "operatingSystem": "iOS",
    "description": "VI One(브이원)은 미용실·네일샵·카페·식당 같은 소상공인을 위한 AI CRM 앱입니다. 예약 관리, VIP·단골·신규·노쇼 고객 자동 태그, 간편 매출 기록, 문자·카카오톡·WhatsApp 고객 소통, AI FAQ 자동응대(Pro)를 한 앱에서 제공합니다.",
    "url": SITE, "author": {"@id": SITE + "/#org"}, "inLanguage": ["ko", "en"],
    "offers": [
        {"@type": "Offer", "name": "Starter", "price": "0", "priceCurrency": "KRW", "description": "예약·고객·간편 매출 기록·고객 소통 (무료)"},
        {"@type": "Offer", "name": "Pro 월간", "price": "39000", "priceCurrency": "KRW", "description": "Starter 전체 + AI FAQ 자동응대 · 월 구독(Apple 인앱결제)"},
        {"@type": "Offer", "name": "Pro 연간", "price": "249000", "priceCurrency": "KRW", "description": "Starter 전체 + AI FAQ 자동응대 · 연 구독(Apple 인앱결제)"},
    ],
    "featureList": ["예약 관리", "고객 관리(VIP·단골·신규·노쇼 자동 태그)", "간편 매출 기록", "고객 소통(문자·카카오톡·WhatsApp)", "AI FAQ 자동응대(Pro, 사람 확인 기본)"],
}
if APP_STORE_URL:
    APP_LD["installUrl"] = APP_STORE_URL
    APP_LD["sameAs"] = [APP_STORE_URL]

# ---------------- layout ----------------
CSS = (SRC / 'site.css').read_text(encoding='utf-8')

def esc(s): return html.escape(s, quote=True)

def ga():
    if not GA_MEASUREMENT_ID: return ''
    return f"""<script async src="https://www.googletagmanager.com/gtag/js?id={GA_MEASUREMENT_ID}"></script>
<script>window.dataLayer=window.dataLayer||[];function gtag(){{dataLayer.push(arguments)}}gtag('js',new Date());gtag('config','{GA_MEASUREMENT_ID}');</script>"""

def cta_button(cls='btn primary', text_ready='App Store에서 다운로드', text_wait='출시 알림 받기', lang='ko'):
    if APP_STORE_URL:
        return f'<a class="{cls}" href="{APP_STORE_URL}" rel="noopener">{esc(text_ready)}</a>'
    subj = 'VI One 출시 알림 신청' if lang == 'ko' else 'VI One launch notification'
    return f'<a class="{cls}" href="mailto:{CONTACT}?subject={esc(subj)}">{esc(text_wait)}</a>'

def nav(lang='ko', path='/'):
    if lang == 'en':
        items = [('/en/', 'Home'), ('/features/', '기능 (KO)'), ('/pricing/', '요금 (KO)'), ('/faq/', 'FAQ (KO)')]
        cta = cta_button('btn small primary', 'Download on the App Store', 'Get launch email', 'en')
    else:
        items = [('/features/', '기능'), ('/pricing/', '요금'), ('/guides/', '가이드'), ('/compare/', '비교'), ('/faq/', 'FAQ'), ('/about/', '소개')]
        cta = cta_button('btn small primary')
    CUR = ' aria-current="page"'
    links = ''.join(f'<a href="{h}"{CUR if h == path else ""}>{t}</a>' for h, t in items)
    return f"""<header class="nav"><div class="wrap">
  <a class="logo" href="{'/en/' if lang=='en' else '/'}" aria-label="VI One 홈"><img src="/assets/img/app-icon.svg" alt="" width="34" height="34"><span>VI One<b>.</b></span></a>
  <nav class="links">{links}</nav>
  <div class="nav-cta">{cta}<a class="lang" href="{'/' if lang=='en' else '/en/'}">{'KO' if lang=='en' else 'EN'}</a></div>
</div></header>"""

def footer(lang='ko'):
    if lang == 'en':
        return f"""<footer><div class="wrap">
  <div class="fgrid">
    <div><div class="flogo">VI One<b>.</b></div><p>AI CRM for small business owners — bookings, customers, sales, messaging and FAQ auto-reply in one app.</p></div>
    <div><h4>Product</h4><a href="/en/">English</a><a href="/features/">Features (KO)</a><a href="/pricing/">Pricing (KO)</a><a href="/faq/">FAQ (KO)</a></div>
    <div><h4>Legal</h4><a href="{LEGAL_TERMS}" rel="noopener">Terms of Use (EULA)</a><a href="{LEGAL_PRIVACY}" rel="noopener">Privacy Policy</a></div>
    <div><h4>Contact</h4><a href="mailto:{CONTACT}">{CONTACT}</a><p class="muted">Seoul, Korea</p></div>
  </div>
  <p class="fine">© 2026 VI One. AI replies are for reference; the owner makes the final decision. Screens shown are examples.</p>
</div></footer>"""
    return f"""<footer><div class="wrap">
  <div class="fgrid">
    <div><div class="flogo">VI One<b>.</b></div><p>소상공인을 위한 AI CRM 앱. 예약·고객·매출·소통·AI FAQ 응대를 한 앱에.</p></div>
    <div><h4>제품</h4><a href="/features/">기능</a><a href="/pricing/">요금</a><a href="/faq/">자주 묻는 질문</a><a href="/en/">English</a></div>
    <div><h4>가이드</h4><a href="/guides/no-show/">노쇼 줄이기</a><a href="/guides/repeat-questions/">반복 질문 자동응답</a><a href="/guides/customer-messaging/">고객 메시지 템플릿</a><a href="/compare/naver-booking/">네이버 예약과 함께 쓰기</a></div>
    <div><h4>회사·법적 고지</h4><a href="/about/">소개·연락처</a><a href="{LEGAL_TERMS}" rel="noopener">이용약관(EULA)</a><a href="{LEGAL_PRIVACY}" rel="noopener">개인정보처리방침</a><a href="mailto:{CONTACT}">{CONTACT}</a></div>
  </div>
  <p class="fine">© 2026 VI One · 서울 · AI 응답은 참고용이며 최종 판단과 결정은 사장님이 하십니다 · 화면은 예시입니다 · 구독은 Apple 인앱결제로 관리되며 App Store 승인 후 이용 가능합니다.</p>
</div></footer>"""

def page(path, title, desc, body, lang='ko', ld=None, og_type='website', modified=None, alt=None, noindex=False, priority=None):
    """path like '/features/' -> writes features/index.html"""
    url = SITE + path
    lds = [ORG_LD, APP_LD] + (ld or [])
    ld_html = ''.join(f'<script type="application/ld+json">{json.dumps(x, ensure_ascii=False)}</script>' for x in lds)
    hreflang = ''
    if alt:  # (lang_code, path) pairs
        hreflang = ''.join(f'<link rel="alternate" hreflang="{l}" href="{SITE}{p}">' for l, p in alt) + f'<link rel="alternate" hreflang="x-default" href="{SITE}{alt[0][1]}">'
    robots = '<meta name="robots" content="noindex">' if noindex else '<meta name="robots" content="index,follow,max-snippet:-1,max-image-preview:large">'
    mod = f'<meta property="article:modified_time" content="{modified or BUILD_DATE}">'
    doc = f"""<!DOCTYPE html>
<html lang="{lang}">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width,initial-scale=1">
<title>{esc(title)}</title>
<meta name="description" content="{esc(desc)}">
<link rel="canonical" href="{url}">
{robots}
{hreflang}
<meta property="og:type" content="{og_type}"><meta property="og:site_name" content="VI One"><meta property="og:locale" content="{'en_US' if lang=='en' else 'ko_KR'}">
<meta property="og:title" content="{esc(title)}"><meta property="og:description" content="{esc(desc)}"><meta property="og:url" content="{url}">
<meta property="og:image" content="{SITE}/assets/img/og.png"><meta property="og:image:width" content="1200"><meta property="og:image:height" content="630">
<meta name="twitter:card" content="summary_large_image"><meta name="twitter:title" content="{esc(title)}"><meta name="twitter:description" content="{esc(desc)}"><meta name="twitter:image" content="{SITE}/assets/img/og.png">
{mod}
<link rel="icon" href="/assets/img/favicon.svg" type="image/svg+xml"><link rel="apple-touch-icon" href="/assets/img/apple-touch-icon.png">
<link rel="preconnect" href="https://cdn.jsdelivr.net" crossorigin>
<link rel="stylesheet" href="https://cdn.jsdelivr.net/gh/orioncactus/pretendard@v1.3.9/dist/web/static/pretendard.min.css">
<style>{CSS}</style>
{ld_html}
{ga()}
</head>
<body>
{nav(lang, path)}
<main>
{body}
</main>
{footer(lang)}
</body>
</html>"""
    out = ROOT / path.strip('/') / 'index.html' if path != '/' else ROOT / 'index.html'
    if path == '/404': out = ROOT / '404.html'
    out.parent.mkdir(parents=True, exist_ok=True)
    out.write_text(doc, encoding='utf-8')
    return url

# ---------------- build ----------------
def main():
    pages = []  # (url, lastmod, priority)
    for p in C.pages(cta_button):
        url = page(**p)
        if not p.get('noindex'): pages.append((url, p.get('modified') or BUILD_DATE, p.get('priority', 0.7)))
    for p in CE.pages(cta_button):
        url = page(**p)
        if not p.get('noindex'): pages.append((url, p.get('modified') or BUILD_DATE, p.get('priority', 0.6)))

    # sitemap
    sm = ['<?xml version="1.0" encoding="UTF-8"?>', '<urlset xmlns="http://www.sitemaps.org/schemas/sitemap/0.9">']
    for u, m, pr in pages:
        sm.append(f'  <url><loc>{u}</loc><lastmod>{m}</lastmod><priority>{pr}</priority></url>')
    sm.append('</urlset>')
    (ROOT / 'sitemap.xml').write_text('\n'.join(sm), encoding='utf-8')

    # robots.txt — allow every search/AI crawler that can cite us; block only Bytespider
    robots = f"""# vione.app — we welcome search engines and AI answer engines.
User-agent: *
Allow: /

User-agent: Bytespider
Disallow: /

Sitemap: {SITE}/sitemap.xml
"""
    (ROOT / 'robots.txt').write_text(robots, encoding='utf-8')

    # llms.txt / llms-full.txt
    (ROOT / 'llms.txt').write_text(C.llms_txt(pages, SITE), encoding='utf-8')
    (ROOT / 'llms-full.txt').write_text(C.llms_full(SITE), encoding='utf-8')


    # /app/ — smart link used by printed material (business card QR etc.): never changes, redirects by platform.
    # Before the store URLs are filled in it lands on the homepage, so the printed QR keeps working.
    ios = APP_STORE_URL or SITE + '/'
    android = PLAY_STORE_URL or (APP_STORE_URL and SITE + '/') or SITE + '/'
    app_dir = ROOT / 'app'; app_dir.mkdir(exist_ok=True)
    (app_dir / 'index.html').write_text(f"""<!doctype html>
<html lang="ko"><head><meta charset="utf-8"><meta name="viewport" content="width=device-width,initial-scale=1">
<meta name="robots" content="noindex,nofollow"><title>VI One 앱 열기</title>
<link rel="canonical" href="{SITE}/">
<style>body{{font-family:-apple-system,'Apple SD Gothic Neo','Noto Sans KR',sans-serif;background:#0D1B3D;color:#fff;margin:0;min-height:100vh;display:flex;align-items:center;justify-content:center;text-align:center;padding:24px}}a{{color:#50AAEE}}p{{opacity:.8}}</style>
<script>
(function(){{var ua=navigator.userAgent||'';var ios=/iPhone|iPad|iPod/i.test(ua)||(navigator.platform==='MacIntel'&&navigator.maxTouchPoints>1);var and=/Android/i.test(ua);
var url=ios?{ios!r}:(and?{android!r}:{ios!r});location.replace(url);}})();
</script></head>
<body><div><h1>VI One</h1><p>앱으로 이동합니다…</p><p><a href="{ios}">자동으로 열리지 않으면 여기를 누르세요</a></p></div></body></html>
""", encoding='utf-8')

    (ROOT / 'CNAME').write_text('vione.app\n', encoding='utf-8')
    (ROOT / '.nojekyll').write_text('', encoding='utf-8')
    (ROOT / 'humans.txt').write_text(f"/* TEAM */\nVI One — Seoul, Korea\nContact: {CONTACT}\n\n/* SITE */\nLast update: {BUILD_DATE}\nStandards: HTML5, CSS3, JSON-LD\n", encoding='utf-8')
    print(f'built {len(pages)} pages')

if __name__ == '__main__':
    main()
