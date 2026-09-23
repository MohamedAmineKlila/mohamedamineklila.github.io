@echo off
REM One-click publish: commit all changes and push to GitHub Pages.
cd /d "%~dp0"
git add -A
git commit -m "portfolio update"
git push
echo.
echo Deployed! Check https://mohamedamineklila.github.io/ in ~1-2 minutes.
pause