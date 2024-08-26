import logging
import boto3
from botocore.exceptions import NoCredentialsError, ClientError
from app.core.config import settings

class NotificationService:

    
    def __init__(self):
        self.sns_client = boto3.client(
            'sns',
            region_name=settings.default_region,
            aws_access_key_id=settings.aws_access_key_id,
            aws_secret_access_key=settings.aws_secret_access_key,
            endpoint_url='http://localhost:4566'
        )
        self.logger = logging.getLogger(__name__)
        self.configurar_logger()

    def configurar_logger(self):
        formato = "%(asctime)s - %(levelname)s - %(message)s"
        logging.basicConfig(level=logging.INFO, format=formato)

    def send_email(self, email: str, subject: str, message: str):
        try:
            response = self.sns_client.publish(
                TopicArn='arn:aws:sns:us-east-1:000000000000:email-topic',
                Message=message,
                Subject=subject,
                MessageAttributes={
                    'email': {'DataType': 'String', 'StringValue': email}
                }
            )
            self.logger.info(f"se envion el correo a {email}")
            return response
        except (NoCredentialsError, ClientError) as e:
            raise Exception(f"Failed to send email: {str(e)}")

    def send_sms(self, phone_number: str, message: str):
        try:
            response = self.sns_client.publish(
                PhoneNumber=phone_number,
                Message=message
            )
            self.logger.info(f"se envion un sms a {phone_number}")
            return response
        except (NoCredentialsError, ClientError) as e:
            raise Exception(f"Failed to send SMS: {str(e)}")
