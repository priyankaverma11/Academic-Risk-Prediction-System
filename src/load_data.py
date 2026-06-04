import pandas as pd

df = pd.read_csv("data/StudentsPerformance.csv")

print(df.head())

print("\nRows and Columns:")
print(df.shape)

print("\nColumn Names:")
print(df.columns)