import streamlit as st
import pandas as pd
import numpy as np
from sklearn.preprocessing import StandardScaler
from sklearn.linear_model import LogisticRegression
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import accuracy_score, precision_score, recall_score, f1_score, roc_auc_score
import matplotlib.pyplot as plt

st.set_page_config(page_title="FIFA 2026 Finalists Prediction", layout="wide")
st.title("FIFA World Cup 2026 - Model-Based Finalists Prediction")

# -----------------------------
# Dataset (Corrected Teams)
# -----------------------------
teams = [
    "Argentina","France","Brazil","Germany","Spain","England","Portugal",
    "Netherlands","Italy","Croatia","Uruguay","Mexico","USA","Japan","Senegal",
    "Morocco","South Korea","Australia","Canada"
]

# Synthetic team features
np.random.seed(42)
df = pd.DataFrame({
    "Team": teams,
    "Avg_Age": np.random.randint(23, 32, size=len(teams)),
    "FIFA_Ranking": np.random.randint(1, 50, size=len(teams)),
    "Goal_Diff": np.random.randint(-5, 20, size=len(teams)),
    "Win_Rate": np.round(np.random.uniform(0.4, 0.9, size=len(teams)), 2)
})

# Synthetic targets for demonstration
y_rf = np.array([1 if t in ["Argentina","France","Brazil","Germany"] else 0 for t in df["Team"]])
y_lr = np.array([1 if t in ["Argentina","France","Brazil","Spain"] else 0 for t in df["Team"]])

# Features
feature_cols = ["Avg_Age","FIFA_Ranking","Goal_Diff","Win_Rate"]
X = df[feature_cols]
scaler = StandardScaler()
X_scaled = scaler.fit_transform(X)

# -----------------------------
# Train models
# -----------------------------
logreg = LogisticRegression()
logreg.fit(X_scaled, y_lr)

rf = RandomForestClassifier(n_estimators=100, random_state=42)
rf.fit(X, y_rf)

df["LR_Prob"] = logreg.predict_proba(X_scaled)[:,1]
df["RF_Prob"] = rf.predict_proba(X)[:,1]

# -----------------------------
# User selects model
# -----------------------------
model_choice = st.radio("Select Model", ("Random Forest", "Logistic Regression"))

if model_choice == "Random Forest":
    st.subheader("Random Forest Predictions")
    top_teams = df.sort_values("RF_Prob", ascending=False).head(2)
    st.write(top_teams[["Team","RF_Prob"]])
    
    st.subheader("Feature Importance")
    rf_imp = pd.DataFrame({"Feature": feature_cols, "Importance": rf.feature_importances_})
    st.bar_chart(rf_imp.set_index("Feature"))
    
    st.subheader("Metrics")
    st.write(f"Accuracy: {accuracy_score(y_rf, rf.predict(X)):.2f}")
    st.write(f"F1-Score: {f1_score(y_rf, rf.predict(X)):.2f}")
    st.write(f"ROC-AUC: {roc_auc_score(y_rf, df['RF_Prob']):.2f}")

else:
    st.subheader("Logistic Regression Predictions")
    top_teams = df.sort_values("LR_Prob", ascending=False).head(2)
    st.write(top_teams[["Team","LR_Prob"]])
    
    st.subheader("Feature Coefficients")
    lr_coef = pd.DataFrame({"Feature": feature_cols, "Coefficient": logreg.coef_[0]})
    st.bar_chart(lr_coef.set_index("Feature"))
    
    st.subheader("Metrics")
    st.write(f"Precision: {precision_score(y_lr, logreg.predict(X_scaled), zero_division=0):.2f}")
    st.write(f"Recall: {recall_score(y_lr, logreg.predict(X_scaled), zero_division=0):.2f}")
    st.write(f"F1-Score: {f1_score(y_lr, logreg.predict(X_scaled), zero_division=0):.2f}")

# -----------------------------
# Show full dataset table
# -----------------------------
st.subheader("Full Dataset")
st.dataframe(df)
