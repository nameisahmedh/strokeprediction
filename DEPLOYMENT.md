# Deploy to Render (Docker)

This guide will help you deploy the Stroke Prediction app to Render using Docker.

## Prerequisites

- GitHub account with the repository pushed
- Render account (free tier available)

## Deployment Steps

### Step 1: Sign Up for Render

1. Go to https://render.com
2. Click **"Get Started"** or **"Sign In"**
3. Sign in with your GitHub account
4. Authorize Render to access your repositories

### Step 2: Create New Web Service

1. Click **"New +"** button (top right)
2. Select **"Web Service"**
3. Connect your repository: `nameisahmedh/strokeprediction`
4. Click **"Connect"**

### Step 3: Configure Service

**Name:** `strokeprediction` (or your preferred name)

**Region:** **Singapore** (closest to India)

**Branch:** `main`

**Root Directory:** Leave blank

**Environment:** **Docker** ⚠️ **CRITICAL - Must select Docker, NOT Python!**

**Instance Type:** **Free**

### Step 4: Deploy

1. Click **"Create Web Service"**
2. Wait 5-7 minutes for first build
3. Your app will be live at: `https://strokeprediction.onrender.com`

## After Deployment

### First-Time Setup

1. Visit your deployed URL
2. Upload the dataset: `healthcare-dataset-stroke-data.csv`
3. Click "Preprocess Data"
4. Click "Train Model" (takes 2-3 minutes)
5. Navigate to "Predictions" to test

### Important Notes

⚠️ **Free Tier Limitations:**
- Instance sleeps after 15 minutes of inactivity
- First request after sleep takes 30-60 seconds
- 750 hours/month (sufficient for personal projects)

⚠️ **Model Training:**
- Model is not saved in the repository
- Train model after each deployment
- Takes 2-3 minutes on first training

## Troubleshooting

### Build Fails

**Solution:** Ensure you selected **Docker** as environment, not Python

### Long First Load

**Solution:** Free tier instances sleep. Wait 30-60 seconds for wake-up

### "This site can't be reached"

**Solution:** Build may still be in progress. Check Render dashboard for status

## Auto-Deploy

Render automatically redeploys when you push to GitHub:

```bash
git add .
git commit -m "Update app"
git push origin main
# Render auto-deploys in 3-5 minutes
```

## Manual Redeploy

1. Go to Render dashboard
2. Click your service
3. Click **"Manual Deploy"** → **"Deploy latest commit"**

## Free Tier Details

- **750 hours/month** - enough for 24/7 with one app
- **512 MB RAM** - sufficient for this application
- **Automatic HTTPS** - included
- **Custom domain** - supported (optional)
- **Auto-deploy** - on git push

## Repository Files Used

- `Dockerfile` - Defines Python 3.11.9 environment
- `requirements.txt` - Python dependencies
- `Procfile` - Start command (used by Docker)
- `.gitignore` - Excludes unnecessary files

## Support

For deployment issues, check:
- Render docs: https://render.com/docs
- Render community: https://community.render.com

---

**Your app is now live!** 🚀

Visit your URL and start predicting stroke risk!
