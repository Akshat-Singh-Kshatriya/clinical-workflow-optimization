# OncoPath: Digital Twin Clinical Workflow

## 📋 Project Overview
OncoPath is a digital twin-based oncology routing system designed to optimize clinical workflow efficiency[cite: 1]. The system maps 500+ patient records to NCCN (National Comprehensive Cancer Network) treatment guidelines to simulate patient flow, validate decision logic, and evaluate performance in resource-constrained environments[cite: 1].

## 📊 Key Results & Impact
* **Dramatic Efficiency Gains**: Reduced the average time-to-treatment from **14 days to 2.5 days** for high-priority cases[cite: 1].
* **Automated Triage**: Successfully categorized patients into three distinct pathways: **Accelerated**, **Standard**, and **Outpatient Monitoring** based on biopsy markers[cite: 2].
* **Tumor Morphology Analysis**: Mapped real tumor markers (mean radius and texture) to care pathways to validate the digital twin's routing accuracy[cite: 2].
* **Improved Prioritization**: Enabled clinical teams to better prioritize urgent cases in complex hospital systems[cite: 1].

## 🛠 Technical Implementation
* **Language**: Python (Pandas, NumPy)[cite: 2].
* **Data Management**: SQL (SQLite3) used to simulate clinical workflow databases and aggregate patient metrics[cite: 2].
* **Clinical Routing Engine (`main.py`)**: Uses tumor radius and diagnosis data to assign optimized care pathways[cite: 2].
* **Operational Reporting**: Seaborn visualization suite used to analyze "Days to Treatment" distributions and resource utilization[cite: 2].

## 📈 Performance Summary
| Metric | Result |
| :--- | :--- |
| **Patient Records Simulated** | 500+ |
| **Time-to-Treatment (Pre-System)** | 14 Days |
| **Time-to-Treatment (Post-System)** | 2.5 Days |
| **Pathway Accuracy** | Validated against NCCN Guidelines |
