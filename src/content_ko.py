# -*- coding: utf-8 -*-
"""Korean content for vione.app. Facts are limited to what VI One 1.0 actually ships."""

SITE = 'https://vione.app'
MOD = '2026-09-02'

def pic(name, alt, w=300):
    return f'<picture><source srcset="/assets/img/{name}.webp" type="image/webp"><img src="/assets/img/{name}.png" alt="{alt}" width="{w}" loading="lazy"></picture>'

FAQ = [
    ("VI One(브이원)은 어떤 앱인가요?", "VI One(브이원)은 미용실·네일샵·카페·식당처럼 사장님 한 명이 예약과 손님 응대를 함께 감당하는 매장을 위한 AI CRM 앱입니다. 예약 관리, 고객 관리(VIP·단골·신규·노쇼 자동 태그), 간편 매출 기록, 문자·카카오톡·WhatsApp 고객 소통을 한 앱에서 처리하고, Pro 플랜에서는 주차·영업시간·가격 같은 반복 질문에 AI가 매장 FAQ로 답변 초안을 만들어 드립니다."),
    ("누구에게 맞는 앱인가요?", "전화와 문자로 예약이 들어오고, 손님 응대 중에 연락을 놓치기 쉬운 1인·소규모 매장에 맞습니다. 미용실, 네일·피부관리, 카페, 예약제 식당, 공방, 학원처럼 '단골을 기억하고 다시 오게 하는 일'이 매출인 업종이 대표적입니다."),
    ("가격은 얼마인가요?", "Starter는 무료입니다(예약·고객·간편 매출 기록·고객 소통). AI FAQ 자동응대가 포함된 Pro는 월 39,000원 또는 연 249,000원(월 대비 약 47% 절약)이며, 별도 무료 체험 기간은 없습니다. 구독은 Apple 인앱결제로 처리됩니다."),
    ("무료 Starter로 무엇을 할 수 있나요?", "예약 확인·승인·변경·취소, 고객 프로필과 방문·소통 이력, VIP·단골·신규·노쇼 자동 태그, 간편 매출(결제) 기록, 문자·카카오톡·WhatsApp 메시지 템플릿 발송과 소통 이력 기록을 모두 무료로 사용할 수 있습니다."),
    ("AI 자동응대는 어떻게 동작하나요?", "사장님이 앱의 'AI 응대' 탭에서 영업시간·주차·예약·가격·위치 같은 FAQ를 우리 매장 답변으로 채워 두면, 고객 질문이 들어왔을 때 AI가 그 FAQ 중 가장 맞는 답을 찾아 초안을 만듭니다. 사장님이 확인·수정한 뒤 보내는 방식이 기본이며, Pro에서 자동응답을 켜면 FAQ에 있는 질문은 자동으로 답합니다."),
    ("AI가 모르는 질문을 받으면 어떻게 되나요?", "지어내지 않습니다. FAQ에 없는 질문은 '사장님 답변 대기' 목록으로 넘어가고, 사장님이 한 번 답하면 그 답이 FAQ로 등록되어 다음부터는 AI가 같은 질문에 답할 수 있습니다."),
    ("어떤 메신저로 고객에게 연락할 수 있나요?", "고객 상세 화면에서 문자(SMS), WhatsApp, 카카오톡, 전화 버튼으로 바로 연락할 수 있습니다. 카카오톡은 앱 정책상 전화번호로 1:1 대화를 여는 공개 링크가 없어, 메시지를 복사해 카카오톡을 열어 붙여넣는 방식입니다. 보낸 메시지는 고객의 소통 이력에 자동 기록됩니다."),
    ("고객이 보낸 문자·WhatsApp도 앱에서 받을 수 있나요?", "설정에서 수신 번호를 연결하면 고객이 보낸 문자·WhatsApp 메시지가 '소통' 탭에 모이고, 미처리 대화를 따로 볼 수 있습니다. 수신 번호 연결은 별도 메시징 서비스 계정이 필요하며, 연결 전에도 발신·이력 기록 기능은 모두 사용할 수 있습니다."),
    ("VIP·단골·노쇼 태그는 어떻게 정해지나요?", "방문 횟수·누적 결제·노쇼 기록을 바탕으로 앱이 자동 계산합니다. 누적 결제나 방문이 많은 고객은 VIP, 3회 이상 방문은 단골, 첫 방문은 신규, 노쇼가 2회 이상이면 '주의'로 표시되어 예약 전날 확인 문자를 보내기 좋습니다."),
    ("노쇼를 줄이는 데 어떻게 도움이 되나요?", "노쇼 이력이 고객 태그로 남고, 대시보드 인사이트가 '노쇼 2회 이상 고객'을 알려 줍니다. 고객 상세에서 '노쇼 방지 확인' 템플릿을 한 번에 보낼 수 있어 예약 전날 확인 연락을 습관화할 수 있습니다. 자세한 방법은 <a href='/guides/no-show/'>노쇼 줄이는 7가지 방법</a>을 참고하세요."),
    ("매출 기록은 어떻게 하나요?", "고객 상세에서 '결제 추가'로 상품명·수량·금액·결제수단을 입력하면 고객별 이용 내역과 이번 달 매출이 함께 정리됩니다. 1.0은 사장님이 직접 기록하는 간편 방식이며, 결제 단말 연동은 이후 버전에서 검토 중입니다."),
    ("네이버 예약을 쓰고 있는데 같이 써도 되나요?", "네. 네이버 예약은 손님이 네이버에서 직접 잡는 예약 채널이고, VI One은 전화·문자·카카오톡으로 들어오는 예약과 고객 이력, 응대를 정리하는 사장님용 CRM입니다. 두 도구는 역할이 달라 함께 쓰는 매장이 자연스럽습니다. <a href='/compare/naver-booking/'>함께 쓰는 법</a>을 정리해 두었습니다."),
    ("카카오톡 채널 자동응답(카나나 상담매니저)과는 무엇이 다른가요?", "카카오톡 채널의 AI 응답은 카카오톡 채널 문의에 답하는 기능입니다. VI One은 문자·WhatsApp·카카오톡을 아우르는 고객 소통과 예약·고객 이력·매출까지 한 앱에서 관리하고, AI 답변은 매장 FAQ만 사용하며 사장님 확인이 기본입니다. <a href='/compare/kakao-kanana/'>비교 글</a>에서 자세히 설명합니다."),
    ("어떤 기기에서 쓸 수 있나요?", "현재 iPhone(iOS) App Store에서 제공합니다. 한국어와 English를 지원하며, Android 버전은 검토 중입니다."),
    ("데이터는 안전한가요?", "매장별로 데이터가 분리되어 보관되며, 계정과 데이터는 앱 안의 설정에서 언제든 직접 삭제할 수 있습니다. 개인정보 처리에 관한 자세한 내용은 개인정보처리방침을 확인해 주세요."),
    ("구독은 어떻게 해지하나요?", "구독은 Apple ID로 결제되며, iPhone 설정 → Apple 계정 → 구독에서 해지할 수 있습니다. 기간 종료 24시간 전까지 해지하지 않으면 자동 갱신됩니다. 앱의 설정 탭에도 '구독 관리 / 해지' 버튼이 있습니다."),
    ("AI 응답은 얼마나 믿을 수 있나요?", "AI는 사장님이 직접 적어 둔 매장 FAQ만 근거로 답하고, 근거가 없으면 답하지 않습니다. 그래도 AI 응답은 참고용이며 최종 판단과 결정은 사장님이 하십니다. 답장을 보내기 전 확인하는 흐름이 기본값인 이유입니다."),
    ("설치 후 첫 설정은 얼마나 걸리나요?", "매장 이름·업종을 입력하면 기본 FAQ 5종(영업시간·주차·예약·가격·위치)이 채워지고, 각 항목을 우리 매장 답변으로 바꾸는 데 5~10분이면 충분합니다. 서비스(메뉴)와 가격을 등록하면 예약 입력이 더 빨라집니다."),
    ("여러 직원이 함께 쓸 수 있나요?", "1.0은 매장당 사장님 계정 1개 기준으로 설계되어 있습니다. 직원 계정과 다지점 기능은 이용 매장의 의견을 모아 이후 버전에서 검토합니다."),
    ("문의는 어디로 하나요?", "hello@vione.app 으로 메일을 보내 주세요. 기능 제안, 업종별 요청, 도입 문의 모두 환영합니다."),
]

def faq_ld(items):
    return {"@context": "https://schema.org", "@type": "FAQPage",
            "mainEntity": [{"@type": "Question", "name": q, "acceptedAnswer": {"@type": "Answer", "text": _strip(a)}} for q, a in items]}

def _strip(s):
    import re
    return re.sub(r'<[^>]+>', '', s)

def faq_html(items):
    return '<div class="faq">' + ''.join(f'<details><summary>{q}</summary><div class="a">{a}</div></details>' for q, a in items) + '</div>'

def article(path_label, title, meta, lede, body, cta_fn, sources=None, crumbs=None):
    src = ''
    if sources:
        src = '<div class="sources"><strong>참고 자료</strong><ul>' + ''.join(f'<li><a href="{u}" rel="noopener nofollow">{t}</a></li>' for t, u in sources) + '</ul></div>'
    cr = f'<div class="crumbs"><a href="/">홈</a> › {crumbs}</div>' if crumbs else ''
    return f"""<article class="article">
{cr}
<div class="meta">{meta}</div>
<h1>{title}</h1>
<p class="lede">{lede}</p>
{body}
<div class="cta"><h3>VI One으로 바로 실행해 보세요</h3><p>예약·고객·매출·소통, 그리고 반복 질문 AI 응대(Pro)까지 한 앱에. Starter는 무료입니다.</p>{cta_fn('btn primary')} <a class="btn ghost" href="/features/" style="color:#fff;border-color:rgba(255,255,255,.4);background:rgba(255,255,255,.12)">기능 보기</a></div>
{src}
</article>"""

