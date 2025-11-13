from sqlalchemy.orm import Session

from app.db.entities.stroke_patient import StrokePatient
from app.schemas import stroke_patient_schema

def create_stroke_patient(db: Session, create_data: stroke_patient_schema.StrokePatientCreate):
    """Create"""
    db_data = StrokePatient(**create_data.model_dump(exclude_unset=True))
    db.add(db_data)
    db.commit()
    db.refresh(db_data)
    return db_data

def get_stroke_patient(db: Session, id: int):
    """Read (by id)"""
    return db.query(StrokePatient).filter(StrokePatient.id == id).first()

def get_stroke_patients(db: Session, skip: int = 0, limit: int = 100):
    """Read all"""
    return db.query(StrokePatient).offset(skip).limit(limit).all()

def update_stroke_patient(db: Session, id: int, model_update: stroke_patient_schema.StrokePatientUpdate):
    """Update"""
    db_data = db.query(StrokePatient).filter(StrokePatient.id == id).first()
    if not db_data:
        return None
    update_data = model_update.model_dump(exclude_unset=True)
    for key, value in update_data.items():
        setattr(db_data, key, value)
    db.commit()
    db.refresh(db_data)
    return db_data

def delete_stroke_patient(db: Session, id: int):
    """Delete"""
    db_data = db.query(StrokePatient).filter(StrokePatient.id == id).first()
    if not db_data:
        return None
    db.delete(db_data)
    db.commit()
    return db_data
