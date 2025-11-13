## カルテ (`kartes`)

| 物理名 | 型 | Not Null | 和名 | 説明 |
|---|---|:--:|---|---|
| `id` | INTEGER | Y | ID | 主キー |
| `karte_data_id` | VARCHAR(50) | Y | カルテID | 一意制約 |
| `karte_name` | VARCHAR(255) | Y | カルテ名 |  |
| `data_type` | VARCHAR(20) | Y | データタイプ |  |
| `status` | VARCHAR(50) |  | ステータス |  |

## 退院時サマリー (`discharge_summaries`)

**一意制約(複合)**
- `karte_id`, `registered_type`

**リレーション**
- `karte_id` → `kartes`.`id`
- `registered_by` → `user_accounts`.`id`

| 物理名 | 型 | Not Null | 和名 | 説明 |
|---|---|:--:|---|---|
| `id` | INTEGER | Y | ID | 主キー |
| `karte_id` | INTEGER | Y | カルテID | 外部キー(kartes.id) |
| `registered_type` | VARCHAR(10) | Y | 登録タイプ |  |
| `registered_at` | DATETIME | Y | 登録日 |  |
| `registered_by` | INTEGER | Y | 登録者 | 外部キー(user_accounts.id) |
| `patient_name` | VARCHAR(512) | Y | 患者名 |  |
| `patient_id` | VARCHAR(50) | Y | 患者ID |  |
| `taiin_summary_answerable` | INTEGER |  | 退院時サマリ_回答可否 |  |
| `main_disease_1` | VARCHAR(512) |  | 主病名及び副病名1 |  |
| `main_disease_2` | VARCHAR(512) |  | 主病名及び副病名2 |  |
| `main_disease_3` | VARCHAR(512) |  | 主病名及び副病名3 |  |
| `main_disease_4` | VARCHAR(512) |  | 主病名及び副病名4 |  |
| `main_disease_5` | VARCHAR(512) |  | 主病名及び副病名5 |  |
| `surgery_1` | VARCHAR(256) |  | 手術1 |  |
| `surgery_2` | VARCHAR(256) |  | 手術2 |  |
| `surgery_3` | VARCHAR(256) |  | 手術3 |  |
| `chief_complaint` | VARCHAR(256) |  | 主訴 |  |
| `present_illness` | VARCHAR(256) |  | 現病歴 |  |
| `past_history` | VARCHAR(256) |  | 既往歴 |  |
| `family_history` | VARCHAR(256) |  | 家族歴 |  |
| `life_history` | VARCHAR(256) |  | 生活歴 |  |
| `main_condition` | VARCHAR(256) |  | 主な入退院時現症 |  |
| `main_exam_finding` | VARCHAR(256) |  | 主な検査所見 |  |
| `problem_list` | VARCHAR(256) |  | 問題リスト |  |
| `hospital_course` | VARCHAR(256) |  | 入院後経過 |  |
| `prescription` | VARCHAR(256) |  | 処方内容 |  |
| `future_plan` | VARCHAR(256) |  | 今後の治療方針 |  |
| `comment` | VARCHAR(256) |  | コメント |  |
| `referral_answerable` | INTEGER |  | 診療情報提供書_回答可否 |  |
| `condition_1` | TEXT |  | 状況設定1 |  |
| `disease_1` | VARCHAR(256) |  | 傷病名1 |  |
| `purpose_1` | VARCHAR(256) |  | 紹介目的1 |  |
| `past_family_1` | VARCHAR(256) |  | 既往歴及び家族歴1 |  |
| `course_exam_1` | VARCHAR(256) |  | 症状経過及び検査結果1 |  |
| `treatment_1` | VARCHAR(256) |  | 治療経過1 |  |
| `current_med_1` | VARCHAR(256) |  | 現在の処方1 |  |
| `note_1` | VARCHAR(256) |  | 備考1 |  |
| `annotation_comment_1` | VARCHAR(256) |  | コメント1 |  |
| `condition_2` | TEXT |  | 状況設定2 |  |
| `disease_2` | VARCHAR(256) |  | 傷病名2 |  |
| `purpose_2` | VARCHAR(256) |  | 紹介目的2 |  |
| `past_family_2` | VARCHAR(256) |  | 既往歴及び家族歴2 |  |
| `course_exam_2` | VARCHAR(256) |  | 症状経過及び検査結果2 |  |
| `treatment_2` | VARCHAR(256) |  | 治療経過2 |  |
| `current_med_2` | VARCHAR(256) |  | 現在の処方2 |  |
| `note_2` | VARCHAR(256) |  | 備考2 |  |
| `annotation_comment_2` | VARCHAR(256) |  | コメント2 |  |
| `condition_3` | TEXT |  | 状況設定3 |  |
| `disease_3` | VARCHAR(256) |  | 傷病名3 |  |
| `purpose_3` | VARCHAR(256) |  | 紹介目的3 |  |
| `past_family_3` | VARCHAR(256) |  | 既往歴及び家族歴3 |  |
| `course_exam_3` | VARCHAR(256) |  | 症状経過及び検査結果3 |  |
| `treatment_3` | VARCHAR(256) |  | 治療経過3 |  |
| `current_med_3` | VARCHAR(256) |  | 現在の処方3 |  |
| `note_3` | VARCHAR(256) |  | 備考3 |  |
| `annotation_comment_3` | VARCHAR(256) |  | コメント3 |  |
| `condition_4` | TEXT |  | 状況設定4 |  |
| `disease_4` | VARCHAR(256) |  | 傷病名4 |  |
| `purpose_4` | VARCHAR(256) |  | 紹介目的4 |  |
| `past_family_4` | VARCHAR(256) |  | 既往歴及び家族歴4 |  |
| `course_exam_4` | VARCHAR(256) |  | 症状経過及び検査結果4 |  |
| `treatment_4` | VARCHAR(256) |  | 治療経過4 |  |
| `current_med_4` | VARCHAR(256) |  | 現在の処方4 |  |
| `note_4` | VARCHAR(256) |  | 備考4 |  |
| `annotation_comment_4` | VARCHAR(256) |  | コメント4 |  |

