from sqlalchemy.orm import Session
from app.models.signal import Signal

def compute_day_awareness(db: Session, day_id: int):
    signals = db.query(Signal).filter(Signal.day_id == day_id).all()

    pressure = sum(s.value for s in signals if s.type == "pressure")
    activity = sum(s.value for s in signals if s.type == "activity")
    delay = sum(s.value for s in signals if s.type == "delay")

    if pressure > 70:
        pressure_level = "high"
    elif pressure > 40:
        pressure_level = "medium"
    else:
        pressure_level = "low"

    if activity > 60 and delay < 20:
        flow_level = "smooth"
    elif activity > 30:
        flow_level = "normal"
    else:
        flow_level = "low"

    return {
        "day_id": day_id,
        "pressure_level": pressure_level,
        "flow_level": flow_level,
        "activity_score": activity,
        "delay_score": delay,
    }
