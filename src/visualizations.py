import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_csv("data/StudentsPerformance.csv")

df["average_score"] = (
    df["math score"]
    + df["reading score"]
    + df["writing score"]
) / 3

# Graph 1
plt.figure()

plt.hist(df["average_score"], bins=20)

plt.title("Distribution of Student Scores")
plt.xlabel("Average Score")
plt.ylabel("Number of Students")

plt.savefig("images/score_distribution.png")

# Graph 2
plt.figure()

df.groupby(
    "test preparation course"
)["average_score"].mean().plot(
    kind="bar"
)

plt.title("Impact of Test Preparation on Scores")
plt.xlabel("Test Preparation")
plt.ylabel("Average Score")

plt.savefig("images/test_prep_impact.png")

plt.show()

# Graph 3
plt.figure()

df.groupby(
    "lunch"
)["average_score"].mean().plot(
    kind="bar"
)

plt.title("Impact of Lunch Type on Scores")
plt.xlabel("Lunch Type")
plt.ylabel("Average Score")

plt.savefig("images/lunch_impact.png")