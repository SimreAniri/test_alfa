from datetime import datetime
from sqlalchemy import VARCHAR, Date, JSON
from sqlalchemy.orm import Mapped, mapped_column
from app.database import Base

class Table(Base):
    __tablename__ = "table"
    id: Mapped[int] = mapped_column(primary_key=True, autoincrement=True, nullable=False)
    name: Mapped[str] = mapped_column(VARCHAR(50), unique=True, nullable=False)
    value: Mapped[list[str]] = mapped_column(JSON)
    date_update: Mapped[datetime] = mapped_column(Date, nullable=False)