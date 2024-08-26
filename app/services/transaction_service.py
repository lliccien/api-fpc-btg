
from decimal import Decimal
from functools import reduce
from fastapi import HTTPException
from app.models.fundation import Fundation
from app.models.transaction import Transaction
from app.repositories.transaction_repository import TransactionRepository
from app.services.fundation_service import FundationService
from app.services.notification_services import NotificationService
from app.core.config import settings

class TransactionService:
    def __init__(self, repository: TransactionRepository, fund_service: FundationService, notification_service: NotificationService):
        self.repository = repository
        self.fund_service = fund_service
        self.notification_service = notification_service

    def create_transaction(self, transaction_data: dict) -> Transaction:
    
        fund = self.fund_service.get_fund_by_id(transaction_data["fund_id"])

        transaction_data["balance"] =  self.set_subscription_balance(fund)

        transaction = Transaction(**transaction_data)

        self.repository.create_transaction(transaction)

        self.send_notification(transaction.email_sms, fund["name"])

        return transaction
    
    def set_subscription_balance(self, fundation: Fundation):
        transactions = self.repository.get_all_transactions()

        if len(transactions) == 0:
            balance = (settings.initial_amount - fundation["min_amount"])
        elif transactions[0]["balance"] >= fundation["min_amount"]:
            balance = (transactions[0]["balance"] - fundation["min_amount"])
        else:
            raise HTTPException(status_code=400, detail=f"No tiene saldo disponible para vincularse al fondo {fundation['name']}")

        return balance
    
    def create_cancellation_transaction(self, transaction_id: str):
        transaction = self.repository.get_transaction_by_id(transaction_id)

        fund = self.fund_service.get_fund_by_id(transaction["fund_id"])

        if transaction["balance"] < Decimal(settings.initial_amount):
            balance = (transaction["balance"] + fund["min_amount"])
            cancellation_transaction = {
                "fund_id": transaction["fund_id"],
                "action": "cancellation",
                "balance": balance
            }
        else:
            raise HTTPException(status_code=400, detail=f"El valor inicial se encuentra totalmente disponible")
        
        transaction = Transaction(**cancellation_transaction)

        self.repository.create_transaction(transaction)

        return transaction

    
    def get_all_transactions(self) -> list[Transaction]:
        transactions = self.repository.get_all_transactions()
        return transactions
    
    def send_notification(self, transaction_email_sms: str, fund_name: str):
        if "@" in transaction_email_sms:
        
            email = transaction_email_sms
            subject = "Confirmación de Suscripción"
            message = f"Su suscripción al fondo {fund_name} ha sido exitosa."
            try:
                self.notification_service.send_email(email, subject, message)
            except Exception as e:
                raise HTTPException(
                    status_code=500,
                    detail=f"Error al enviar el correo electrónico: {str(e)}"
                )
        else:
        
            phone_number = transaction_email_sms
            message = f"Su suscripción al fondo {fund_name} ha sido exitosa."
            try:
                self.notification_service.send_sms(phone_number, message)
            except Exception as e:
                raise HTTPException(
                    status_code=500,
                    detail=f"Error al enviar el SMS: {str(e)}"
                )   