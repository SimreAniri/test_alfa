from datetime import datetime
from sqlalchemy import insert, update

from app.database import async_session_maker
from app.dao.base import BaseDAO
from app.table.models import Table


class TableDAO(BaseDAO):
    model = Table

    @classmethod
    async def add(cls, name, value):
        async with async_session_maker() as session:
            query = insert(Table).values(name=name, value=value, date_update=datetime.utcnow())
            await session.execute(query)
            await session.commit()