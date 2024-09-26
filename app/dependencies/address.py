from typing import Annotated

from fastapi import Depends, HTTPException, Path, status
from sqlalchemy.ext.asyncio import AsyncSession

from db import Address, db_helper, AddressRepository


async def address_by_id(
    address_id: Annotated[int, Path],
    session: AsyncSession = Depends(db_helper.scoped_session_dependency),
) -> Address:
    address_repo = AddressRepository(session=session)
    address = await address_repo.get_address_by_id(address_id=address_id)
    if address:
        return address
    raise HTTPException(
        status_code=status.HTTP_404_NOT_FOUND, detail=f"Address {address_id} not found!"
    )
