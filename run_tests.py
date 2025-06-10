import os
import subprocess
from datetime import datetime

os.makedirs("reports", exist_ok=True)

timestamp = datetime.now().strftime("%Y-%m-%d_%H-%M-%S")
report_path = f"reports/report_{timestamp}.html"

command = [
    "pytest",
    "--html", report_path,
    "--self-contained-html"
]

result = subprocess.run(command)

if result.returncode == 0:
    print(f"\nAll tests passed. Report saved to {report_path}")
else:
    print(f"\nSome tests failed. See report: {report_path}")
