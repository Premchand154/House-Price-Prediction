# House-Price-Prediction
A production-ready **Machine Learning API** built with **FastAPI** that predicts house prices based on key housing and geographical features. The project demonstrates best practices in **ML model serving, API design, validation, and deployment readiness**.

# Key Features

- Predicts house prices using a trained **Scikit-learn** model
- High-performance REST API with **FastAPI**
- Strong input validation with **Pydantic**
- Pre-trained ML model loaded at startup
- Test-ready and deployment-ready architecture
- Clean, modular, and scalable codebase

---

# Project Structure

```

.
├── main.py               # FastAPI application entry point
├── model.py              # Model loading and prediction logic
├── schema.py             # Input & output validation schemas
├── requirements.txt      # Python dependencies
├── models/
│   └── house_price_model.pkl   # Trained ML model
└── README.md

````

---

# Machine Learning Model

- Algorithm: Scikit-learn regression model
- Input: 12 housing and geographic features
- Output: Predicted house price (float)
- Model is loaded once for efficient inference

---

# Input Features

| Feature | Description |
|-------|------------|
| median_income | Median household income |
| housing_median_age | Median age of houses |
| total_rooms | Total number of rooms |
| total_bedrooms | Total number of bedrooms |
| bedrooms_per_room | Bedroom-to-room ratio |
| rooms_per_household | Rooms per household |
| population | Total population |
| population_per_household | Population per household |
| households | Number of households |
| latitude | Latitude |
| longitude | Longitude |
| ocean_proximity | Proximity to ocean |

---

# Installation

# Clone the repository
```bash
git clone https://github.com/your-username/house-price-prediction-api.git
cd house-price-prediction-api
````

# Create and activate virtual environment (recommended)

```bash
python -m venv venv
source venv/bin/activate     # Windows: venv\Scripts\activate
```

# Install dependencies

```bash
pip install -r requirements.txt
```

---

# Running the API

Start the FastAPI server using Uvicorn:

```bash
uvicorn main:app --reload
```

API will be available at:

```
http://127.0.0.1:8000
```

---

# API Documentation

FastAPI automatically provides interactive documentation:

* **Swagger UI:** [http://127.0.0.1:8000/docs](http://127.0.0.1:8000/docs)
* **ReDoc:** [http://127.0.0.1:8000/redoc](http://127.0.0.1:8000/redoc)

---

# API Endpoints

# Health Check

```http
GET /
GET /health
```

# Predict House Price

```http
POST /predict
```

# Example Request

```json
{
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
```

# Example Response

```json
{
  "predicted_price": 452600.0
}
```

---

# Testing

The project supports testing with **pytest** and **httpx**.

```bash
pytest
```

---

# Deployment

This API can be deployed on:

* AWS (EC2 / ECS)
* Google Cloud Run
* Azure
* Render / Railway / Fly.io
* Docker-based platforms

---

# Error Handling & Validation

* Strict request validation with Pydantic
* Clear HTTP error responses
* Logging enabled for monitoring and debugging

---

