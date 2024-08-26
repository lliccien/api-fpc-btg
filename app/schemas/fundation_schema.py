from decimal import Decimal
from pydantic import BaseModel, Field
from typing import Optional
import uuid

class FundationSchema(BaseModel):
    id: Optional[str] = Field(default_factory=lambda: str(uuid.uuid4()))
    name: str
    min_amount: Decimal
    category: str

class UpdateFundationSchema(BaseModel):
    name: Optional[str]
    min_amount: Optional[Decimal]
    category: Optional[str]
