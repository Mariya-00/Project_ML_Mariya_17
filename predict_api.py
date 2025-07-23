from fastapi import FastAPI
from pydantic import BaseModel
import pandas as pd
import joblib

# Load the trained model
model = joblib.load("model.pkl")

# Create the FastAPI app
app = FastAPI()

# Define input format for the API
class PropertyInput(BaseModel):
    yearBuilt: int

# Create a POST endpoint for predictions
@app.post("/predict")
def predict_price(data: PropertyInput):
    # Convert input to DataFrame
    input_df = pd.DataFrame([data.dict()])
    
    # Predict using the loaded model
    prediction = model.predict(input_df)

    # Return prediction as JSON
    return {"predicted_price": float(prediction[0])}
