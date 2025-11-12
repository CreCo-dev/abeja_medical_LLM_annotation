from sqlalchemy.orm import Session

from app.db.entities.karte import Karte
from app.schemas import karte_schema

def create_karte(db: Session, create_data: karte_schema.KarteCreate):
    """Create"""
    db_data = Karte(**create_data.model_dump(exclude_unset=True))
    db.add(db_data)
    db.commit()
    db.refresh(db_data)
    return db_data

def get_karte(db: Session, id: int):
    """Read (by id)"""
    return db.query(Karte).filter(Karte.id == id).first()

def get_kartes(db: Session, skip: int = 0, limit: int = 100):
    """Read all"""
    return db.query(Karte).offset(skip).limit(limit).all()

def update_karte(db: Session, id: int, model_update: karte_schema.KarteUpdate):
    """Update"""
    db_data = db.query(Karte).filter(Karte.id == id).first()
    if not db_data:
        return None
    update_data = model_update.model_dump(exclude_unset=True)
    for key, value in update_data.items():
        setattr(db_data, key, value)
    db.commit()
    db.refresh(db_data)
    return db_data

def delete_karte(db: Session, id: int):
    """Delete"""
    db_data = db.query(Karte).filter(Karte.id == id).first()
    if not db_data:
        return None
    db.delete(db_data)
    db.commit()
    return db_data
