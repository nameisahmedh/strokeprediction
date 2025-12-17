# Deployment Guide - Stroke Prediction Application

This guide provides step-by-step instructions for deploying the Stroke Prediction Flask application to various hosting platforms.

## Prerequisites

- GitHub repository: https://github.com/nameisahmedh/strokeprediction
- Python 3.10+ runtime
- Git installed locally

## Application Overview

The Stroke Prediction application is a Flask-based ML system featuring:
- 7 ML algorithms (RandomForest, XGBoost, CatBoost, SVM, KNN, Logistic Regression, Naive Bayes)
- Sequential workflow: Upload → Preprocess → Train → Predict → Analysis
- Automatic model training on first run
- Modern responsive UI

## Important Notes

⚠️ **Model File**: The trained model (`stroke_model.pkl`) is NOT included in the repository (12MB file, gitignored). The application will automatically train a new model on first run when you upload a dataset and follow the workflow.

⚠️ **First Deployment**: The initial model training may take 2-3 minutes. This is normal and only happens once per deployment.

## Option 1: Deploy to Render (Recommended - Free Tier Available)

Render offers a generous free tier and easy deployment.

### Steps:

1. **Sign up for Render**
   - Go to https://render.com
   - Sign up with GitHub

2. **Create New Web Service**
   - Click "New +" → "Web Service"
   - Connect your GitHub repository: `nameisahmedh/strokeprediction`

3. **Configure Build Settings**
   - **Name**: `stroke-prediction` (or your choice)
   - **Environment**: `Python 3`
   - **Build Command**: `pip install -r requirements.txt`
   - **Start Command**: `gunicorn flask_app:app`

4. **Advanced Settings**
   - **Python Version**: `3.10.13` (auto-detected from runtime.txt)
   - **Instance Type**: `Free`

5. **Deploy**
   - Click "Create Web Service"
   - Wait 3-5 minutes for deployment
   - Your app will be available at: `https://stroke-prediction-xxxx.onrender.com`

6. **First Run Setup**
   - Visit your app URL
   - Upload the dataset (`Dataset/healthcare-dataset-stroke-data.csv`)
   - Follow the workflow: Preprocess → Train → Predict
   - First training will take 2-3 minutes

## Option 2: Deploy to Railway

Railway offers easy deployment with a generous free trial.

### Steps:

1. **Sign up for Railway**
   - Go to https://railway.app
   - Sign up with GitHub

2. **Deploy from GitHub**
   - Click "New Project" → "Deploy from GitHub repo"
   - Select `nameisahmedh/strokeprediction`

3. **Configure**
   - Railway automatically detects Python and uses Procfile
   - No additional configuration needed

4. **Deploy**
   - Click "Deploy"
   - Get your app URL from the deployment dashboard

## Option 3: Deploy to Heroku

Heroku is a popular platform but requires a credit card for verification (free tier available).

### Steps:

1. **Install Heroku CLI**
   ```powershell
   winget install Heroku.HerokuCLI
   ```

2. **Login to Heroku**
   ```powershell
   heroku login
   ```

3. **Create Heroku App**
   ```powershell
   cd c:\Users\Ahmed\OneDrive\Documents\PROJECTS_AHMED\StrokePrediction
   heroku create stroke-prediction-app
   ```

4. **Deploy**
   ```powershell
   git push heroku main
   ```

5. **Open App**
   ```powershell
   heroku open
   ```

## Option 4: Deploy to PythonAnywhere

PythonAnywhere offers a free tier with persistent storage.

### Steps:

1. **Sign up**
   - Go to https://www.pythonanywhere.com
   - Create a free account

2. **Upload Files**
   - Use the Files tab to create a new directory
   - Upload all project files except `__pycache__` and `.pkl` files

3. **Install Dependencies**
   - Open a Bash console
   ```bash
   cd mysite
   pip install --user -r requirements.txt
   ```

4. **Configure Web App**
   - Go to Web tab
   - Add a new web app (Flask)
   - Set working directory and WSGI file
   - Point to `flask_app.py`

5. **Reload and Test**

## Troubleshooting

### Issue: "Application Error" on First Load
**Solution**: Wait 2-3 minutes for the first deployment to complete. Check deployment logs.

### Issue: "No Module Named 'flask'"
**Solution**: Ensure `requirements.txt` is present and all dependencies are installed during build.

### Issue: "Model Not Found"
**Solution**: This is expected! Upload a dataset and train the model using the UI workflow.

### Issue: Memory Errors During Training
**Solution**: 
- Use the free tier dataset (included: `healthcare-dataset-stroke-data.csv`)
- For larger datasets, upgrade to a paid tier with more RAM
- Consider reducing the number of algorithms in `stroke_ml.py`

### Issue: Slow First Response
**Solution**: Free tier instances may sleep after inactivity. First request might take 30-60 seconds to wake up.

## Post-Deployment Checklist

- [ ] Visit the deployed URL
- [ ] Verify homepage loads correctly
- [ ] Upload the default dataset
- [ ] Complete preprocessing step
- [ ] Train the model (wait 2-3 minutes)
- [ ] Make a prediction
- [ ] View analysis and feature importance
- [ ] Test saving/loading model

## Updating the Deployment

When you push new changes to GitHub:

```powershell
cd c:\Users\Ahmed\OneDrive\Documents\PROJECTS_AHMED\StrokePrediction
git add .
git commit -m "Description of changes"
git push origin main
```

**Render/Railway**: Auto-deploys on push (if enabled)
**Heroku**: Run `git push heroku main`

## Support

For deployment issues:
- Render: https://render.com/docs
- Railway: https://docs.railway.app
- Heroku: https://devcenter.heroku.com

For application issues, check the deployment logs on your platform's dashboard.
