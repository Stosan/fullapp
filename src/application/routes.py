from src.config.settings import get_settings
settings = get_settings()

from src.services.prediction_pipeline import PredictionPipeline
from .data_model import predictionRequest, chatRequest

from fastapi import APIRouter


prediction_route = APIRouter()

@prediction_route.post("/predict")
async def predict(request: predictionRequest):
    print(request)
    pipeline = PredictionPipeline()
    return {"message": request}

# @chat_route.post("/predict")
# async def predict(request: chatRequest):
#     pipeline = PredictionPipeline()
#     return {"message": pipeline.predict()}