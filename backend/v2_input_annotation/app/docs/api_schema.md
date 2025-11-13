# API 定義書

## GET /


---
## GET /user_accounts


#### Response Model (UserAccount)

| フィールド | 型 | 必須 | 説明 |
|---|---|:--:|---|
| `id` | <class 'int'> | Y |  |
| `login_id` | <class 'str'> | Y |  |
| `name` | <class 'str'> | Y |  |

---
## GET /user_accounts/{account_id}


#### パス・クエリパラメータ

| パラメータ | 型 | 必須 | 説明 |
|---|---|:--:|---|
| `account_id` | None | Y |  |

#### Response Model (UserAccount)

| フィールド | 型 | 必須 | 説明 |
|---|---|:--:|---|
| `id` | <class 'int'> | Y |  |
| `login_id` | <class 'str'> | Y |  |
| `name` | <class 'str'> | Y |  |

---
## POST /user_accounts


#### Response Model (UserAccount)

| フィールド | 型 | 必須 | 説明 |
|---|---|:--:|---|
| `id` | <class 'int'> | Y |  |
| `login_id` | <class 'str'> | Y |  |
| `name` | <class 'str'> | Y |  |

---
## PUT /user_accounts/{account_id}


#### パス・クエリパラメータ

| パラメータ | 型 | 必須 | 説明 |
|---|---|:--:|---|
| `account_id` | None | Y |  |

#### Response Model (UserAccount)

| フィールド | 型 | 必須 | 説明 |
|---|---|:--:|---|
| `id` | <class 'int'> | Y |  |
| `login_id` | <class 'str'> | Y |  |
| `name` | <class 'str'> | Y |  |

---
## DELETE /user_accounts/{account_id}


#### パス・クエリパラメータ

| パラメータ | 型 | 必須 | 説明 |
|---|---|:--:|---|
| `account_id` | None | Y |  |

---
## POST /login

**説明:** ログインID(login_id)とパスワードを受け取り、JWTを返す

#### Response Model (TokenResponse)

| フィールド | 型 | 必須 | 説明 |
|---|---|:--:|---|
| `access_token` | <class 'str'> | Y |  |
| `token_type` | <class 'str'> | Y |  |

---
## GET /user_accounts_with_auth/me

**説明:** ログイン中ユーザーの情報取得

---
## POST /kartes/

**説明:** 新規登録

#### Response Model (KarteResponse)

| フィールド | 型 | 必須 | 説明 |
|---|---|:--:|---|
| `karte_data_id` | <class 'str'> | Y |  |
| `karte_name` | <class 'str'> | Y |  |
| `data_type` | <class 'str'> | Y |  |
| `status` | typing.Optional[str] |  |  |
| `id` | <class 'int'> | Y |  |

---
## GET /kartes/{id}

**説明:** IDで1件取得

#### パス・クエリパラメータ

| パラメータ | 型 | 必須 | 説明 |
|---|---|:--:|---|
| `id` | None | Y |  |

#### Response Model (KarteResponse)

| フィールド | 型 | 必須 | 説明 |
|---|---|:--:|---|
| `karte_data_id` | <class 'str'> | Y |  |
| `karte_name` | <class 'str'> | Y |  |
| `data_type` | <class 'str'> | Y |  |
| `status` | typing.Optional[str] |  |  |
| `id` | <class 'int'> | Y |  |

---
## GET /kartes/

**説明:** 一覧取得

#### パス・クエリパラメータ

| パラメータ | 型 | 必須 | 説明 |
|---|---|:--:|---|
| `skip` | None |  |  |
| `limit` | None |  |  |

#### Response Model (KarteResponse)

| フィールド | 型 | 必須 | 説明 |
|---|---|:--:|---|
| `karte_data_id` | <class 'str'> | Y |  |
| `karte_name` | <class 'str'> | Y |  |
| `data_type` | <class 'str'> | Y |  |
| `status` | typing.Optional[str] |  |  |
| `id` | <class 'int'> | Y |  |

---
## PUT /kartes/{id}

**説明:** 更新

#### パス・クエリパラメータ

| パラメータ | 型 | 必須 | 説明 |
|---|---|:--:|---|
| `id` | None | Y |  |

#### Response Model (KarteResponse)

| フィールド | 型 | 必須 | 説明 |
|---|---|:--:|---|
| `karte_data_id` | <class 'str'> | Y |  |
| `karte_name` | <class 'str'> | Y |  |
| `data_type` | <class 'str'> | Y |  |
| `status` | typing.Optional[str] |  |  |
| `id` | <class 'int'> | Y |  |

---
## DELETE /kartes/{id}

**説明:** 削除

#### パス・クエリパラメータ

| パラメータ | 型 | 必須 | 説明 |
|---|---|:--:|---|
| `id` | None | Y |  |

---
## POST /discharge_summaries/

**説明:** 新規登録

#### Response Model (DischargeSummaryResponse)

