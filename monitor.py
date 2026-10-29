import numpy as np
import pandas as pd
from evidently.report import Report
from evidently.metric_preset import DataDriftPreset

# Reference data = "old" data
reference = pd.DataFrame({
    "age": np.random.normal(30, 5, 200),
    "salary": np.random.normal(50000, 8000, 200),
})

# Current data = "new" data (slightly different on purpose)
current = pd.DataFrame({
    "age": np.random.normal(38, 5, 200),
    "salary": np.random.normal(50000, 8000, 200),
})

report = Report(metrics=[DataDriftPreset()])
report.run(reference_data=reference, current_data=current)
report.save_html("monitoring_report.html")
print("Report saved: monitoring_report.html")