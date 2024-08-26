from app.core.config import dynamodb
from boto3.dynamodb.conditions import Key

from app.models.transaction import Transaction
from app.schemas.transaction_schema import TransactionSchema
from botocore.exceptions import ClientError
from app.core.config import settings

class TransactionRepository:
    def __init__(self):
        self.table = dynamodb.Table(settings.dynamodb_table_transactions)

    def create_transaction(self, transaction: TransactionSchema):
        try:
            self.table.put_item(Item=transaction.dict())
            return transaction
        except ClientError as e:
            raise Exception(f"Error creating transaction: {e}")

    def get_all_transactions(self) -> list[Transaction]:
        try:
            response = self.table.scan()
            transactions = response.get('Items', [])

            sorted_transactions = sorted(transactions, key=lambda x: x['created_at'], reverse=True)
            
            return sorted_transactions
        except ClientError as e:
            raise Exception(f"Error fetching all transactions: {e}")
        
    def get_transaction_by_id(self, id: str) -> Transaction:
        try:
            response = self.table.get_item(Key={'id': id})
            if 'Item' in response:
                return response['Item']
            else:
                return None
        except ClientError as e:
            raise Exception(f"Error fetching transaction by ID: {e}")