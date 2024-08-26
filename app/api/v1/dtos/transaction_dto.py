from decimal import Decimal
from typing import Optional, Literal
from pydantic import BaseModel, Field

class TransactionCreateDTO(BaseModel):
    fund_id: str = Field(..., min_length=1)
    action: Literal['subscription', 'cancellation']  
    email_sms: str = Field(..., min_length=1)
    

class TransactionCancelDTO(BaseModel):
    id: str = Field(..., min_length=1)
    
