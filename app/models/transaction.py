from datetime import datetime
from decimal import Decimal
from typing import Optional
from pydantic import BaseModel, Field
import uuid

class Transaction(BaseModel):
    id: str = Field(default_factory=lambda: str(uuid.uuid4()))
    fund_id: str
    action: str
    email_sms: Optional[str] = None
    balance: Optional[Decimal]
    created_at: Decimal = Field(default_factory=lambda: Decimal(str(datetime.now().timestamp())))
    

    def to_dict(self):
        """
        Convert the Transaction instance to a dictionary for DynamoDB storage.
        """
        return {
            "id": self.transaction_id,
            "fund_id": self.fund_id,
            "action": self.action,
            "email_sms": self.email_sms,
            "balance": self.balance,
            "created_at": self.created_at
            
        }
