from pydantic import BaseModel

class dataModel(BaseModel):
    rainfall_lag1: int
    rainfall_rolling3: int

# class dataModel(BaseModel):
#     query: str

class PredictionPipeline:
    def __init__(self):
        pass    

    def predict(self)->str:
        return "predict"