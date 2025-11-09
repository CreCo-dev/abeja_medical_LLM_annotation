from sqlalchemy import Column, Integer, String, Date, Time, Float, DateTime, ForeignKey, UniqueConstraint
from sqlalchemy.orm import relationship
from app.db.database import Base, engine

# 登録タイプ
class RegisteredType:
    LLM = "LLMが生成した初期データ"
    MAIN = "主担当アノテーター"
    SUB = "副担当アノテーター"
    CHK = "Check者のデータ"

#脳卒中患者
class StrokePatient(Base):
    __tablename__ = "stroke_patients"
    __table_args__ = (
        # karte_id + registered_type の組み合わせをユニークにする
        UniqueConstraint("karte_id", "registered_type", name="uq_stroke_patients_karte_id_registered_type"),
    )

    # ID
    id = Column(Integer, primary_key=True, index=True)
    # カルテID
    karte_id = Column(String(50), ForeignKey("kartes.karte_id"), nullable=False)
    # 登録タイプ
    registered_type = Column(String(10), nullable=False)
    # 登録日
    registered_at = Column(DateTime, nullable=False)
    # 登録者 (user_accounts.id)
    registered_by = Column(Integer, ForeignKey("user_accounts.id"), nullable=False)
    # ---------------- 患者情報 ----------------
    # 年齢
    age = Column(Integer)
    # 性別
    sex = Column(Integer)
    # ---------------- 入院基本情報 ----------------
    # 病院名
    sitename = Column(String(255))
    # 発症日
    onset_dt = Column(Date)
    # 発症時間
    onset_tm = Column(Time)
    # 来院時間
    arrival_tm = Column(Integer)
    # 入院日
    admit_dt = Column(Date)
    # 入院手順
    admit_proc = Column(Integer)
    # 入院経路
    admit_route = Column(Integer)
    # ---------------- 診断情報 ----------------
    # 主病名
    diagnosis = Column(Integer)
    # 持続時間
    duration = Column(String(20))
    # 臨床病型
    subtype = Column(Integer)
    # 部位
    location = Column(String(255))
    # 責任病巣
    culprit = Column(String(255))
    # 責任血管
    culprit_ves = Column(String(255))
    # 塞栓源
    emb_source = Column(String(255))
    # 臨床症状
    symptom = Column(String(1000))
    # ---------------- 危険因子情報 ----------------
    # 喫煙
    rf_smoking = Column(Integer)
    # 飲酒
    rf_alcohol = Column(Integer)
    # アレルギー
    rf_allergy = Column(Integer)
    # 高血圧
    rf_ht = Column(Integer)
    # 糖尿病
    rf_dm = Column(Integer)
    # 脂質異常症
    rf_dl = Column(Integer)
    # 透析
    rf_dialysis = Column(Integer)
    # 心房細動
    rf_af = Column(Integer)
    # 腎不全
    rf_renal = Column(Integer)
    # 脳卒中既往
    mh_stroke = Column(Integer)
    # 認知症
    mh_dementia = Column(Integer)
    # 虚血性心疾患
    mh_ihd = Column(Integer)
    # 発症前mRS
    pre_mrs = Column(Integer)
    # ---------------- 現病歴・現症情報 ----------------
    # 主訴
    chief_comp = Column(String(255))
    # 現病歴
    present_ill = Column(String(2000))
    # 身長(cm)
    hgt = Column(Float)
    # 体重(kg)
    wgt = Column(Float)
    # 腹囲(cm)
    abd_cir = Column(Float)
    # 血圧(mmHg)
    bp = Column(String(20))
    # 血圧(mmHg)
    sbp = Column(Integer)
    # 血圧(mmHg)
    dbp = Column(Integer)
    # 脈拍(回/分)
    pulse = Column(Integer)
    # 雑音
    murmur = Column(Integer)
    # 意識
    conscious = Column(Integer)
    # 皮質症状
    cortical = Column(Integer)
    # 運動障害
    motor_dis = Column(Integer)
    # 感覚障害
    sensory_dis = Column(Integer)
    # NIHSS
    nihss = Column(Integer)
    # ---------------- 採血検査情報 ----------------
    # CBC
    lab_cbc = Column(String(255))
    # 生化学一般
    lab_chem = Column(String(255))
    # D-dimer
    lab_ddimer = Column(Float)
    # 高感度CRP
    lab_hscrp = Column(Float)
    # ---------------- 画像検査情報 ----------------
    # CT
    img_ct = Column(Integer)
    # MRI
    img_mri = Column(Integer)
    # MRA
    img_mra = Column(Integer)
    # SPECT
    img_spect = Column(Integer)
    # エコーの所見等
    img_echo = Column(String(255))
    # ---------------- 治療情報 ----------------
    # 再灌流療法
    reperfusion = Column(Integer)
    # t-PA
    rtpa = Column(Integer)
    # 血栓回収療法
    evt = Column(Integer)
    # 入院前の抗血栓療法
    pre_at = Column(Integer)
    # 入院前の抗血小板療法
    pre_ap = Column(Integer)
    # 入院前の抗凝固療法
    pre_ac = Column(Integer)
    # 入院中の抗血栓療法
    in_at = Column(Integer)
    # 入院中の抗血小板療法
    in_ap = Column(Integer)
    # 入院中の抗凝固療法
    in_ac = Column(Integer)
    # 降圧治療
    anti_ht_tx = Column(Integer)
    # ---------------- 入院後経過情報 ----------------
    # 経過
    progress = Column(String(2000))
    # 再発や増悪
    recur = Column(Integer)
    # 心血管イベントの有無
    cv_event = Column(Integer)
    # 合併症の有無
    complication = Column(Integer)
    # ---------------- 退院時情報 ----------------
    # 退院時転帰
    dc_outcome = Column(Integer)
    # 退院時NIHSS
    dc_nihss = Column(Integer)
    # 退院時mRS
    dc_mrs = Column(Integer)
    # 退院日
    dc_dt = Column(Date)
    # 退院時処方
    dc_med = Column(String(1000))
    # ---------------- 退院後経過情報 ----------------
    # 追跡時点でのmRS
    fu_mrs = Column(Integer)
    # 再発
    fu_recur = Column(Integer)
    # 心血管イベント
    fu_cvevent = Column(Integer)
    # 死亡の有無
    fu_death = Column(Integer)
    # ---------------- リレーション ----------------
    karte = relationship("Karte", back_populates="stroke_patients")
    user = relationship("UserAccount", backref="stroke_patients")

Base.metadata.create_all(bind=engine)
print("[DB INIT] stroke_patients created.", flush=True)
