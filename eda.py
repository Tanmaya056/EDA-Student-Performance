
# ============================================================
# EXPLORATORY DATA ANALYSIS (EDA)
# Project: Students Performance in Exams
# ============================================================


# 1. IMPORT LIBRARIES

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
from scipy.stats import ttest_ind

sns.set_style("whitegrid")


# 2. LOAD DATASET

df = pd.read_csv("StudentsPerformance.csv")

print("\n========== DATASET PREVIEW ==========")
print(df.head())

print("\nDataset Shape:")
print(df.shape)

print("\nDataset Columns:")
print(df.columns.tolist())

print("\nDataset Information:")
df.info()


# 3. CHECK MISSING VALUES

print("\n========== MISSING VALUES ==========")
print(df.isnull().sum())

total_missing = df.isnull().sum().sum()
print("\nTotal Missing Values:", total_missing)


# 4. CHECK DUPLICATE ROWS

print("\n========== DUPLICATE VALUES ==========")

duplicate_count = df.duplicated().sum()

print("Duplicate rows:", duplicate_count)


# 5. DESCRIPTIVE STATISTICS

print("\n========== DESCRIPTIVE STATISTICS ==========")

score_columns = [
    "math score",
    "reading score",
    "writing score"
]

print(df[score_columns].describe().to_string())


# 6. CATEGORICAL DATA ANALYSIS

categorical_columns = [
    "gender",
    "race/ethnicity",
    "parental level of education",
    "lunch",
    "test preparation course"
]

print("\n========== UNIQUE CATEGORIES ==========")

for column in categorical_columns:
    print("\n", column)
    print(df[column].unique())


# 7. CATEGORY COUNTS AND PERCENTAGES

print("\n========== CATEGORY DISTRIBUTION ==========")

for column in categorical_columns:

    print("\n", column)

    print("\nCategory Counts:")
    print(df[column].value_counts().to_string())

    print("\nCategory Percentages:")
    print(
        (df[column].value_counts(normalize=True) * 100)
        .round(2)
        .to_string()
    )


# 8. SUBJECT-WISE AVERAGE SCORES

print("\n========== SUBJECT AVERAGES ==========")

subject_averages = df[score_columns].mean()

print(subject_averages)

highest_subject = subject_averages.idxmax()

print("\nSubject with highest average:", highest_subject)


# 9. HISTOGRAM - DISTRIBUTION OF SUBJECT SCORES

plt.figure(figsize=(10, 6))

for column in score_columns:

    sns.histplot(
        data=df,
        x=column,
        bins=10,
        kde=True,
        alpha=0.4,
        label=column
    )

plt.title("Distribution of Student Scores")
plt.xlabel("Score")
plt.ylabel("Number of Students")
plt.legend()
plt.tight_layout()

plt.savefig(
    "score_distribution.png",
    dpi=300,
    bbox_inches="tight"
)

plt.show()


# 10. BOXPLOT - OUTLIER VISUALIZATION

plt.figure(figsize=(9, 6))

sns.boxplot(data=df[score_columns])

plt.title("Boxplot of Student Scores")
plt.xlabel("Subjects")
plt.ylabel("Scores")
plt.tight_layout()

plt.savefig(
    "score_boxplot.png",
    dpi=300,
    bbox_inches="tight"
)

plt.show()


# 11. OUTLIER DETECTION USING IQR

print("\n========== OUTLIER ANALYSIS ==========")

for column in score_columns:

    Q1 = df[column].quantile(0.25)
    Q3 = df[column].quantile(0.75)

    IQR = Q3 - Q1

    lower_limit = Q1 - 1.5 * IQR
    upper_limit = Q3 + 1.5 * IQR

    outliers = df[
        (df[column] < lower_limit) |
        (df[column] > upper_limit)
    ]

    print("\nSubject:", column)
    print("Lower Limit:", lower_limit)
    print("Upper Limit:", upper_limit)
    print("Number of Outliers:", len(outliers))


# 12. TEST PREPARATION COURSE VS SCORES

print("\n========== TEST PREPARATION ANALYSIS ==========")

preparation_result = df.groupby(
    "test preparation course"
)[score_columns].mean()

print(preparation_result.to_string())


# 13. BAR CHART - TEST PREPARATION COMPARISON

preparation_result.plot(
    kind="bar",
    figsize=(9, 6)
)

