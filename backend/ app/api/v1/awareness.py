from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from app.core.db import SessionLocal
from app.services.awareness import compute_day_awareness

router = APIRouter()

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

@router.get("/day/{day_id}")
def get_day_awareness(day_id: int, db: Session = Depends(get_db)):
    return compute_day_awareness(db, day_id)
