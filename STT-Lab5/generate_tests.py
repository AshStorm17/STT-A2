import subprocess
import os
import re

# Step 1: Generate coverage report
print("Generating coverage report...")
subprocess.run(["coverage", "report", "--show-missing"], capture_output=True, text=True)

# Step 2: Extract uncovered modules
coverage_output = subprocess.run(["coverage", "report", "--show-missing"], capture_output=True, text=True).stdout
uncovered_modules = []

for line in coverage_output.split("\n"):
    match = re.match(r"(\S+)\s+\d+\s+\d+\s+\d+%\s+(.*)", line)
    if match and "100%" not in match.group(2):  # Ignore fully covered files
        module_path = match.group(1).replace("/", ".").replace(".py", "")
        if module_path.startswith("algorithms"):
            uncovered_modules.append(module_path)

if not uncovered_modules:
    print("No uncovered modules found.")
    exit()

# Step 3: Run Pynguin for each uncovered module
output_dir = "./generated_tests"
os.makedirs(output_dir, exist_ok=True)

for module in uncovered_modules:
    print(f"Generating tests for {module}...")
    subprocess.run([
        "pynguin",
        "--project-path", ".",
        "--output-path", output_dir,
        "--module-name", module,
    ])
