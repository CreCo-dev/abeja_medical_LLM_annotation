from sqlalchemy.orm import Session
from app.db.entities.discharge_summary import DischargeSummary
from app.schemas import discharge_summary_schema

# Create
def create_discharge_summary(db: Session, summary: discharge_summary_schema.DischargeSummaryCreate):
    db_summary = DischargeSummary(**summary.model_dump(exclude_unset=True))
    db.add(db_summary)
    db.commit()
    db.refresh(db_summary)
    return db_summary

# Read (by id)
def get_discharge_summary(db: Session, id: int):
    return db.query(DischargeSummary).filter(DischargeSummary.id == id).first()

# Read all
def get_discharge_summaries(db: Session, skip: int = 0, limit: int = 100):
    return db.query(DischargeSummary).offset(skip).limit(limit).all()

# Update
def update_discharge_summary(db: Session, id: int, summary_update: discharge_summary_schema.DischargeSummaryUpdate):
    db_summary = db.query(DischargeSummary).filter(DischargeSummary.id == id).first()
    if not db_summary:
        return None
    update_data = summary_update.model_dump(exclude_unset=True)
    for key, value in update_data.items():
        setattr(db_summary, key, value)
    db.commit()
    db.refresh(db_summary)
    return db_summary

# Delete
def delete_discharge_summary(db: Session, id: int):
    db_summary = db.query(DischargeSummary).filter(DischargeSummary.id == id).first()
    if not db_summary:
        return None
    db.delete(db_summary)
    db.commit()
    return db_summary
