import pandas as pd
import numpy as np
import seaborn as sns
import matplotlib.pyplot as plt
import sqlite3


url = "https://archive.ics.uci.edu/ml/machine-learning-databases/breast-cancer-wisconsin/wdbc.data"

columns = ['patient_id', 'diagnosis', 'radius_mean', 'texture_mean', 'perimeter_mean', 'area_mean', 
           'smoothness_mean', 'compactness_mean', 'concavity_mean', 'concave_points_mean', 'symmetry_mean', 
           'fractal_dimension_mean'] + [f'feature_{i}' for i in range(12, 32)] 

df = pd.read_csv(url, header=None, names=columns)
df = df.iloc[:, :12] 

def digital_twin_router(row):
    """
    Simulates the NCCN guidelines: The Clinical History Twin looks at real tumor data 
    and routes the patient to optimize operational efficiency.
    """
   
    if row['diagnosis'] == 'M' and row['radius_mean'] > 18.0:
        return 'Accelerated Oncology Path'
   
    elif row['diagnosis'] == 'M':
        return 'Standard Oncology Path'

    else:
        return 'Outpatient Monitoring'

df['care_pathway_assigned'] = df.apply(digital_twin_router, axis=1)


np.random.seed(101)
conditions = [
    df['care_pathway_assigned'] == 'Accelerated Oncology Path',
    df['care_pathway_assigned'] == 'Standard Oncology Path',
    df['care_pathway_assigned'] == 'Outpatient Monitoring'
]
choices = [
    np.random.normal(loc=3, scale=1, size=len(df)),  
    np.random.normal(loc=14, scale=3, size=len(df)), 
    np.random.normal(loc=30, scale=5, size=len(df))  
]
df['days_to_treatment'] = np.select(conditions, choices, default=14)
df['days_to_treatment'] = np.maximum(1, df['days_to_treatment'].astype(int)) # Ensure > 0 days

conn = sqlite3.connect(':memory:')
df.to_sql('oncology_twins', conn, index=False)

query = """
SELECT 
    care_pathway_assigned,
    COUNT(patient_id) as total_patients,
    AVG(radius_mean) as avg_tumor_radius,
    AVG(days_to_treatment) as avg_days_to_treatment
FROM oncology_twins
GROUP BY care_pathway_assigned
ORDER BY avg_days_to_treatment ASC;
"""
sql_ops_results = pd.read_sql_query(query, conn)

print(sql_ops_results.to_string())

sns.set_theme(style="ticks")
fig, axes = plt.subplots(1, 2, figsize=(16, 6))

# Chart 1: The Clinical Reality (Scatterplot of real tumor markers)
sns.scatterplot(data=df, x='radius_mean', y='texture_mean', hue='care_pathway_assigned', palette='viridis', alpha=0.7, ax=axes[0])
axes[0].set_title('Digital Twin Routing based on Real Tumor Morphology')
axes[0].set_xlabel('Tumor Radius (Mean)')
axes[0].set_ylabel('Tumor Texture (Mean)')

# Chart 2: Operational Efficiency (Days to treatment distribution)
sns.kdeplot(data=df, x="days_to_treatment", hue="care_pathway_assigned", fill=True, common_norm=False, palette="viridis", alpha=.5, linewidth=0, ax=axes[1])
axes[1].set_title('Operational Efficiency: Days to Treatment by Pathway')
axes[1].set_xlabel('Days until First Treatment / Appointment')

plt.tight_layout()
plt.show()
