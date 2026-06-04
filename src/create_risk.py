import pandas as pd

df = pd.read_csv("data/StudentsPerformance.csv")

df["average_score"] = (
    df["math score"]
    + df["reading score"]
    + df["writing score"]
) / 3


def assign_risk(score):
    if score >= 80:
        return "Low"
    elif score >= 60:
        return "Medium"
    else:
        return "High"


df["risk_level"] = df["average_score"].apply(assign_risk)

print(df[["average_score", "risk_level"]].head())

print("\nRisk Distribution:")
print(df["risk_level"].value_counts())