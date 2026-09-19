from sqlalchemy import Column, Integer, String, ForeignKey
from app.core.db import Base

class Signal(Base):
    __tablename__ = "signals"

    id = Column(Integer, primary_key=True, index=True)
    type = Column(String, index=True)
    value = Column(Integer)
    unit_id = Column(Integer, ForeignKey("units.id"))
    entity_id = Column(Integer, ForeignKey("entities.id"))
    day_id = Column(Integer, ForeignKey("days.id"))
