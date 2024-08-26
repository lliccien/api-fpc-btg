from datetime import datetime
from decimal import Decimal
from pydantic import BaseModel, Field
from typing import Optional
import uuid

class TransactionSchema(BaseModel):
    id: str = Field(default_factory=lambda: str(uuid.uuid4()))
    fund_id: str
    action: str
    email_sms: Optional[str]
    balance: Optional[Decimal]
    created_at: int = Field(default_factory=lambda: datetime.utcnow().timestamp())
    

class UpdateTransactionSchema(BaseModel):
    action: Optional[str]
    balance: Optional[Decimal]
