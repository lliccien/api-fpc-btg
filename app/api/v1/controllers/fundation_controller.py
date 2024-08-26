from fastapi import APIRouter, Depends, HTTPException
from app.models.fundation import Fundation
from app.services.fundation_service import FundationService
from app.repositories.fundation_repository import FundationRepository
from app.api.v1.dtos.fundation_dto import FundationCreateDTO, FundationUpdateDTO
from app.core.config import settings

router = APIRouter()

def get_fundation_service():
    repository = FundationRepository()
    return FundationService(repository=repository)

@router.post("/fundations", response_model=Fundation)
def create_fundation(fundation_dto: FundationCreateDTO, service: FundationService = Depends(get_fundation_service)):
    fundation = service.create_fundation(fundation_data=fundation_dto.dict())
    return function

@router.get('/fundations', response_model=list[Fundation])
def get_all_fundations(service: FundationService = Depends(get_fundation_service)):
    fundations = service.get_all_fundations()
    return fundations

@router.get("/fundations/{fundation_id}", response_model=Fundation)
def get_fundation(fundation_id: str, service: FundationService = Depends(get_fundation_service)):
    fundation = service.get_fundation(fundation_id=fundation_id)
    if not fundation:
        raise HTTPException(status_code=404, detail="Fundation not found")
    return fundation

@router.put("/fundations/{fundation_id}")
def update_fundation(fundation_id: str, update_dto: FundationUpdateDTO, service: FundationService = Depends(get_fundation_service)):
    service.update_fundation(fundation_id=fundation_id, update_data=update_dto.dict(exclude_unset=True))
    return {"message": "Fundation updated successfully"}

@router.delete("/fundations/{fundation_id}")
def delete_fundation(fundation_id: str, service: FundationService = Depends(get_fundation_service)):
    service.delete_fundation(fundation_id=fundation_id)
    return {"message": "Fundation deleted successfully"}