| フィールド | 型 | 必須 | 説明 |
|---|---|:--:|---|
| `karte_id` | <class 'int'> | Y |  |
| `registered_type` | <class 'str'> | Y |  |
| `registered_at` | <class 'datetime.datetime'> | Y |  |
| `registered_by` | <class 'int'> | Y |  |
| `patient_name` | <class 'str'> | Y |  |
| `patient_id` | <class 'str'> | Y |  |
| `taiin_summary_answerable` | typing.Optional[int] |  |  |
| `main_disease_1` | typing.Optional[str] |  |  |
| `main_disease_2` | typing.Optional[str] |  |  |
| `main_disease_3` | typing.Optional[str] |  |  |
| `main_disease_4` | typing.Optional[str] |  |  |
| `main_disease_5` | typing.Optional[str] |  |  |
| `surgery_1` | typing.Optional[str] |  |  |
| `surgery_2` | typing.Optional[str] |  |  |
| `surgery_3` | typing.Optional[str] |  |  |
| `chief_complaint` | typing.Optional[str] |  |  |
| `present_illness` | typing.Optional[str] |  |  |
| `past_history` | typing.Optional[str] |  |  |
| `family_history` | typing.Optional[str] |  |  |
| `life_history` | typing.Optional[str] |  |  |
| `main_condition` | typing.Optional[str] |  |  |
| `main_exam_finding` | typing.Optional[str] |  |  |
| `problem_list` | typing.Optional[str] |  |  |
| `hospital_course` | typing.Optional[str] |  |  |
| `prescription` | typing.Optional[str] |  |  |
| `future_plan` | typing.Optional[str] |  |  |
| `comment` | typing.Optional[str] |  |  |
| `referral_answerable` | typing.Optional[int] |  |  |
| `condition_1` | typing.Optional[str] |  |  |
| `disease_1` | typing.Optional[str] |  |  |
| `purpose_1` | typing.Optional[str] |  |  |
| `past_family_1` | typing.Optional[str] |  |  |
| `course_exam_1` | typing.Optional[str] |  |  |
| `treatment_1` | typing.Optional[str] |  |  |
| `current_med_1` | typing.Optional[str] |  |  |
| `note_1` | typing.Optional[str] |  |  |
| `annotation_comment_1` | typing.Optional[str] |  |  |
| `condition_2` | typing.Optional[str] |  |  |
| `disease_2` | typing.Optional[str] |  |  |
| `purpose_2` | typing.Optional[str] |  |  |
| `past_family_2` | typing.Optional[str] |  |  |
| `course_exam_2` | typing.Optional[str] |  |  |
| `treatment_2` | typing.Optional[str] |  |  |
| `current_med_2` | typing.Optional[str] |  |  |
| `note_2` | typing.Optional[str] |  |  |
| `annotation_comment_2` | typing.Optional[str] |  |  |
| `condition_3` | typing.Optional[str] |  |  |
| `disease_3` | typing.Optional[str] |  |  |
| `purpose_3` | typing.Optional[str] |  |  |
| `past_family_3` | typing.Optional[str] |  |  |
| `course_exam_3` | typing.Optional[str] |  |  |
| `treatment_3` | typing.Optional[str] |  |  |
| `current_med_3` | typing.Optional[str] |  |  |
| `note_3` | typing.Optional[str] |  |  |
| `annotation_comment_3` | typing.Optional[str] |  |  |
| `condition_4` | typing.Optional[str] |  |  |
| `disease_4` | typing.Optional[str] |  |  |
| `purpose_4` | typing.Optional[str] |  |  |
| `past_family_4` | typing.Optional[str] |  |  |
| `course_exam_4` | typing.Optional[str] |  |  |
| `treatment_4` | typing.Optional[str] |  |  |
| `current_med_4` | typing.Optional[str] |  |  |
| `note_4` | typing.Optional[str] |  |  |
| `annotation_comment_4` | typing.Optional[str] |  |  |
| `id` | <class 'int'> | Y |  |

---
## GET /discharge_summaries/{id}

**説明:** IDで1件取得

#### パス・クエリパラメータ

| パラメータ | 型 | 必須 | 説明 |
|---|---|:--:|---|
| `id` | None | Y |  |

#### Response Model (DischargeSummaryResponse)

