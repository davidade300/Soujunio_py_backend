from datetime import datetime

from sqlalchemy import DATE, TIMESTAMP, ForeignKey, Integer, String, Text, func
from sqlalchemy.orm import (
    Mapped,
    MappedColumn,
    mapped_column,
    relationship,
    DeclarativeBase,
)
from sqlalchemy.types import TEXT


class Base(DeclarativeBase):
    pass


class WorkBlock(Base):
    __tablename__ = "workblock"
    
    id: Mapped[int] = mapped_column(Integer, primary_key=True, autoincrement=True)
    nivel_foco: Mapped[int] = mapped_column(Integer, nullable=False)
    tempo_minutos: Mapped[int] = mapped_column(Integer, nullable=False)
    comentario: Mapped[str] = mapped_column(TEXT, nullable=False)
    criado_em: Mapped[datetime] = mapped_column(TIMESTAMP, server_default=func.now())
