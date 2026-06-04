import pandas as pd
import joblib

from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestClassifier

df = pd.read_csv("data/StudentsPerformance.csv")

df["average_score"] = (
    df["math score"]
    + df["reading score"]
    + df["writing score"]
) / 3

def assign_risk(score):
    if score >= 80:
        return 2
    elif score >= 60:
        return 1
    else:
        return 0

df["risk_level"] = df["average_score"].apply(assign_risk)

X = df[
    [
        "gender",
        "race/ethnicity",
        "parental level of education",
        "lunch",
        "test preparation course"
    ]
]

X = pd.get_dummies(X)

y = df["risk_level"]

model = RandomForestClassifier(
    n_estimators=100,
    random_state=42
)

model.fit(X, y)

joblib.dump(model, "student_risk_model.pkl")

print("Model saved successfully!")
