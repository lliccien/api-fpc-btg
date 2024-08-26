from decimal import Decimal
from pydantic import Field
from pydantic_settings import BaseSettings

import boto3

class Settings(BaseSettings):
    aws_access_key_id: str = Field(..., env="AWS_ACCESS_KEY_ID")
    aws_secret_access_key: str = Field(..., env="AWS_SECRET_ACCESS_KEY")
    default_region: str = Field(default="us-east-1", env="DEFAULT_REGION")
    
    dynamodb_table_funds: str = Field(default="fundations", env="DYNAMODB_TABLE_FUNDS")
    dynamodb_table_transactions: str = Field(default="transactions", env="DYNAMODB_TABLE_TRANSACTIONS")

    initial_amount: Decimal = Field(default=Decimal("500000.00"), env="INITIAL_AMOUNT")

    fastapi_debug: bool = Field(default=False, env="FASTAPI_DEBUG")

    class Config:
        env_file = ".env"  

settings = Settings()

boto3_session = boto3.Session(
    aws_access_key_id=settings.aws_access_key_id,
    aws_secret_access_key=settings.aws_secret_access_key,
    region_name=settings.default_region
)

dynamodb = boto3_session.resource('dynamodb', endpoint_url='http://localhost:4566')
funds_table = dynamodb.Table(settings.dynamodb_table_funds)
transactions_table = dynamodb.Table(settings.dynamodb_table_transactions)
