#!/bin/bash

# Check if a repository folder is provided
if [ -z "$1" ]; then
  echo "Usage: $0 <repository_folder>"
  exit 1
fi

REPO_FOLDER=$1

# Navigate to the repository folder
cd "$REPO_FOLDER" || { echo "Folder $REPO_FOLDER not found"; exit 1; }

# Ensure we are on the main branch
git checkout main

# Get the last 100 non-merge commits
git log --oneline --no-merges -n 100 --pretty=format:"%H" > commits.txt

# Create a directory to store Bandit results
mkdir -p bandit_results

# Run Bandit on each commit
while read -r commit; do
  echo "Analyzing commit: $commit"
  git checkout "$commit" > /dev/null 2>&1
  bandit -r . -f json -o "bandit_results/bandit_$commit.json"
done < commits.txt

# Return to the main branch
git checkout main

echo "Bandit analysis completed. Results are stored in $REPO_FOLDER/bandit_results/"