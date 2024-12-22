from pydantic import BaseModel
from typing import Optional
from datetime import date

class UserCreate(BaseModel):
    first_name: str
    last_name: str
    email: str
    age: Optional[int] = None
    address: Optional[str] = None
    joining_date: Optional[date] = None

class UserUpdate(BaseModel):
    first_name: Optional[str] = None
    last_name: Optional[str] = None
    email: Optional[str] = None
    age: Optional[int] = None
    address: Optional[str] = None

class UserResponse(BaseModel):
    id: int
    first_name: str
    last_name: str
    email: str
    age: Optional[int]
    address: Optional[str]
    joining_date: date
    is_registered: bool

    class Config:
        orm_mode = True