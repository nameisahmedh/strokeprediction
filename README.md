# 🏥 Arix Stroke Prediction System

<div align="center">

![Python](https://img.shields.io/badge/Python-3.8%2B-blue)
![Flask](https://img.shields.io/badge/Flask-3.0%2B-green)
![License](https://img.shields.io/badge/License-MIT-yellow)
![ML](https://img.shields.io/badge/ML-7%20Algorithms-orange)

**AI-powered healthcare application for early stroke risk detection using machine learning**

[Live Demo](https://strokeprediction.onrender.com) • [Report Bug](https://github.com/nameisahmedh/strokeprediction/issues) • [Request Feature](https://github.com/nameisahmedh/strokeprediction/issues)

</div>

---

## 📖 Table of Contents

- [Features](#-features)
- [Demo](#-demo)
- [Quick Start](#-quick-start)
- [Workflow](#-workflow)
- [Tech Stack](#-tech-stack)
- [Project Structure](#-project-structure)
- [ML Models](#-ml-models)
- [Deployment](#-deployment)
- [Contributing](#-contributing)
- [License](#-license)

## ✨ Features

- **🔒 Sequential Workflow** - Enforced step-by-step process preventing errors
- **🤖 7 ML Algorithms** - RandomForest, XGBoost, CatBoost, SVM, KNN, LogisticRegression, NaiveBayes
- **⚙️ Smart Preprocessing** - SMOTE oversampling, MinMax scaling, Chi2 feature selection
- **🎯 Flexible Predictions** - Single patient or batch CSV predictions
- **💾 Model Persistence** - Save and load trained models (`.pkl` format)
- **📊 Rich Analytics** - Interactive visualizations, feature importance, confusion matrix
- **📱 Responsive UI** - Modern, mobile-friendly interface with smooth animations
- **🚀 Production Ready** - Deployed on Render with gunicorn

## 🎬 Demo

### Workflow Steps
1. **Upload** → Load default dataset (5,110 records) or upload custom CSV
2. **Preprocess** → Automatic data cleaning, encoding, SMOTE, feature selection
3. **Train** → Select algorithm, train model, view metrics
4. **Predict** → Individual or batch predictions
5. **Analysis** → Data insights, visualizations, feature importance

### Screenshots

*Coming soon - Add screenshots of your deployed app*

## 🚀 Quick Start

### Prerequisites
```bash
Python 3.8+
pip
Git
```

### Local Installation

1. **Clone the repository**
```bash
git clone https://github.com/nameisahmedh/strokeprediction.git
cd strokeprediction
```

2. **Install dependencies**
```bash
pip install -r requirements.txt
```

3. **Run the application**
```bash
python flask_app.py
```

4. **Open browser**
```
http://127.0.0.1:5000
```

### Quick Start (Windows)
Double-click `RUN_APP.bat`

## 📊 Workflow

The application enforces a **strict sequential workflow** to ensure data integrity:

```
┌─────────────┐     ┌──────────────┐     ┌─────────────┐     ┌─────────────┐     ┌──────────────┐
│   Upload    │ --> │  Preprocess  │ --> │    Train    │ --> │   Predict   │ --> │   Analysis   │
│   Dataset   │     │     Data     │     │    Model    │     │   Results   │     │   Insights   │
└─────────────┘     └──────────────┘     └─────────────┘     └─────────────┘     └──────────────┘
```

> **Note:** You must complete each step before proceeding to the next. The system automatically redirects if prerequisites are missing.

## 🛠️ Tech Stack

### Backend
- **Framework:** Flask 3.0+
- **ML/Data:** scikit-learn, XGBoost, CatBoost, pandas, numpy
- **Preprocessing:** imbalanced-learn (SMOTE)
- **Visualization:** matplotlib, seaborn
- **Server:** Gunicorn (production)

### Frontend
- **UI Framework:** Bootstrap 5
- **JavaScript:** Vanilla JS (async/await)
- **Icons:** Font Awesome
- **Styling:** Custom CSS with animations

### Deployment
- **Platform:** Render
- **CI/CD:** GitHub integration
- **Storage:** In-memory session (can upgrade to Redis)

## 📁 Project Structure

```
strokeprediction/
├── flask_app.py              # Main Flask application (routes, API endpoints)
├── stroke_ml.py              # ML module (preprocessing, training, prediction)
├── requirements.txt          # Python dependencies
├── Procfile                  # Render deployment config
├── .gitignore                # Git ignore rules
├── README.md                 # Project documentation
├── RUN_APP.bat               # Windows quick start
├── PUSH_TO_GITHUB.bat        # Git push automation
│
├── Dataset/
│   ├── healthcare-dataset-stroke-data.csv  # Training data (5,110 records)
│   └── testData.csv                        # Sample test data
│
├── templates/                # HTML templates
│   ├── base.html            # Base layout with navbar
│   ├── home.html            # Landing page
│   ├── upload.html          # Data upload interface
│   ├── preprocess.html      # Preprocessing page
│   ├── train.html           # Model training interface
│   ├── predict.html         # Prediction interface
│   ├── analysis.html        # Analytics dashboard
│   └── learn_more.html      # Information page
│
├── static/                   # Static assets
│   └── images/              # Images, logos
│
└── uploads/                 # Temporary upload directory (git-ignored)
    └── .gitkeep
```

## 🤖 ML Models

| Model | Type | Best For | Accuracy* |
|-------|------|----------|-----------|
| **Random Forest** ⭐ | Ensemble | Default choice, balanced performance | ~94% |
| **XGBoost** | Gradient Boosting | High accuracy, feature importance | ~95% |
| **CatBoost** | Gradient Boosting | Categorical features | ~94% |
| **SVM** | Support Vector | Non-linear patterns | ~92% |
| **KNN** | Instance-based | Small datasets | ~89% |
| **Logistic Regression** | Linear | Interpretability | ~91% |
| **Naive Bayes** | Probabilistic | Fast training | ~88% |

*Approximate accuracy on default dataset after preprocessing

### Preprocessing Pipeline
1. **Missing Values** → Fill with 0
2. **Encoding** → LabelEncoder for categorical features
3. **Scaling** → MinMaxScaler (0-1 range)
4. **Balancing** → SMOTE oversampling for minority class
5. **Feature Selection** → SelectKBest (Chi2, k=9)
6. **Train/Test Split** → 80/20 split

## 📋 Dataset Format

### Required Columns for Training

| Column | Type | Values | Description |
|--------|------|--------|-------------|
| `gender` | Categorical | Male, Female, Other | Patient gender |
| `age` | Numeric | 0-120 | Patient age in years |
| `hypertension` | Binary | 0, 1 | Has hypertension |
| `heart_disease` | Binary | 0, 1 | Has heart disease |
| `ever_married` | Categorical | Yes, No | Marital status |
| `work_type` | Categorical | Private, Self-employed, Govt_job, children, Never_worked | Work type |
| `Residence_type` | Categorical | Urban, Rural | Residence type |
| `avg_glucose_level` | Numeric | 50-300 | Average glucose level |
| `bmi` | Numeric | 10-100 | Body Mass Index |
| `smoking_status` | Categorical | formerly smoked, never smoked, smokes, Unknown | Smoking status |
| `stroke` | Binary | 0, 1 | **Target variable** (1=stroke, 0=no stroke) |

## 🚀 Deployment

### Deploy to Render

1. **Push code to GitHub**
```bash
git add .
git commit -m "Deploy to Render"
git push origin main
```

2. **Create Render account**
- Go to [render.com](https://render.com)
- Sign up with GitHub

3. **Create Web Service**
- New → Web Service
- Connect repository: `nameisahmedh/strokeprediction`
- Build Command: `pip install -r requirements.txt`
- Start Command: `gunicorn flask_app:app`
- Instance: Free or Starter ($7/month)

4. **Deploy**
- Click "Create Web Service"
- Wait 5-10 minutes
- Access at: `https://strokeprediction.onrender.com`

### Environment Variables (Optional)
```
PYTHON_VERSION=3.11.0
SECRET_KEY=your-secret-key-here
```

## 📈 Usage Example

```python
# 1. Start the application
python flask_app.py

# 2. Open browser
http://127.0.0.1:5000

# 3. Upload dataset
- Click "Load Default Dataset" (5,110 records)
- Or upload custom CSV

# 4. Preprocess
- Click "Run Preprocessing"
- Automatic: encoding, scaling, SMOTE, feature selection

# 5. Train model
- Select algorithm (e.g., Random Forest)
- Click "Train Model"
- View accuracy, precision, recall, F1-score

# 6. Make predictions
- Single patient: Fill form, click "Predict"
- Batch: Upload CSV, click "Predict from CSV"

# 7. View analysis
- Click "Generate Analysis"
- View charts, statistics, feature importance
```

## 🤝 Contributing

Contributions are welcome! Please follow these steps:

1. Fork the repository
2. Create feature branch (`git checkout -b feature/AmazingFeature`)
3. Commit changes (`git commit -m 'Add AmazingFeature'`)
4. Push to branch (`git push origin feature/AmazingFeature`)
5. Open Pull Request

## 📝 License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## 👨‍💻 Author

**Ahmed**
- GitHub: [@nameisahmedh](https://github.com/nameisahmedh)
- Project: [Stroke Prediction System](https://github.com/nameisahmedh/strokeprediction)

## 🙏 Acknowledgments

- Dataset: [Kaggle Healthcare Stroke Dataset](https://www.kaggle.com/datasets/fedesoriano/stroke-prediction-dataset)
- Built with Flask & scikit-learn
- UI inspired by modern healthcare dashboards
- Deployed on Render

## 📞 Support

For support, email [your-email@example.com] or open an issue on GitHub.

---

<div align="center">
Made with ❤️ by Ahmed | © 2024-2025
</div>
