# Project_ML_Mariya_17
Machine Learning project 17

## Objectives

- Collect real estate data from two different APIs
- Clean and combine data into a single dataset
- Train machine learning models to predict property prices
- Build a REST API to make real-time predictions


## APIs Used for Data Collection

1. **ATTOM API**  
   Used to collect property data such as address, city, province, country, yearBuild, and price.

2. **Datafiniti API**  
   Used to collect detailed property information including address, city, province, country, yearBuild, and price.


##  Data Collection & Cleaning Steps

- Collected raw data from two public APIs (Datafiniti and ATTOM) using Python scripts
- Saved API responses into:
  - `attom_raw.csv`
  - `datafiniti_raw.csv`
- Cleaned and selected useful columns:
  - `address`, `city`, `province`, `yearBuilt`, and `price`
- Merged both datasets into one final file: `merged_real_estate.csv`


##  Prediction API (FastAPI)

A REST API was implemented to predict property prices using the trained model.

### ▶ How to Run the API

1. Save my model first:
   ```python
   joblib.dump(model_boosting, "model.pkl")
   run the API using:
    uvicorn predict_api:app --reload
   Go to: http://127.0.0.1:8000/docs
   Test the endpoint /predict with:
   {"yearBuilt" : 2010 }
   Receive a predicted price like:
   { "predicted_price": 184700.0 }

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




## Model Evaluation Results:

| Model              | MAE              | RMSE             | R² Score             |
|-------------------|------------------|------------------|----------------------|
| Linear Regression | 226,688.62       | 265,346.79       | -0.34                |
| Decision Tree     | 269,926.92       | 464,841.72       | -3.11                |
| Random Forest     | 264,880.14       | 378,002.66       | -1.72                |
| Gradient Boosting | 248,499.93       | 435,217.15       | -2.61                |

>  **MAE** = Mean Absolute Error (average price error)  
>  **RMSE** = Root Mean Square Error (penalizes large errors)  
>  **R² Score** = Model accuracy (closer to 1 is better, negative means poor fit)

## Conclusion

- All models had **negative R² scores**, which means the models do **not fit the data well**.
- However, **Linear Regression** performed slightly better than others in terms of RMSE and R².
- **Gradient Boosting** had the **lowest MAE**, which means smaller average error.