import os
import json
import pandas as pd

# Directory containing Bandit reports
REPORTS_DIR = "mace/bandit_results"

# Data storage
results = []

# Process each Bandit report
for filename in sorted(os.listdir(REPORTS_DIR)):
    if filename.endswith(".json"):
        commit_hash = filename.split("_")[-1].split(".")[0]  # Extract commit hash
        file_path = os.path.join(REPORTS_DIR, filename)

        with open(file_path, "r") as file:
            data = json.load(file)

            # Extract confidence and severity metrics
            high_conf = 0
            med_conf = 0
            low_conf = 0
            high_sev = 0
            med_sev = 0
            low_sev = 0
            cwes = set()

            for file_metrics in data.get("metrics", {}).values():
                high_conf += file_metrics.get("CONFIDENCE.HIGH", 0)
                med_conf += file_metrics.get("CONFIDENCE.MEDIUM", 0)
                low_conf += file_metrics.get("CONFIDENCE.LOW", 0)
                high_sev += file_metrics.get("SEVERITY.HIGH", 0)
                med_sev += file_metrics.get("SEVERITY.MEDIUM", 0)
                low_sev += file_metrics.get("SEVERITY.LOW", 0)

            # Extract unique CWEs from "results" section
            for issue in data.get("results", []):
                if "issue_cwe" in issue and "id" in issue["issue_cwe"]:
                    cwes.add(issue["issue_cwe"]["id"])

            results.append({
                "commit": commit_hash,
                "high_confidence": high_conf,
                "medium_confidence": med_conf,
                "low_confidence": low_conf,
                "high_severity": high_sev,
                "medium_severity": med_sev,
                "low_severity": low_sev,
                "unique_cwes": list(cwes),
            })

# Convert to DataFrame
df = pd.DataFrame(results)

# Save to CSV
df.to_csv("mace.csv", index=False)

# Print Summary
print("Analysis Complete. Results saved to 'bandit_analysis.csv'.")
print(df.head())
