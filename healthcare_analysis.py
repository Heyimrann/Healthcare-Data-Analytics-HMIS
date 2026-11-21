import pandas as pd
import os
import glob

print("=" * 50)
print("HEALTHCARE DATA ANALYTICS - HMIS PROJECT")
print("=" * 50)

# 1. Find CSV files
csv_files = glob.glob("*.csv")

if len(csv_files) == 0:
    print("No CSV file found!")
else:
    file_path = csv_files[0]

    # 2. Load dataset
    df = pd.read_csv(file_path, low_memory=False)

    # 3. Clean column names
    df.columns = df.columns.str.strip()

    print("\nDATASET LOADED SUCCESSFULLY")
    print("File:", file_path)

    # 4. Dataset dimensions
    print("\nDataset Shape:", df.shape)

    # 5. Column names
    print("\nColumn Names:")
    print(df.columns.tolist())

    # 6. First five records
    print("\nFirst Five Records:")
    print(df.head())

    # 7. Data types
    print("\nData Types:")
    print(df.dtypes)

    # 8. Missing values
    print("\nMissing Values:")
    print(df.isnull().sum())
    print("\nDataset Columns:")
    print(df.columns.tolist())
    print("\nFirst 5 Rows:")
    print(df.head())
    # =====================================
# DATA CLEANING AND PREPARATION
# =====================================

print("\n========== DATA CLEANING ==========")

# Clean column names
df.columns = df.columns.str.strip()

# Convert value into numeric format
df["value"] = pd.to_numeric(df["value"], errors="coerce")

# Check missing values
print("\nMissing Values:")
print(df.isnull().sum())

# Check duplicate records
print("\nDuplicate Records:", df.duplicated().sum())

# Total districts
print("\nTotal Districts:",
      df["district_as_per_lgd"].nunique())

# Total financial years
print("\nFinancial Years:")
print(sorted(df["fiscal_year"].dropna().unique()))

# Total indicators
print("\nTotal Indicators:",
      df["indicator"].nunique())

# Indicator categories
print("\nIndicator Heads:")
print(df["indicator_head"].value_counts())

print("\nDATA CLEANING CHECK COMPLETED")

# =====================================
# VISUALIZATION 1: MISSING VALUES
# =====================================

import matplotlib.pyplot as plt
import seaborn as sns

missing = df.isnull().sum()
missing = missing[missing > 0].sort_values(ascending=False)

plt.figure(figsize=(10, 5))

sns.barplot(
    x=missing.values,
    y=missing.index
)

plt.title("Missing Values in HMIS Dataset")
plt.xlabel("Number of Missing Values")
plt.ylabel("Dataset Columns")

plt.tight_layout()
plt.savefig("missing_values_chart.png", dpi=300)
plt.show()

print("Missing values chart saved successfully!")


# YEAR-WISE HMIS VISUALIZATION

import matplotlib
matplotlib.use("Agg")

import matplotlib.pyplot as plt

year_data = df.groupby("fiscal_year").size().sort_index()

fig, ax = plt.subplots(figsize=(12, 6))

ax.bar(year_data.index, year_data.values)

ax.set_title("Year-wise HMIS Records (2008-09 to 2021-22)")
ax.set_xlabel("Financial Year")
ax.set_ylabel("Number of Records")

plt.xticks(rotation=45)
plt.tight_layout()

plt.savefig("year_wise_records.png", dpi=300)

print("Graph saved:", __import__("os").path.exists("year_wise_records.png"))
print("Year-wise records:")
print(year_data)

plt.close()

# =====================================
# VISUALIZATION 3: DISTRICT-WISE RECORDS
# =====================================

district_data = (
    df.groupby("district_as_per_lgd")
    .size()
    .sort_values(ascending=False)
)

plt.figure(figsize=(12, 8))

sns.barplot(
    x=district_data.values,
    y=district_data.index
)

plt.title("District-wise HMIS Records")
plt.xlabel("Number of Records")
plt.ylabel("District")

plt.tight_layout()

plt.savefig(
    "district_wise_records.png",
    dpi=300,
    bbox_inches="tight"
)

plt.close()

print("District-wise graph saved successfully!")
print(district_data)

# =====================================
# VISUALIZATION 4: INDICATOR DISTRIBUTION
# =====================================

indicator_data = (
    df["indicator_head"]
    .value_counts()
    .head(10)
)

plt.figure(figsize=(10, 8))

plt.pie(
    indicator_data.values,
    labels=indicator_data.index,
    autopct="%1.1f%%",
    startangle=90
)

plt.title("Top 10 Healthcare Indicator Heads Distribution")

plt.tight_layout()

plt.savefig(
    "indicator_distribution.png",
    dpi=300,
    bbox_inches="tight"
)

plt.close()

print("Indicator distribution chart saved successfully!")

# =====================================
# STEP 1: IDENTIFY OPD INDICATORS
# =====================================

opd_indicators = df[
    df["indicator"].str.contains(
        "Outpatient attendance",
        case=False,
        na=False
    )
]

print("\nOPD INDICATORS FOUND:")
print(opd_indicators["indicator"].value_counts())

# ==========================================
# VISUALIZATION 5: OPD ATTENDANCE TREND
# ==========================================

opd_data = df[
    df["indicator"].isin([
        "Allopathic- Outpatient attendance",
        "Ayush - Outpatient attendance"
    ])
].copy()

# Convert values to numeric
opd_data["value"] = pd.to_numeric(
    opd_data["value"],
    errors="coerce"
)

