# Future Interns - Machine Learning Internship

## Task 1: Sales / Demand Forecasting System
Track Code: ML  
Repository: FUTURE_ML_01

### Project Overview
This project builds a predictive machine learning pipeline utilizing historical retail data to forecast future demand and sales trends. It establishes a baseline regression workflow that ingests raw transaction data, extracts time-series elements, and maps visual forecasts against actual records.

### 📊 Dataset Source
* Dataset Used: Sample - [Superstore Sales Dataset](https://www.kaggle.com/datasets/vivek468/superstore-dataset-final) (Standard Kaggle Retail Data)
* Storage Note: The raw CSV file (`Sample-Superstore.csv`) is included in the local environment for execution but has been omitted from this repository via .gitignore to optimize repository size.
* Replication: To run this pipeline locally, download the Superstore sales dataset, rename it to Sample-Superstore.csv, and place it directly into the root directory of this project.

### Features Developed
* Data Cleaning: Handled missing data points across features using automated imputation techniques and adapted data parsing to support Excel/Windows character sets (`ISO-8859-1` encoding).
* Feature Engineering: Deconstructed the raw timeline data into explicit cyclical parameters (Year, Month, Day, and Day of Week) to capture structural business trends.
* Predictive Modeling: Built and evaluated a Linear Regression baseline model using a chronological 80/20 train-test split to ensure realistic future-demand testing without data leakage.

### Performance Evaluation & Insights
* Model Baseline: The Linear Regression model successfully captures the mid-line operational average and general trajectory of the business.
* Analytical Critique: Because daily retail transaction volumes are inherently chaotic and highly susceptible to seasonal spikes (e.g., holiday rushes, marketing campaigns, or bulk corporate orders), a linear model cuts through the average rather than mimicking the volatile peaks and valleys. 
* Future Recommendations: To further optimize forecasting accuracy in subsequent tasks, implementation of non-linear ensemble models (such as Random Forest Regressors or Gradient Boosting) or aggregating data into weekly/monthly buckets to filter out day-to-day transaction noise is recommended.

### Visualizations
The script automatically evaluates data over the testing timeline and saves a high-resolution comparison plot to the root directory as sales_forecast.png.