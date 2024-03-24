import json
from fastapi import APIRouter

from app.exceptions import NameAlreadyExistsException, NameNotExistsException
from app.table.dao import TableDAO
from app.table.schemas import SNameAdd

router = APIRouter(
    prefix="/tab",
    tags=["Таблица"]
)

@router.post("/add")
async def add_name(table_data: SNameAdd):
    existing_name = await TableDAO.find_one_or_none(name=table_data.name)
    if existing_name:
        raise NameAlreadyExistsException
    value = json.loads(table_data.value)
    await TableDAO.add(name=table_data.name,
                       value=value)
    return table_data.name, value

@router.get("/get_data/{name}")
async def get_data(name: str):
    name = await TableDAO.find_one_or_none(name=name)
    if name:
        return name.value
    raise NameNotExistsException

@router.delete("/{name}")
async def del_data(name: str):
    existing_name = await TableDAO.find_one_or_none(name=name)
    if existing_name:
        await TableDAO.delete(name=name)
    else:
        raise NameNotExistsException
    
@router.patch("/patch/{name}")
async def patch_value(name: str, value: str):
    existing_name = await TableDAO.find_one_or_none(name=name)
    if existing_name:
        value = json.loads(value)
        await TableDAO.update_data(name=name, value=value)
    else:
        raise NameNotExistsException