from decimal import Decimal
from pydantic import BaseModel, Field
import uuid

class Fundation(BaseModel):
    id: str = Field(default_factory=lambda: str(uuid.uuid4()))
    name: str
    min_amount: Decimal 
    category: str

    def to_dict(self):
        """
        Convert the Fundation instance to a dictionary for DynamoDB storage.
        """
        return {
            "id": self.id,
            "name": self.name,
            "min_amount": self.min_amount,
            "category": self.category
        }
