from boto3.dynamodb.conditions import Key
from app.core.config import dynamodb
from app.schemas.fundation_schema import FundationSchema
from botocore.exceptions import ClientError
from app.core.config import settings

class FundationRepository:
    def __init__(self):
        self.table = dynamodb.Table(settings.dynamodb_table_funds)

    def create_fundation(self, fundation: FundationSchema):
        try:
            self.table.put_item(Item=fundation.dict())
            return fundation
        except ClientError as e:
            raise Exception(f"Error creating fundation: {e}")

    def get_fundation(self, fundation_id: str):
        try:
            response = self.table.get_item(Key={'id': fundation_id})
            return response.get('Item')
        except ClientError as e:
            raise Exception(f"Error fetching fundation: {e}")

    def update_fundation(self, fundation_id: str, update_data: dict):
        try:
            response = self.table.update_item(
                Key={'id': fundation_id},
                UpdateExpression="set #name=:n, min_amount=:m, category=:c",
                ExpressionAttributeValues={
                    ':n': update_data['name'],
                    ':m': update_data['min_amount'],
                    ':c': update_data['category']
                },
                ExpressionAttributeNames={"#name": "name"},
                ReturnValues="UPDATED_NEW"
            )
            return response
        except ClientError as e:
            raise Exception(f"Error updating fundation: {e}")

    def delete_fundation(self, fundation_id: str):
        try:
            self.table.delete_item(Key={'id': fundation_id})
            return {"message": "Fundation deleted successfully"}
        except ClientError as e:
            raise Exception(f"Error deleting fundation: {e}")

    def get_all_fundations(self):
        try:
            response = self.table.scan()
            return response.get('Items')
        except ClientError as e:
            raise Exception(f"Error fetching all fundations: {e}")