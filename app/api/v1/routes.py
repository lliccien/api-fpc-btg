from fastapi import APIRouter
from app.api.v1.controllers.fundation_controller import router as fundation_router
from app.api.v1.controllers.transaction_controller import router as transaction_router

api_router = APIRouter()

api_router.include_router(fundation_router, prefix="/api/v1", tags=["Fundations"])
api_router.include_router(transaction_router, prefix="/api/v1", tags=["Transactions"])