# ---------------- pages ----------------
def pages(cta):
    P = []

    # ---- HOME ----
    home_faq = FAQ[:6]
    P.append(dict(path='/', priority=1.0, modified=MOD,
        title='VI One(브이원) — 소상공인 AI CRM: 예약·고객·매출·소통·AI 응대를 한 앱에',
        desc='VI One(브이원)은 미용실·네일·카페·식당 사장님을 위한 AI CRM 앱입니다. 예약 관리, VIP·단골·노쇼 자동 태그, 간편 매출 기록, 문자·카카오톡·WhatsApp 소통, 반복 질문 AI 응대(Pro). Starter 무료, Pro 월 39,000원.',
        alt=[('ko', '/'), ('en', '/en/')],
        ld=[{"@context": "https://schema.org", "@type": "WebSite", "url": SITE, "name": "VI One", "alternateName": "브이원", "inLanguage": "ko", "publisher": {"@id": SITE + "/#org"}}],
        body=f"""
<section class="hero"><div class="wrap">
  <div>
    <span class="kicker">소상공인 AI CRM · iPhone</span>
    <h1>손님 응대는 사장님이,<br><span class="em">반복 질문은 AI가.</span></h1>
    <p class="lede"><strong>VI One(브이원)</strong>은 미용실·네일·카페·식당 사장님을 위한 AI CRM 앱입니다. 예약, 고객, 매출 기록, 문자·카카오톡·WhatsApp 소통, 그리고 주차·영업시간·가격 같은 반복 질문의 AI 응대(Pro)를 한 앱에서 처리합니다.</p>
    <div class="cta-row">{cta('btn primary')}<a class="btn ghost" href="/features/">기능 자세히 보기</a></div>
    <p class="note">Starter 무료 · Pro 월 39,000원(연 249,000원) · AI 응답은 참고용, 최종 확인은 사장님이</p>
  </div>
  <div class="phone">{pic('screen-dash', 'VI One 대시보드 화면 — 오늘 예약, 전체 고객, 이번달 매출, 인사이트, 처리할 일', 330)}</div>
</div></section>

<section><div class="wrap">
  <h2>VI One은 무엇인가요?</h2>
  <p class="def"><strong>VI One(브이원)은 사장님 한 명이 예약·응대·고객관리를 모두 감당하는 매장을 위한 iPhone용 AI CRM 앱</strong>입니다. 전화·문자·카카오톡으로 들어오는 예약을 정리하고, 고객을 VIP·단골·신규·노쇼로 자동 태그하며, 결제를 간단히 기록하고, 고객에게 문자·카카오톡·WhatsApp으로 바로 연락합니다. Pro 플랜에서는 AI가 매장 FAQ를 근거로 반복 질문의 답변 초안을 만들고, 모르는 질문은 지어내지 않고 사장님께 넘깁니다. Starter는 무료, Pro는 월 39,000원 또는 연 249,000원입니다.</p>
  <p class="def small muted">제공 기능(1.0): 예약 관리 · 고객 관리 · 간편 매출 기록 · 고객 소통 · AI FAQ 자동응대(Pro) · 한국어/English</p>
</div></section>

<section class="soft"><div class="wrap">
  <div class="sec-h"><h2>사장님이 매일 겪는 세 가지 문제</h2><p>시술 중, 조리 중, 계산 중에는 전화도 문자도 받을 수 없습니다. 그런데 매출은 바로 그 전화와 문자에서 시작됩니다.</p></div>
  <div class="grid3">
    <div class="card"><div class="ic">📵</div><h3>놓친 전화가 곧 놓친 예약</h3><p>손님 응대 중에 울린 전화는 대부분 다시 걸려오지 않습니다. 전화·문자 예약을 한 곳에 기록하고 요청 대기부터 처리해야 합니다.</p></div>
    <div class="card"><div class="ic">🔁</div><h3>매일 같은 질문, 같은 답</h3><p>"주차 되나요?", "몇 시까지 하세요?", "가격이요?" — 하루의 문자 절반은 반복 질문입니다. 답을 한 번만 적어 두면 AI가 초안을 만듭니다.</p></div>
    <div class="card"><div class="ic">👑</div><h3>단골을 기억하는 일</h3><p>누가 VIP인지, 누가 60일째 안 오는지, 누가 노쇼를 두 번 했는지 — 기억에 의존하면 놓칩니다. 태그와 인사이트로 자동 정리합니다.</p></div>
  </div>
</div></section>

<section id="features"><div class="wrap">
  <div class="sec-h"><h2>한 앱에 담은 다섯 가지</h2><p>1.0에서 실제로 제공하는 기능만 소개합니다. 화면은 데모 매장 예시입니다.</p></div>
  <div class="feat-row"><div class="media">{pic('screen-book', 'VI One 예약 화면 — 오늘 예약 리스트와 상태 표시')}</div><div><span class="tag">예약 관리</span><h3>들어온 예약을 한눈에, 처리는 한 번에</h3><p>오늘의 예약과 요청 대기를 리스트·주간 보기로 확인하고 승인·변경·취소합니다. 전화로 받은 예약도 대화 기록에서 바로 예약으로 만들 수 있습니다.</p><ul><li>리스트 보기 / 주간 캘린더 보기</li><li>요청 → 확정 → 완료 상태 관리, 노쇼 표시</li><li>서비스(메뉴)·가격·소요시간 등록으로 빠른 입력</li></ul></div></div>
  <div class="feat-row rev"><div class="media">{pic('screen-cust', 'VI One 고객 화면 — VIP, 단골, 신규, 주의 태그 필터')}</div><div><span class="tag">고객 관리</span><h3>VIP·단골·신규·노쇼, 자동으로 정리</h3><p>방문 횟수와 누적 결제, 노쇼 기록으로 고객 등급이 자동 계산됩니다. 고객별 메모, 방문·결제·소통 이력이 한 화면에 모입니다.</p><ul><li>👑 VIP · 단골 · 신규 · ⚠️ 주의(노쇼 2회 이상) 필터</li><li>뜸한 고객 알림 — "단골 ○○님이 60일째 안 오셨어요"</li><li>이름·전화 검색, 고객 추가 한 번에</li></ul></div></div>
  <div class="feat-row"><div class="media">{pic('screen-cust-detail', 'VI One 고객 상세 — 방문, 총 지출, 결제 내역, 예약 이력')}</div><div><span class="tag">간편 매출 기록</span><h3>결제를 기록하면 고객 이력과 매출이 함께 정리</h3><p>상품명·수량·금액·결제수단만 입력하면 고객별 이용 내역과 이번 달 매출이 자동으로 집계됩니다. 결제 단말 없이도 매장 흐름이 보입니다.</p><ul><li>고객 상세에서 '+ 결제 추가'</li><li>대시보드 KPI — 오늘 예약, 이번달 예약·매출·노쇼</li><li>고객 누적 결제가 VIP 판정에 반영</li></ul></div></div>
  <div class="feat-row rev"><div class="media">{pic('screen-composer', 'VI One 문자 보내기 — 노쇼 방지 확인 템플릿')}</div><div><span class="tag">고객 소통</span><h3>문자·카카오톡·WhatsApp·전화, 고객 화면에서 바로</h3><p>예약 리마인드, 감사·재방문 유도, 노쇼 방지 확인, 이벤트 안내 템플릿을 골라 보내면 소통 이력에 자동 기록됩니다. 수신 번호를 연결하면 고객이 보낸 문자·WhatsApp이 소통함에 모입니다.</p><ul><li>템플릿 4종 + 직접 입력, 리뷰 요청 링크</li><li>소통함 — 전체 / 미처리 / 보낸 메시지</li><li>카카오톡은 메시지 복사 후 붙여넣기 방식</li></ul></div></div>
  <div class="feat-row"><div class="media">{pic('screen-msg-draft', 'VI One 대화 상세 — AI가 매장 FAQ로 만든 답변 초안과 답장 보내기')}</div><div><span class="tag pro">AI FAQ 자동응대 · Pro</span><h3>반복 질문은 AI가 초안, 사장님은 확인만</h3><p>영업시간·주차·예약·가격·위치 FAQ를 우리 매장 답변으로 채워 두면, 고객 질문에 가장 맞는 FAQ로 AI가 초안을 만듭니다. 사장님이 확인·수정 후 보내는 것이 기본이고, 자동응답을 켜면 FAQ에 있는 질문은 자동으로 답합니다.</p><ul><li>모르는 질문은 지어내지 않고 '사장님 답변 대기'로</li><li>사장님이 한 번 답하면 다음부터는 FAQ로 자동 응답</li><li>AI 응답 테스트로 미리 확인</li></ul></div></div>
</div></section>

<section class="soft"><div class="wrap">
  <div class="sec-h"><h2>믿고 쓸 수 있게 만든 원칙</h2><p>AI가 매장 대신 말하는 순간, 사장님의 신뢰가 걸려 있습니다. 그래서 다음 네 가지를 기본값으로 두었습니다.</p></div>
  <div class="grid2">
    <div class="card"><h3>✓ 사람 확인이 기본</h3><p>AI 초안은 사장님이 확인한 뒤 전송합니다. 자동응답은 Pro에서 사장님이 직접 켜는 선택 기능입니다.</p></div>
    <div class="card"><h3>✓ AI는 매장 FAQ만 답합니다</h3><p>사장님이 적어 둔 답변만 근거로 삼고, 근거가 없으면 답하지 않습니다. 새 질문은 사장님께 넘깁니다.</p></div>
    <div class="card"><h3>✓ 매장별 데이터 분리</h3><p>매장 데이터는 다른 매장과 분리되어 보관됩니다.</p></div>
    <div class="card"><h3>✓ 앱 안에서 언제든 삭제</h3><p>설정에서 계정과 데이터를 직접 삭제할 수 있습니다. 구독 관리·해지 버튼도 설정에 있습니다.</p></div>
  </div>
</div></section>

<section id="pricing"><div class="wrap">
  <div class="sec-h"><h2>요금</h2><p>Starter는 무료로 시작하고, 반복 질문 AI 응대가 필요해질 때 Pro로 올리세요. 무료 체험 기간은 없습니다.</p></div>
  <div class="plans">
    <div class="plan"><h3>Starter</h3><div class="price">무료</div><p class="muted small">기본 CRM — 사장님 한 분이 시작하기에 충분</p><ul><li>예약 관리 (리스트·주간)</li><li>고객 관리 · VIP/단골/신규/노쇼 자동 태그</li><li>간편 매출 기록</li><li>고객 소통 (문자·카카오톡·WhatsApp·전화) + 이력</li><li class="x">AI FAQ 자동응대</li></ul>{cta('btn')}</div>
    <div class="plan hot"><span class="badge">AI 응대 포함</span><h3>Pro</h3><div class="price">월 39,000원 <small>또는 연 249,000원</small></div><p class="muted small">연간 결제 시 월 대비 약 47% 절약(5개월치)</p><ul><li>Starter 전체 기능</li><li>AI FAQ 자동응대 · AI 답변 초안</li><li>모르는 질문 → 사장님 답변 대기 → FAQ 자동 등록</li><li>Apple 인앱결제 · iPhone 설정에서 해지</li></ul>{cta('btn blue')}</div>
  </div>
  <p class="notice">가격은 App Store 표시 가격과 동일하며 부가세 포함 여부 등 결제 조건은 Apple 인앱결제 정책에 따릅니다. <a href="/pricing/">요금 자세히 보기 →</a></p>
</div></section>

<section class="soft"><div class="wrap">
  <div class="sec-h"><h2>자주 묻는 질문</h2><p>더 많은 질문과 답은 <a href="/faq/">FAQ 페이지</a>에 있습니다.</p></div>
  {faq_html(home_faq)}
</div></section>

<section class="cta-band"><div class="wrap"><h2>놓친 전화는 있어도, 놓친 예약은 없게.</h2><p>VI One — 예약부터 응대까지, 한 앱에. Starter는 무료입니다.</p>{cta('btn primary')}<p class="notice" style="color:rgba(255,255,255,.7)">문의 hello@vione.app</p></div></section>
"""))

    # ---- FEATURES ----
    P.append(dict(path='/features/', priority=0.9, modified=MOD,
        title='VI One 기능 — 예약 관리·고객 태그·매출 기록·고객 소통·AI FAQ 응대',
        desc='VI One(브이원) 1.0 기능 안내: 예약 리스트·주간 보기, VIP·단골·신규·노쇼 자동 태그, 간편 매출 기록, 문자·카카오톡·WhatsApp 템플릿 발송과 소통함, AI FAQ 자동응대(Pro)와 사람 확인 원칙.',
        body=f"""<article class="article">
<div class="crumbs"><a href="/">홈</a> › 기능</div>
<div class="meta">VI One 1.0 · 갱신 {MOD}</div>
<h1>VI One 기능 안내</h1>
<p class="lede">VI One(브이원)은 예약 관리, 고객 관리, 간편 매출 기록, 고객 소통, AI FAQ 자동응대(Pro) 다섯 가지를 iPhone 앱 하나에 담았습니다. 이 페이지는 1.0 버전에서 실제로 제공하는 기능만 설명합니다.</p>

<h2>대시보드 — 오늘 해야 할 일이 먼저 보입니다</h2>
<p>앱을 열면 오늘 예약, 전체 고객, 이번달 예약, 이번달 매출, 이번달 노쇼, 등록 서비스 6개 KPI가 먼저 보입니다. 그 아래 <strong>오늘의 인사이트</strong>가 "이번주 예약이 지난주보다 늘었어요", "단골 ○○님이 60일째 안 오셨어요", "노쇼 2회 이상 고객 1명" 같은 실행 가능한 문장을 알려 주고, <strong>처리할 일</strong>에는 새 고객 메시지·예약 요청·미답변 질문이 모입니다. 뜸한 고객에게는 바로 '메시지' 버튼으로 연락할 수 있습니다.</p>
<div class="shots">{pic('screen-dash','대시보드')}{pic('screen-book','예약')}{pic('screen-cust','고객')}</div>

<h2>예약 관리</h2>
<ul>
<li><strong>리스트 보기</strong>: 날짜를 고르면 그날 예약이 시간순으로, <strong>주간 보기</strong>: 요일×시간 블록으로 한 주가 보입니다.</li>
<li>상태는 요청 → 확정 → 완료로 관리하고, 취소·노쇼를 표시하면 고객의 노쇼 횟수에 반영됩니다.</li>
<li>전화·문자로 받은 예약은 소통 기록에서 <strong>'이 대화로 예약 생성'</strong>을 눌러 고객·서비스·메모가 채워진 예약으로 만듭니다.</li>
<li>설정에서 서비스(메뉴)·가격·소요시간을 등록하면 예약 입력이 빨라지고 매출 기록과 연결됩니다.</li>
</ul>

<h2>고객 관리 — VIP·단골·신규·노쇼 자동 태그</h2>
<p>고객 등급은 방문 횟수, 누적 결제, 노쇼 기록으로 앱이 자동 계산합니다.</p>
<table><thead><tr><th>태그</th><th>기준(자동)</th><th>추천 액션</th></tr></thead><tbody>
<tr><td>👑 VIP</td><td>누적 결제 또는 방문이 많은 고객</td><td>감사 메시지, 우선 예약 안내</td></tr>
<tr><td>단골</td><td>3회 이상 방문</td><td>재방문 유도, 신메뉴·이벤트 안내</td></tr>
<tr><td>신규</td><td>첫 방문</td><td>방문 감사 + 다음 예약 제안</td></tr>
<tr><td>⚠️ 주의</td><td>노쇼 2회 이상</td><td>예약 전날 '노쇼 방지 확인' 문자</td></tr>
</tbody></table>
<p>고객 상세에는 방문 횟수, 총 지출, 최근 방문·통화, 결제 내역, 예약 이력, 소통(메시지) 이력이 한 화면에 모입니다.</p>

<h2>간편 매출 기록</h2>
<p>고객 상세의 <strong>'+ 결제 추가'</strong>에서 상품명·수량·금액·결제수단(카드·현금·간편결제)을 입력하면 고객의 방문 횟수와 누적 결제가 갱신되고 대시보드의 이번달 매출에 집계됩니다. 결제 단말 연동 없이 사장님이 직접 기록하는 방식으로, 매장 흐름과 고객별 소비 패턴을 함께 볼 수 있습니다.</p>

<h2>고객 소통 — 문자·카카오톡·WhatsApp·전화</h2>
<div class="shots">{pic('screen-composer','문자 보내기 템플릿')}{pic('screen-msg','소통함')}{pic('screen-msg-draft','대화 상세와 AI 초안')}</div>
<ul>
<li>고객 상세의 <strong>💬 문자 · WhatsApp · 카카오 · 전화</strong> 버튼으로 바로 연락합니다.</li>
<li>템플릿: <strong>예약 리마인드 / 감사·재방문 유도 / 노쇼 방지 확인 / 이벤트·프로모션</strong>, 설정에 리뷰 링크를 넣으면 <strong>리뷰 요청</strong> 템플릿이 추가됩니다. 직접 입력도 가능합니다.</li>
<li>보낸 메시지는 <strong>소통 이력</strong>에 자동 기록됩니다. 카카오톡은 앱 정책상 전화번호로 1:1 대화를 여는 공개 링크가 없어 메시지를 복사한 뒤 카카오톡을 열어 붙여넣는 방식입니다.</li>
<li><strong>소통 탭</strong>: 전체 / 미처리 / 보낸 메시지 필터로 대화를 관리하고, 설정에서 수신 번호를 연결하면 고객이 보낸 문자·WhatsApp이 이곳으로 들어옵니다.</li>
</ul>

<h2>AI FAQ 자동응대 (Pro)</h2>
<div class="shots">{pic('screen-ai','AI 응대 FAQ 목록')}{pic('screen-ai-miss','사장님 답변 대기 (미답변) 목록')}{pic('screen-msg-draft','AI 초안')}</div>
<ol>
<li><strong>FAQ 채우기</strong>: 기본 FAQ 5종(영업시간·주차·예약·가격·위치)을 우리 매장 답변으로 바꿉니다. 저장한 내용 그대로 AI가 응대합니다.</li>
<li><strong>AI 초안</strong>: 대화 상세에서 '🤖 AI 초안'을 누르면 고객 질문에 가장 맞는 FAQ로 답변 초안이 만들어지고, 매칭 정도가 표시됩니다. 사장님이 확인·수정 후 보냅니다.</li>
<li><strong>자동응답</strong>: 설정에서 켜면 FAQ에 있는 질문은 자동으로 답합니다(Pro).</li>
<li><strong>모르는 질문</strong>: FAQ에 없으면 지어내지 않고 <strong>'사장님 답변 대기'</strong>로 넘깁니다. 사장님이 답하면 FAQ로 등록되어 다음부터 자동 응답됩니다.</li>
<li><strong>AI 응답 테스트</strong>: 고객 질문을 직접 입력해 어떻게 답하는지 미리 확인할 수 있습니다.</li>
</ol>
<blockquote>AI 응답은 참고용이며 최종 판단과 결정은 사장님이 하십니다. 그래서 '확인 후 전송'이 기본값입니다.</blockquote>

<h2>설정·계정</h2>
<ul><li>매장 정보(이름·전화·주소·영업시간·주차 안내·AI 인사말·리뷰 링크), 서비스(메뉴) 관리</li><li>언어: 한국어 / English</li><li>구독(Pro 월간·연간) · 구독 관리/해지 · 구매 복원</li><li>로그아웃 · 계정 삭제(데이터 포함)</li></ul>
<p class="small muted">1.0에 없는 것: 결제 단말(POS) 자동 연동, 전화 자동 수신·응답, 직원 계정·다지점. 이용 매장의 의견을 모아 이후 버전에서 검토합니다.</p>
<div class="cta"><h3>Starter는 무료입니다</h3><p>예약·고객·매출·소통은 무료로, AI 응대가 필요해질 때 Pro로.</p>{cta('btn primary')} <a class="btn" href="/pricing/">요금 보기</a></div>
</article>"""))

    # ---- PRICING ----
    P.append(dict(path='/pricing/', priority=0.9, modified=MOD,
        title='VI One 요금 — Starter 무료, Pro 월 39,000원 · 연 249,000원',
        desc='VI One(브이원) 요금제: Starter 무료(예약·고객·매출 기록·소통), Pro 월 39,000원 또는 연 249,000원(AI FAQ 자동응대 포함). 무료 체험 없음, Apple 인앱결제, iPhone 설정에서 해지.',
        ld=[faq_ld([FAQ[2], FAQ[3], FAQ[15]])],
        body=f"""<article class="article">
<div class="crumbs"><a href="/">홈</a> › 요금</div>
<div class="meta">갱신 {MOD} · App Store 표시 가격과 동일</div>
<h1>VI One 요금</h1>
<p class="lede">VI One은 <strong>Starter(무료)</strong>와 <strong>Pro(월 39,000원 또는 연 249,000원)</strong> 두 가지 플랜입니다. 별도 무료 체험 기간은 없으며, Starter로 기본 CRM을 계속 무료로 쓰다가 AI FAQ 자동응대가 필요할 때 Pro로 올리면 됩니다.</p>
<table><thead><tr><th>항목</th><th>Starter</th><th>Pro</th></tr></thead><tbody>
<tr><td>가격</td><td><strong>무료</strong></td><td><strong>월 39,000원</strong> 또는 <strong>연 249,000원</strong>(월 환산 약 20,750원, 월 대비 약 47% 절약)</td></tr>
<tr><td>예약 관리 (리스트·주간)</td><td>✓</td><td>✓</td></tr>
<tr><td>고객 관리 · VIP/단골/신규/노쇼 자동 태그</td><td>✓</td><td>✓</td></tr>
<tr><td>간편 매출 기록</td><td>✓</td><td>✓</td></tr>
<tr><td>고객 소통 (문자·카카오톡·WhatsApp·전화) + 템플릿 + 이력</td><td>✓</td><td>✓</td></tr>
<tr><td>소통함 (수신 번호 연결 시 문자·WhatsApp 수신)</td><td>✓</td><td>✓</td></tr>
<tr><td>AI 답변 초안 (대화 상세)</td><td>–</td><td>✓</td></tr>
<tr><td>AI FAQ 자동응답 (설정에서 켜기)</td><td>–</td><td>✓</td></tr>
<tr><td>모르는 질문 → 사장님 답변 대기 → FAQ 등록</td><td>–</td><td>✓</td></tr>
<tr><td>결제 방식</td><td>–</td><td>Apple 인앱결제(자동 갱신)</td></tr>
</tbody></table>
<h2>가격을 이렇게 정한 이유</h2>
<p>Pro의 가치는 "반복 질문에 사장님 대신 답할 준비가 되어 있는 것"입니다. 하루 1,300원 정도의 비용으로 놓치는 문의를 줄이는 것이 목표이며, 연간 결제는 5개월치를 절약하는 대신 1년을 함께 쓰겠다는 약속에 대한 할인입니다. 무료 체험을 두지 않는 대신 Starter를 무료로 열어 두었습니다.</p>
<h2>결제·해지</h2>
<ul>
<li>구독은 Apple ID로 결제되며, 기간 종료 24시간 전까지 해지하지 않으면 자동 갱신됩니다.</li>
<li>해지: iPhone 설정 → Apple 계정 → 구독. 앱의 설정 탭에도 '구독 관리 / 해지'와 '구매 복원' 버튼이 있습니다.</li>
<li>결제 조건(세금 포함 여부, 환불)은 Apple의 인앱결제 정책에 따릅니다.</li>
<li>가격은 앱 안 표시 가격과 App Store 표시 가격이 동일합니다. 변경 시 이 페이지와 앱을 함께 갱신합니다.</li>
</ul>
<h2>요금 관련 질문</h2>
{faq_html([FAQ[2], FAQ[3], FAQ[15]])}
<div class="cta"><h3>Starter로 오늘 시작하세요</h3><p>필요해질 때 Pro로 올리면 됩니다.</p>{cta('btn primary')}</div>
</article>"""))

    # ---- FAQ ----
    P.append(dict(path='/faq/', priority=0.8, modified=MOD,
        title='VI One 자주 묻는 질문(FAQ) — 기능·요금·AI 응대·데이터',
        desc='VI One(브이원) FAQ 20문항: 어떤 앱인지, 누구에게 맞는지, 가격, 무료 Starter 범위, AI 자동응대 동작 방식과 한계, 메신저 채널, 노쇼 태그, 네이버 예약·카카오톡 채널과의 차이, 기기·데이터·해지.',
        ld=[faq_ld(FAQ)],
        body=f"""<article class="article">
<div class="crumbs"><a href="/">홈</a> › FAQ</div>
<div class="meta">갱신 {MOD}</div>
<h1>자주 묻는 질문</h1>
<p class="lede">VI One(브이원)에 대해 사장님들이 가장 많이 묻는 20가지를 정리했습니다. 답은 1.0 버전 기준이며, 기능이 바뀌면 이 페이지를 먼저 갱신합니다.</p>
{faq_html(FAQ)}
<div class="cta"><h3>더 궁금한 점이 있으신가요?</h3><p>hello@vione.app 으로 보내 주시면 답변 드리고, 자주 나오는 질문은 이 페이지에 추가합니다.</p>{cta('btn primary')}</div>
</article>"""))

    # ---- GUIDES INDEX ----
    P.append(dict(path='/guides/', priority=0.7, modified=MOD,
        title='사장님 가이드 — 노쇼 줄이기, 반복 질문 자동응답, 고객 메시지 템플릿',
        desc='미용실·네일·카페·식당 사장님을 위한 실무 가이드: 노쇼 줄이는 7가지 방법, 반복 질문 자동응답 FAQ 설계법, 문자·카카오톡·WhatsApp 고객 메시지 템플릿 10선.',
        body=f"""<section><div class="wrap">
<div class="crumbs"><a href="/">홈</a> › 가이드</div>
<div class="sec-h"><h2>사장님 가이드</h2><p>도구와 상관없이 바로 쓸 수 있는 매장 운영 방법을 정리합니다. 각 글 끝에 VI One에서 실행하는 방법을 덧붙였습니다.</p></div>
<div class="grid3 list-cards">
<a class="card" href="/guides/no-show/"><div class="ic">📅</div><h3>미용실·네일샵 노쇼 줄이는 7가지 방법</h3><p>확정 문자, 전날 리마인드, 노쇼 태그, 취소 정책, 대기 명단까지 — 바로 적용 가능한 순서로.</p></a>
<a class="card" href="/guides/repeat-questions/"><div class="ic">🔁</div><h3>반복 질문 자동응답 만드는 법 (FAQ 설계)</h3><p>질문 수집부터 답변 원칙, 모르는 질문 처리, 월 1회 갱신까지 FAQ 설계 5단계.</p></a>
<a class="card" href="/guides/customer-messaging/"><div class="ic">💬</div><h3>고객 메시지 템플릿 10선</h3><p>예약 확정·리마인드·감사·재방문·리뷰 요청·이벤트 문구와 광고성 메시지 표기 규칙.</p></a>
</div></div></section>"""))

    # ---- GUIDE: NO-SHOW ----
    P.append(dict(path='/guides/no-show/', priority=0.8, modified=MOD, og_type='article',
        ld=[{"@context": "https://schema.org", "@type": "Article", "headline": "미용실·네일샵 노쇼 줄이는 7가지 방법", "datePublished": MOD, "dateModified": MOD, "author": {"@id": SITE + "/#org"}, "publisher": {"@id": SITE + "/#org"}, "inLanguage": "ko", "mainEntityOfPage": SITE + "/guides/no-show/"}],
        title='미용실·네일샵 노쇼 줄이는 7가지 방법 (2026) — 리마인드 문자 예시 포함',
        desc='예약 노쇼를 줄이는 실무 순서: 확정 문자 즉시 발송, 전날 리마인드, 노쇼 이력 태그, 취소·예약금 정책 명시, 변경 경로 단순화, 대기 명단, 노쇼율 측정. 바로 쓰는 문자 템플릿 3개 포함.',
        body=article('가이드', '미용실·네일샵 노쇼 줄이는 7가지 방법', f'가이드 · 사장님 실무 · 갱신 {MOD}',
            '노쇼는 "예약을 잊은 손님"과 "가볍게 잡은 손님" 두 종류에서 나옵니다. 앞은 리마인드로, 뒤는 정책과 태그로 줄입니다. 아래 7가지를 순서대로 적용하면 도구가 무엇이든 효과가 납니다.',
            f"""
<h2>노쇼는 왜 생기나요?</h2>
<p>노쇼의 대부분은 악의가 아니라 <strong>망각</strong>과 <strong>낮은 약속 비용</strong>에서 나옵니다. 전화로 가볍게 잡은 예약은 캘린더에 남지 않고, 취소가 번거로우면 그냥 안 옵니다. 그래서 대책도 두 갈래입니다: 기억을 도와주는 <em>리마인드</em>, 그리고 약속의 무게를 만드는 <em>정책·기록</em>.</p>

<h2>1. 예약 직후 확정 문자를 보냅니다</h2>
<p>전화를 끊자마자 날짜·시간·시술·소요시간·주차 안내가 담긴 확정 문자를 보내면 손님 폰에 기록이 남습니다. 이것만으로 "그날인 줄 몰랐어요"가 크게 줄어듭니다.</p>
<div class="tpl">[서촌 헤어살롱] 김민지님, 9/5(금) 14:00 펌(약 2시간) 예약 확정되었습니다. 건물 뒤 주차 2시간 무료. 변경·취소는 이 번호로 회신 주세요.</div>

<h2>2. 전날 오후에 리마인드를 보냅니다</h2>
<p>리마인드는 <strong>전날 오후 5~7시</strong>가 가장 효과적입니다. 아침에 보내면 잊히고, 당일 아침은 이미 다른 일정이 굳어 있습니다. 회신을 요청하는 문장으로 끝내야 확인 응답이 늘어납니다.</p>
<div class="tpl">[서촌 헤어살롱] 김민지님, 내일 9/5(금) 14:00 예약 확인차 연락드립니다. 방문 가능하시면 '네'라고 답장 주세요. 변경이 필요하면 편하게 말씀해 주세요.</div>

<h2>3. 노쇼 이력을 고객 기록에 남깁니다</h2>
<p>노쇼를 '기억'이 아니라 '기록'으로 관리해야 대응이 일관됩니다. 노쇼 2회 이상 고객에게는 예약 시 확인 절차를 한 단계 추가하고(전날 확인 회신 필수, 또는 예약금), 처음 노쇼한 손님에게는 부드럽게 다음 예약을 제안하는 식으로 <strong>등급별 대응</strong>을 정해 두면 감정 소모가 줄어듭니다.</p>

<h2>4. 취소·예약금 정책을 미리, 짧게 알립니다</h2>
<p>정책은 예약 확정 문자 한 줄로 충분합니다. "당일 취소·노쇼 시 다음 예약은 예약금이 필요합니다" 정도의 문장이 약속의 무게를 만듭니다. 예약금·위약금 기준을 정할 때는 공정거래위원회 <a href="https://www.law.go.kr/" rel="noopener nofollow">소비자분쟁해결기준</a>의 해당 업종 항목을 참고해 과도하지 않게 정하고, 정책을 매장 안내와 예약 문자에 동일하게 적습니다.</p>

<h2>5. 변경·취소를 답장 한 번으로 만들 수 있게 합니다</h2>
<p>취소가 번거로우면 손님은 '말없이 안 오는' 쪽을 택합니다. "변경·취소는 이 번호로 회신"이라는 문장을 모든 예약 문자에 넣고, 회신이 오면 빠르게 처리해 주세요. 취소가 빨리 들어와야 빈 자리를 채울 수 있습니다.</p>

<h2>6. 대기 명단으로 빈 자리를 채웁니다</h2>
<p>인기 시간대는 "그 시간에 자리 나면 알려 주세요"라는 손님이 항상 있습니다. 대기 희망 고객을 메모해 두고 취소가 나오면 바로 연락하면, 노쇼가 생겨도 매출 손실을 줄일 수 있습니다.</p>

<h2>7. 노쇼율을 매달 한 번 봅니다</h2>
<p><strong>노쇼율 = 노쇼 건수 ÷ 전체 예약 건수</strong>입니다. 이번 달 숫자를 한 번 보는 것만으로 어떤 시간대·어떤 유형의 예약에서 노쇼가 나는지 감이 생기고, 리마인드 문구나 정책을 조정할 근거가 됩니다.</p>

<h2>정리 — 오늘 바로 할 것</h2>
<table><thead><tr><th>순서</th><th>할 일</th><th>소요</th></tr></thead><tbody>
<tr><td>1</td><td>확정 문자·리마인드 문자 템플릿 2개 저장</td><td>10분</td></tr>
<tr><td>2</td><td>취소·예약금 정책 한 문장 정하기</td><td>10분</td></tr>
<tr><td>3</td><td>노쇼 고객 표시 시작 (2회 이상은 확인 절차 추가)</td><td>계속</td></tr>
<tr><td>4</td><td>매달 1일 노쇼율 확인</td><td>5분/월</td></tr>
</tbody></table>

<div class="box"><strong>VI One에서는 이렇게 합니다.</strong> 예약을 취소·노쇼로 표시하면 고객의 노쇼 횟수가 쌓이고, 2회 이상이면 고객 목록에 <strong>⚠️ 주의</strong> 태그가 붙습니다. 대시보드 인사이트가 "노쇼 2회 이상 고객 N명"을 알려 주고, 고객 상세에서 <strong>'노쇼 방지 확인'</strong> 템플릿을 문자·카카오톡·WhatsApp으로 바로 보낼 수 있습니다. 보낸 메시지는 소통 이력에 남습니다. (Starter 무료)</div>
""", cta, sources=[('공정거래위원회 소비자분쟁해결기준 (국가법령정보센터)', 'https://www.law.go.kr/'), ('VI One 기능 — 예약·고객 태그·소통', SITE + '/features/')], crumbs='<a href="/guides/">가이드</a> › 노쇼 줄이기')))

    # ---- GUIDE: REPEAT QUESTIONS ----
    P.append(dict(path='/guides/repeat-questions/', priority=0.8, modified=MOD, og_type='article',
        ld=[{"@context": "https://schema.org", "@type": "Article", "headline": "매장 반복 질문 자동응답 만드는 법 — FAQ 설계 5단계", "datePublished": MOD, "dateModified": MOD, "author": {"@id": SITE + "/#org"}, "publisher": {"@id": SITE + "/#org"}, "inLanguage": "ko", "mainEntityOfPage": SITE + "/guides/repeat-questions/"}],
        title='매장 반복 질문 자동응답 만드는 법 — 사장님 FAQ 설계 5단계 (예시 포함)',
        desc='"주차 되나요?" "몇 시까지 하세요?" 같은 반복 질문을 자동응답으로 바꾸는 방법: 1주 질문 수집, 상위 5개 선정, 답변 작성 원칙(숫자·예외·다음 행동), 채널별 적용, 모르는 질문 처리와 월 1회 갱신.',
        body=article('가이드', '매장 반복 질문 자동응답 만드는 법 — FAQ 설계 5단계', f'가이드 · 사장님 실무 · 갱신 {MOD}',
            '매장에 들어오는 문의의 절반 이상은 다섯 가지 질문의 변형입니다: 영업시간, 주차, 가격, 예약 가능 여부, 위치. 이 다섯 개의 답을 "한 번 제대로" 적어 두는 것이 자동응답의 90%입니다. 나머지 10%는 모르는 질문을 사람에게 넘기는 규칙입니다.',
            f"""
<h2>1단계 — 일주일 동안 질문을 그대로 적습니다</h2>
<p>손님이 실제로 쓴 문장을 그대로 모으세요. "주차 되나요?"와 "차 대고 갈 수 있어요?"는 같은 질문이지만 표현이 다릅니다. 표현을 많이 모아야 자동응답이 질문을 잘 알아봅니다. 메모장이나 앱의 미답변 목록에 하루 3~5개씩, 일주일이면 충분합니다.</p>

<h2>2단계 — 상위 5개만 고릅니다</h2>
<p>많이 만들수록 좋아 보이지만, 처음엔 <strong>5개</strong>가 정답입니다. 적을수록 답이 정확하고 관리가 됩니다. 대부분의 매장에서 순위는 비슷합니다.</p>
<table><thead><tr><th>주제</th><th>손님 표현 예</th><th>답변에 꼭 들어갈 것</th></tr></thead><tbody>
<tr><td>영업시간</td><td>몇 시까지 해요? / 주말도 하나요? / 공휴일은?</td><td>평일·주말 시간, 공휴일 원칙, 마지막 접수 시간</td></tr>
<tr><td>주차</td><td>주차 되나요? / 차 갖고 가도 돼요?</td><td>위치, 무료 시간, 안 될 때 대안</td></tr>
<tr><td>가격</td><td>커트 얼마예요? / 펌 가격이요</td><td>대표 시술 '부터' 가격, 달라지는 조건</td></tr>
<tr><td>예약</td><td>토요일 3시 돼요? / 예약하고 싶어요</td><td>예약 방법, 확정 절차, 필요한 정보</td></tr>
<tr><td>위치</td><td>어디예요? / 역에서 어떻게 가요?</td><td>주소, 출구·도보 시간, 건물 특징</td></tr>
</tbody></table>

<h2>3단계 — 답변은 '숫자·예외·다음 행동' 세 가지로 씁니다</h2>
<ul>
<li><strong>숫자</strong>: "오후까지" 대신 "평일 10:00–20:00, 주말 11:00–18:00".</li>
<li><strong>예외</strong>: "공휴일은 인스타그램 공지 확인", "기장·시술에 따라 달라질 수 있어요".</li>
<li><strong>다음 행동</strong>: "원하시는 날짜·시간과 시술을 남겨 주시면 확인 후 확정 문자 드립니다."</li>
</ul>
<div class="tpl">Q. 주차 되나요?
A. 건물 뒤편 주차장을 2시간 무료로 이용하실 수 있어요. 만차일 때는 건너편 공영주차장(도보 2분)을 이용해 주세요.</div>
<p>답변은 <strong>사장님 말투</strong>로 씁니다. 자동응답의 목표는 "사람이 아닌 것처럼" 보이는 게 아니라, 사장님이 바쁠 때 사장님 대신 <em>정확한 정보</em>를 전하는 것입니다.</p>

<h2>4단계 — 채널별로 같은 답을 씁니다</h2>
<p>문자, 카카오톡 채널, WhatsApp, 인스타 DM 어디로 물어도 답이 같아야 합니다. FAQ를 한 곳(문서나 앱)에 두고 각 채널에 복사해 쓰되, <strong>원본은 하나</strong>로 관리하세요. 가격이 바뀌면 원본만 고치고 채널에 반영합니다.</p>

<h2>5단계 — 모르는 질문은 사람에게 넘기는 규칙을 정합니다</h2>
<p>자동응답에서 가장 중요한 규칙은 <strong>"모르면 답하지 않는다"</strong>입니다. FAQ에 없는 질문("아이 의자 있나요?", "반려동물 동반 되나요?")에 자동응답이 그럴듯한 말을 지어내면 신뢰가 한 번에 깨집니다. 모르는 질문은 "확인 후 답변 드릴게요"로 받고 사장님이 답한 뒤, 그 답을 FAQ에 추가합니다. 이렇게 한 달이면 FAQ가 10~15개로 자연스럽게 늘어납니다.</p>

<h2>월 1회 갱신 체크리스트</h2>
<ul><li>가격·영업시간 변경 반영</li><li>이번 달 미답변 질문 중 2회 이상 나온 것을 FAQ로 추가</li><li>손님이 자꾸 되묻는 답변은 문장을 더 구체적으로</li></ul>

<div class="box"><strong>VI One에서는 이렇게 합니다.</strong> 앱의 <strong>AI 응대</strong> 탭에 기본 FAQ 5종(영업시간·주차·예약·가격·위치)이 준비되어 있어 우리 매장 답변으로 바꾸기만 하면 됩니다. Pro에서는 고객 문의에 AI가 가장 맞는 FAQ로 <strong>답변 초안</strong>을 만들어 사장님이 확인 후 보내고, 자동응답을 켜면 FAQ에 있는 질문은 자동으로 답합니다. FAQ에 없는 질문은 지어내지 않고 <strong>'사장님 답변 대기'</strong>로 넘어가며, 사장님이 답하면 FAQ로 등록됩니다. <strong>AI 응답 테스트</strong>로 미리 확인할 수 있습니다.</div>
""", cta, sources=[('VI One 기능 — AI FAQ 자동응대', SITE + '/features/'), ('카카오 비즈니스 — 카카오톡 채널 안내', 'https://business.kakao.com/')], crumbs='<a href="/guides/">가이드</a> › 반복 질문 자동응답')))

    # ---- GUIDE: MESSAGING TEMPLATES ----
    P.append(dict(path='/guides/customer-messaging/', priority=0.8, modified=MOD, og_type='article',
        ld=[{"@context": "https://schema.org", "@type": "Article", "headline": "고객 메시지 템플릿 10선 — 예약 확정·리마인드·재방문·리뷰 요청", "datePublished": MOD, "dateModified": MOD, "author": {"@id": SITE + "/#org"}, "publisher": {"@id": SITE + "/#org"}, "inLanguage": "ko", "mainEntityOfPage": SITE + "/guides/customer-messaging/"}],
        title='매장 고객 메시지 템플릿 10선 — 예약 확정·리마인드·재방문·리뷰 요청 (문자·카카오톡·WhatsApp)',
        desc='미용실·네일·카페·식당에서 바로 쓰는 고객 메시지 문구 10개와 보내는 타이밍, 광고성 메시지 표기 규칙((광고)·무료수신거부), 알림톡·친구톡·문자 채널 선택 기준.',
        body=article('가이드', '고객 메시지 템플릿 10선 — 예약 확정부터 리뷰 요청까지', f'가이드 · 사장님 실무 · 갱신 {MOD}',
            '좋은 매장 메시지는 짧고, 이름을 부르고, 다음 행동이 하나입니다. 아래 10개 템플릿은 [매장명]·[이름]·[일시]만 바꿔 바로 쓸 수 있게 만들었고, 각 문구 옆에 보내는 타이밍을 적었습니다. 광고성 메시지는 표기 규칙이 있으니 마지막 절을 꼭 확인하세요.',
            f"""
<h2>메시지의 기본 규칙 4가지</h2>
<ul><li><strong>[매장명]</strong>으로 시작 — 모르는 번호에서 온 문자를 열게 하는 첫 장치</li><li><strong>이름</strong>을 부르기 — "고객님"보다 "김민지님"</li><li>문장 2~3개, <strong>다음 행동 하나</strong>("네라고 답장", "예약 원하시면 회신")</li><li>보내는 <strong>시간</strong>은 오전 10시~오후 8시 사이</li></ul>

<h2>1. 예약 확정 <span class="muted small">— 예약 직후</span></h2>
<div class="tpl">[매장명] [이름]님, [일시] [시술](약 [소요시간]) 예약 확정되었습니다. [주차 안내]. 변경·취소는 이 번호로 회신 주세요.</div>
<h2>2. 전날 리마인드 <span class="muted small">— 전날 오후 5~7시</span></h2>
<div class="tpl">[매장명] [이름]님, 내일 [일시] 예약 확인차 연락드립니다. 방문 가능하시면 '네'라고 답장 주세요. 변경이 필요하면 편하게 말씀해 주세요.</div>
<h2>3. 당일 리마인드 <span class="muted small">— 예약 2~3시간 전, 노쇼 이력 고객에게</span></h2>
<div class="tpl">[매장명] [이름]님, 오늘 [시간] 예약 기다리고 있겠습니다. 늦으시면 미리 연락 주시면 자리 조정해 드릴게요.</div>
<h2>4. 노쇼 방지 확인 <span class="muted small">— 노쇼 2회 이상 고객, 전날</span></h2>
<div class="tpl">[매장명] [이름]님, [일시] 예약 확인 부탁드립니다. 오늘 중 확인 회신이 없으면 예약이 취소될 수 있어요. 방문 가능하시면 '확인'이라고 답장 주세요.</div>
<h2>5. 방문 감사 <span class="muted small">— 방문 당일 저녁</span></h2>
<div class="tpl">[매장명] [이름]님, 오늘 방문 감사합니다! [시술 후 관리 팁 한 줄]. 궁금한 점은 언제든 이 번호로 문의해 주세요.</div>
<h2>6. 재방문 유도 (뜸한 고객) <span class="muted small">— 마지막 방문 후 45~60일</span></h2>
<div class="tpl">[매장명] [이름]님, 마지막 방문이 [기간] 정도 되셨네요. 편한 시간 말씀해 주시면 예약 잡아 드릴게요. 이번 달 [혜택 한 줄].</div>
<blockquote>혜택·할인이 들어가면 광고성 메시지입니다. 아래 표기 규칙을 지켜야 합니다.</blockquote>
<h2>7. 리뷰 요청 <span class="muted small">— 방문 다음 날 오전</span></h2>
<div class="tpl">[매장명] [이름]님, 어제 방문 감사합니다 🙏 괜찮으셨다면 리뷰 한 줄 부탁드려요! [리뷰 링크]</div>
<h2>8. 이벤트·프로모션 <span class="muted small">— 월 1회 이하</span></h2>
<div class="tpl">(광고)[매장명] [이름]님, [기간] [혜택 내용]. 예약은 이 번호로 회신 주세요. 무료수신거부 [번호]</div>
<h2>9. 예약 변경 안내 <span class="muted small">— 매장 사정 변경 즉시</span></h2>
<div class="tpl">[매장명] [이름]님, 죄송합니다. [사유]로 [기존 일시] 예약을 [대안 일시 1] 또는 [대안 일시 2]로 조정 부탁드려도 될까요? 편한 쪽으로 답장 주세요.</div>
<h2>10. 휴무·영업시간 변경 안내 <span class="muted small">— 최소 3일 전</span></h2>
<div class="tpl">[매장명] 안내드립니다. [날짜]는 [사유]로 휴무입니다. [재개일]부터 정상 영업합니다. 예약 변경이 필요하시면 회신 주세요.</div>

<h2>광고성 메시지 표기 규칙</h2>
<p>할인·이벤트·혜택처럼 <strong>영리 목적의 광고성 정보</strong>를 문자로 보낼 때는 정보통신망법에 따라 수신자의 사전 동의가 필요하고, 메시지 앞에 <strong>(광고)</strong> 표기와 <strong>무료수신거부</strong> 안내(수신거부 번호 등)를 넣어야 합니다. 예약 확정·리마인드·변경 안내처럼 거래 관계에 따른 안내는 광고가 아니지만, 그 안에 혜택 문구를 섞으면 광고성으로 볼 수 있으니 분리해서 보내는 것이 안전합니다. 자세한 기준은 <a href="https://www.kisa.or.kr/" rel="noopener nofollow">한국인터넷진흥원(KISA)</a>의 불법스팸 방지 안내를 참고하세요.</p>

<h2>채널은 어떻게 고르나요?</h2>
<table><thead><tr><th>채널</th><th>맞는 용도</th><th>참고</th></tr></thead><tbody>
<tr><td>문자(SMS/LMS)</td><td>예약 확정·리마인드 등 거래 안내, 광고(표기 규칙 준수)</td><td>모든 폰에 도착, 사장님 폰에서 바로 발송 가능</td></tr>
<tr><td>카카오톡 1:1 대화</td><td>이미 대화 중인 손님과의 소통</td><td>전화번호로 새 대화를 여는 공개 링크가 없어 메시지 복사·붙여넣기</td></tr>
<tr><td>카카오 알림톡</td><td>사업자 채널에서 보내는 정보성 알림(예약 확정 등)</td><td>사전 심사된 템플릿만, 광고 불가, 채널·발송 서비스 계약 필요</td></tr>
<tr><td>카카오 친구톡</td><td>채널 친구에게 보내는 광고성 메시지</td><td>채널 친구 추가한 고객에게만</td></tr>
<tr><td>WhatsApp</td><td>외국인 고객, 해외 손님</td><td>wa.me 링크로 바로 대화</td></tr>
</tbody></table>

<div class="box"><strong>VI One에서는 이렇게 합니다.</strong> 고객 상세의 <strong>문자 · WhatsApp · 카카오 · 전화</strong> 버튼을 누르면 템플릿(예약 리마인드 / 감사·재방문 유도 / 노쇼 방지 확인 / 이벤트·프로모션 / 리뷰 요청)이 매장명과 고객 이름이 채워진 상태로 뜨고, 수정 후 보내면 <strong>소통 이력</strong>에 자동 기록됩니다. 뜸한 고객은 대시보드 '재방문 유도' 목록에서 바로 메시지를 보낼 수 있습니다. (Starter 무료)</div>
""", cta, sources=[('한국인터넷진흥원(KISA) — 불법스팸 방지 안내', 'https://www.kisa.or.kr/'), ('카카오 비즈니스 — 알림톡·친구톡 안내', 'https://business.kakao.com/'), ('VI One 기능 — 고객 소통', SITE + '/features/')], crumbs='<a href="/guides/">가이드</a> › 고객 메시지 템플릿')))

    # ---- COMPARE INDEX ----
    P.append(dict(path='/compare/', priority=0.6, modified=MOD,
        title='비교 — 네이버 예약, 카카오톡 채널 자동응답과 VI One은 어떻게 다른가',
        desc='네이버 예약·카카오톡 채널(카나나 상담매니저) 같은 기존 도구와 VI One(브이원)의 역할 차이, 함께 쓰는 방법을 사실 기준으로 정리했습니다.',
        body=f"""<section><div class="wrap">
<div class="crumbs"><a href="/">홈</a> › 비교</div>
<div class="sec-h"><h2>기존 도구와 함께 쓰기</h2><p>VI One은 대체가 아니라 보완으로 설계했습니다. 사장님이 이미 쓰는 도구와 어떻게 나눠 쓰면 좋은지 정리합니다.</p></div>
<div class="grid2 list-cards">
<a class="card" href="/compare/naver-booking/"><div class="ic">🟢</div><h3>네이버 예약과 VI One 함께 쓰는 법</h3><p>손님이 잡는 예약(네이버)과 전화·문자로 들어오는 예약·고객 이력(VI One)의 역할 분담.</p></a>
<a class="card" href="/compare/kakao-kanana/"><div class="ic">💛</div><h3>카카오톡 채널 AI 응답과 VI One AI FAQ의 차이</h3><p>채널 하나의 자동응답 vs 문자·WhatsApp·카카오톡을 아우르는 CRM, 그리고 '사람 확인 기본' 원칙.</p></a>
</div></div></section>"""))

    # ---- COMPARE: NAVER ----
    P.append(dict(path='/compare/naver-booking/', priority=0.7, modified=MOD, og_type='article',
        title='네이버 예약과 VI One, 함께 쓰는 법 — 역할 분담과 이력 관리',
        desc='네이버 예약(스마트플레이스)은 손님이 네이버에서 직접 잡는 예약 채널, VI One은 전화·문자·카카오톡 예약과 고객 이력·응대를 정리하는 사장님용 AI CRM. 두 도구의 역할과 함께 쓰는 순서를 정리했습니다.',
        body=article('비교', '네이버 예약과 VI One, 함께 쓰는 법', f'비교 · 갱신 {MOD}',
            '네이버 예약은 "손님이 네이버에서 직접 잡는 예약"을 받는 채널이고, VI One(브이원)은 "전화·문자·카카오톡으로 들어오는 예약과 그 손님의 이력·응대"를 사장님이 관리하는 CRM입니다. 둘은 경쟁 관계가 아니라 입구가 다른 두 문입니다.',
            f"""
<h2>두 도구는 무엇이 다른가요?</h2>
<table><thead><tr><th></th><th>네이버 예약(스마트플레이스)</th><th>VI One</th></tr></thead><tbody>
<tr><td>예약이 들어오는 길</td><td>손님이 네이버 검색·지도에서 직접 예약</td><td>전화·문자·카카오톡·WhatsApp으로 들어온 요청을 사장님이 기록·확정</td></tr>
<tr><td>주 사용자</td><td>손님(예약) + 사장님(관리)</td><td>사장님</td></tr>
<tr><td>고객 이력</td><td>네이버 예약 고객 중심</td><td>채널 무관 — 방문·결제·소통·노쇼 이력, VIP·단골·신규·주의 태그</td></tr>
<tr><td>고객 연락</td><td>플랫폼 내 알림 중심</td><td>문자·카카오톡·WhatsApp·전화 템플릿 발송 + 이력 기록</td></tr>
<tr><td>반복 질문 응대</td><td>—</td><td>AI FAQ 초안·자동응답(Pro), 모르면 사장님께</td></tr>
<tr><td>매출 기록</td><td>—</td><td>간편 결제 기록 → 고객별 이력·월 매출</td></tr>
</tbody></table>
<p class="small muted">네이버 예약의 세부 기능·정책은 네이버 스마트플레이스 안내를 기준으로 확인하세요. 이 표는 역할 차이를 설명하기 위한 요약입니다.</p>

<h2>함께 쓰는 순서</h2>
<ol>
<li><strong>네이버 예약은 그대로 둡니다.</strong> 검색으로 들어오는 새 손님의 입구입니다.</li>
<li><strong>전화·문자 예약은 VI One에 기록합니다.</strong> 대화 기록에서 '이 대화로 예약 생성'을 누르면 고객·시술·메모가 채워집니다.</li>
<li><strong>모든 손님의 이력은 VI One에 모읍니다.</strong> 네이버로 온 손님도 방문 후 결제를 기록하면 VIP·단골 태그와 재방문 관리가 한 곳에서 됩니다.</li>
<li><strong>리마인드·재방문·리뷰 요청은 VI One 템플릿으로</strong> 문자·카카오톡·WhatsApp에 보냅니다. 보낸 기록이 고객 이력에 남습니다.</li>
<li><strong>반복 질문은 VI One AI FAQ(Pro)</strong>에 맡기고, 모르는 질문은 사장님이 답해 FAQ를 키웁니다.</li>
</ol>

<h2>이런 매장에 특히 맞습니다</h2>
<ul><li>단골 비중이 높아 전화·카톡 예약이 많은 미용실·네일샵</li><li>네이버 예약 손님과 전화 손님을 한 명의 '우리 손님'으로 관리하고 싶은 매장</li><li>노쇼 이력, 뜸한 고객, VIP를 기억이 아닌 기록으로 관리하고 싶은 사장님</li></ul>
""", cta, sources=[('네이버 스마트플레이스', 'https://smartplace.naver.com/'), ('VI One 기능', SITE + '/features/')], crumbs='<a href="/compare/">비교</a> › 네이버 예약')))

    # ---- COMPARE: KAKAO ----
    P.append(dict(path='/compare/kakao-kanana/', priority=0.7, modified=MOD, og_type='article',
        title='카카오톡 채널 AI 자동응답(카나나 상담매니저)과 VI One AI FAQ의 차이',
        desc='카카오톡 채널의 AI 상담(카나나 상담매니저)은 카카오톡 채널 문의에 답하는 기능, VI One은 문자·WhatsApp·카카오톡을 아우르는 고객 소통과 예약·고객 이력·매출을 한 앱에서 관리하며 AI 답변은 매장 FAQ만 사용하고 사장님 확인이 기본입니다.',
        body=article('비교', '카카오톡 채널 AI 자동응답과 VI One AI FAQ, 무엇이 다른가', f'비교 · 갱신 {MOD}',
            '카카오는 2025년 9월 카카오톡 채널용 AI 상담 기능(카나나 상담매니저)을 정식 출시해, 매장 정보와 메뉴를 바탕으로 채널 문의에 AI가 답하고 예약·주문을 받도록 했습니다. VI One(브이원)의 AI FAQ는 채널 하나가 아니라 사장님의 고객 소통 전체와 예약·고객 이력 위에서 동작하고, "사람 확인 기본"이라는 다른 원칙을 택했습니다.',
            f"""
<h2>한 표로 보는 차이</h2>
<table><thead><tr><th></th><th>카카오톡 채널 AI 상담(카나나 상담매니저)</th><th>VI One AI FAQ(Pro)</th></tr></thead><tbody>
<tr><td>답하는 곳</td><td>카카오톡 채널 1:1 채팅</td><td>고객 소통 전체(문자·WhatsApp 수신 대화, 카카오톡 붙여넣기 발송) + 앱 내 답변 초안</td></tr>
<tr><td>답의 근거</td><td>채널에 등록한 매장 정보·메뉴 등</td><td>사장님이 직접 적은 매장 FAQ만 (근거 없으면 답하지 않음)</td></tr>
<tr><td>기본 동작</td><td>AI가 응답</td><td>AI 초안 → 사장님 확인 후 전송(자동응답은 Pro에서 선택적으로 켬)</td></tr>
<tr><td>모르는 질문</td><td>플랫폼 정책에 따름</td><td>'사장님 답변 대기'로 넘기고, 사장님 답을 FAQ로 등록</td></tr>
<tr><td>함께 있는 것</td><td>카카오톡 채널 운영 도구</td><td>예약 관리, 고객 태그(VIP·단골·노쇼), 간편 매출 기록, 소통 이력</td></tr>
<tr><td>플랫폼</td><td>카카오 비즈니스(채널 필요)</td><td>iPhone 앱(App Store)</td></tr>
</tbody></table>
<p class="small muted">카카오톡 채널 AI 상담의 세부 기능·요금은 카카오 비즈니스 공지를 기준으로 확인하세요. 이 표는 설계 원칙의 차이를 설명하기 위한 요약입니다.</p>

<h2>둘 중 하나를 골라야 하나요?</h2>
<p>아닙니다. 카카오톡 채널을 운영 중이라면 채널 문의는 채널의 AI 상담이 받고, 전화·문자·WhatsApp으로 오는 문의와 <strong>모든 손님의 이력·예약·매출</strong>은 VI One에서 관리하는 구성이 자연스럽습니다. 중요한 것은 두 곳의 FAQ 답변(영업시간·주차·가격·예약·위치)을 <strong>같은 내용</strong>으로 유지하는 것입니다. <a href="/guides/repeat-questions/">반복 질문 자동응답 만드는 법</a>에서 원본 하나로 관리하는 방법을 설명합니다.</p>

<h2>VI One이 '사람 확인 기본'을 택한 이유</h2>
<p>매장 응대는 한 문장의 실수가 예약 하나, 단골 한 명으로 이어집니다. 그래서 VI One은 AI가 매장 FAQ에 있는 답만 쓰고, 근거가 없으면 답하지 않으며, 기본은 사장님이 확인한 뒤 보내도록 했습니다. 자동응답은 FAQ가 충분히 쌓인 뒤 사장님이 직접 켜는 선택 기능입니다. AI 응답은 참고용이며 최종 판단은 사장님이 하십니다.</p>
""", cta, sources=[('카카오 — 카나나 상담매니저 정식 출시 안내 (2025-09)', 'https://www.kakaocorp.com/page/detail/11719'), ('카카오 비즈니스', 'https://business.kakao.com/'), ('VI One 기능 — AI FAQ 자동응대', SITE + '/features/')], crumbs='<a href="/compare/">비교</a> › 카카오톡 채널 AI')))

    # ---- ABOUT ----
    P.append(dict(path='/about/', priority=0.6, modified=MOD,
        title='VI One 소개 — 만든 이유, 운영 원칙, 연락처',
        desc='VI One(브이원)은 서울에서 만드는 소상공인 AI CRM 앱입니다. 왜 만들었는지, AI 응대에서 지키는 원칙, 데이터 원칙, 연락처를 안내합니다.',
        body=f"""<article class="article">
<div class="crumbs"><a href="/">홈</a> › 소개</div>
<div class="meta">갱신 {MOD}</div>
<h1>VI One 소개</h1>
<p class="lede">VI One(브이원)은 "사장님 한 명이 예약·응대·고객관리를 다 하는 매장"을 위해 서울에서 만드는 AI CRM 앱입니다. 기업용 AI 시스템을 만들던 경험을 소상공인 가격대의 도구로 옮기는 것이 목표입니다.</p>
<h2>왜 만들었나요?</h2>
<p>미용실·네일샵·카페·식당 사장님은 손이 바쁠 때 전화를 받을 수 없고, 하루의 문자 절반은 같은 질문입니다. 놓친 전화는 놓친 매출이고, 기억에 의존한 단골 관리는 결국 놓칩니다. 대기업 콜센터가 쓰는 "자주 묻는 질문은 자동으로, 나머지는 사람이" 구조를 매장 한 곳이 월 몇 만 원으로 쓸 수 있게 만들고 싶었습니다.</p>
<h2>지키는 원칙</h2>
<ul>
<li><strong>고객과의 끊김 없는 소통이 핵심입니다.</strong> 문자·카카오톡·WhatsApp·전화 버튼은 어떤 버전에서도 빠지지 않습니다.</li>
<li><strong>AI는 매장 FAQ만 답합니다.</strong> 모르면 지어내지 않고 사장님께 넘깁니다. 사람 확인이 기본이고, 자동응답은 사장님이 켜는 선택입니다.</li>
<li><strong>없는 기능을 있다고 말하지 않습니다.</strong> 이 사이트와 App Store 설명은 실제 제공 기능만 적습니다.</li>
<li><strong>데이터는 매장별로 분리</strong>되고, 계정과 데이터는 앱 안에서 언제든 삭제할 수 있습니다.</li>
</ul>
<h2>운영</h2>
<p>VI One은 서울 종로에서 운영합니다(운영 주체: Rigid Point Advisory). 앱은 iPhone용으로 App Store에서 제공되며, 구독은 Apple 인앱결제로 처리됩니다.</p>
<h2>연락처</h2>
<ul><li>이메일: <a href="mailto:hello@vione.app">hello@vione.app</a> — 기능 제안, 업종별 요청, 도입·제휴 문의</li><li><a href="https://hellosangwoo-ctrl.github.io/vione-legal/terms-of-service.html" rel="noopener">이용약관(EULA)</a> · <a href="https://hellosangwoo-ctrl.github.io/vione-legal/privacy-policy.html" rel="noopener">개인정보처리방침</a></li></ul>
<h2>언론·제휴 안내용 한 줄 소개</h2>
<div class="box">VI One(브이원)은 미용실·네일·카페·식당 등 소상공인을 위한 iPhone용 AI CRM 앱으로, 예약 관리·고객 관리(VIP·단골·노쇼 자동 태그)·간편 매출 기록·문자/카카오톡/WhatsApp 고객 소통·AI FAQ 자동응대(Pro)를 한 앱에 담았다. Starter 무료, Pro 월 39,000원·연 249,000원. 문의 hello@vione.app.</div>
<div class="cta"><h3>함께 만들어 주세요</h3><p>초기 이용 매장의 의견이 다음 버전을 결정합니다.</p>{cta('btn primary')}</div>
</article>"""))

    # ---- 404 ----
    P.append(dict(path='/404', noindex=True, title='페이지를 찾을 수 없습니다 — VI One', desc='요청한 페이지가 없습니다.',
        body=f"""<section><div class="wrap" style="text-align:center;padding:60px 0"><h1>페이지를 찾을 수 없습니다</h1><p class="muted">주소가 바뀌었거나 삭제된 페이지입니다.</p><p><a class="btn primary" href="/">홈으로</a> <a class="btn" href="/faq/">FAQ</a></p></div></section>"""))
    return P

