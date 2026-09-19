from fastapi import FastAPI
from app.core.db import Base, engine
from app.api.v1 import entities, units, tasks, signals, awareness

app = FastAPI(title="Dazzle Adaptive Core")

Base.metadata.create_all(bind=engine)

app.include_router(entities.router, prefix="/api/v1/entities", tags=["entities"])
app.include_router(units.router, prefix="/api/v1/units", tags=["units"])
app.include_router(tasks.router, prefix="/api/v1/tasks", tags=["tasks"])
app.include_router(signals.router, prefix="/api/v1/signals", tags=["signals"])
app.include_router(awareness.router, prefix="/api/v1/awareness", tags=["awareness"])
