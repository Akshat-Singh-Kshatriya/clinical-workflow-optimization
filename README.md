# OncoPath: Digital Twin Clinical Workflow

## Project Overview
OncoPath is a digital twin-based oncology routing system designed to optimize clinical workflow efficiency. The system maps 500+ patient records to NCCN (National Comprehensive Cancer Network) treatment guidelines to simulate patient flow, validate decision logic, and evaluate performance in resource-constrained environments.

## Key Results & Impact
* **Dramatic Efficiency Gains**: Reduced the average time-to-treatment from **14 days to 2.5 days** for high-priority cases.
* **Automated Triage**: Successfully categorized patients into three distinct pathways: **Accelerated**, **Standard**, and **Outpatient Monitoring** based on biopsy markers.
* **Tumor Morphology Analysis**: Mapped real tumor markers (mean radius and texture) to care pathways to validate the digital twin's routing accuracy.
* **Improved Prioritization**: Enabled clinical teams to better prioritize urgent cases in complex hospital systems.

## Technical Implementation
* **Language**: Python (Pandas, NumPy).
* **Data Management**: SQL (PostgreSQL) used to simulate clinical workflow databases and aggregate patient metrics.
* **Clinical Routing Engine (`main.py`)**: Uses tumor radius and diagnosis data to assign optimized care pathways.
* **Operational Reporting**: Seaborn visualization suite used to analyze "Days to Treatment" distributions and resource utilization.

## Performance Summary
| Metric | Result |
| :--- | :--- |
| **Patient Records Simulated** | 500+ |
| **Time-to-Treatment (Pre-System)** | 14 Days |
| **Time-to-Treatment (Post-System)** | 2.5 Days |
| **Pathway Accuracy** | Validated against NCCN Guidelines |
