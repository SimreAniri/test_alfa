from pydantic import BaseModel, validator
from sqlalchemy import JSON

from app.exceptions import NameAlreadyExistsException
from app.table.dao import TableDAO

class SNameAdd(BaseModel):
    name: str
    value: str
