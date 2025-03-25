import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import ast

# Load the analysis results
df = pd.read_csv("mace.csv")

# Convert commit column to string for better labeling
df["commit"] = df["commit"].astype(str)

# Set style
sns.set_theme(style="whitegrid")

# Plot confidence levels
plt.figure(figsize=(12, 6))
sns.lineplot(x=df["commit"], y=df["high_confidence"], label="High Confidence", marker="o", color="red")
sns.lineplot(x=df["commit"], y=df["medium_confidence"], label="Medium Confidence", marker="o", color="orange")
sns.lineplot(x=df["commit"], y=df["low_confidence"], label="Low Confidence", marker="o", color="green")
plt.xticks(rotation=45)
plt.xticks(range(0, len(df["commit"]), max(1, len(df["commit"]) // 10)), df["commit"][::max(1, len(df["commit"]) // 10)])
plt.title("Confidence Level of Issues per Commit")
plt.xlabel("Commit Hash")
plt.ylabel("Number of Issues")
plt.legend()
plt.grid(True, linestyle="--", alpha=0.5)
plt.tight_layout()
plt.savefig("confidence_mace.png")
plt.show()

# Plot severity levels
plt.figure(figsize=(12, 6))
sns.lineplot(x=df["commit"], y=df["high_severity"], label="High Severity", marker="o", color="red")
sns.lineplot(x=df["commit"], y=df["medium_severity"], label="Medium Severity", marker="o", color="orange")
sns.lineplot(x=df["commit"], y=df["low_severity"], label="Low Severity", marker="o", color="green")
plt.xticks(rotation=45)
plt.xticks(range(0, len(df["commit"]), max(1, len(df["commit"]) // 10)), df["commit"][::max(1, len(df["commit"]) // 10)])
plt.title("Severity Level of Issues per Commit")
plt.xlabel("Commit Hash")
plt.ylabel("Number of Issues")
plt.legend()
plt.grid(True, linestyle="--", alpha=0.5)
plt.tight_layout()
plt.savefig("severity_mace.png")
plt.show()

# Visualize CWE Frequency
df["unique_cwes"] = df["unique_cwes"].apply(lambda x: ast.literal_eval(x) if isinstance(x, str) else [])
cwe_series = df["unique_cwes"].explode().dropna().astype(str)
cwe_counts = cwe_series.value_counts().head(10)  # Top 10 CWEs

plt.figure(figsize=(10, 5))
sns.barplot(x=cwe_counts.index, y=cwe_counts.values, palette="Blues_r")
plt.title("Top 10 Most Frequent CWEs Across Commits")
plt.xlabel("CWE ID")
plt.ylabel("Frequency")
plt.xticks(rotation=45)
plt.grid(axis="y", linestyle="--", alpha=0.5)
plt.tight_layout()
plt.savefig("cwe_mace.png")
plt.show()
