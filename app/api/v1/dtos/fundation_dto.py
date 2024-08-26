from decimal import Decimal
from pydantic import BaseModel, Field

class FundationCreateDTO(BaseModel):
    name: str = Field(..., min_length=3)
    min_amount: Decimal = Field(..., gt=0)
    category: str = Field(..., min_length=2)

class FundationUpdateDTO(BaseModel):
    name: str = Field(None, min_length=3)
    min_amount: Decimal = Field(None, gt=0)
    category: str = Field(None, min_length=2)
