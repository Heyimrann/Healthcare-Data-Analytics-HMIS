# Healthcare Data Analytics: Hospital Performance Evaluation Using India's HMIS Data

**A B.Tech Biotechnology Major Project | Galgotias University**

## Project Overview

This project focuses on analysing district-level healthcare data from India's Health Management Information System (HMIS). The objective is to explore healthcare service indicators, examine reporting patterns across districts and financial years, and present meaningful insights through data analytics and visualisation.

The project uses Python, SQL and Power BI for data processing, analysis and dashboard development.

## Project Objectives

- Explore district-wise healthcare indicators.
- Analyse healthcare reporting patterns across financial years.
- Examine selected OPD, IPD, maternal health, child immunisation and laboratory indicators.
- Identify missing data and other data-quality issues.
- Develop an interactive healthcare analytics dashboard.

## Dataset Information

| Attribute | Description |
|---|---|
| Data source | Health Management Information System (HMIS) |
| State | Jharkhand, India |
| Records | 264,240 |
| Columns | 13 |
| Districts (LGD) | 24 |
| Financial years | 2008–09 to 2021–22 |
| Distinct indicators | 599 |
| Indicator categories | 36 |

**Source attribution:** Health Management Information System, Ministry of Health and Family Welfare, Government of India. Dataset accessed through Dataful.

## Tools & Technologies

- **Python:** Data analysis and processing
- **Pandas:** Data cleaning and manipulation
- **SQL:** Data querying and management
- **Power BI:** Dashboard and visualisation
- **Google Colab:** Python development environment

## Project Workflow

1. Dataset collection and loading
2. Data exploration and profiling
3. Data cleaning and preprocessing
4. Healthcare indicator identification
5. District-wise and year-wise analysis
6. SQL-based data querying
7. Power BI dashboard development
8. Findings and project documentation

## Repository Structure

```text
Healthcare-Data-Analytics-HMIS/
│
├── data/
├── notebooks/
├── sql/
├── powerbi/
├── presentation/
├── reports/
├── README.md
├── requirements.txt
└── .gitignore
```

## Current Project Status

**In Progress**

Initial dataset profiling has been completed. Healthcare KPI validation, detailed analysis, SQL implementation and Power BI dashboard development are in progress.

## Important Data Limitations

- The dataset contains district-level annual records, not individual patient records.
- Missing values require careful interpretation.
- Facility categories must be checked for overlap before calculating combined totals.
- Findings will be reported only after validating indicator definitions and units.

## Expected Outcome

The project aims to develop a structured healthcare analytics workflow that can help explore reported health-service patterns and support evidence-informed interpretation of district-level HMIS data.

## Author

**Md Imran**  
B.Tech Biotechnology  
Galgotias University

---

*Academic project developed for educational and analytical purposes.*
