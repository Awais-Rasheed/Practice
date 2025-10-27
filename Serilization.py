from pydantic import BaseModel, ConfigDict
from typing import List
from datetime import datetime

class Address(BaseModel):
    street:str
    city:str
    zip_code:str

class User(BaseModel):
    id: int
    name:str
    address: Address
    createdAt: datetime
    tags: List[str] = []

    model_config = ConfigDict(
        json_encoders = {datetime: lambda v: v.strftime('%d/%m/%Y, %H: %M')}
    )


user = User(
    id = 101,
    name = "Awais",
    address = Address(
        street="Street 1",
        city = "Kasur",
        zip_code="E123"
    ),
    tags = ["Golden", "Developer"],
    createdAt = datetime(2025, 3, 12, 4, 30)
)



print(user.model_dump())
print("\n+++++++++++++++++++++++++++++++++++++++++++++\n")
print(user.model_dump_json())