| フィールド | 型 | 必須 | 説明 |
|---|---|:--:|---|
| `karte_id` | <class 'int'> | Y |  |
| `registered_type` | <class 'str'> | Y |  |
| `registered_at` | <class 'datetime.datetime'> | Y |  |
| `registered_by` | <class 'int'> | Y |  |
| `patient_name` | <class 'str'> | Y |  |
| `patient_id` | <class 'str'> | Y |  |
| `taiin_summary_answerable` | typing.Optional[int] |  |  |
| `main_disease_1` | typing.Optional[str] |  |  |
| `main_disease_2` | typing.Optional[str] |  |  |
| `main_disease_3` | typing.Optional[str] |  |  |
| `main_disease_4` | typing.Optional[str] |  |  |
| `main_disease_5` | typing.Optional[str] |  |  |
| `surgery_1` | typing.Optional[str] |  |  |
| `surgery_2` | typing.Optional[str] |  |  |
| `surgery_3` | typing.Optional[str] |  |  |
| `chief_complaint` | typing.Optional[str] |  |  |
| `present_illness` | typing.Optional[str] |  |  |
| `past_history` | typing.Optional[str] |  |  |
| `family_history` | typing.Optional[str] |  |  |
| `life_history` | typing.Optional[str] |  |  |
| `main_condition` | typing.Optional[str] |  |  |
| `main_exam_finding` | typing.Optional[str] |  |  |
| `problem_list` | typing.Optional[str] |  |  |
| `hospital_course` | typing.Optional[str] |  |  |
| `prescription` | typing.Optional[str] |  |  |
| `future_plan` | typing.Optional[str] |  |  |
| `comment` | typing.Optional[str] |  |  |
| `referral_answerable` | typing.Optional[int] |  |  |
| `condition_1` | typing.Optional[str] |  |  |
| `disease_1` | typing.Optional[str] |  |  |
| `purpose_1` | typing.Optional[str] |  |  |
| `past_family_1` | typing.Optional[str] |  |  |
| `course_exam_1` | typing.Optional[str] |  |  |
| `treatment_1` | typing.Optional[str] |  |  |
| `current_med_1` | typing.Optional[str] |  |  |
| `note_1` | typing.Optional[str] |  |  |
| `annotation_comment_1` | typing.Optional[str] |  |  |
| `condition_2` | typing.Optional[str] |  |  |
| `disease_2` | typing.Optional[str] |  |  |
| `purpose_2` | typing.Optional[str] |  |  |
| `past_family_2` | typing.Optional[str] |  |  |
| `course_exam_2` | typing.Optional[str] |  |  |
| `treatment_2` | typing.Optional[str] |  |  |
| `current_med_2` | typing.Optional[str] |  |  |
| `note_2` | typing.Optional[str] |  |  |
| `annotation_comment_2` | typing.Optional[str] |  |  |
| `condition_3` | typing.Optional[str] |  |  |
| `disease_3` | typing.Optional[str] |  |  |
| `purpose_3` | typing.Optional[str] |  |  |
| `past_family_3` | typing.Optional[str] |  |  |
| `course_exam_3` | typing.Optional[str] |  |  |
| `treatment_3` | typing.Optional[str] |  |  |
| `current_med_3` | typing.Optional[str] |  |  |
| `note_3` | typing.Optional[str] |  |  |
| `annotation_comment_3` | typing.Optional[str] |  |  |
| `condition_4` | typing.Optional[str] |  |  |
| `disease_4` | typing.Optional[str] |  |  |
| `purpose_4` | typing.Optional[str] |  |  |
| `past_family_4` | typing.Optional[str] |  |  |
| `course_exam_4` | typing.Optional[str] |  |  |
| `treatment_4` | typing.Optional[str] |  |  |
| `current_med_4` | typing.Optional[str] |  |  |
| `note_4` | typing.Optional[str] |  |  |
| `annotation_comment_4` | typing.Optional[str] |  |  |
| `id` | <class 'int'> | Y |  |

---
## GET /discharge_summaries/

**説明:** 一覧取得

#### パス・クエリパラメータ

| パラメータ | 型 | 必須 | 説明 |
|---|---|:--:|---|
| `skip` | None |  |  |
| `limit` | None |  |  |

#### Response Model (DischargeSummaryResponse)

| フィールド | 型 | 必須 | 説明 |
|---|---|:--:|---|
| `karte_id` | <class 'int'> | Y |  |
| `registered_type` | <class 'str'> | Y |  |
| `registered_at` | <class 'datetime.datetime'> | Y |  |
| `registered_by` | <class 'int'> | Y |  |
| `patient_name` | <class 'str'> | Y |  |
| `patient_id` | <class 'str'> | Y |  |
| `taiin_summary_answerable` | typing.Optional[int] |  |  |
| `main_disease_1` | typing.Optional[str] |  |  |
| `main_disease_2` | typing.Optional[str] |  |  |
| `main_disease_3` | typing.Optional[str] |  |  |
| `main_disease_4` | typing.Optional[str] |  |  |
| `main_disease_5` | typing.Optional[str] |  |  |
| `surgery_1` | typing.Optional[str] |  |  |
| `surgery_2` | typing.Optional[str] |  |  |
| `surgery_3` | typing.Optional[str] |  |  |
| `chief_complaint` | typing.Optional[str] |  |  |
| `present_illness` | typing.Optional[str] |  |  |
| `past_history` | typing.Optional[str] |  |  |
| `family_history` | typing.Optional[str] |  |  |
| `life_history` | typing.Optional[str] |  |  |
| `main_condition` | typing.Optional[str] |  |  |
| `main_exam_finding` | typing.Optional[str] |  |  |
| `problem_list` | typing.Optional[str] |  |  |
| `hospital_course` | typing.Optional[str] |  |  |
| `prescription` | typing.Optional[str] |  |  |
| `future_plan` | typing.Optional[str] |  |  |
| `comment` | typing.Optional[str] |  |  |
| `referral_answerable` | typing.Optional[int] |  |  |
| `condition_1` | typing.Optional[str] |  |  |
| `disease_1` | typing.Optional[str] |  |  |
| `purpose_1` | typing.Optional[str] |  |  |
| `past_family_1` | typing.Optional[str] |  |  |
| `course_exam_1` | typing.Optional[str] |  |  |
| `treatment_1` | typing.Optional[str] |  |  |
| `current_med_1` | typing.Optional[str] |  |  |
| `note_1` | typing.Optional[str] |  |  |
| `annotation_comment_1` | typing.Optional[str] |  |  |
| `condition_2` | typing.Optional[str] |  |  |
| `disease_2` | typing.Optional[str] |  |  |
| `purpose_2` | typing.Optional[str] |  |  |
| `past_family_2` | typing.Optional[str] |  |  |
| `course_exam_2` | typing.Optional[str] |  |  |
| `treatment_2` | typing.Optional[str] |  |  |
| `current_med_2` | typing.Optional[str] |  |  |
| `note_2` | typing.Optional[str] |  |  |
| `annotation_comment_2` | typing.Optional[str] |  |  |
| `condition_3` | typing.Optional[str] |  |  |
| `disease_3` | typing.Optional[str] |  |  |
| `purpose_3` | typing.Optional[str] |  |  |
| `past_family_3` | typing.Optional[str] |  |  |
| `course_exam_3` | typing.Optional[str] |  |  |
| `treatment_3` | typing.Optional[str] |  |  |
| `current_med_3` | typing.Optional[str] |  |  |
| `note_3` | typing.Optional[str] |  |  |
| `annotation_comment_3` | typing.Optional[str] |  |  |
| `condition_4` | typing.Optional[str] |  |  |
| `disease_4` | typing.Optional[str] |  |  |
| `purpose_4` | typing.Optional[str] |  |  |
| `past_family_4` | typing.Optional[str] |  |  |
| `course_exam_4` | typing.Optional[str] |  |  |
| `treatment_4` | typing.Optional[str] |  |  |
| `current_med_4` | typing.Optional[str] |  |  |
| `note_4` | typing.Optional[str] |  |  |
| `annotation_comment_4` | typing.Optional[str] |  |  |
| `id` | <class 'int'> | Y |  |

