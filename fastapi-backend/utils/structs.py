from pydantic import BaseModel


class CreatePinModel(BaseModel):
    title: str
    description: str
    filter_type: str
    x_coordinate: float
    y_coordinate: float


class CreateAlertModel(BaseModel):
    title: str
    description: str
    x_coordinate: float
    y_coordinate: float
