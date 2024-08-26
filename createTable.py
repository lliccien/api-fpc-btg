import boto3
import os
import uuid
from dotenv import load_dotenv
from botocore.exceptions import ClientError

# Cargar variables del archivo .env
load_dotenv()

# Obtener credenciales de AWS desde el archivo .env
aws_access_key_id: str = os.getenv('AWS_ACCESS_KEY_ID')
aws_secret_access_key: str = os.getenv('AWS_SECRET_ACCESS_KEY')
aws_region: str = os.getenv('DEFAULT_REGION', 'us-east-1')
dynamodb_table_funds: str = os.getenv('DYNAMODB_TABLE_FUNDS')
dynamodb_table_transactions: str = os.getenv("DYNAMODB_TABLE_TRANSACTIONS")

# Inicializamos la sesión boto3 y los recursos de DynamoDB con las credenciales
session = boto3.Session(
    aws_access_key_id=aws_access_key_id,
    aws_secret_access_key=aws_secret_access_key,
    region_name=aws_region
)


dynamodb = session.resource('dynamodb', endpoint_url='http://localhost:4566')

def create_funds_table():
    try:
        table = dynamodb.create_table(
            TableName=dynamodb_table_funds,
            KeySchema=[
                {'AttributeName': 'id', 'KeyType': 'HASH'},  # Partition key
            ],
            AttributeDefinitions=[
                {'AttributeName': 'id', 'AttributeType': 'S'},  # Cambiar el tipo a String (S)
            ],
            ProvisionedThroughput={
                'ReadCapacityUnits': 5,
                'WriteCapacityUnits': 5
            }
        )
        table.wait_until_exists()
        print("Fundations table created successfully!")
    except ClientError as e:
        print(f"Error: {e}")

def prepopulate_funds_table():
    table = dynamodb.Table(dynamodb_table_funds)
    funds = [
        {"id": str(uuid.uuid4()), "name": "FPV_BTG_PACTUAL_RECAUDADORA", "min_amount": 75000, "category": "FPV"},
        {"id": str(uuid.uuid4()), "name": "FPV_BTG_PACTUAL_ECOPETROL", "min_amount": 125000, "category": "FPV"},
        {"id": str(uuid.uuid4()), "name": "DEUDAPRIVADA", "min_amount": 50000, "category": "FIC"},
        {"id": str(uuid.uuid4()), "name": "FDO-ACCIONES", "min_amount": 250000, "category": "FIC"},
        {"id": str(uuid.uuid4()), "name": "FPV_BTG_PACTUAL_DINAMICA", "min_amount": 100000, "category": "FPV"}
    ]
    
    for fund in funds:
        table.put_item(Item=fund)
    print("Funds table prepopulated with data.")

def create_transactions_table():
    try:
        table = dynamodb.create_table(
            TableName=dynamodb_table_transactions,
            KeySchema=[
                {'AttributeName': 'id', 'KeyType': 'HASH'},  # Partition key
            ],
            AttributeDefinitions=[
                {'AttributeName': 'id', 'AttributeType': 'S'},  # Cambiar el tipo a String (S)
            ],
            ProvisionedThroughput={
                'ReadCapacityUnits': 5,
                'WriteCapacityUnits': 5
            }
        )
        table.wait_until_exists()
        print("Transactions table created successfully!")
    except ClientError as e:
        print(f"Error: {e}")

if __name__ == "__main__":
    create_funds_table()
    prepopulate_funds_table()
    create_transactions_table()
