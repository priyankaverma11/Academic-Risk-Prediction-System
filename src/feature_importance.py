import pandas as pd
import matplotlib.pyplot as plt

from sklearn.ensemble import RandomForestClassifier

df = pd.read_csv("data/StudentsPerformance.csv")

# Average score
df["average_score"] = (
    df["math score"]
    + df["reading score"]
    + df["writing score"]
) / 3

# Risk labels
def assign_risk(score):
    if score >= 80:
        return 2
    elif score >= 60:
        return 1
    else:
        return 0

df["risk_level"] = df["average_score"].apply(assign_risk)

# Features
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

# Train model
model = RandomForestClassifier(
    n_estimators=100,
    random_state=42
)

model.fit(X, y)

# Feature importance
importance = pd.DataFrame({
    "Feature": X.columns,
    "Importance": model.feature_importances_
})

importance = importance.sort_values(
    by="Importance",
    ascending=False
)

top10 = importance.head(10)

plt.figure(figsize=(10, 6))

plt.barh(
    top10["Feature"],
    top10["Importance"]
)

plt.title("Top 10 Most Important Features")
plt.xlabel("Importance")

plt.tight_layout()

plt.savefig(
    "images/feature_importance.png"
)

plt.show()
