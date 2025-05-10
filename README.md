# 🧠 Stroke Prediction Desktop App

This is a desktop-based Stroke Prediction application built using **Python (Tkinter)** and multiple **machine learning models**. It allows users to input health parameters and predicts the likelihood of a stroke using models like Random Forest, Logistic Regression, SVM, KNN, Naive Bayes, XGBoost, and CatBoost.

## 🚀 Features

* User-friendly GUI built with Tkinter
* Multiple ML model options for prediction
* Data preprocessing with handling of missing values and label encoding
* SMOTE applied for balancing imbalanced datasets
* Visualizations like confusion matrix, ROC curve, and feature importance

## ⚙️ Technologies Used

* Python
* Tkinter
* Scikit-learn
* XGBoost, CatBoost
* imbalanced-learn (SMOTE)
* Pandas, NumPy
* Matplotlib / Seaborn

## 📅 How to Run

1. Clone the repository:

   ```bash
   git clone https://github.com/nameisahmedh/strokeprediction.git
   cd strokeprediction
   ```

2. Install dependencies:

   ```bash
   pip install -r requirements.txt
   ```

3. Run the application:

   ```bash
   python Main.py
   ```

## 📊 Input Parameters

* Age
* Hypertension
* Heart Disease
* Avg Glucose Level
* BMI
* Smoking Status
* Gender
* Work Type
* Residence Type

## 📌 Project Goal

To assist in early detection of stroke risk using ML and a simple interface, especially useful for healthcare screening and educational purposes.

---

## 🤝 Contributing

Pull requests are welcome. For major changes, please open an issue first to discuss what you would like to change.

---

## 📜 License

[MIT](LICENSE)
