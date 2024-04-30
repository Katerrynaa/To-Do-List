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


class UserBase(BaseModel):
    username: str
    email: str
    password: str

class UserOut(UserBase):
    pass

class UserAuth(UserBase):
    pass