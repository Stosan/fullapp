from pydantic import BaseModel


class predictionRequest(BaseModel):
    rainfall_lag1: int
    rainfall_rolling3: int

class chatRequest(BaseModel):
    query: str