# ---------------- llms.txt ----------------
def llms_txt(pages, site):
    lines = ["# VI One (브이원)", "",
             "> VI One(브이원)은 미용실·네일·카페·식당 같은 소상공인을 위한 iPhone용 AI CRM 앱입니다. 예약 관리, 고객 관리(VIP·단골·신규·노쇼 자동 태그), 간편 매출 기록, 문자·카카오톡·WhatsApp 고객 소통, AI FAQ 자동응대(Pro, 사람 확인 기본)를 한 앱에서 제공합니다. Starter 무료, Pro 월 39,000원 또는 연 249,000원(무료 체험 없음, Apple 인앱결제).", "",
             "핵심 원칙: AI는 사장님이 적어 둔 매장 FAQ만 근거로 답하고, 모르는 질문은 지어내지 않고 '사장님 답변 대기'로 넘깁니다. 1.0에는 결제 단말 연동·전화 자동 수신·직원 계정이 없습니다.", "",
             "## 주요 페이지", ""]
    names = {'/': '홈 — VI One 소개·기능 요약·요금·FAQ', '/features/': '기능 상세', '/pricing/': '요금(Starter 무료 / Pro 39,000원·249,000원)', '/faq/': 'FAQ 20문항',
             '/guides/': '사장님 가이드 목록', '/guides/no-show/': '미용실·네일샵 노쇼 줄이는 7가지 방법', '/guides/repeat-questions/': '반복 질문 자동응답 만드는 법(FAQ 설계 5단계)', '/guides/customer-messaging/': '고객 메시지 템플릿 10선',
             '/compare/': '비교 목록', '/compare/naver-booking/': '네이버 예약과 함께 쓰는 법', '/compare/kakao-kanana/': '카카오톡 채널 AI 상담과의 차이', '/about/': '소개·운영·연락처', '/en/': 'English overview'}
    for u, m, pr in pages:
        path = u.replace(site, '') or '/'
        lines.append(f"- [{names.get(path, path)}]({u})")
    lines += ["", "## 법적 고지", "", "- [이용약관(EULA)](https://hellosangwoo-ctrl.github.io/vione-legal/terms-of-service.html)", "- [개인정보처리방침](https://hellosangwoo-ctrl.github.io/vione-legal/privacy-policy.html)", "", "## 연락", "", "- hello@vione.app", "", f"## 전체 텍스트", "", f"- [llms-full.txt]({site}/llms-full.txt)"]
    return '\n'.join(lines) + '\n'

