# Customer Retention Intelligence System

## Overview

Customer churn is one of the most critical challenges faced by subscription-based businesses. Acquiring new customers is often more expensive than retaining existing ones, making customer retention a key business priority.

The **Customer Retention Intelligence System** is an end-to-end analytics and machine learning project designed to predict customer churn and uncover actionable retention insights using the IBM Telco Customer Churn dataset.

The project combines **Exploratory Data Analysis (EDA), Machine Learning, Business Intelligence, and Streamlit Deployment** to help organizations identify customers at risk of leaving and support data-driven retention strategies.

---

## Business Problem

Telecom companies face significant revenue loss when customers discontinue their services and switch to competitors.

This project aims to answer the following business questions:

* Which customers are most likely to churn?
* What factors are associated with customer churn?
* How can the business improve customer retention?
* Which customer segments should be prioritized for retention campaigns?

---

## Dataset

**Source:** IBM Telco Customer Churn Dataset

**Records:** 7,043 Customers

**Features:** 21 Customer Attributes

**Target Variable:** Churn (Yes/No)

Key attributes include:

* Customer Tenure
* Monthly Charges
* Total Charges
* Contract Type
* Internet Service
* Payment Method
* Customer Demographics
* Subscription Services

---

## Tools & Technologies

### Programming & Analytics

* Python
* Pandas
* NumPy

### Data Visualization

* Matplotlib
* Seaborn
* Looker Studio

### Machine Learning

* Scikit-Learn
* XGBoost
* SMOTE (Imbalanced-Learn)

### Deployment

* Streamlit
* Joblib

---

## Project Workflow

### 1. Data Cleaning

* Converted `TotalCharges` from object to numeric format
* Handled missing values
* Removed invalid records
* Prepared data for analysis and modeling

### 2. Exploratory Data Analysis (EDA)

Performed business-focused analysis to identify churn drivers.

Key analyses included:

* Churn Distribution
* Contract Type vs Churn
* Tenure vs Churn
* Monthly Charges vs Churn
* Payment Method vs Churn

### 3. Machine Learning

Built and evaluated multiple classification models:

* Decision Tree
* Random Forest
* XGBoost

### 4. Class Imbalance Handling

Applied **SMOTE (Synthetic Minority Oversampling Technique)** to improve churn customer detection and compare model performance before and after balancing.

### 5. Model Evaluation

Compared models using:

* Accuracy
* Precision
* Recall
* F1 Score

### 6. Feature Importance Analysis

Identified the most influential factors associated with customer churn.

### 7. Streamlit Deployment

Built an interactive application that allows users to:

* Enter customer information
* Predict churn risk
* Generate business recommendations

### 8. Business Intelligence Dashboard

Developed an interactive Looker Studio dashboard for stakeholder reporting and retention analysis.

---

## Key Business Insights

### 1. Contract Type Drives Retention

Customers with month-to-month contracts showed significantly higher churn rates compared to customers on long-term contracts.

**Recommendation:** Encourage customers to upgrade to annual or multi-year plans through discounts and loyalty programs.

---

### 2. New Customers Are More Likely to Churn

Customers who churned had significantly lower average tenure compared to retained customers.

**Recommendation:** Improve onboarding and engagement programs during the early customer lifecycle.

---

### 3. Higher Monthly Charges Are Associated With Churn

Customers paying higher monthly charges were more likely to leave.

**Recommendation:** Provide personalized offers and retention incentives to high-value customers.

---

### 4. Payment Method Is an Important Churn Indicator

Electronic check payment method emerged as one of the strongest churn predictors.

**Recommendation:** Investigate payment experience and encourage automatic payment options.

---

## Model Performance

| Model                 | Accuracy |
| --------------------- | -------- |
| Decision Tree         | 72.14%   |
| Decision Tree + SMOTE | 72.49%   |
| Random Forest         | 78.54%   |
| Random Forest + SMOTE | 77.40%   |
| XGBoost               | 77.40%   |
| XGBoost + SMOTE       | 76.97%   |

### Final Model Selection

**Selected Model:** XGBoost + SMOTE

Although Random Forest achieved the highest overall accuracy, XGBoost + SMOTE achieved the highest churn recall, making it more suitable for customer retention use cases where identifying at-risk customers is critical.

---

## Top Churn Drivers

1. Payment Method (Electronic Check)
2. Internet Service (Fiber Optic)
3. Internet Service (No Internet Service)
4. Contract Type (Two-Year Contract)
5. Paperless Billing

---

## Looker Studio Dashboard

Dashboard Components:

* Total Customers KPI
* Churned Customers KPI
* Retained Customers KPI
* Churn Rate KPI
* Customer Churn Distribution
* Contract Type vs Churn
* Average Tenure Analysis
* Average Monthly Charges Analysis
* Payment Method Analysis
* Internet Service Analysis
* Business Recommendations

---

## Streamlit Application

The Streamlit app allows users to:

* Input customer information
* Predict churn risk
* View churn classification
* Generate retention recommendations

Run locally:

```bash
streamlit run app.py
```

---

## Installation

Clone the repository:

```bash
git clone <repository-link>
```

Navigate to the project folder:

```bash
cd Customer-Retention-Intelligence-System
```

Install dependencies:

```bash
pip install -r requirements.txt
```

Run the application:

```bash
streamlit run app.py
```

---

## Author

**Ramit Sakhuja**

Final Year B.Tech (AI & ML)

Aspiring Data Analyst | SQL | Python | Power BI | Looker Studio | Machine Learning
