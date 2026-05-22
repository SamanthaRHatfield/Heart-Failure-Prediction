# Data Dictionary

## Dataset: heart.csv

| Column Name | Data Type | Description | Example Values |
|---|---|---|---|
| Age | Integer | Age of the patient in years | 45, 62 |
| Sex | Categorical | Biological sex of the patient | M, F |
| ChestPainType | Categorical | Type of chest pain experienced | ASY, ATA, NAP, TA |
| RestingBP | Integer | Resting blood pressure | 120, 140 |
| Cholesterol | Integer | Serum cholesterol level | 220, 310 |
| FastingBS | Binary | Fasting blood sugar > 120 mg/dl | 0, 1 |
| RestingECG | Categorical | Resting electrocardiogram results | Normal, ST, LVH |
| MaxHR | Integer | Maximum heart rate achieved | 150, 180 |
| ExerciseAngina | Binary | Exercise-induced angina | Y, N |
| Oldpeak | Numeric | ST depression induced by exercise | 0.0, 2.5 |
| ST_Slope | Categorical | Slope of peak exercise ST segment | Up, Flat, Down |
| HeartDisease | Binary | Presence of heart disease | 0, 1 |

## Dataset: heart_processed.csv

Processed version of the dataset used for machine learning workflows.

Additional fields include:

| Column Name | Description |
|---|---|
| PatientID | Unique identifier assigned during preprocessing |

## Dataset: predictions.csv

Prediction output dataset generated from the Random Forest classification model.

| Column Name | Description |
|---|---|
| PatientID | Unique patient identifier |
| HeartDisease | Actual observed outcome |
| PredictedHeartDisease_RF | Model prediction |
| PredictedProbability_RF | Probability of heart disease |
| Risk Category | Segmented prediction risk level |