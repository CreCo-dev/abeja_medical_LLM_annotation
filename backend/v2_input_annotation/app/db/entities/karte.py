from sqlalchemy import Column, Integer, String
from sqlalchemy.orm import relationship
from app.db.database import Base, engine

class DataType:
    DC = "退院時サマリー"
    STR = "脳卒中患者"

# カルテ
class Karte(Base):
    __tablename__ = "kartes"
    __table_args__ = {"info": {"ja_name": "カルテ"}}

    id = Column(Integer, primary_key=True, index=True, info={"ja_name": "ID"})
    karte_data_id = Column(String(50), unique=True, nullable=False, info={"ja_name": "カルテID"})
    karte_name = Column(String(255), nullable=False, info={"ja_name": "カルテ名"})
    data_type = Column(String(20), nullable=False, info={"ja_name": "データタイプ"})
    status = Column(String(50), info={"ja_name": "ステータス"})

    # リレーション
    discharge_summaries = relationship("DischargeSummary", back_populates="karte")
    stroke_patients = relationship("StrokePatient", back_populates="karte")

Base.metadata.create_all(bind=engine)
print("[DB INIT] kartes created.", flush=True)
