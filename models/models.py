"""The models file for the application"""
from beanie import Document, PydanticObjectId
from pydantic import HttpUrl


class Customers(Document):
    """The class model for Customers

    Args:
        Document (The base class): The basis for all models
    """
    index: int
    OrganizationId: PydanticObjectId
    name: str
    website: HttpUrl
    Country: str
    Description: str
    Founded: int
    Industry: str
    NumberOfEmployees: int

    class Settings:
        """The class containing the name of the collection"""
        name = "organizations_collection"

    class Config:
        """The class responsible for model configuration"""
        json_schema_extra = {
            "example": {
                "index": 1,
                "OrganizationId": "5f0f7e8d0f8b8f0f8b8f0f8b",
                "name": "Acme",
                "website": "https://acme.com",
                "Country": "USA",
                "Description": "A company",
                "Founded": 1990,
                "Industry": "Technology",
                "NumberOfEmployees": 100
            }
        }
