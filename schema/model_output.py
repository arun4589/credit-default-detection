from pydantic import BaseModel,Field
from typing import Dict


class PredictionResponse(BaseModel):
    predicted_category: str=Field(
        ...,
        description='Predicted category by model',
        examples=['Default','Not Default']
    )
    confidence:float=Field(
        ...,
        description="Confidence score of model on predicted category",
        examples=[0.234,0.456]
    )
    class_probalbilities:Dict[str,float]=Field(
        ...,
        description='Probabilities of all the classes',
        examples=[{'Default':0.345,'Not Default':0.655}]
    )