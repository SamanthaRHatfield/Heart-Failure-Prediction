# Heart Failure Prediction

## Overview
This project analyzes heart disease data to identify key risk factors and high-risk demographic segments. Using Power BI, the analysis focuses on transforming raw clinical and demographic data into actionable insights that support early identification and decision-making.

The project is structured across three analytical perspectives:

Overview – Understanding overall prevalence and population trends
Risk Factors – Identifying clinical indicators associated with heart disease
Demographics & Segmentation – Determining which population groups are most affected

## Business Problem
Heart disease remains a leading cause of mortality. Organizations need tools to:

Identify high-risk patients early
Understand contributing clinical factors
Segment populations for targeted interventions

This project demonstrates how data analytics can support those objectives using exploratory and descriptive techniques.

## Research Question
Can we predict which patient may experience heart failure?

## Repository Structure
```text
Heart-Failure-Prediction/
│
├── data/
│   ├── raw
│       ├── heart.csv
│
├── powerbi_only/
│   └── heart_dashboard.pbix
│
├── python_powerbi/
│   ├── notebooks/
│   ├── outputs/
│       ├── figures
│       └── predictions
│   ├── src
│       ├── data_loader.py
│       ├── evaluation.py
│       ├── models.py
│       └── preprocessing.py
│   └── powerbi/
│       └── 
│
├── .gitignore
├── README.md
└── requirements.txt
```

## Dataset
The dataset contains patient-level clinical and demographic attributes, including:

Age
Sex
Chest Pain Type
Resting Blood Pressure
Cholesterol
Exercise-Induced Angina
ST Slope
Oldpeak
Fasting Blood Sugar
Heart Disease (target variable)

## Features Used
Interactive filtering by:
  Sex
  Chest Pain Type
  Exercise Angina
  ST Slope
Use of 100% stacked visuals to show prevalence instead of raw counts
Custom segmentation combining age and sex to identify high-risk groups
Clean, consistent design focused on interpretability and decision support

## Models Included


## Evaluation Metrics


## Expected Portfolio Value


## Suggested Resume Wording


## Next Improvements
Add predictive modeling using Python (e.g., logistic regression, random forest)
Integrate risk scoring into Power BI
Expand dataset for broader population analysis