---
## PUT /discharge_summaries/{id}

**説明:** 更新

#### パス・クエリパラメータ

| パラメータ | 型 | 必須 | 説明 |
|---|---|:--:|---|
| `id` | None | Y |  |

#### Response Model (DischargeSummaryResponse)

| フィールド | 型 | 必須 | 説明 |
|---|---|:--:|---|
| `karte_id` | <class 'int'> | Y |  |
| `registered_type` | <class 'str'> | Y |  |
| `registered_at` | <class 'datetime.datetime'> | Y |  |
| `registered_by` | <class 'int'> | Y |  |
| `patient_name` | <class 'str'> | Y |  |
| `patient_id` | <class 'str'> | Y |  |
| `taiin_summary_answerable` | typing.Optional[int] |  |  |
| `main_disease_1` | typing.Optional[str] |  |  |
| `main_disease_2` | typing.Optional[str] |  |  |
| `main_disease_3` | typing.Optional[str] |  |  |
| `main_disease_4` | typing.Optional[str] |  |  |
| `main_disease_5` | typing.Optional[str] |  |  |
| `surgery_1` | typing.Optional[str] |  |  |
| `surgery_2` | typing.Optional[str] |  |  |
| `surgery_3` | typing.Optional[str] |  |  |
| `chief_complaint` | typing.Optional[str] |  |  |
| `present_illness` | typing.Optional[str] |  |  |
| `past_history` | typing.Optional[str] |  |  |
| `family_history` | typing.Optional[str] |  |  |
| `life_history` | typing.Optional[str] |  |  |
| `main_condition` | typing.Optional[str] |  |  |
| `main_exam_finding` | typing.Optional[str] |  |  |
| `problem_list` | typing.Optional[str] |  |  |
| `hospital_course` | typing.Optional[str] |  |  |
| `prescription` | typing.Optional[str] |  |  |
| `future_plan` | typing.Optional[str] |  |  |
| `comment` | typing.Optional[str] |  |  |
| `referral_answerable` | typing.Optional[int] |  |  |
| `condition_1` | typing.Optional[str] |  |  |
| `disease_1` | typing.Optional[str] |  |  |
| `purpose_1` | typing.Optional[str] |  |  |
| `past_family_1` | typing.Optional[str] |  |  |
| `course_exam_1` | typing.Optional[str] |  |  |
| `treatment_1` | typing.Optional[str] |  |  |
| `current_med_1` | typing.Optional[str] |  |  |
| `note_1` | typing.Optional[str] |  |  |
| `annotation_comment_1` | typing.Optional[str] |  |  |
| `condition_2` | typing.Optional[str] |  |  |
| `disease_2` | typing.Optional[str] |  |  |
| `purpose_2` | typing.Optional[str] |  |  |
| `past_family_2` | typing.Optional[str] |  |  |
| `course_exam_2` | typing.Optional[str] |  |  |
| `treatment_2` | typing.Optional[str] |  |  |
| `current_med_2` | typing.Optional[str] |  |  |
| `note_2` | typing.Optional[str] |  |  |
| `annotation_comment_2` | typing.Optional[str] |  |  |
| `condition_3` | typing.Optional[str] |  |  |
| `disease_3` | typing.Optional[str] |  |  |
| `purpose_3` | typing.Optional[str] |  |  |
| `past_family_3` | typing.Optional[str] |  |  |
| `course_exam_3` | typing.Optional[str] |  |  |
| `treatment_3` | typing.Optional[str] |  |  |
| `current_med_3` | typing.Optional[str] |  |  |
| `note_3` | typing.Optional[str] |  |  |
| `annotation_comment_3` | typing.Optional[str] |  |  |
| `condition_4` | typing.Optional[str] |  |  |
| `disease_4` | typing.Optional[str] |  |  |
| `purpose_4` | typing.Optional[str] |  |  |
| `past_family_4` | typing.Optional[str] |  |  |
| `course_exam_4` | typing.Optional[str] |  |  |
| `treatment_4` | typing.Optional[str] |  |  |
| `current_med_4` | typing.Optional[str] |  |  |
| `note_4` | typing.Optional[str] |  |  |
| `annotation_comment_4` | typing.Optional[str] |  |  |
| `id` | <class 'int'> | Y |  |

