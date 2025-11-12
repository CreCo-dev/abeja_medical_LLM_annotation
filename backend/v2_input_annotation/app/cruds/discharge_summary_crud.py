from sqlalchemy.orm import Session

from app.db.entities.discharge_summary import DischargeSummary
from app.schemas import discharge_summary_schema

def create_discharge_summary(db: Session, create_data: discharge_summary_schema.DischargeSummaryCreate):
    """Create"""
    db_data = DischargeSummary(**create_data.model_dump(exclude_unset=True))
    db.add(db_data)
    db.commit()
    db.refresh(db_data)
    return db_data

def get_discharge_summary(db: Session, id: int):
    """Read (by id)"""
    return db.query(DischargeSummary).filter(DischargeSummary.id == id).first()

def get_discharge_summaries(db: Session, skip: int = 0, limit: int = 100):
    """Read all"""
    return db.query(DischargeSummary).offset(skip).limit(limit).all()

def update_discharge_summary(db: Session, id: int, model_update: discharge_summary_schema.DischargeSummaryUpdate):
    """Update"""
    db_data = db.query(DischargeSummary).filter(DischargeSummary.id == id).first()
    if not db_data:
        return None
    update_data = model_update.model_dump(exclude_unset=True)
    for key, value in update_data.items():
        setattr(db_data, key, value)
    db.commit()
    db.refresh(db_data)
    return db_data

def delete_discharge_summary(db: Session, id: int):
    """Delete"""
    db_data = db.query(DischargeSummary).filter(DischargeSummary.id == id).first()
    if not db_data:
        return None
    db.delete(db_data)
    db.commit()
    return db_data
