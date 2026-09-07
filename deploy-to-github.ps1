# VI One - vione.app GitHub Pages 1-shot Deploy
# Run (PowerShell):
#   cd C:\Users\hello\Downloads\vione_release\site ; .\deploy-to-github.ps1
#
# Requirements: Git + GitHub CLI logged in (gh auth login) - same as the legal repo deploy.

$ErrorActionPreference = "Stop"

$USER = "hellosangwoo-ctrl"
$REPO = "vione-site"
$DOMAIN = "vione.app"
$DIR = $PSScriptRoot

Write-Host ""
Write-Host "VI One site -> GitHub Pages deploy" -ForegroundColor Cyan
Write-Host "  User  : $USER"
Write-Host "  Repo  : $REPO"
Write-Host "  Dir   : $DIR"
Write-Host "  Domain: $DOMAIN"
Write-Host ""

Set-Location $DIR

if (-not (Test-Path "CNAME")) { Set-Content -Path "CNAME" -Value $DOMAIN -Encoding ASCII -NoNewline }
if (-not (Test-Path ".nojekyll")) { Set-Content -Path ".nojekyll" -Value "" -Encoding ASCII -NoNewline }

# 1) git init (first time only)
if (-not (Test-Path ".git")) {
    git init -b main | Out-Null
    Write-Host "[ok] git init" -ForegroundColor Green
}

# 2) commit
git add .
git commit -m "vione.app site publish" 2>&1 | Out-Null
Write-Host "[ok] commit" -ForegroundColor Green

# 3) create repo + push (skips creation if the repo already exists)
$exists = $false
try { gh repo view "$USER/$REPO" 2>&1 | Out-Null; $exists = $true } catch { $exists = $false }
if (-not $exists) {
    gh repo create "$USER/$REPO" --public --source=. --push --description "VI One (vione.app) marketing site - static HTML"
    Write-Host "[ok] repo created + pushed" -ForegroundColor Green
} else {
    if (-not (git remote 2>$null | Select-String -Quiet "origin")) { git remote add origin "https://github.com/$USER/$REPO.git" }
    git push -u origin main
    Write-Host "[ok] pushed to existing repo" -ForegroundColor Green
}

# 4) enable Pages (main, /) - ignore error if already enabled
try {
    gh api -X POST "repos/$USER/$REPO/pages" -f "source[branch]=main" -f "source[path]=/" 2>&1 | Out-Null
    Write-Host "[ok] Pages enabled" -ForegroundColor Green
} catch { Write-Host "[..] Pages already enabled" -ForegroundColor Yellow }

# 5) custom domain
try {
    gh api -X PUT "repos/$USER/$REPO/pages" -f "cname=$DOMAIN" 2>&1 | Out-Null
    Write-Host "[ok] custom domain set: $DOMAIN" -ForegroundColor Green
} catch { Write-Host "[..] set custom domain manually: Settings > Pages > Custom domain" -ForegroundColor Yellow }

Write-Host ""
Write-Host "Done. Next: GoDaddy DNS (see DEPLOY.md section 2)" -ForegroundColor Yellow
Write-Host "  A     @    185.199.108.153 / 185.199.109.153 / 185.199.110.153 / 185.199.111.153"
Write-Host "  CNAME www  $USER.github.io"
Write-Host "Then: GitHub > $REPO > Settings > Pages > Enforce HTTPS (after DNS check passes)"
Write-Host "Temporary URL (unstyled until domain works): https://$USER.github.io/$REPO/"
Write-Host ""
