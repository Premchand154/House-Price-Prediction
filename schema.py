from pydantic import BaseModel, Field, validator

class HouseInput(BaseModel):
    median_income: float = Field(..., gt=0, description="Median household income")
    housing_median_age: float = Field(..., ge=0, le=100, description="Age of housing in years")
    total_rooms: float = Field(..., gt=0, description="Total number of rooms")
    total_bedrooms: float = Field(..., gt=0, description="Total number of bedrooms")
    bedrooms_per_room: float = Field(..., gt=0, description="Ratio of bedrooms to rooms")
    rooms_per_household: float = Field(..., gt=0, description="Rooms per household")
    population: float = Field(..., ge=0, description="Total population")
    population_per_household: float = Field(..., gt=0, description="People per household")
    households: float = Field(..., gt=0, description="Number of households")
    latitude: float = Field(..., ge=-90, le=90, description="Latitude coordinate")
    longitude: float = Field(..., ge=-180, le=180, description="Longitude coordinate")
    ocean_proximity: str = Field(..., description="Proximity to ocean (e.g., '<1H OCEAN', 'INLAND')")
    
    @validator("bedrooms_per_room", "rooms_per_household", "population_per_household")
    def check_ratios(cls, v):
        if v <= 0:
            raise ValueError("Ratio values must be positive")
        return v
    
    class Config:
        schema_extra = {
            "example": {
                "median_income": 8.3252,
                "housing_median_age": 41,
                "total_rooms": 880,
                "total_bedrooms": 129,
                "bedrooms_per_room": 0.2,
                "rooms_per_household": 6.0,
                "population": 322,
                "population_per_household": 2.555,
                "households": 126,
                "latitude": 37.88,
                "longitude": -122.23,
                "ocean_proximity": "<1H OCEAN"
            }
        }

class PredictionOutput(BaseModel):
    predicted_price: float = Field(..., gt=0, description="Predicted house price")
    
    class Config:
        schema_extra = {
            "example": {
                "predicted_price": 452600.0
            }
        }
