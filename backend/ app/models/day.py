from sqlalchemy import Column, Integer, Date
from app.core.db import Base

class Day(Base):
    __tablename__ = "days"

    id = Column(Integer, primary_key=True, index=True)
    date = Column(Date, unique=True, index=True)
