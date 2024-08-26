from typing import List
from fastapi import APIRouter, Depends, HTTPException
from app.models.transaction import Transaction
from app.repositories.fundation_repository import FundationRepository
from app.services.fundation_service import FundationService
from app.services.notification_services import NotificationService
from app.services.transaction_service import TransactionService
from app.repositories.transaction_repository import TransactionRepository
from app.api.v1.dtos.transaction_dto import TransactionCreateDTO, TransactionCancelDTO


router = APIRouter()

def get_transaction_service():
    repository = TransactionRepository()
    fund_repository = FundationRepository()
    fund_service = FundationService(fund_repository)
    notification_service = NotificationService()
    return TransactionService(repository, fund_service, notification_service)

@router.post("/transactions", response_model=Transaction)
async def create_transaction(transaction_dto: TransactionCreateDTO, service: TransactionService = Depends(get_transaction_service)):
    transaction = service.create_transaction(transaction_data=transaction_dto.dict())
    return transaction

@router.get('/transactions', response_model=list[Transaction])
def get_all_transaction(service: TransactionService = Depends(get_transaction_service)):
    transactions = service.get_all_transactions()
    return transactions

@router.post("/transactions/cancel", response_model=TransactionCancelDTO)
def cancel_transaction(transaction_cancel_dto: TransactionCancelDTO, service: TransactionService = Depends(get_transaction_service)):
    transaction = service.create_cancellation_transaction(transaction_id=transaction_cancel_dto.id)
    return transaction