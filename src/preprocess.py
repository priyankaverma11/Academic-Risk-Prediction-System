import pandas as pd

df = pd.read_csv("data/StudentsPerformance.csv")

# Create average score
df["average_score"] = (
    df["math score"]
    + df["reading score"]
    + df["writing score"]
) / 3

# Create risk level
def assign_risk(score):
    if score >= 80:
        return "Low"
    elif score >= 60:
        return "Medium"
    else:
        return "High"

df["risk_level"] = df["average_score"].apply(assign_risk)

# Convert text columns to numbers
df_encoded = pd.get_dummies(df)

print(df_encoded.head())

print("\nShape:")
print(df_encoded.shape)