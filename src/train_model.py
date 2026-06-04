import pandas as pd

from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import accuracy_score

# Load dataset
df = pd.read_csv("data/StudentsPerformance.csv")

# Average score
df["average_score"] = (
    df["math score"]
    + df["reading score"]
    + df["writing score"]
) / 3

# Risk level
def assign_risk(score):
    if score >= 80:
        return 2      # Low Risk
    elif score >= 60:
        return 1      # Medium Risk
    else:
        return 0      # High Risk

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

# Convert text columns
X = pd.get_dummies(X)

# Target
y = df["risk_level"]

# Split data
X_train, X_test, y_train, y_test = train_test_split(
    X,
    y,
    test_size=0.2,
    random_state=42
)

# Train model
model = RandomForestClassifier(
    n_estimators=100,
    random_state=42
)

model.fit(X_train, y_train)

# Predictions
predictions = model.predict(X_test)

# Accuracy
accuracy = accuracy_score(y_test, predictions)

print("Accuracy:", accuracy)

from sklearn.metrics import confusion_matrix

print(confusion_matrix(y_test, predictions))

import pandas as pd

importance = pd.DataFrame({
    "Feature": X.columns,
    "Importance": model.feature_importances_
})

importance = importance.sort_values(
    by="Importance",
    ascending=False
)

print(importance.head(10))