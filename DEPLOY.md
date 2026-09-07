# vione.app 배포 가이드 (GitHub Pages · 약 10분)

이 폴더(`site/`)가 그대로 웹사이트입니다. 빌드 없이 정적 HTML로 배포됩니다. 사장님이 직접 해야 하는 것은 **① GitHub 레포 생성·푸시(스크립트 1줄) ② GoDaddy DNS 변경** 두 가지입니다.

## 0. 폴더 구성

| 경로 | 내용 |
|---|---|
| `index.html` 외 13페이지 | 랜딩·기능·요금·FAQ·가이드 3·비교 2·소개·English·404 |
| `robots.txt` `sitemap.xml` `llms.txt` `llms-full.txt` `humans.txt` | 검색·AI 엔진용 |
| `CNAME` | `vione.app` (GitHub Pages 커스텀 도메인) |
| `.nojekyll` | Jekyll 처리 끄기(HTML 그대로 서빙) |
| `assets/img/` | 실제 앱 화면(590px), 아이콘, OG 이미지 |
| `src/build.py` `src/content_ko.py` `src/content_en.py` `src/site.css` | 페이지 생성기(수정 시 `python src/build.py` 실행) |
| `deploy-to-github.ps1` | 1회 배포 스크립트 (legal 레포와 같은 방식) |

## 1. GitHub Pages 배포 (PowerShell 한 줄)

사전 조건: Git + GitHub CLI 설치·로그인 (legal 레포 배포 때 이미 완료된 상태)

```powershell
cd C:\Users\hello\Downloads\vione_release\site ; .\deploy-to-github.ps1
```

스크립트가 하는 일: `git init` → 커밋 → `hellosangwoo-ctrl/vione-site` 공개 레포 생성·푸시 → Pages 활성화(main, /) → 커스텀 도메인 `vione.app` 설정.
1~3분 뒤 `https://hellosangwoo-ctrl.github.io/vione-site/` 에서 먼저 확인할 수 있습니다(커스텀 도메인 연결 전에는 CSS 경로가 절대경로라 이 임시 주소에서는 스타일이 깨져 보일 수 있음 — 정상. DNS 연결 후 vione.app에서 확인).

## 2. GoDaddy DNS 변경 (5분, 반영 10분~24시간)

GoDaddy → 내 도메인 → vione.app → DNS 관리. **기존 파킹/포워딩(Forwarding) 설정은 삭제**하고 아래 레코드를 넣습니다.

| 유형 | 이름 | 값 | TTL |
|---|---|---|---|
| A | @ | 185.199.108.153 | 600 |
| A | @ | 185.199.109.153 | 600 |
| A | @ | 185.199.110.153 | 600 |
| A | @ | 185.199.111.153 | 600 |
| CNAME | www | hellosangwoo-ctrl.github.io | 600 |

(선택) IPv6: AAAA @ → 2606:50c0:8000::153 / 8001::153 / 8002::153 / 8003::153

그 다음 GitHub → vione-site → Settings → Pages → Custom domain에 `vione.app`이 들어가 있는지 확인 → DNS 체크가 초록색이 되면 **Enforce HTTPS** 체크(인증서 발급 후 활성화됨, 최대 1시간).

## 3. 배포 직후 확인 (5분)

```
https://vione.app/            → 랜딩
https://vione.app/robots.txt  → "User-agent: *" 보이면 OK
https://vione.app/sitemap.xml
https://vione.app/llms.txt
https://www.vione.app/        → vione.app 으로 리다이렉트
```

## 4. 검색·AI 엔진 등록 (각 5분, 사장님 로그인 필요)

1. **Google Search Console** https://search.google.com/search-console — 도메인 속성 `vione.app` → GoDaddy에 TXT 레코드 추가로 소유 확인 → Sitemaps에 `https://vione.app/sitemap.xml` 제출 → URL 검사로 홈·기능·요금·FAQ 색인 요청
2. **Bing Webmaster Tools** https://www.bing.com/webmasters — "Google Search Console에서 가져오기" → 사이트맵 자동 → (설정) IndexNow 키 생성 → AI 성과 리포트 확인(Copilot 인용)
3. **네이버 서치어드바이저** https://searchadvisor.naver.com — 웹마스터 도구 → `https://vione.app` 등록 → 소유확인(HTML 파일: 다운로드한 파일을 `site/` 루트에 넣고 커밋·푸시 후 확인) → 요청 → 사이트맵 제출 `https://vione.app/sitemap.xml` → 웹페이지 수집 요청(페이지별)
4. **다음 검색등록** https://register.search.daum.net — 신규 등록 → `https://vione.app`

## 5. 나중에 바꿀 것

- **App Store 승인 후**: `src/build.py`의 `APP_STORE_URL = ''` 에 앱 URL 입력 → `python src/build.py` → 커밋·푸시. 모든 "출시 알림 받기" 버튼이 "App Store에서 다운로드"로 바뀌고 JSON-LD에 installUrl이 들어갑니다. (Claude에게 "App Store URL 반영해줘"라고 하면 됩니다)
- **GA4**: `GA_MEASUREMENT_ID = 'G-XXXX'` 입력 → 재빌드
- **콘텐츠 추가**: `src/content_ko.py`에 페이지 dict 추가 → 재빌드 → sitemap/llms.txt 자동 갱신

## 6. 업데이트 배포 (매번)

```powershell
cd C:\Users\hello\Downloads\vione_release\site ; python src\build.py ; git add . ; git commit -m "update" ; git push
```

## 참고 — legal 레포 한글 깨짐

`hellosangwoo-ctrl.github.io/vione-legal/index.html`(법적 문서 목록 페이지)의 한글이 깨져 보입니다(PowerShell 인코딩 문제). 약관·개인정보처리방침 문서 자체는 정상입니다. 원하시면 다음 세션에서 수정본을 만들어 드립니다.
