"""The database configuration file"""
from beanie import init_beanie
from motor.motor_asyncio import AsyncIOMotorClient

from models.models import Customers


async def init_db():
    """The function which communicates with the database"""
    client = AsyncIOMotorClient("https://localhost:27017")
    await init_beanie(database=client.Organizations, document_models=[Customers])
