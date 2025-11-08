from sqlalchemy import Column, Integer, String, Enum
from sqlalchemy.orm import relationship
from db.database import Base, engine

class DataType:
    DC = "退院時サマリー"
    STR = "脳卒中患者"

#カルテ
class Karte(Base):
    __tablename__ = "kartes"

    # ID
    id = Column(Integer, primary_key=True, index=True)
    # カルテID
    karte_id = Column(String(50), unique=True, nullable=False)
    # カルテ名
    karte_name = Column(String(255), nullable=False)
    # データタイプ (退院時サマリー / 脳卒中患者)
    data_type = Column(String(20), nullable=False)
    # ステータス
    status = Column(String(50))

    # リレーション
    discharge_summaries = relationship("DischargeSummary", back_populates="karte")
    stroke_patients = relationship("StrokePatient", back_populates="karte")

Base.metadata.create_all(bind=engine)
print("[DB INIT] kartes created.", flush=True)
