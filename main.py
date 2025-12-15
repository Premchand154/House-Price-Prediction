from fastapi import FastAPI, HTTPException
from fastapi.responses import JSONResponse
from schema import HouseInput, PredictionOutput
from model import predict_house_price
import logging

# Setup logging
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

app = FastAPI(
    title="House Price Prediction API",
    description="ML API to predict house prices based on features",
    version="1.0.0"
)

@app.get("/", tags=["Health"])
def root():
    """Health check endpoint"""
    return {"status": "API is running", "version": "1.0.0"}

@app.post("/predict", response_model=PredictionOutput, tags=["Prediction"])
def predict(data: HouseInput):
    """
    Predict house price based on input features.
    
    Returns predicted house price as a float value.
    """
    try:
        # Extract features in correct order
        features = [
            data.median_income,
            data.housing_median_age,
            data.total_rooms,
            data.rooms_per_household,
            data.population_per_household,
            data.total_bedrooms,
            data.bedrooms_per_room,
            data.population,
            data.households,
            data.latitude,
            data.longitude,
            data.ocean_proximity,
        ]

        logger.info(f"Received prediction request with features: {features}")
        price = predict_house_price(features)
        
        logger.info(f"Prediction successful: ${price:,.2f}")
        return PredictionOutput(predicted_price=price)
        
    except ValueError as ve:
        logger.error(f"Validation error: {str(ve)}")
        raise HTTPException(status_code=400, detail=f"Invalid input: {str(ve)}")
    except Exception as e:
        logger.error(f"Prediction error: {str(e)}")
        raise HTTPException(status_code=500, detail=f"Prediction failed: {str(e)}")

@app.get("/health", tags=["Health"])
def health_check():
    """Extended health check with model status"""
    return {
        "status": "healthy",
        "api": "House Price Prediction API",
        "version": "1.0.0"
    }