plt.title("Average Scores Based on Test Preparation")
plt.xlabel("Test Preparation Course")
plt.ylabel("Average Score")
plt.xticks(rotation=0)
plt.legend(title="Subjects")
plt.tight_layout()

plt.savefig(
    "test_preparation_comparison.png",
    dpi=300,
    bbox_inches="tight"
)

plt.show()


# 14. GENDER-WISE SCORE COMPARISON

print("\n========== GENDER-WISE SCORE COMPARISON ==========")

gender_result = df.groupby("gender")[score_columns].mean()

print(gender_result.to_string())


# 15. BAR CHART - GENDER-WISE SCORES

gender_result.plot(
    kind="bar",
    figsize=(9, 6)
)

plt.title("Average Scores by Gender")
plt.xlabel("Gender")
plt.ylabel("Average Score")
plt.xticks(rotation=0)
plt.legend(title="Subjects")
plt.tight_layout()

plt.savefig(
    "gender_score_comparison.png",
    dpi=300,
    bbox_inches="tight"
)

plt.show()


# 16. READING VS WRITING SCORE CORRELATION

print("\n========== READING AND WRITING CORRELATION ==========")

correlation = df["reading score"].corr(
    df["writing score"]
)

print("Reading-Writing Correlation:", correlation)


# 17. SCATTER PLOT - READING VS WRITING

plt.figure(figsize=(8, 6))

sns.scatterplot(
    data=df,
    x="reading score",
    y="writing score"
)

plt.title("Reading Score vs Writing Score")
plt.xlabel("Reading Score")
plt.ylabel("Writing Score")
plt.tight_layout()

plt.savefig(
    "reading_writing_scatter.png",
    dpi=300,
    bbox_inches="tight"
)

plt.show()


# 18. CORRELATION MATRIX

correlation_matrix = df[score_columns].corr()

print("\n========== CORRELATION MATRIX ==========")

print(correlation_matrix.to_string())


# 19. CORRELATION HEATMAP

plt.figure(figsize=(8, 6))

sns.heatmap(
    correlation_matrix,
    annot=True,
    cmap="coolwarm",
    vmin=-1,
    vmax=1,
    fmt=".2f"
)

plt.title("Correlation Between Subject Scores")
plt.tight_layout()

plt.savefig(
    "correlation_heatmap.png",
    dpi=300,
    bbox_inches="tight"
)

plt.show()


# 20. HYPOTHESIS TESTING - TEST PREPARATION

print("\n========== HYPOTHESIS TESTING ==========")

completed = df[
    df["test preparation course"] == "completed"
]

not_completed = df[
    df["test preparation course"] == "none"
]

for column in score_columns:

    t_stat, p_value = ttest_ind(
        completed[column],
        not_completed[column]
    )

    print("\nSubject:", column)
    print("T-statistic:", t_stat)
    print("P-value:", p_value)

    if p_value < 0.05:
        print("Result: Significant difference between the groups.")
    else:
        print("Result: No statistically significant difference.")


# 21. CHECK INVALID SCORE VALUES

print("\n========== INVALID SCORE CHECK ==========")

for column in score_columns:

    invalid = df[
        (df[column] < 0) |
        (df[column] > 100)
    ]

    print(
        "Invalid values in",
        column,
        ":",
        len(invalid)
    )


# 22. FINAL SUMMARY

print("\n========== FINAL EDA SUMMARY ==========")

print("Total Students:", len(df))
print("Total Columns:", len(df.columns))
print("Missing Values:", total_missing)
print("Duplicate Rows:", duplicate_count)

print("\nAverage Subject Scores:")
print(subject_averages.round(2).to_string())

print("\nGender-wise Average Scores:")
print(gender_result.round(2).to_string())

print("\nTest Preparation Average Scores:")
print(preparation_result.round(2).to_string())

print("\nReading-Writing Correlation:", round(correlation, 4))


# 23. SAVE ANALYSIS RESULTS

subject_averages.to_csv("subject_averages.csv")

gender_result.to_csv("gender_comparison.csv")

preparation_result.to_csv("test_preparation_results.csv")

correlation_matrix.to_csv("correlation_matrix.csv")


# ============================================================
# END OF EXPLORATORY DATA ANALYSIS
# ============================================================

print("\n========== EDA COMPLETED SUCCESSFULLY ==========")
print("All graphs and analysis files have been saved.")
