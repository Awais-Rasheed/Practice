from pydantic import BaseModel, Field , computed_field
from typing import Optional, List, Dict
class Product(BaseModel):
    id:int  
    name:str
    price:float
    in_stock: bool = True
    password:str
    confirm_password: str

class Employee(BaseModel):
    id: int
    name: str = Field(
        ...,
        min_length=3,
        max_length=50,
        example="Awais Rasheed"
    )
    department: Optional[str] = 'General'
    salary:float = Field(
                        ...,
                         ge=10000
                    )
    

    @field_validator('name') #type: ignore
    def username_length(cls, v):
        if len(v)< 4:
            raise ValueError("Username must be more than 4 characters")
        return v
    

    @model_validator(mode='after') #type:ignore
    def password_match(cls, values):
        if values.password != values.confirm_password:
            raise ValueError("Password Doesn't Match")
        return values
    

    
class Booking(BaseModel):
    user_id:int
    room_id: int
    nights: int = Field(..., ge=1)
    rate_per_night: float

    @computed_field
    @property
    def total_amount(self) -> float:
        return self.nights * self.rate_per_night