import pandas as pd

df = pd.read_csv("data/StudentsPerformance.csv")

df["average_score"] = (
    df["math score"]
    + df["reading score"]
    + df["writing score"]
) / 3

print("Missing Values:")
print(df.isnull().sum())

print("\nAverage Score:")
print(df["average_score"].mean())

print("\nPerformance by Test Preparation:")
print(
    df.groupby("test preparation course")[
        "average_score"
    ].mean()
)

print("\nPerformance by Lunch Type:")
print(
    df.groupby("lunch")[
        "average_score"
    ].mean()
)