from pydantic import BaseModel
from datetime import datetime



class ToDoPydanticModel(BaseModel):
    id: int 
    title: str
    description: str 
    is_completed: datetime

    class Config:
        orm_mode = True 


class Message(BaseModel):
    message: str

    class Config:
        orm_mode = True


