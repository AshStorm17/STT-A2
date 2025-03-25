import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Load the CSV file (replace with actual filename)
df = pd.read_csv("mace.csv")

# Display basic information
print("Dataset Overview:\n", df.head())
print("\nSummary Statistics:\n", df.describe())

# Total vulnerabilities per severity
total_high = df["high_severity"].sum()
total_medium = df["medium_severity"].sum()
total_low = df["low_severity"].sum()

print(f"Total High Severity Issues: {total_high}")
print(f"Total Medium Severity Issues: {total_medium}")
print(f"Total Low Severity Issues: {total_low}")

# Average vulnerabilities per commit
print("\nAverage vulnerabilities per commit:")
print(df[["high_severity", "medium_severity", "low_severity"]].mean())

# Find the commit with the highest number of high-severity issues
worst_commit = df.loc[df["high_severity"].idxmax()]
print("\nCommit with Most High-Severity Issues:")
print(worst_commit)
