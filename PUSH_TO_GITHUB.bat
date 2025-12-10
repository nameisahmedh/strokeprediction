@echo off
echo ========================================
echo   GitHub Repository Update Script
echo   Arix Stroke Prediction System
echo ========================================
echo.

:: Check if git is installed
git --version >nul 2>&1
if errorlevel 1 (
    echo ERROR: Git is not installed or not in PATH
    echo Please install Git from https://git-scm.com/
    pause
    exit /b 1
)

cd /d "%~dp0"

echo Step 1: Initializing Git repository...
if not exist ".git" (
    git init
    echo Git repository initialized.
) else (
    echo Git repository already exists.
)

echo.
echo Step 2: Setting up remote repository...
git remote remove origin 2>nul
git remote add origin https://github.com/nameisahmedh/strokeprediction.git
echo Remote repository set to: https://github.com/nameisahmedh/strokeprediction.git

echo.
echo Step 3: Adding all files...
git add .
if errorlevel 1 (
    echo ERROR: Failed to add files
    pause
    exit /b 1
)

echo.
echo Step 4: Committing changes...
git commit -m "Complete rewrite: Arix Stroke Prediction System - Added sequential workflow enforcement - Implemented 7 ML algorithms (RandomForest, XGBoost, CatBoost, SVM, KNN, LogisticRegression, NaiveBayes) - Enhanced UI with modern responsive design - Added comprehensive data preprocessing (SMOTE, scaling, feature selection) - Fixed upload validation and workflow issues - Implemented feature importance visualization - Ready for production deployment"
if errorlevel 1 (
    echo WARNING: Commit failed or nothing to commit
)

echo.
echo Step 5: Setting branch to main...
git branch -M main

echo.
echo ========================================
echo   IMPORTANT: Authentication Required
echo ========================================
echo.
echo You will now be prompted to authenticate with GitHub.
echo.
echo If you have 2FA enabled, you'll need to use a Personal Access Token instead of your password.
echo.
echo To create a token:
echo 1. Go to GitHub Settings ^> Developer settings ^> Personal access tokens
echo 2. Generate new token (classic)
echo 3. Select 'repo' scope
echo 4. Copy the token and use it as your password
echo.
pause

echo.
echo Step 6: Pushing to GitHub (force update)...
echo This will replace all content in the repository.
git push -f origin main

if errorlevel 1 (
    echo.
    echo ERROR: Push failed!
    echo.
    echo Common issues:
    echo - Authentication failed
    echo - No internet connection
    echo - Repository permissions issue
    echo.
    echo Please check your credentials and try again.
    pause
    exit /b 1
)

echo.
echo ========================================
echo   SUCCESS! Repository Updated
echo ========================================
echo.
echo Your GitHub repository has been updated successfully!
echo.
echo Repository URL: https://github.com/nameisahmedh/strokeprediction
echo.
echo Files uploaded:
echo - Source code (flask_app.py, stroke_ml.py)
echo - All HTML templates
echo - Dataset files
echo - Updated README.md
echo - requirements.txt
echo - .gitignore
echo.
echo Visit your repository to see the changes!
echo.
pause