---
## DELETE /discharge_summaries/{id}

**説明:** 削除

#### パス・クエリパラメータ

| パラメータ | 型 | 必須 | 説明 |
|---|---|:--:|---|
| `id` | None | Y |  |

---
## POST /stroke_patients/

**説明:** 新規登録

#### Response Model (StrokePatientResponse)

| フィールド | 型 | 必須 | 説明 |
|---|---|:--:|---|
| `karte_id` | <class 'int'> | Y |  |
| `registered_type` | <class 'str'> | Y |  |
| `registered_at` | <class 'datetime.datetime'> | Y |  |
| `registered_by` | <class 'int'> | Y |  |
| `age` | typing.Optional[int] |  |  |
| `sex` | typing.Optional[int] |  |  |
| `sitename` | typing.Optional[str] |  |  |
| `onset_dt` | typing.Optional[datetime.date] |  |  |
| `onset_tm` | typing.Optional[datetime.time] |  |  |
| `arrival_tm` | typing.Optional[int] |  |  |
| `admit_dt` | typing.Optional[datetime.date] |  |  |
| `admit_proc` | typing.Optional[int] |  |  |
| `admit_route` | typing.Optional[int] |  |  |
| `diagnosis` | typing.Optional[int] |  |  |
| `duration` | typing.Optional[str] |  |  |
| `subtype` | typing.Optional[int] |  |  |
| `location` | typing.Optional[str] |  |  |
| `culprit` | typing.Optional[str] |  |  |
| `culprit_ves` | typing.Optional[str] |  |  |
| `emb_source` | typing.Optional[str] |  |  |
| `symptom` | typing.Optional[str] |  |  |
| `rf_smoking` | typing.Optional[int] |  |  |
| `rf_alcohol` | typing.Optional[int] |  |  |
| `rf_allergy` | typing.Optional[int] |  |  |
| `rf_ht` | typing.Optional[int] |  |  |
| `rf_dm` | typing.Optional[int] |  |  |
| `rf_dl` | typing.Optional[int] |  |  |
| `rf_dialysis` | typing.Optional[int] |  |  |
| `rf_af` | typing.Optional[int] |  |  |
| `rf_renal` | typing.Optional[int] |  |  |
| `mh_stroke` | typing.Optional[int] |  |  |
| `mh_dementia` | typing.Optional[int] |  |  |
| `mh_ihd` | typing.Optional[int] |  |  |
| `pre_mrs` | typing.Optional[int] |  |  |
| `chief_comp` | typing.Optional[str] |  |  |
| `present_ill` | typing.Optional[str] |  |  |
| `hgt` | typing.Optional[float] |  |  |
| `wgt` | typing.Optional[float] |  |  |
| `abd_cir` | typing.Optional[float] |  |  |
| `bp` | typing.Optional[str] |  |  |
| `sbp` | typing.Optional[int] |  |  |
| `dbp` | typing.Optional[int] |  |  |
| `pulse` | typing.Optional[int] |  |  |
| `murmur` | typing.Optional[int] |  |  |
| `conscious` | typing.Optional[int] |  |  |
| `cortical` | typing.Optional[int] |  |  |
| `motor_dis` | typing.Optional[int] |  |  |
| `sensory_dis` | typing.Optional[int] |  |  |
| `nihss` | typing.Optional[int] |  |  |
| `lab_cbc` | typing.Optional[str] |  |  |
| `lab_chem` | typing.Optional[str] |  |  |
| `lab_ddimer` | typing.Optional[float] |  |  |
| `lab_hscrp` | typing.Optional[float] |  |  |
| `img_ct` | typing.Optional[int] |  |  |
| `img_mri` | typing.Optional[int] |  |  |
| `img_mra` | typing.Optional[int] |  |  |
| `img_spect` | typing.Optional[int] |  |  |
| `img_echo` | typing.Optional[str] |  |  |
| `reperfusion` | typing.Optional[int] |  |  |
| `rtpa` | typing.Optional[int] |  |  |
| `evt` | typing.Optional[int] |  |  |
| `pre_at` | typing.Optional[int] |  |  |
| `pre_ap` | typing.Optional[int] |  |  |
| `pre_ac` | typing.Optional[int] |  |  |
| `in_at` | typing.Optional[int] |  |  |
| `in_ap` | typing.Optional[int] |  |  |
| `in_ac` | typing.Optional[int] |  |  |
| `anti_ht_tx` | typing.Optional[int] |  |  |
| `progress` | typing.Optional[str] |  |  |
| `recur` | typing.Optional[int] |  |  |
| `cv_event` | typing.Optional[int] |  |  |
| `complication` | typing.Optional[int] |  |  |
| `dc_outcome` | typing.Optional[int] |  |  |
| `dc_nihss` | typing.Optional[int] |  |  |
| `dc_mrs` | typing.Optional[int] |  |  |
| `dc_dt` | typing.Optional[datetime.date] |  |  |
| `dc_med` | typing.Optional[str] |  |  |
| `fu_mrs` | typing.Optional[int] |  |  |
| `fu_recur` | typing.Optional[int] |  |  |
| `fu_cvevent` | typing.Optional[int] |  |  |
| `fu_death` | typing.Optional[int] |  |  |
| `id` | <class 'int'> | Y |  |