def llms_full(site):
    out = ["# VI One (브이원) — 전체 요약 (llms-full.txt)", "", f"갱신: {MOD}", "",
           "## 정의", "VI One(브이원)은 미용실·네일샵·카페·식당처럼 사장님 한 명이 예약과 손님 응대를 함께 감당하는 매장을 위한 iPhone용 AI CRM 앱입니다. 서울에서 운영합니다(운영 주체: Rigid Point Advisory). 문의 hello@vione.app.", "",
           "## 기능 (1.0)", "- 예약 관리: 리스트·주간 보기, 요청→확정→완료 상태, 취소·노쇼 표시, 대화 기록에서 예약 생성", "- 고객 관리: VIP(누적 결제·방문 많음)·단골(3회 이상)·신규·주의(노쇼 2회 이상) 자동 태그, 메모, 방문·결제·소통 이력", "- 간편 매출 기록: 상품명·수량·금액·결제수단 입력 → 고객별 이력·월 매출 집계 (결제 단말 연동은 1.0에 없음)", "- 고객 소통: 문자·WhatsApp·카카오톡(복사·붙여넣기)·전화 버튼, 템플릿(예약 리마인드/감사·재방문/노쇼 방지 확인/이벤트/리뷰 요청), 소통 이력 자동 기록, 소통함(전체/미처리/보낸 메시지), 수신 번호 연결 시 문자·WhatsApp 수신", "- AI FAQ 자동응대(Pro): 기본 FAQ 5종(영업시간·주차·예약·가격·위치)을 매장 답변으로 편집, 대화 상세에서 AI 답변 초안(매칭 정도 표시) → 사장님 확인 후 전송, 자동응답 토글, 모르는 질문은 '사장님 답변 대기'로 넘기고 답하면 FAQ 등록, AI 응답 테스트", "- 대시보드: 오늘 예약·전체 고객·이번달 예약·매출·노쇼·등록 서비스 KPI, 오늘의 인사이트(룰 기반), 처리할 일, 재방문 유도(뜸한 고객)", "- 설정: 매장 정보, 서비스(메뉴), 언어(한국어/English), 구독 관리/해지, 구매 복원, 계정 삭제", "",
           "## 요금", "- Starter: 무료 (예약·고객·매출 기록·소통 전체)", "- Pro: 월 39,000원 또는 연 249,000원 (AI FAQ 자동응대·AI 초안 포함), 무료 체험 없음, Apple 인앱결제, iPhone 설정 → Apple 계정 → 구독에서 해지, 기간 종료 24시간 전까지 미해지 시 자동 갱신", "",
           "## 원칙", "- 사람 확인 기본: AI 초안은 사장님이 확인 후 전송, 자동응답은 Pro에서 선택적으로 켬", "- AI는 매장 FAQ만 답하고 근거 없으면 답하지 않음(지어내지 않음)", "- 매장별 데이터 분리, 앱 내 계정·데이터 삭제", "- AI 응답은 참고용이며 최종 판단과 결정은 사장님이 함", "",
           "## 1.0에 없는 것", "결제 단말(POS) 자동 연동, 전화 자동 수신·응답, 직원 계정·다지점, Android(검토 중)", "",
           "## 함께 쓰기", "- 네이버 예약: 손님이 직접 잡는 예약 채널 → VI One은 전화·문자·카카오톡 예약과 전체 고객 이력·응대 담당 (보완 관계)", "- 카카오톡 채널 AI 상담(카나나 상담매니저): 카카오톡 채널 문의 응답 → VI One은 다채널 소통+예약·고객·매출 CRM, AI는 FAQ만·사람 확인 기본", "",
           "## FAQ"]
    for q, a in FAQ:
        out.append(f"Q. {q}")
        out.append(f"A. {_strip(a)}")
        out.append("")
    out += ["## 가이드 요약", "- 노쇼 줄이는 7가지: 확정 문자 즉시, 전날 오후 리마인드, 노쇼 이력 기록·등급별 대응, 취소·예약금 정책 한 문장, 변경·취소는 답장 한 번, 대기 명단, 월 1회 노쇼율(노쇼÷예약)", "- 반복 질문 자동응답 5단계: 1주 질문 수집 → 상위 5개(영업시간·주차·가격·예약·위치) → 답변은 숫자·예외·다음 행동 → 채널별 같은 답(원본 하나) → 모르면 답하지 않고 사람에게, 월 1회 갱신", "- 고객 메시지 템플릿 10선: 예약 확정, 전날 리마인드, 당일 리마인드, 노쇼 방지 확인, 방문 감사, 재방문 유도, 리뷰 요청, 이벤트((광고)·무료수신거부 표기), 예약 변경 안내, 휴무 안내", "",
            "## 링크", f"- 홈 {site}/", f"- 기능 {site}/features/", f"- 요금 {site}/pricing/", f"- FAQ {site}/faq/", f"- 가이드 {site}/guides/", f"- 비교 {site}/compare/", f"- 소개 {site}/about/", f"- English {site}/en/", "- 이용약관 https://hellosangwoo-ctrl.github.io/vione-legal/terms-of-service.html", "- 개인정보처리방침 https://hellosangwoo-ctrl.github.io/vione-legal/privacy-policy.html"]
    return '\n'.join(out) + '\n'
