# 🏥 Arix Stroke Prediction System

AI-powered healthcare application for early stroke risk detection using machine learning. Built with Flask, scikit-learn, and modern ML algorithms.

## ✨ Features

- **Sequential Workflow** - Enforced step-by-step process (Upload → Preprocess → Train → Predict → Analysis)
- **7 ML Algorithms** - Random Forest, XGBoost, CatBoost, SVM, KNN, Logistic Regression, Naive Bayes
- **Smart Preprocessing** - SMOTE for class balancing, feature selection, and data scaling
- **Flexible Predictions** - Single patient or batch CSV predictions
- **Model Persistence** - Save and load trained models
- **Rich Analytics** - Interactive visualizations, feature importance, and comprehensive metrics
- **Responsive UI** - Modern, mobile-friendly interface with smooth animations

## 🚀 Quick Start

### Prerequisites
- Python 3.8 or higher
- pip package manager

### Installation

1. **Clone the repository**
```bash
git clone https://github.com/YOUR_USERNAME/StrokePrediction.git
cd StrokePrediction
```

2. **Install dependencies**
```bash
pip install -r requirements.txt
```

3. **Run the application**
```bash
python flask_app.py
```
Or double-click `RUN_APP.bat` (Windows)

4. **Open your browser**
```
http://127.0.0.1:5000
```

## 📊 Workflow

The application enforces a strict sequential workflow to ensure data integrity:

1. **📤 Upload Data** - Upload custom CSV or use the default dataset (5,110 records)
2. **⚙️ Preprocess** - Automatic data cleaning, encoding, scaling, SMOTE, and feature selection
3. **🎯 Train Model** - Choose from 7 ML algorithms and compare performance
4. **🔮 Predict** - Make predictions on individual patients or batch CSV files
5. **📈 Analysis** - View comprehensive data insights, visualizations, and feature importance

> **Note:** You must complete each step before proceeding to the next. The system automatically redirects if you skip steps.

## 📁 Project Structure

```
StrokePrediction/
├── flask_app.py              # Main Flask application with routes
├── stroke_ml.py              # ML backend (preprocessing, training, prediction)
├── requirements.txt          # Python dependencies
├── RUN_APP.bat              # Windows quick start script
├── Dataset/
│   ├── healthcare-dataset-stroke-data.csv  # Default training dataset
│   └── testData.csv         # Sample test data
├── templates/               # HTML templates
│   ├── base.html           # Base template with navbar
│   ├── home.html           # Landing page
│   ├── upload.html         # Data upload page
│   ├── preprocess.html     # Preprocessing page
│   ├── train.html          # Model training page
│   ├── predict.html        # Prediction page
│   ├── analysis.html       # Data analysis & visualizations
│   └── learn_more.html     # Information page
├── static/                  # Static assets (images, CSS, JS)
└── uploads/                # Temporary upload directory (git-ignored)
```

## 📋 Required Dataset Format

For custom CSV uploads, your dataset must include these columns:

**Features:**
- `gender` - Male/Female/Other
- `age` - Patient age
- `hypertension` - 0 (No) or 1 (Yes)
- `heart_disease` - 0 (No) or 1 (Yes)
- `ever_married` - Yes/No
- `work_type` - Private/Self-employed/Govt_job/children/Never_worked
- `Residence_type` - Urban/Rural
- `avg_glucose_level` - Average glucose level
- `bmi` - Body Mass Index
- `smoking_status` - formerly smoked/never smoked/smokes/Unknown

**Target (for training only):**
- `stroke` - 0 (No stroke) or 1 (Stroke)

## 🔧 Technology Stack

- **Backend:** Flask 3.0+
- **ML:** scikit-learn, XGBoost, CatBoost, imbalanced-learn
- **Data:** pandas, numpy
- **Visualization:** matplotlib, seaborn
- **Frontend:** Bootstrap 5, vanilla JavaScript

## 🎨 UI Highlights

- Clean, modern design with smooth animations
- Mobile-responsive interface
- Real-time loading indicators and progress overlays
- Interactive charts and visualizations
- Workflow indicator showing current step

## 🤖 Available ML Models

1. **Random Forest** (Default) - Ensemble of decision trees
2. **XGBoost** - Gradient boosting algorithm
3. **CatBoost** - Gradient boosting optimized for categorical features
4. **SVM** - Support Vector Machine
5. **KNN** - K-Nearest Neighbors
6. **Logistic Regression** - Linear classification
7. **Naive Bayes** - Probabilistic classifier

## 📝 Usage Example

1. Start the app and navigate to Upload page
2. Click "Load Default Dataset" or upload your CSV
3. Click "Run Preprocessing" - data is automatically cleaned and prepared
4. Go to Train page, select "Random Forest", click "Train Model"
5. View metrics (accuracy, precision, recall, F1-score)
6. Navigate to Predict page for individual or batch predictions
7. Check Analysis page for data insights and feature importance

## 👨‍💻 Developer

**Ahmed** - 2024-2025
Arix Stroke Prediction System

## 📄 License

All Rights Reserved

## 🙏 Acknowledgments

- Healthcare dataset from Kaggle
- Built with Flask and scikit-learn
- UI inspired by modern healthcare dashboards