---
## GET /stroke_patients/{id}

**説明:** IDで1件取得

#### パス・クエリパラメータ

| パラメータ | 型 | 必須 | 説明 |
|---|---|:--:|---|
| `id` | None | Y |  |

#### Response Model (StrokePatientResponse)

| フィールド | 型 | 必須 | 説明 |
|---|---|:--:|---|
| `karte_id` | <class 'int'> | Y |  |
| `registered_type` | <class 'str'> | Y |  |
| `registered_at` | <class 'datetime.datetime'> | Y |  |
| `registered_by` | <class 'int'> | Y |  |
| `age` | typing.Optional[int] |  |  |
| `sex` | typing.Optional[int] |  |  |
| `sitename` | typing.Optional[str] |  |  |
| `onset_dt` | typing.Optional[datetime.date] |  |  |
| `onset_tm` | typing.Optional[datetime.time] |  |  |
| `arrival_tm` | typing.Optional[int] |  |  |
| `admit_dt` | typing.Optional[datetime.date] |  |  |
| `admit_proc` | typing.Optional[int] |  |  |
| `admit_route` | typing.Optional[int] |  |  |
| `diagnosis` | typing.Optional[int] |  |  |
| `duration` | typing.Optional[str] |  |  |
| `subtype` | typing.Optional[int] |  |  |
| `location` | typing.Optional[str] |  |  |
| `culprit` | typing.Optional[str] |  |  |
| `culprit_ves` | typing.Optional[str] |  |  |
| `emb_source` | typing.Optional[str] |  |  |
| `symptom` | typing.Optional[str] |  |  |
| `rf_smoking` | typing.Optional[int] |  |  |
| `rf_alcohol` | typing.Optional[int] |  |  |
| `rf_allergy` | typing.Optional[int] |  |  |
| `rf_ht` | typing.Optional[int] |  |  |
| `rf_dm` | typing.Optional[int] |  |  |
| `rf_dl` | typing.Optional[int] |  |  |
| `rf_dialysis` | typing.Optional[int] |  |  |
| `rf_af` | typing.Optional[int] |  |  |
| `rf_renal` | typing.Optional[int] |  |  |
| `mh_stroke` | typing.Optional[int] |  |  |
| `mh_dementia` | typing.Optional[int] |  |  |
| `mh_ihd` | typing.Optional[int] |  |  |
| `pre_mrs` | typing.Optional[int] |  |  |
| `chief_comp` | typing.Optional[str] |  |  |
| `present_ill` | typing.Optional[str] |  |  |
| `hgt` | typing.Optional[float] |  |  |
| `wgt` | typing.Optional[float] |  |  |
| `abd_cir` | typing.Optional[float] |  |  |
| `bp` | typing.Optional[str] |  |  |
| `sbp` | typing.Optional[int] |  |  |
| `dbp` | typing.Optional[int] |  |  |
| `pulse` | typing.Optional[int] |  |  |
| `murmur` | typing.Optional[int] |  |  |
| `conscious` | typing.Optional[int] |  |  |
| `cortical` | typing.Optional[int] |  |  |
| `motor_dis` | typing.Optional[int] |  |  |
| `sensory_dis` | typing.Optional[int] |  |  |
| `nihss` | typing.Optional[int] |  |  |
| `lab_cbc` | typing.Optional[str] |  |  |
| `lab_chem` | typing.Optional[str] |  |  |
| `lab_ddimer` | typing.Optional[float] |  |  |
| `lab_hscrp` | typing.Optional[float] |  |  |
| `img_ct` | typing.Optional[int] |  |  |
| `img_mri` | typing.Optional[int] |  |  |
| `img_mra` | typing.Optional[int] |  |  |
| `img_spect` | typing.Optional[int] |  |  |
| `img_echo` | typing.Optional[str] |  |  |
| `reperfusion` | typing.Optional[int] |  |  |
| `rtpa` | typing.Optional[int] |  |  |
| `evt` | typing.Optional[int] |  |  |
| `pre_at` | typing.Optional[int] |  |  |
| `pre_ap` | typing.Optional[int] |  |  |
| `pre_ac` | typing.Optional[int] |  |  |
| `in_at` | typing.Optional[int] |  |  |
| `in_ap` | typing.Optional[int] |  |  |
| `in_ac` | typing.Optional[int] |  |  |
| `anti_ht_tx` | typing.Optional[int] |  |  |
| `progress` | typing.Optional[str] |  |  |
| `recur` | typing.Optional[int] |  |  |
| `cv_event` | typing.Optional[int] |  |  |
| `complication` | typing.Optional[int] |  |  |
| `dc_outcome` | typing.Optional[int] |  |  |
| `dc_nihss` | typing.Optional[int] |  |  |
| `dc_mrs` | typing.Optional[int] |  |  |
| `dc_dt` | typing.Optional[datetime.date] |  |  |
| `dc_med` | typing.Optional[str] |  |  |
| `fu_mrs` | typing.Optional[int] |  |  |
| `fu_recur` | typing.Optional[int] |  |  |
| `fu_cvevent` | typing.Optional[int] |  |  |
| `fu_death` | typing.Optional[int] |  |  |
| `id` | <class 'int'> | Y |  |

