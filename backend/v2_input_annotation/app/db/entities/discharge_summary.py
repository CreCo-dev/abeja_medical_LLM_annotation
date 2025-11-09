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
    # 患者名
    patient_name = Column(String(512), nullable=False)
    # 患者ID
    patient_id = Column(String(50), nullable=False)
    # ---------------- 退院時サマリ ----------------
    # 退院時サマリ_回答可否
    taiin_summary_answerable = Column(Integer)
    # 主病名及び副病名1
    main_disease_1 = Column(String(512))
    # 主病名及び副病名2
    main_disease_2 = Column(String(512))
    # 主病名及び副病名3
    main_disease_3 = Column(String(512))
    # 主病名及び副病名4
    main_disease_4 = Column(String(512))
    # 主病名及び副病名5
    main_disease_5 = Column(String(512))
    # 手術1
    surgery_1 = Column(String(256))
    # 手術2
    surgery_2 = Column(String(256))
    # 手術3
    surgery_3 = Column(String(256))
    # 主訴
    chief_complaint = Column(String(256))
    # 現病歴
    present_illness = Column(String(256))
    # 既往歴
    past_history = Column(String(256))
    # 家族歴
    family_history = Column(String(256))
    # 生活歴
    life_history = Column(String(256))
    # 主な入退院時現症
    main_condition = Column(String(256))
    # 主な検査所見
    main_exam_finding = Column(String(256))
    # 問題リスト
    problem_list = Column(String(256))
    # 入院後経過
    hospital_course = Column(String(256))
    # 処方内容
    prescription = Column(String(256))
    # 今後の治療方針
    future_plan = Column(String(256))
    # コメント
    comment = Column(String(256))
    # ---------------- 診療情報提供書 ----------------
    # 診療情報提供書_回答可否
    referral_answerable = Column(Integer)
    # 状況設定1
    condition_1 = Column(Text)
    # 傷病名1
    disease_1 = Column(String(256))
    # 紹介目的1
    purpose_1 = Column(String(256))
    # 既往歴及び家族歴1
    past_family_1 = Column(String(256))
    # 症状経過及び検査結果1
    course_exam_1 = Column(String(256))
    # 治療経過1
    treatment_1 = Column(String(256))
    # 現在の処方1
    current_med_1 = Column(String(256))
    # 備考1
    note_1 = Column(String(256))
    # コメント1
    annotation_comment_1 = Column(String(256))
    # 状況設定2
    condition_2 = Column(Text)
    # 傷病名2
    disease_2 = Column(String(256))
    # 紹介目的2
    purpose_2 = Column(String(256))
    # 既往歴及び家族歴2
    past_family_2 = Column(String(256))
    # 症状経過及び検査結果2
    course_exam_2 = Column(String(256))
    # 治療経過2
    treatment_2 = Column(String(256))
    # 現在の処方2
    current_med_2 = Column(String(256))
    # 備考2
    note_2 = Column(String(256))
    # コメント2
    annotation_comment_2 = Column(String(256))
    # 状況設定3
    condition_3 = Column(Text)
    # 傷病名3
    disease_3 = Column(String(256))
    # 紹介目的3
    purpose_3 = Column(String(256))
    # 既往歴及び家族歴3
    past_family_3 = Column(String(256))
    # 症状経過及び検査結果3
    course_exam_3 = Column(String(256))
    # 治療経過3
    treatment_3 = Column(String(256))
    # 現在の処方3
    current_med_3 = Column(String(256))
    # 備考3
    note_3 = Column(String(256))
    # コメント3
    annotation_comment_3 = Column(String(256))
    # 状況設定4
    condition_4 = Column(Text)
    # 傷病名4
    disease_4 = Column(String(256))
    # 紹介目的4
    purpose_4 = Column(String(256))
    # 既往歴及び家族歴4
    past_family_4 = Column(String(256))
    # 症状経過及び検査結果4
    course_exam_4 = Column(String(256))
    # 治療経過4
    treatment_4 = Column(String(256))
    # 現在の処方4
    current_med_4 = Column(String(256))
    # 備考4
    note_4 = Column(String(256))
    # コメント4
    annotation_comment_4 = Column(String(256))


    # リレーション
    karte = relationship("Karte", back_populates="discharge_summaries")
    user = relationship("UserAccount", backref="discharge_summaries")

Base.metadata.create_all(bind=engine)
print("[DB INIT] discharge_summaries created.", flush=True)


