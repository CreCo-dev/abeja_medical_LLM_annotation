from sqlalchemy import Column, Integer, String, Date, Time, Float, DateTime, ForeignKey, UniqueConstraint
from sqlalchemy.orm import relationship
from app.db.database import Base, engine


# 登録タイプ
class RegisteredType:
    LLM = "LLMが生成した初期データ"
    MAIN = "主担当アノテーター"
    SUB = "副担当アノテーター"
    CHK = "Check者のデータ"


# 脳卒中患者
class StrokePatient(Base):
    __tablename__ = "stroke_patients"
    __table_args__ = (
        # karte_id + registered_type の組み合わせをユニークにする
        UniqueConstraint("karte_id", "registered_type", name="uq_stroke_patients_karte_id_registered_type"),
        {"info": {"ja_name": "脳卒中患者"}},  # ← テーブル和名
    )

    id = Column(Integer, primary_key=True, index=True, info={"ja_name": "ID"})
    karte_id = Column(Integer, ForeignKey("kartes.id"), nullable=False, info={"ja_name": "カルテID"})
    registered_type = Column(String(10), nullable=False, info={"ja_name": "登録タイプ"})
    registered_at = Column(DateTime, nullable=False, info={"ja_name": "登録日"})
    registered_by = Column(Integer, ForeignKey("user_accounts.id"), nullable=False, info={"ja_name": "登録者"})

    # ---------------- 患者情報 ----------------
    age = Column(Integer, info={"ja_name": "年齢"})
    sex = Column(Integer, info={"ja_name": "性別"})

    # ---------------- 入院基本情報 ----------------
    sitename = Column(String(255), info={"ja_name": "病院名"})
    onset_dt = Column(Date, info={"ja_name": "発症日"})
    onset_tm = Column(Time, info={"ja_name": "発症時間"})
    arrival_tm = Column(Integer, info={"ja_name": "来院時間"})
    admit_dt = Column(Date, info={"ja_name": "入院日"})
    admit_proc = Column(Integer, info={"ja_name": "入院手順"})
    admit_route = Column(Integer, info={"ja_name": "入院経路"})

    # ---------------- 診断情報 ----------------
    diagnosis = Column(Integer, info={"ja_name": "主病名"})
    duration = Column(String(20), info={"ja_name": "持続時間"})
    subtype = Column(Integer, info={"ja_name": "臨床病型"})
    location = Column(String(255), info={"ja_name": "部位"})
    culprit = Column(String(255), info={"ja_name": "責任病巣"})
    culprit_ves = Column(String(255), info={"ja_name": "責任血管"})
    emb_source = Column(String(255), info={"ja_name": "塞栓源"})
    symptom = Column(String(1000), info={"ja_name": "臨床症状"})

    # ---------------- 危険因子情報 ----------------
    rf_smoking = Column(Integer, info={"ja_name": "喫煙"})
    rf_alcohol = Column(Integer, info={"ja_name": "飲酒"})
    rf_allergy = Column(Integer, info={"ja_name": "アレルギー"})
    rf_ht = Column(Integer, info={"ja_name": "高血圧"})
    rf_dm = Column(Integer, info={"ja_name": "糖尿病"})
    rf_dl = Column(Integer, info={"ja_name": "脂質異常症"})
    rf_dialysis = Column(Integer, info={"ja_name": "透析"})
    rf_af = Column(Integer, info={"ja_name": "心房細動"})
    rf_renal = Column(Integer, info={"ja_name": "腎不全"})
    mh_stroke = Column(Integer, info={"ja_name": "脳卒中既往"})
    mh_dementia = Column(Integer, info={"ja_name": "認知症"})
    mh_ihd = Column(Integer, info={"ja_name": "虚血性心疾患"})
    pre_mrs = Column(Integer, info={"ja_name": "発症前mRS"})

    # ---------------- 現病歴・現症情報 ----------------
    chief_comp = Column(String(255), info={"ja_name": "主訴"})
    present_ill = Column(String(2000), info={"ja_name": "現病歴"})
    hgt = Column(Float, info={"ja_name": "身長(cm)"})
    wgt = Column(Float, info={"ja_name": "体重(kg)"})
    abd_cir = Column(Float, info={"ja_name": "腹囲(cm)"})
    bp = Column(String(20), info={"ja_name": "血圧(mmHg)"})
    sbp = Column(Integer, info={"ja_name": "収縮期血圧"})
    dbp = Column(Integer, info={"ja_name": "拡張期血圧"})
    pulse = Column(Integer, info={"ja_name": "脈拍(回/分)"})
    murmur = Column(Integer, info={"ja_name": "雑音"})
    conscious = Column(Integer, info={"ja_name": "意識"})
    cortical = Column(Integer, info={"ja_name": "皮質症状"})
    motor_dis = Column(Integer, info={"ja_name": "運動障害"})
    sensory_dis = Column(Integer, info={"ja_name": "感覚障害"})
    nihss = Column(Integer, info={"ja_name": "NIHSS"})

    # ---------------- 採血検査情報 ----------------
    lab_cbc = Column(String(255), info={"ja_name": "CBC"})
    lab_chem = Column(String(255), info={"ja_name": "生化学一般"})
    lab_ddimer = Column(Float, info={"ja_name": "D-dimer"})
    lab_hscrp = Column(Float, info={"ja_name": "高感度CRP"})

    # ---------------- 画像検査情報 ----------------
    img_ct = Column(Integer, info={"ja_name": "CT"})
    img_mri = Column(Integer, info={"ja_name": "MRI"})
    img_mra = Column(Integer, info={"ja_name": "MRA"})
    img_spect = Column(Integer, info={"ja_name": "SPECT"})
    img_echo = Column(String(255), info={"ja_name": "エコーの所見等"})

    # ---------------- 治療情報 ----------------
    reperfusion = Column(Integer, info={"ja_name": "再灌流療法"})
    rtpa = Column(Integer, info={"ja_name": "t-PA"})
    evt = Column(Integer, info={"ja_name": "血栓回収療法"})

    pre_at = Column(Integer, info={"ja_name": "入院前の抗血栓療法"})
    pre_ap = Column(Integer, info={"ja_name": "入院前の抗血小板療法"})
    pre_ac = Column(Integer, info={"ja_name": "入院前の抗凝固療法"})
    in_at = Column(Integer, info={"ja_name": "入院中の抗血栓療法"})
    in_ap = Column(Integer, info={"ja_name": "入院中の抗血小板療法"})
    in_ac = Column(Integer, info={"ja_name": "入院中の抗凝固療法"})
    anti_ht_tx = Column(Integer, info={"ja_name": "降圧治療"})
    # ---------------- 入院後経過情報 ----------------
    progress = Column(String(2000), info={"ja_name": "経過"})
    recur = Column(Integer, info={"ja_name": "再発や増悪"})
    cv_event = Column(Integer, info={"ja_name": "心血管イベントの有無"})
    complication = Column(Integer, info={"ja_name": "合併症の有無"})

    # ---------------- 退院時情報 ----------------
    dc_outcome = Column(Integer, info={"ja_name": "退院時転帰"})
    dc_nihss = Column(Integer, info={"ja_name": "退院時NIHSS"})
    dc_mrs = Column(Integer, info={"ja_name": "退院時mRS"})
    dc_dt = Column(Date, info={"ja_name": "退院日"})
    dc_med = Column(String(1000), info={"ja_name": "退院時処方"})

    # ---------------- 退院後経過情報 ----------------
    fu_mrs = Column(Integer, info={"ja_name": "追跡時点でのmRS "})
    fu_recur = Column(Integer, info={"ja_name": "再発"})
    fu_cvevent = Column(Integer, info={"ja_name": "心血管イベント"})
    fu_death = Column(Integer, info={"ja_name": "死亡の有無"})

    # ---------------- リレーション ----------------
    karte = relationship("Karte", back_populates="stroke_patients")
    user = relationship("UserAccount", backref="stroke_patients")


Base.metadata.create_all(bind=engine)
print("[DB INIT] stroke_patients created.", flush=True)
