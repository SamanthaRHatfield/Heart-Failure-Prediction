# Heart Failure Prediction

## Overview

This project analyzes heart disease data to identify key risk factors and high-risk demographic segments.

Using Power BI, the analysis transforms raw clinical and demographic data into actionable insights that support early identification and decision-making.

The project is structured across four analytical perspectives:

- Overview – Understanding overall prevalence and population trends
- Risk Factors – Identifying clinical indicators associated with heart disease
- Demographics & Segmentation – Determining which population groups are most affected
- Prediction Analysis – Evaluating machine learning predictions and patient risk probabilities

## Business Problem

Heart disease remains a leading cause of mortality. Organizations need tools to:

- Identify high-risk patients early
- Understand contributing clinical factors
- Segment populations for targeted interventions

This project demonstrates how data analytics can support those objectives using exploratory and descriptive techniques.

## Research Question

Can we predict which patient may experience heart failure?

## Technologies Used

- Power BI
- Python
- Jupyter Notebook
- GitHub

## Repository Structure

```text
Heart-Failure-Prediction/
│
├── data/
│   ├── raw/
│   │   └── heart.csv
│   │
│   ├── processed/
│   │   └── heart_processed.csv
│   │
│   └── data_attributes.docx
│
├── powerbi_only/
│   └── heart_dashboard.pbix
│
├── python_powerbi/
│   ├── notebooks/
│   │   ├── 01_eda_heart_disease.ipynb
│   │   └── 02_modeling_heart_disease.ipynb
│   │
│   ├── outputs/
│   │   ├── figures/
│   │   │   ├── roc_curve.png
│   │   │   ├── confusion_matrix.png
│   │   │   └── feature_importance.png
│   │   │
│   │   └── predictions/
│   │       └── predictions.csv
│   │
│   └── powerbi/
│       └── heart_prediction_dashboard.pbix
│
├── requirements.txt
├── LICENSE
├── .gitignore
└── README.md
```

## Dataset

The dataset contains patient-level clinical and demographic attributes, including:

- Age
- Sex
- Chest Pain Type
- Resting Blood Pressure
- Cholesterol
- Exercise-Induced Angina
- ST Slope
- Oldpeak
- Fasting Blood Sugar
- Heart Disease (target variable)

## Key Insights

Overall Trends

- Heart disease prevalence is approximately 55.3%
- Prevalence increases significantly with age
- Males exhibit substantially higher prevalence (~63%) compared to females (~26%)

Risk Factors

- Exercise-induced angina shows strong association with heart disease (~85% prevalence)
- Flat and downward ST slope patterns are linked to higher prevalence (~80%)
- Oldpeak demonstrates a strong positive relationship with heart disease risk
- Cholesterol and Max Heart Rate show overlapping distributions, indicating weaker standalone predictive power

Demographic Segmentation

- The highest-risk group is males aged 60+ (~81%)
- Males aged 40–59 also show elevated risk (~59%)
- Female groups show significantly lower prevalence across all age ranges
- Combining age and sex provides stronger segmentation than either variable alone

## Features Used

- Interactive filtering by:
  - Sex
  - Chest Pain Type
  - Exercise Angina
  - ST Slope
- Use of 100% stacked visuals to show prevalence instead of raw counts
- Custom segmentation combining age and sex to identify high-risk groups
- Clean, consistent design focused on interpretability and decision support

## Predictive Modeling

A Random Forest classification model was developed using Python and scikit-learn to predict the likelihood of heart disease.

The modeling workflow included:

- Train/test split using stratified sampling
- Feature preprocessing and encoding
- Random Forest classification modeling
- Probability-based risk scoring
- Model evaluation using classification metrics
- Exporting predictions into Power BI for operational reporting

Prediction outputs were exported to:

`python_powerbi/outputs/predictions/predictions.csv`

## Model Performance

| Metric | Result |
|---|---|
| Accuracy | 90.2% |
| ROC-AUC | 93.3% |
| Correct Predictions | 166 |
| Incorrect Predictions | 18 |

The Random Forest model demonstrated strong predictive performance with high classification accuracy and strong probability separation between risk groups.

## Dashboard Pages

### Overview
Provides a high-level summary of prevalence, age distribution, and population trends.

### Risk Factors
Analyzes clinical indicators associated with heart disease including:
- Exercise-induced angina
- ST slope
- Oldpeak
- Fasting blood sugar

### Demographics & Segmentation
Identifies high-risk demographic groups using:
- Age segmentation
- Sex-based prevalence analysis
- Combined demographic segmentation

### Prediction Analysis
Evaluates machine learning predictions using:
- Probability distributions
- Risk categories
- Confusion matrix evaluation
- High-risk patient identification
