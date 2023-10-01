"""The organizations router"""
from typing import List, Optional

from fastapi import APIRouter, HTTPException

from models.models import Customers
from services.organization_service import (create_one_organization,
                                           get_all_organizations)

organizations_router = APIRouter(
    prefix="/organizations",
    tags=["Organizations"]
)


@organizations_router.get("/")
async def get_all_organizations_endpoint(
    skip: Optional[int] = 0,
    limit: Optional[int] = 10,
    search: Optional[str] = ""
) -> List[Customers]:
    """The endpoint to retrieve all organization data

    Args:
        skip (int, optional): Pagination Parameter. Defaults to 0.
        limit (int, optional): The number of records shown at a time. Defaults to 10.

    Returns:
        _type_: _description_
    """
    return await get_all_organizations(skip=skip, limit=limit, search=search)


@organizations_router.post("/")
async def create_one_organization_endpoint(organization: Customers) -> Customers:
    """The endpoint to create one organization

    Args:
        organization (Customers): The organization object

    Returns:
        Customers: The created organization object
    """
    return await create_one_organization(organization)
