# Exploratory Data Analysis – Students Performance in Exams

## 1. Project Overview

This project focuses on performing Exploratory Data Analysis (EDA) on a Students Performance dataset. The objective is to analyse students' academic scores, identify patterns, explore relationships between different subjects, and understand how factors such as gender and test preparation relate to academic performance.

The analysis uses Python libraries to clean, examine, analyse, and visualise the dataset.

## 2. Dataset Information

**Dataset:** Students Performance in Exams

- Total records: 1,000 students
- Total columns: 8
- Numerical columns: 3
- Categorical columns: 5

### Dataset Features

| Column | Description |
|---|---|
| gender | Student's gender |
| race/ethnicity | Student's group |
| parental level of education | Parents' education level |
| lunch | Type of lunch |
| test preparation course | Course completion status |
| math score | Mathematics score |
| reading score | Reading score |
| writing score | Writing score |

## 3. Technologies and Libraries Used

- Python
- Pandas – Data manipulation and analysis
- NumPy – Numerical operations
- Matplotlib – Data visualisation
- Seaborn – Statistical visualisation
- SciPy – Statistical hypothesis testing

## 4. Exploratory Data Analysis Performed

The following analyses were performed:

1. Dataset loading and inspection.
2. Checking missing values and duplicate records.
3. Descriptive statistical analysis.
4. Identifying unique values in categorical columns.
5. Analysing category counts and percentages.
6. Subject-wise average score analysis.
7. Score distribution using histograms.
8. Outlier detection using boxplots and the IQR method.
9. Comparing scores based on test preparation.
10. Gender-wise academic performance comparison.
11. Reading and writing score relationship using scatter plots.
12. Correlation analysis using a heatmap.
13. Hypothesis testing using an independent-samples t-test.
14. Checking invalid score values.

## 5. Key Findings

- The dataset contains 1,000 student records and 8 columns.
- No missing values or duplicate records were found.
- Reading had the highest average score (69.17), followed by writing (68.05) and mathematics (66.09).
- Female students had higher average reading and writing scores, while male students had a higher average mathematics score.
- Students who completed the test preparation course had higher average scores in all three subjects.
- Reading and writing scores showed a strong positive correlation of approximately 0.955.
- Outliers were identified in all three subject scores using the IQR method.
- Hypothesis testing showed statistically significant differences between the test preparation groups for mathematics, reading, and writing.
- No invalid score values outside the 0–100 range were found.

## 6. Visualisations

The project generates the following visualisations:

- Subject Score Distribution
- Boxplot of Student Scores
- Test Preparation Score Comparison
- Gender-wise Score Comparison
- Reading vs Writing Scatter Plot
- Correlation Heatmap

All visualisations are saved as PNG files.

## 7. Statistical Analysis

An independent-samples t-test was performed to compare the average scores of students who completed the test preparation course with those who did not.

A significance level of 0.05 was used.

The p-values for all three subjects were below 0.05, indicating statistically significant differences between the two groups.

These results show an association between test preparation completion and academic scores, but do not establish causation.

## 8. Project Structure

```text
EDA_Student_Performance/
│
├── eda.py
├── StudentsPerformance.csv
├── score_distribution.png
├── score_boxplot.png
├── test_preparation_comparison.png
├── gender_score_comparison.png
├── reading_writing_scatter.png
├── correlation_heatmap.png
├── subject_averages.csv
├── gender_comparison.csv
├── test_preparation_results.csv
└── correlation_matrix.csv
```

## 9. How to Run the Project

### Step 1: Install the required libraries

```bash
pip install pandas numpy matplotlib seaborn scipy
```

### Step 2: Keep the dataset and Python script in the same folder.

### Step 3: Run the Python file

```bash
python eda.py
```

The script performs the analysis, displays the visualisations, and saves the generated graphs and result files in the project folder.

## 10. Conclusion

This project demonstrates how Exploratory Data Analysis can be used to understand student performance through statistical summaries, data visualisations, correlation analysis, and hypothesis testing.

The findings highlight differences in subject-wise performance, relationships between reading and writing scores, and associations between test preparation and academic results.

The project provided practical experience in Python-based data analysis, statistical methods, and data visualisation.