---
## GET /stroke_patients/

**説明:** 一覧取得

#### パス・クエリパラメータ

| パラメータ | 型 | 必須 | 説明 |
|---|---|:--:|---|
| `skip` | None |  |  |
| `limit` | None |  |  |

#### Response Model (StrokePatientResponse)

| フィールド | 型 | 必須 | 説明 |
|---|---|:--:|---|
| `karte_id` | <class 'int'> | Y |  |
| `registered_type` | <class 'str'> | Y |  |
| `registered_at` | <class 'datetime.datetime'> | Y |  |
| `registered_by` | <class 'int'> | Y |  |
| `age` | typing.Optional[int] |  |  |
| `sex` | typing.Optional[int] |  |  |
| `sitename` | typing.Optional[str] |  |  |
| `onset_dt` | typing.Optional[datetime.date] |  |  |
| `onset_tm` | typing.Optional[datetime.time] |  |  |
| `arrival_tm` | typing.Optional[int] |  |  |
| `admit_dt` | typing.Optional[datetime.date] |  |  |
| `admit_proc` | typing.Optional[int] |  |  |
| `admit_route` | typing.Optional[int] |  |  |
| `diagnosis` | typing.Optional[int] |  |  |
| `duration` | typing.Optional[str] |  |  |
| `subtype` | typing.Optional[int] |  |  |
| `location` | typing.Optional[str] |  |  |
| `culprit` | typing.Optional[str] |  |  |
| `culprit_ves` | typing.Optional[str] |  |  |
| `emb_source` | typing.Optional[str] |  |  |
| `symptom` | typing.Optional[str] |  |  |
| `rf_smoking` | typing.Optional[int] |  |  |
| `rf_alcohol` | typing.Optional[int] |  |  |
| `rf_allergy` | typing.Optional[int] |  |  |
| `rf_ht` | typing.Optional[int] |  |  |
| `rf_dm` | typing.Optional[int] |  |  |
| `rf_dl` | typing.Optional[int] |  |  |
| `rf_dialysis` | typing.Optional[int] |  |  |
| `rf_af` | typing.Optional[int] |  |  |
| `rf_renal` | typing.Optional[int] |  |  |
| `mh_stroke` | typing.Optional[int] |  |  |
| `mh_dementia` | typing.Optional[int] |  |  |
| `mh_ihd` | typing.Optional[int] |  |  |
| `pre_mrs` | typing.Optional[int] |  |  |
| `chief_comp` | typing.Optional[str] |  |  |
| `present_ill` | typing.Optional[str] |  |  |
| `hgt` | typing.Optional[float] |  |  |
| `wgt` | typing.Optional[float] |  |  |
| `abd_cir` | typing.Optional[float] |  |  |
| `bp` | typing.Optional[str] |  |  |
| `sbp` | typing.Optional[int] |  |  |
| `dbp` | typing.Optional[int] |  |  |
| `pulse` | typing.Optional[int] |  |  |
| `murmur` | typing.Optional[int] |  |  |
| `conscious` | typing.Optional[int] |  |  |
| `cortical` | typing.Optional[int] |  |  |
| `motor_dis` | typing.Optional[int] |  |  |
| `sensory_dis` | typing.Optional[int] |  |  |
| `nihss` | typing.Optional[int] |  |  |
| `lab_cbc` | typing.Optional[str] |  |  |
| `lab_chem` | typing.Optional[str] |  |  |
| `lab_ddimer` | typing.Optional[float] |  |  |
| `lab_hscrp` | typing.Optional[float] |  |  |
| `img_ct` | typing.Optional[int] |  |  |
| `img_mri` | typing.Optional[int] |  |  |
| `img_mra` | typing.Optional[int] |  |  |
| `img_spect` | typing.Optional[int] |  |  |
| `img_echo` | typing.Optional[str] |  |  |
| `reperfusion` | typing.Optional[int] |  |  |
| `rtpa` | typing.Optional[int] |  |  |
| `evt` | typing.Optional[int] |  |  |
| `pre_at` | typing.Optional[int] |  |  |
| `pre_ap` | typing.Optional[int] |  |  |
| `pre_ac` | typing.Optional[int] |  |  |
| `in_at` | typing.Optional[int] |  |  |
| `in_ap` | typing.Optional[int] |  |  |
| `in_ac` | typing.Optional[int] |  |  |
| `anti_ht_tx` | typing.Optional[int] |  |  |
| `progress` | typing.Optional[str] |  |  |
| `recur` | typing.Optional[int] |  |  |
| `cv_event` | typing.Optional[int] |  |  |
| `complication` | typing.Optional[int] |  |  |
| `dc_outcome` | typing.Optional[int] |  |  |
| `dc_nihss` | typing.Optional[int] |  |  |
| `dc_mrs` | typing.Optional[int] |  |  |
| `dc_dt` | typing.Optional[datetime.date] |  |  |
| `dc_med` | typing.Optional[str] |  |  |
| `fu_mrs` | typing.Optional[int] |  |  |
| `fu_recur` | typing.Optional[int] |  |  |
| `fu_cvevent` | typing.Optional[int] |  |  |
| `fu_death` | typing.Optional[int] |  |  |
| `id` | <class 'int'> | Y |  |

---
## PUT /stroke_patients/{id}

**説明:** 更新

