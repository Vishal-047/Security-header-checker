@echo off
echo ========================================
echo Security Header Checker - Vercel Deployment
echo ========================================
echo.

echo Step 1: Initializing Git repository...
git init
git add .
git commit -m "Initial commit for Vercel deployment"

echo.
echo Step 2: Git repository initialized successfully!
echo.
echo Next steps:
echo 1. Create a GitHub repository at https://github.com
echo 2. Run these commands (replace with your repo URL):
echo    git remote add origin https://github.com/YOUR_USERNAME/YOUR_REPO_NAME.git
echo    git branch -M main
echo    git push -u origin main
echo.
echo 3. Deploy to Vercel:
echo    - Go to https://vercel.com/dashboard
echo    - Click "New Project"
echo    - Import your GitHub repository
echo    - Deploy!
echo.
echo For detailed instructions, see DEPLOYMENT.md
echo.
pause 