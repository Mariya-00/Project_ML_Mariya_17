# Project_ML_Mariya_17
Machine Learning project 17

## Objectives

- Collect real estate data from two different APIs
- Clean and combine data into a single dataset
- Train machine learning models to predict property prices
- Build a REST API to make real-time predictions
---

## APIs Used for Data Collection

1. **ATTOM API**  
   Used to collect property data such as address, city, province, and zip code.

2. **Datafiniti API**  
   Used to collect detailed property information including estimated prices and number of rooms.

---
##  Data Collection & Cleaning Steps

- Fetched data from both APIs using `requests` in Python.
- Saved raw API data into:
  - `attom_raw.csv`
  - `datafiniti_raw.csv`
- Cleaned and selected useful columns:
  - `address`, `city`, `province`, `yearBuilt`, and `price`
- Combined both datasets into `merged_real_estate.csv`

---
##  Cleaning API (Optional)

Implemented, and I run the cleaning API using:

```bash
- uvicorn cleaning_api:app --reload
- Go to: http://127.0.0.1:8000/docs
- Upload raw property data to /clean-data/
  and receive cleaned JSON back.
```
--- 
## Modelling approch % Results

 Models Trained:
Linear Regression (baseline)

Decision Tree Regressor

Random Forest Regressor

Gradient Boosting Regressor

# Evaluation Metrics:
MAE – Mean Absolute Error

RMSE – Root Mean Square Error

R² Score – Model accuracy (closer to 1 is better)

# Visualizations:
Scatter plots of Actual vs Predicted

MAE Bar Comparison

Histogram of Residual Errors

--- 

# Best Performance: Random Forest and Gradient Boosting 