#### パス・クエリパラメータ

| パラメータ | 型 | 必須 | 説明 |
|---|---|:--:|---|
| `id` | None | Y |  |

#### Response Model (StrokePatientResponse)

| フィールド | 型 | 必須 | 説明 |
|---|---|:--:|---|
| `karte_id` | <class 'int'> | Y |  |
| `registered_type` | <class 'str'> | Y |  |
| `registered_at` | <class 'datetime.datetime'> | Y |  |
| `registered_by` | <class 'int'> | Y |  |
| `age` | typing.Optional[int] |  |  |
| `sex` | typing.Optional[int] |  |  |
| `sitename` | typing.Optional[str] |  |  |
| `onset_dt` | typing.Optional[datetime.date] |  |  |
| `onset_tm` | typing.Optional[datetime.time] |  |  |
| `arrival_tm` | typing.Optional[int] |  |  |
| `admit_dt` | typing.Optional[datetime.date] |  |  |
| `admit_proc` | typing.Optional[int] |  |  |
| `admit_route` | typing.Optional[int] |  |  |
| `diagnosis` | typing.Optional[int] |  |  |
| `duration` | typing.Optional[str] |  |  |
| `subtype` | typing.Optional[int] |  |  |
| `location` | typing.Optional[str] |  |  |
| `culprit` | typing.Optional[str] |  |  |
| `culprit_ves` | typing.Optional[str] |  |  |
| `emb_source` | typing.Optional[str] |  |  |
| `symptom` | typing.Optional[str] |  |  |
| `rf_smoking` | typing.Optional[int] |  |  |
| `rf_alcohol` | typing.Optional[int] |  |  |
| `rf_allergy` | typing.Optional[int] |  |  |
| `rf_ht` | typing.Optional[int] |  |  |
| `rf_dm` | typing.Optional[int] |  |  |
| `rf_dl` | typing.Optional[int] |  |  |
| `rf_dialysis` | typing.Optional[int] |  |  |
| `rf_af` | typing.Optional[int] |  |  |
| `rf_renal` | typing.Optional[int] |  |  |
| `mh_stroke` | typing.Optional[int] |  |  |
| `mh_dementia` | typing.Optional[int] |  |  |
| `mh_ihd` | typing.Optional[int] |  |  |
| `pre_mrs` | typing.Optional[int] |  |  |
| `chief_comp` | typing.Optional[str] |  |  |
| `present_ill` | typing.Optional[str] |  |  |
| `hgt` | typing.Optional[float] |  |  |
| `wgt` | typing.Optional[float] |  |  |
| `abd_cir` | typing.Optional[float] |  |  |
| `bp` | typing.Optional[str] |  |  |
| `sbp` | typing.Optional[int] |  |  |
| `dbp` | typing.Optional[int] |  |  |
| `pulse` | typing.Optional[int] |  |  |
| `murmur` | typing.Optional[int] |  |  |
| `conscious` | typing.Optional[int] |  |  |
| `cortical` | typing.Optional[int] |  |  |
| `motor_dis` | typing.Optional[int] |  |  |
| `sensory_dis` | typing.Optional[int] |  |  |
| `nihss` | typing.Optional[int] |  |  |
| `lab_cbc` | typing.Optional[str] |  |  |
| `lab_chem` | typing.Optional[str] |  |  |
| `lab_ddimer` | typing.Optional[float] |  |  |
| `lab_hscrp` | typing.Optional[float] |  |  |
| `img_ct` | typing.Optional[int] |  |  |
| `img_mri` | typing.Optional[int] |  |  |
| `img_mra` | typing.Optional[int] |  |  |
| `img_spect` | typing.Optional[int] |  |  |
| `img_echo` | typing.Optional[str] |  |  |
| `reperfusion` | typing.Optional[int] |  |  |
| `rtpa` | typing.Optional[int] |  |  |
| `evt` | typing.Optional[int] |  |  |
| `pre_at` | typing.Optional[int] |  |  |
| `pre_ap` | typing.Optional[int] |  |  |
| `pre_ac` | typing.Optional[int] |  |  |
| `in_at` | typing.Optional[int] |  |  |
| `in_ap` | typing.Optional[int] |  |  |
| `in_ac` | typing.Optional[int] |  |  |
| `anti_ht_tx` | typing.Optional[int] |  |  |
| `progress` | typing.Optional[str] |  |  |
| `recur` | typing.Optional[int] |  |  |
| `cv_event` | typing.Optional[int] |  |  |
| `complication` | typing.Optional[int] |  |  |
| `dc_outcome` | typing.Optional[int] |  |  |
| `dc_nihss` | typing.Optional[int] |  |  |
| `dc_mrs` | typing.Optional[int] |  |  |
| `dc_dt` | typing.Optional[datetime.date] |  |  |
| `dc_med` | typing.Optional[str] |  |  |
| `fu_mrs` | typing.Optional[int] |  |  |
| `fu_recur` | typing.Optional[int] |  |  |
| `fu_cvevent` | typing.Optional[int] |  |  |
| `fu_death` | typing.Optional[int] |  |  |
| `id` | <class 'int'> | Y |  |

---
## DELETE /stroke_patients/{id}

**説明:** 削除

#### パス・クエリパラメータ

| パラメータ | 型 | 必須 | 説明 |
|---|---|:--:|---|
| `id` | None | Y |  |

---