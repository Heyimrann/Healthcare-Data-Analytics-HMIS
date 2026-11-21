# Healthcare Data Analytics: Hospital Performance Evaluation Using India's HMIS Data

## Project Overview

This project focuses on analysing healthcare indicators using district-wise and year-wise data from India's Health Management Information System (HMIS) for Jharkhand.

The objective is to understand healthcare reporting patterns, outpatient department (OPD) attendance and maternal healthcare indicators through data cleaning, exploratory data analysis and visualization.

This project was carried out as part of my Healthcare Data Analyst Internship at **YuvaIntern**.

## Objectives

- Clean and preprocess healthcare data.
- Explore district-wise and financial-year-wise reporting patterns.
- Analyse missing values and healthcare indicator distribution.
- Study Allopathic and AYUSH OPD attendance trends.
- Examine maternal healthcare indicators.
- Present findings through meaningful visualizations.

## Dataset Information

- **State:** Jharkhand, India
- **Source:** Health Management Information System (HMIS), Ministry of Health and Family Welfare, Government of India
- **Dataset access:** Dataful
- **Total Records:** 264,240
- **Total Columns:** 13
- **Districts:** 24
- **Financial Years:** 2008–09 to 2021–22
- **Healthcare Indicators:** 599

*Note: The original dataset is not included in this repository. Please refer to the original data source and its applicable usage terms.*

## Tools and Technologies

- Python
- Pandas
- NumPy
- Matplotlib
- Seaborn
- Jupyter Notebook
- Power BI (dashboard development)

## Project Workflow

1. Project planning and understanding the dataset.
2. Data cleaning and preprocessing.
3. Exploratory Data Analysis (EDA).
4. Healthcare indicator analysis.
5. Data visualization.
6. Interpretation of findings and recommendations.

## Key Analysis Areas

### 1. Data Quality Analysis
- Missing value analysis.
- Duplicate record checking.
- Data type conversion and preprocessing.

### 2. Healthcare Reporting Analysis
- Year-wise record distribution.
- District-wise record distribution.
- Healthcare indicator distribution.

### 3. OPD Attendance Analysis
- Allopathic outpatient attendance.
- AYUSH outpatient attendance.
- Annual attendance trends.

### 4. Maternal Healthcare Analysis
- Pregnant women registered for ANC.
- Women receiving four or more ANC check-ups.
- Institutional deliveries.

## Visualizations

The repository includes the following analysis graphs:

- Missing Values Analysis
- Year-wise Records Distribution
- District-wise Records Distribution
- Healthcare Indicator Distribution
- OPD Attendance Trends
- Maternal Health Trends
- Top 10 Districts by Institutional Deliveries

## Repository Structure

```text
Healthcare-Data-Analytics-HMIS/
│
├── README.md
├── healthcare_analysis.py
│
├── missing_values_chart.png
├── year_wise_records.png
├── district_wise_records.png
├── indicator_distribution.png
├── opd_attendance_trend.png
├── maternal_health_trend.png
├── top10_district_deliveries.png
│
├── maternal_health_yearly_summary.csv
└── district_maternal_health_2021_22.csv
```

## Important Findings

- The dataset contains 264,240 records across 24 districts and 14 financial years.
- Missing values were identified in several fields, particularly the value and note columns.
- Allopathic and AYUSH OPD attendance declined during 2020–21 and showed recovery in 2021–22.
- Maternal healthcare indicators showed changes across the analysed financial years.
- District-wise differences in reported institutional delivery counts were observed.

## Limitations

- The dataset contains aggregate district-level information rather than individual patient records.
- Reported counts should not be interpreted as direct measures of healthcare quality or performance.
- Changes in reporting coverage may influence year-wise record counts.
- Missing values and indicator definitions require careful interpretation.
- Predictive modelling and dashboard development should only be considered completed when the corresponding implementation and validation are available.

**Project:** Healthcare Data Analytics using HMIS Data

## Author

**Md Imran**  
B.Tech Biotechnology  
Galgotias University
