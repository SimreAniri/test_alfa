from sqlalchemy import update
from app.database import async_session_maker
from app.dao.base import BaseDAO
from app.table.models import Table


class TableDAO(BaseDAO):
    model = Table
