import pandas as pd
import joblib
import os

# Load model with proper error handling
model_path = "models/house_price_model.pkl"
if os.path.exists(model_path):
    model = joblib.load(model_path)
else:
    raise FileNotFoundError(f"Model file not found at {model_path}")

# Feature names must match training data
FEATURE_NAMES = [
    "median_income", "housing_median_age", "total_rooms", "rooms_per_household",
    "population_per_household", "total_bedrooms", "bedrooms_per_room", 
    "population", "households", "latitude", "longitude", "ocean_proximity"
]

def predict_house_price(features: list) -> float:
    """
    Predict house price given a list of features.
    
    Args:
        features: List of 12 feature values
        
    Returns:
        float: Predicted house price
    """
    if len(features) != len(FEATURE_NAMES):
        raise ValueError(f"Expected {len(FEATURE_NAMES)} features, got {len(features)}")
    
    # Create DataFrame with proper column names
    df = pd.DataFrame([features], columns=FEATURE_NAMES)
    prediction = model.predict(df)
    return float(prediction[0])
