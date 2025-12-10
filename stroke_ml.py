"""
Stroke Prediction ML Backend Module

Provides functions for:
- Data preprocessing (encoding, scaling, SMOTE, feature selection)
- Model training and evaluation
- Predictions on new data
- Model persistence (save/load)
"""
import numpy as np
import pandas as pd
from sklearn.preprocessing import LabelEncoder, MinMaxScaler
from imblearn.over_sampling import SMOTE
from sklearn.feature_selection import SelectKBest, chi2
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestClassifier
from sklearn.linear_model import LogisticRegression
from sklearn import svm
from sklearn.neighbors import KNeighborsClassifier
from sklearn.naive_bayes import GaussianNB
from sklearn.metrics import accuracy_score, precision_score, recall_score, f1_score, confusion_matrix, roc_curve, auc, precision_recall_curve
import joblib
import warnings

# Optional heavy libs
try:
    from xgboost import XGBClassifier
    HAS_XGBOOST = True
except Exception:
    XGBClassifier = None
    HAS_XGBOOST = False

try:
    import catboost as cb
    CatBoostClassifier = cb.CatBoostClassifier
    HAS_CATBOOST = True
except Exception:
    CatBoostClassifier = None
    HAS_CATBOOST = False

warnings.filterwarnings("ignore")


def get_model_ctor(name):
    name = name.lower()
    if name == "randomforest":
        return lambda: RandomForestClassifier(n_estimators=100, random_state=42)
    if name == "logisticregression":
        return lambda: LogisticRegression(max_iter=200, solver='lbfgs')
    if name == "svm":
        return lambda: svm.SVC(probability=True)
    if name == "knn":
        return lambda: KNeighborsClassifier(n_neighbors=3)
    if name == "naivebayes":
        return lambda: GaussianNB()
    if name == "xgboost" and HAS_XGBOOST:
        return lambda: XGBClassifier(use_label_encoder=False, eval_metric='logloss', verbosity=0)
    if name == "catboost" and HAS_CATBOOST:
        return lambda: CatBoostClassifier(verbose=0)
    raise ValueError(f"Unknown or unavailable model: {name}")


def preprocess_df(df: pd.DataFrame, categorical_cols=None, target='stroke', remove_cols=None, k_features=9):
    df = df.copy()
    remove_cols = remove_cols or ['id']
    df.fillna(0, inplace=True)
    if categorical_cols is None:
        categorical_cols = [c for c in ['gender', 'ever_married', 'work_type', 'Residence_type', 'smoking_status'] if c in df.columns]
    encoders = {}
    for c in categorical_cols:
        le = LabelEncoder()
        df[c] = le.fit_transform(df[c].astype(str))
        encoders[c] = le
    if target not in df.columns:
        raise ValueError(f"Target column '{target}' not found in dataframe.")
    y = df[target].values
    X_df = df.drop(columns=[target] + [c for c in remove_cols if c in df.columns], errors='ignore')
    feature_names = list(X_df.columns)
    scaler = MinMaxScaler()
    X_scaled = scaler.fit_transform(X_df.values)
    sm = SMOTE(random_state=42)
    X_res, y_res = sm.fit_resample(X_scaled, y)
    k = min(k_features, X_res.shape[1])
    selector = SelectKBest(score_func=chi2, k=k)
    X_sel = selector.fit_transform(np.abs(X_res), y_res)
    X_train, X_test, y_train, y_test = train_test_split(X_sel, y_res, test_size=0.2, random_state=42)
    return {
        "X_train": X_train, "X_test": X_test, "y_train": y_train, "y_test": y_test,
        "scaler": scaler, "selector": selector, "encoders": encoders, "feature_names": feature_names
    }


def train_and_evaluate(model_name: str, X_train, y_train, X_test, y_test):
    ctor = get_model_ctor(model_name)
    model = ctor()
    model.fit(X_train, y_train)
    y_pred = model.predict(X_test)
    y_proba = None
    if hasattr(model, "predict_proba"):
        try:
            y_proba = model.predict_proba(X_test)[:, 1]
        except Exception:
            y_proba = None
    metrics = {
        "accuracy": accuracy_score(y_test, y_pred),
        "precision": precision_score(y_test, y_pred, average='macro', zero_division=0),
        "recall": recall_score(y_test, y_pred, average='macro', zero_division=0),
        "f1": f1_score(y_test, y_pred, average='macro', zero_division=0),
        "confusion_matrix": confusion_matrix(y_test, y_pred),
        "y_pred": y_pred,
        "y_proba": y_proba
    }
    return model, metrics


def compare_models(names, X_train, y_train, X_test, y_test):
    results = {}
    for n in names:
        try:
            m, met = train_and_evaluate(n, X_train, y_train, X_test, y_test)
            results[n] = met
        except Exception as e:
            results[n] = {"error": str(e)}
    return results


def predict_dataframe(model, meta, df):
    df = df.copy()
    df.fillna(0, inplace=True)
    encoders = meta.get("encoders", {})
    feature_names = meta.get("feature_names", [])
    
    # Encode categorical columns
    for col, le in encoders.items():
        if col in df.columns:
            df[col] = df[col].astype(str).map(lambda v: v if v in le.classes_ else le.classes_[0])
            df[col] = le.transform(df[col])
    
    # Ensure all required features exist
    for col in feature_names:
        if col not in df.columns:
            df[col] = 0
    
    # Select only the features used in training
    X_raw = df[feature_names].values
    X_scaled = meta["scaler"].transform(X_raw)
    X_sel = meta["selector"].transform(X_scaled)
    preds = model.predict(X_sel)
    return preds


def save_artifact(path, model, meta):
    joblib.dump({"model": model, "meta": meta}, path)


def load_artifact(path):
    return joblib.load(path)


def roc_pr_curves(y_true, y_proba):
    if y_proba is None:
        return None
    fpr, tpr, _ = roc_curve(y_true, y_proba)
    roc_auc = auc(fpr, tpr)
    precision, recall, _ = precision_recall_curve(y_true, y_proba)
    return {"fpr": fpr, "tpr": tpr, "roc_auc": roc_auc, "precision": precision, "recall": recall}