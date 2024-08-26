from app.models.fundation import Fundation
from app.repositories.fundation_repository import FundationRepository

class FundationService:
    def __init__(self, repository: FundationRepository):
        self.repository = repository

    def create_fundation(self, fundation_data: dict) -> Fundation:
        fundation = Fundation(**fundation_data)
        self.repository.create_fundation(fundation)
        return fundation

    def get_fundation(self, fundation_id: str) -> Fundation:
        return self.repository.get_fundation(fundation_id)

    def update_fundation(self, fundation_id: str, update_data: dict) -> Fundation:
        self.repository.update_fundation(fundation_id, update_data)

    def delete_fundation(self, fundation_id: str):
        self.repository.delete_fundation(fundation_id)

    def get_all_fundations(self):
        fundations = self.repository.get_all_fundations()
        return fundations
    
    def get_fund_by_id(self, id: str) -> Fundation:
        return self.repository.get_fundation(id)