# Deploy to Render (Free Forever)

This guide will help you deploy to Render using Docker to avoid Python version issues.

## Why Docker on Render?

✅ **Bypasses Python version cache issues**  
✅ **Guaranteed Python 3.11.9**  
✅ **Free tier: 750 hours/month forever**  
✅ **No credit card required**

---

## Step-by-Step Deployment

### Step 1: Create Render Account
1. Go to https://render.com
2. Click "Get Started" and sign up with GitHub
3. Authorize Render to access your repositories

### Step 2: Create New Web Service
1. Click "New +" button in the top right
2. Select "Web Service"
3. Connect your GitHub repository: `nameisahmedh/strokeprediction`
4. Click "Connect"

### Step 3: Configure Service (IMPORTANT)

**Basic Settings:**
- **Name**: `strokeprediction` (or any name you like)
- **Region**: Choose closest to you
- **Branch**: `main`
- **Root Directory**: Leave blank

**Environment:**
- **Environment**: Select **`Docker`** ⚠️ **CRITICAL - Must select Docker**
- (Don't select Python - this causes the version issue)

**Instance Type:**
- Select **`Free`**

### Step 4: Deploy
1. Scroll down and click **"Create Web Service"**
2. Render will:
   - Use the `Dockerfile` from your repo
   - Install Python 3.11.9 (from Dockerfile)
   - Install all dependencies
   - Start the app with gunicorn
3. Wait 5-7 minutes for first build

### Step 5: Get Your URL
- Once deployed, you'll get a URL like: `https://strokeprediction.onrender.com`
- Click on it to open your app!

---

## After Deployment

### First-Time Setup:
1. Visit your Render URL
2. Click "Upload Dataset"
3. Upload: `Dataset/healthcare-dataset-stroke-data.csv`
4. Click "Preprocess Data"
5. Click "Train Model" (takes 2-3 minutes first time)
6. Navigate to "Predictions" to test!

### Important Notes:
⚠️ **Free tier sleeps after 15 minutes of inactivity**
- First request after sleep takes 30-60 seconds to wake up
- This is normal for free tier

⚠️ **Model is not saved in repo**
- You'll need to train the model after each deployment
- Takes 2-3 minutes

---

## Troubleshooting

### Build Fails?
**Solution**: Make sure you selected **Docker** as the environment, not Python!

### "This site can't be reached"?
**Solution**: Wait a few minutes after deployment. First build can take 5-7 minutes.

### App shows error on first load?
**Solution**: The free tier instance may be starting up. Wait 30-60 seconds and refresh.

### Need to redeploy?
1. Go to Render dashboard
2. Click your service
3. Click "Manual Deploy" → "Deploy latest commit"

---

## Auto-Deploy on Git Push

Render automatically redeploys when you push to GitHub:
```powershell
git add .
git commit -m "Update app"
git push origin main
# Render will auto-deploy in 2-3 minutes
```

---

## Free Tier Limits

- **750 hours/month** (enough for always-on with one app)
- **512 MB RAM** (sufficient for this app)
- **Sleeps after 15 min inactivity** (wakes on request)
- **No credit card required**
- **Forever free**

---

## Summary

1. Create Render account → https://render.com
2. New Web Service → Connect GitHub repo
3. **Select Docker environment** (not Python!)
4. Click "Create Web Service"
5. Wait 5-7 minutes
6. Visit your URL and upload dataset!

Your app will be live at: `https://strokeprediction.onrender.com` 🚀