## 脳卒中患者 (`stroke_patients`)

**一意制約(複合)**
- `karte_id`, `registered_type`

**リレーション**
- `registered_by` → `user_accounts`.`id`
- `karte_id` → `kartes`.`id`

| 物理名 | 型 | Not Null | 和名 | 説明 |
|---|---|:--:|---|---|
| `id` | INTEGER | Y | ID | 主キー |
| `karte_id` | INTEGER | Y | カルテID | 外部キー(kartes.id) |
| `registered_type` | VARCHAR(10) | Y | 登録タイプ |  |
| `registered_at` | DATETIME | Y | 登録日 |  |
| `registered_by` | INTEGER | Y | 登録者 | 外部キー(user_accounts.id) |
| `age` | INTEGER |  | 年齢 |  |
| `sex` | INTEGER |  | 性別 |  |
| `sitename` | VARCHAR(255) |  | 病院名 |  |
| `onset_dt` | DATE |  | 発症日 |  |
| `onset_tm` | TIME |  | 発症時間 |  |
| `arrival_tm` | INTEGER |  | 来院時間 |  |
| `admit_dt` | DATE |  | 入院日 |  |
| `admit_proc` | INTEGER |  | 入院手順 |  |
| `admit_route` | INTEGER |  | 入院経路 |  |
| `diagnosis` | INTEGER |  | 主病名 |  |
| `duration` | VARCHAR(20) |  | 持続時間 |  |
| `subtype` | INTEGER |  | 臨床病型 |  |
| `location` | VARCHAR(255) |  | 部位 |  |
| `culprit` | VARCHAR(255) |  | 責任病巣 |  |
| `culprit_ves` | VARCHAR(255) |  | 責任血管 |  |
| `emb_source` | VARCHAR(255) |  | 塞栓源 |  |
| `symptom` | VARCHAR(1000) |  | 臨床症状 |  |
| `rf_smoking` | INTEGER |  | 喫煙 |  |
| `rf_alcohol` | INTEGER |  | 飲酒 |  |
| `rf_allergy` | INTEGER |  | アレルギー |  |
| `rf_ht` | INTEGER |  | 高血圧 |  |
| `rf_dm` | INTEGER |  | 糖尿病 |  |
| `rf_dl` | INTEGER |  | 脂質異常症 |  |
| `rf_dialysis` | INTEGER |  | 透析 |  |
| `rf_af` | INTEGER |  | 心房細動 |  |
| `rf_renal` | INTEGER |  | 腎不全 |  |
| `mh_stroke` | INTEGER |  | 脳卒中既往 |  |
| `mh_dementia` | INTEGER |  | 認知症 |  |
| `mh_ihd` | INTEGER |  | 虚血性心疾患 |  |
| `pre_mrs` | INTEGER |  | 発症前mRS |  |
| `chief_comp` | VARCHAR(255) |  | 主訴 |  |
| `present_ill` | VARCHAR(2000) |  | 現病歴 |  |
| `hgt` | FLOAT |  | 身長(cm) |  |
| `wgt` | FLOAT |  | 体重(kg) |  |
| `abd_cir` | FLOAT |  | 腹囲(cm) |  |
| `bp` | VARCHAR(20) |  | 血圧(mmHg) |  |
| `sbp` | INTEGER |  | 収縮期血圧 |  |
| `dbp` | INTEGER |  | 拡張期血圧 |  |
| `pulse` | INTEGER |  | 脈拍(回/分) |  |
| `murmur` | INTEGER |  | 雑音 |  |
| `conscious` | INTEGER |  | 意識 |  |
| `cortical` | INTEGER |  | 皮質症状 |  |
| `motor_dis` | INTEGER |  | 運動障害 |  |
| `sensory_dis` | INTEGER |  | 感覚障害 |  |
| `nihss` | INTEGER |  | NIHSS |  |
| `lab_cbc` | VARCHAR(255) |  | CBC |  |
| `lab_chem` | VARCHAR(255) |  | 生化学一般 |  |
| `lab_ddimer` | FLOAT |  | D-dimer |  |
| `lab_hscrp` | FLOAT |  | 高感度CRP |  |
| `img_ct` | INTEGER |  | CT |  |
| `img_mri` | INTEGER |  | MRI |  |
| `img_mra` | INTEGER |  | MRA |  |
| `img_spect` | INTEGER |  | SPECT |  |
| `img_echo` | VARCHAR(255) |  | エコーの所見等 |  |
| `reperfusion` | INTEGER |  | 再灌流療法 |  |
| `rtpa` | INTEGER |  | t-PA |  |
| `evt` | INTEGER |  | 血栓回収療法 |  |
| `pre_at` | INTEGER |  | 入院前の抗血栓療法 |  |
| `pre_ap` | INTEGER |  | 入院前の抗血小板療法 |  |
| `pre_ac` | INTEGER |  | 入院前の抗凝固療法 |  |
| `in_at` | INTEGER |  | 入院中の抗血栓療法 |  |
| `in_ap` | INTEGER |  | 入院中の抗血小板療法 |  |
| `in_ac` | INTEGER |  | 入院中の抗凝固療法 |  |
| `anti_ht_tx` | INTEGER |  | 降圧治療 |  |
| `progress` | VARCHAR(2000) |  | 経過 |  |
| `recur` | INTEGER |  | 再発や増悪 |  |
| `cv_event` | INTEGER |  | 心血管イベントの有無 |  |
| `complication` | INTEGER |  | 合併症の有無 |  |
| `dc_outcome` | INTEGER |  | 退院時転帰 |  |
| `dc_nihss` | INTEGER |  | 退院時NIHSS |  |
| `dc_mrs` | INTEGER |  | 退院時mRS |  |
| `dc_dt` | DATE |  | 退院日 |  |
| `dc_med` | VARCHAR(1000) |  | 退院時処方 |  |
| `fu_mrs` | INTEGER |  | 追跡時点でのmRS  |  |
| `fu_recur` | INTEGER |  | 再発 |  |
| `fu_cvevent` | INTEGER |  | 心血管イベント |  |
| `fu_death` | INTEGER |  | 死亡の有無 |  |

## ユーザーアカウント (`user_accounts`)

| 物理名 | 型 | Not Null | 和名 | 説明 |
|---|---|:--:|---|---|
| `id` | INTEGER | Y | ID | 主キー |
| `login_id` | VARCHAR(50) | Y | ログインID | 一意制約 |
| `password` | VARCHAR(255) | Y | パスワード |  |
| `name` | VARCHAR(50) | Y | 名前 |  |
