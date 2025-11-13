from sqlalchemy import Column, Integer, String, DateTime, Text, ForeignKey, UniqueConstraint
from sqlalchemy.orm import relationship
from app.db.database import Base, engine

# 登録タイプ
class RegisteredType:
    LLM = "LLMが生成した初期データ"
    MAIN = "主担当アノテーター"
    SUB = "副担当アノテーター"
    CHK = "Check者のデータ"


# 退院時サマリ
class DischargeSummary(Base):
    __tablename__ = "discharge_summaries"
    __table_args__ = (
        # karte_id + registered_type の組み合わせをユニークにする
        UniqueConstraint("karte_id", "registered_type", name="uq_discharge_summary_karte_id_registered_type"),
        {"info": {"ja_name": "退院時サマリー"}},
    )

    id = Column(Integer, primary_key=True, index=True, info={"ja_name": "ID"})
    karte_id = Column(Integer, ForeignKey("kartes.id"), nullable=False, info={"ja_name": "カルテID"})
    registered_type = Column(String(10), nullable=False, info={"ja_name": "登録タイプ"})
    registered_at = Column(DateTime, nullable=False, info={"ja_name": "登録日"})
    registered_by = Column(Integer, ForeignKey("user_accounts.id"), nullable=False, info={"ja_name": "登録者"})

    # ---------------- 患者情報 ----------------
    patient_name = Column(String(512), nullable=False, info={"ja_name": "患者名"})
    patient_id = Column(String(50), nullable=False, info={"ja_name": "患者ID"})

    # ---------------- 退院時サマリ ----------------
    taiin_summary_answerable = Column(Integer, info={"ja_name": "退院時サマリ_回答可否"})
    main_disease_1 = Column(String(512), info={"ja_name": "主病名及び副病名1"})
    main_disease_2 = Column(String(512), info={"ja_name": "主病名及び副病名2"})
    main_disease_3 = Column(String(512), info={"ja_name": "主病名及び副病名3"})
    main_disease_4 = Column(String(512), info={"ja_name": "主病名及び副病名4"})
    main_disease_5 = Column(String(512), info={"ja_name": "主病名及び副病名5"})
    surgery_1 = Column(String(256), info={"ja_name": "手術1"})
    surgery_2 = Column(String(256), info={"ja_name": "手術2"})
    surgery_3 = Column(String(256), info={"ja_name": "手術3"})
    chief_complaint = Column(String(256), info={"ja_name": "主訴"})
    present_illness = Column(String(256), info={"ja_name": "現病歴"})
    past_history = Column(String(256), info={"ja_name": "既往歴"})
    family_history = Column(String(256), info={"ja_name": "家族歴"})
    life_history = Column(String(256), info={"ja_name": "生活歴"})
    main_condition = Column(String(256), info={"ja_name": "主な入退院時現症"})
    main_exam_finding = Column(String(256), info={"ja_name": "主な検査所見"})
    problem_list = Column(String(256), info={"ja_name": "問題リスト"})
    hospital_course = Column(String(256), info={"ja_name": "入院後経過"})
    prescription = Column(String(256), info={"ja_name": "処方内容"})
    future_plan = Column(String(256), info={"ja_name": "今後の治療方針"})
    comment = Column(String(256), info={"ja_name": "コメント"})

    # ---------------- 診療情報提供書 ----------------
    referral_answerable = Column(Integer, info={"ja_name": "診療情報提供書_回答可否"})
    condition_1 = Column(Text, info={"ja_name": "状況設定1"})
    disease_1 = Column(String(256), info={"ja_name": "傷病名1"})
    purpose_1 = Column(String(256), info={"ja_name": "紹介目的1"})
    past_family_1 = Column(String(256), info={"ja_name": "既往歴及び家族歴1"})
    course_exam_1 = Column(String(256), info={"ja_name": "症状経過及び検査結果1"})
    treatment_1 = Column(String(256), info={"ja_name": "治療経過1"})
    current_med_1 = Column(String(256), info={"ja_name": "現在の処方1"})
    note_1 = Column(String(256), info={"ja_name": "備考1"})
    annotation_comment_1 = Column(String(256), info={"ja_name": "コメント1"})
    condition_2 = Column(Text, info={"ja_name": "状況設定2"})
    disease_2 = Column(String(256), info={"ja_name": "傷病名2"})
    purpose_2 = Column(String(256), info={"ja_name": "紹介目的2"})
    past_family_2 = Column(String(256), info={"ja_name": "既往歴及び家族歴2"})
    course_exam_2 = Column(String(256), info={"ja_name": "症状経過及び検査結果2"})
    treatment_2 = Column(String(256), info={"ja_name": "治療経過2"})
    current_med_2 = Column(String(256), info={"ja_name": "現在の処方2"})
    note_2 = Column(String(256), info={"ja_name": "備考2"})
    annotation_comment_2 = Column(String(256), info={"ja_name": "コメント2"})
    condition_3 = Column(Text, info={"ja_name": "状況設定3"})
    disease_3 = Column(String(256), info={"ja_name": "傷病名3"})
    purpose_3 = Column(String(256), info={"ja_name": "紹介目的3"})
    past_family_3 = Column(String(256), info={"ja_name": "既往歴及び家族歴3"})
    course_exam_3 = Column(String(256), info={"ja_name": "症状経過及び検査結果3"})
    treatment_3 = Column(String(256), info={"ja_name": "治療経過3"})
    current_med_3 = Column(String(256), info={"ja_name": "現在の処方3"})
    note_3 = Column(String(256), info={"ja_name": "備考3"})
    annotation_comment_3 = Column(String(256), info={"ja_name": "コメント3"})
    condition_4 = Column(Text, info={"ja_name": "状況設定4"})
    disease_4 = Column(String(256), info={"ja_name": "傷病名4"})
    purpose_4 = Column(String(256), info={"ja_name": "紹介目的4"})
    past_family_4 = Column(String(256), info={"ja_name": "既往歴及び家族歴4"})
    course_exam_4 = Column(String(256), info={"ja_name": "症状経過及び検査結果4"})
    treatment_4 = Column(String(256), info={"ja_name": "治療経過4"})
    current_med_4 = Column(String(256), info={"ja_name": "現在の処方4"})
    note_4 = Column(String(256), info={"ja_name": "備考4"})
    annotation_comment_4 = Column(String(256), info={"ja_name": "コメント4"})

    # リレーション
    karte = relationship("Karte", back_populates="discharge_summaries")
    user = relationship("UserAccount", backref="discharge_summaries")

Base.metadata.create_all(bind=engine)
print("[DB INIT] discharge_summaries created.", flush=True)


