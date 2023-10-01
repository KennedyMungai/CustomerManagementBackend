"""The organizations service file"""
from typing import List, Optional

from models.models import Customers


async def get_all_organizations(
    skip: Optional[int] = 0,
    limit: Optional[int] = 0,
    search: Optional[str] = ''
) -> List[Customers]:
    """The function to retrieve all documents from db

    Args:
        skip (int, optional): The pagination query. Defaults to 0.
        limit (int, optional): The limit per page. Defaults to 0.
        search (str, optional): The search query. Defaults to "".

    Returns:
        List[Customers]: _description_
    """
    return await Customers.find_all().filter(search).skip(skip).limit(limit).to_list()
