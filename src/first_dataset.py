import pandas as pd

data = {
    "attendance": [95, 80, 60, 75, 90],
    "study_hours": [20, 12, 5, 8, 15],
    "assignments": [100, 80, 50, 70, 95],
    "risk_level": ["Low", "Medium", "High", "Medium", "Low"]
}

df = pd.DataFrame(data)

print("Full Dataset:")
print(df)

print("\nFirst 3 rows:")
print(df.head(3))

print("\nDataset Information:")
df.info()

print("\nStatistics:")
print(df.describe())