# Aggregate yearly attendance
opd_trend = opd_data.pivot_table(
    index="fiscal_year",
    columns="indicator",
    values="value",
    aggfunc="sum"
).sort_index()

# Create line chart
plt.figure(figsize=(13, 6))

for column in opd_trend.columns:
    plt.plot(
        opd_trend.index,
        opd_trend[column],
        marker="o",
        label=column
    )

plt.title("Year-wise OPD Attendance: Allopathic vs Ayush")
plt.xlabel("Financial Year")
plt.ylabel("Reported OPD Attendance")
plt.xticks(rotation=45)
plt.legend()
plt.grid(alpha=0.3)

plt.tight_layout()

plt.savefig(
    "opd_attendance_trend.png",
    dpi=300,
    bbox_inches="tight"
)

plt.close()

print("OPD trend graph saved successfully!")
print(opd_trend)

# =====================================
# MATERNAL HEALTHCARE INDICATORS
# =====================================

maternal_data = df[
    df["indicator"].str.contains(
        "ANC|antenatal|delivery|deliveries|institutional delivery",
        case=False,
        na=False
    )
]

print("\nMATERNAL HEALTHCARE INDICATORS:")
print(maternal_data["indicator"].value_counts().to_string())

print("\nFACILITY CATEGORIES:")
print(maternal_data["facility_category"].value_counts().to_string())

# =====================================
# SELECTED MATERNAL HEALTHCARE INDICATORS
# =====================================

selected_indicators = [
    "Total number of pregnant women registered for ANC",
    "Number of PW received 4 or more ANC check ups",
    "Number of Institutional Deliveries conducted (Including C-Sections)"
]

maternal_kpi = df[
    df["indicator"].isin(selected_indicators)
].copy()

print("\nSELECTED MATERNAL INDICATORS:")
print(maternal_kpi["indicator"].value_counts().to_string())

print("\nYEAR-WISE RECORD COUNTS:")
print(
    maternal_kpi.groupby(
        ["indicator", "fiscal_year"]
    ).size().to_string()
)

print("\nFACILITY CATEGORY DETAILS:")
print(
    maternal_kpi.groupby(
        ["indicator", "facility_category"]
    ).size().to_string()
)
combined_maternal = maternal_kpi[
    maternal_kpi["facility_category"] ==
    "Public and Private Facilities OR Rural and Urban Facilities"
].copy()

print("\nCOMBINED MATERNAL HEALTH DATA:")

print(
    combined_maternal[
        [
            "fiscal_year",
            "district_as_per_source",
            "indicator",
            "value",
            "unit"
        ]
    ].head(20).to_string(index=False)
)

print("\nMISSING VALUES:")
print(combined_maternal["value"].isna().sum())

print("\nTOTAL RECORDS:")
print(len(combined_maternal))

# MATERNAL HEALTH YEAR-WISE TREND ANALYSIS

maternal_yearly = combined_maternal.pivot_table(
    index="fiscal_year",
    columns="indicator",
    values="value",
    aggfunc="sum"
)

print("\nYEAR-WISE MATERNAL HEALTH PERFORMANCE:")
print(maternal_yearly.to_string())

# Save yearly summary
maternal_yearly.to_csv("maternal_health_yearly_summary.csv")

# Create visualization
import matplotlib.pyplot as plt

plt.figure(figsize=(12, 6))

for column in maternal_yearly.columns:
    plt.plot(
        maternal_yearly.index,
        maternal_yearly[column],
        marker="o",
        linewidth=2,
        label=column
    )

plt.title("Year-wise Maternal Healthcare Trends in Jharkhand")
plt.xlabel("Financial Year")
plt.ylabel("Reported Count (Absolute Number)")
plt.xticks(rotation=45)
plt.legend(fontsize=8)
plt.grid(alpha=0.3)
plt.tight_layout()

plt.savefig("maternal_health_trend.png", dpi=300)
plt.close()

print("\nMaternal health graph saved successfully!")

# DISTRICT-WISE MATERNAL HEALTHCARE ANALYSIS (2021-22)

district_maternal = combined_maternal[
    combined_maternal["fiscal_year"] == "2021-22"
].pivot_table(
    index="district_as_per_source",
    columns="indicator",
    values="value",
    aggfunc="sum"
)

# Sort districts by institutional deliveries
district_maternal = district_maternal.sort_values(
    by="Number of Institutional Deliveries conducted (Including C-Sections)",
    ascending=False
)

print("\nDISTRICT-WISE MATERNAL HEALTHCARE PERFORMANCE (2021-22):")
print(district_maternal.to_string())

print("\nHIGHEST INSTITUTIONAL DELIVERIES:")
print(district_maternal.head(5).to_string())

print("\nLOWEST INSTITUTIONAL DELIVERIES:")
print(district_maternal.tail(5).to_string())

# Save results
district_maternal.to_csv("district_maternal_health_2021_22.csv")

print("\nDistrict-wise analysis completed!")

# TOP 10 DISTRICTS BY INSTITUTIONAL DELIVERIES

delivery_column = (
    "Number of Institutional Deliveries conducted (Including C-Sections)"
)

top10 = district_maternal.head(10).sort_values(
    by=delivery_column,
    ascending=True
)

import matplotlib.pyplot as plt

plt.figure(figsize=(10, 6))

plt.barh(
    top10.index,
    top10[delivery_column]
)

plt.title("Top 10 Districts by Institutional Deliveries (2021-22)")
plt.xlabel("Reported Institutional Deliveries")
plt.ylabel("District")

plt.tight_layout()
plt.savefig("top10_district_deliveries.png", dpi=300)
plt.close()

print("\nTop 10 district graph saved successfully!")
