# Quick Deployment Guide - Railway (Recommended)

Railway is the easiest and most reliable platform for this app. It handles Python versions correctly and has excellent free tier.

## Deploy to Railway (5 Minutes)

### Step 1: Sign Up
1. Go to https://railway.app
2. Click "Login" and sign in with GitHub
3. Authorize Railway to access your repositories

### Step 2: Create New Project
1. Click "New Project"
2. Select "Deploy from GitHub repo"
3. Choose `nameisahmedh/strokeprediction`
4. Railway will automatically detect it's a Python app

### Step 3: Configure (Automatic)
Railway automatically:
- Detects Python from `runtime.txt` 
- Installs dependencies from `requirements.txt`
- Uses `Procfile` for start command
- Sets up environment variables

### Step 4: Deploy
1. Click "Deploy"
2. Wait 3-5 minutes for build
3. Railway will give you a URL like: `https://strokeprediction-production.up.railway.app`

### Step 5: Generate Domain (Optional)
1. Go to Settings → Networking
2. Click "Generate Domain"
3. Your app will be live!

## Why Railway?
✅ No Python 3.13 issues - properly respects runtime.txt
✅ Faster builds - uses pre-compiled wheels
✅ Free tier: 500 hours/month, $5 credit
✅ Auto-deploys on git push
✅ Better error messages
✅ No credit card required for free tier

## Troubleshooting

If build fails, check:
- Logs in Railway dashboard
- Make sure all files are pushed to GitHub
- Verify runtime.txt has `python-3.11.9`

## After Deployment

Visit your app URL and:
1. Upload dataset from `Dataset/healthcare-dataset-stroke-data.csv`
2. Preprocess data
3. Train model (2-3 minutes first time)
4. Make predictions!

---

# Alternative: Fix Render Deployment

If you must use Render, try these steps:

## Clear Render Cache
1. Go to your Render dashboard
2. Navigate to your web service
3. Click "Manual Deploy"   → "Clear build cache & deploy"
4. This forces Render to rebuild from scratch

## Or Create New Service
1. **Delete** the old Render service
2. Create a **brand new** web service
3. Fresh builds don't have caching issues

---

# Alternative: Heroku Deployment

```powershell
# Install Heroku CLI
winget install Heroku.HerokuCLI

# Login
heroku login

# Create app
cd c:\Users\Ahmed\OneDrive\Documents\PROJECTS_AHMED\StrokePrediction
heroku create strokeprediction

# Deploy
git push heroku main

# Open app
heroku open
```

---

**RECOMMENDATION**: Use Railway - it's specifically designed to avoid the issues you're experiencing with Render.
