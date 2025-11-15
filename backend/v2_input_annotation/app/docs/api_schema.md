# API 定義書

# default

## GET /

### リクエスト

None
### レスポンス

**形式:** dict

**モデル:**  Any
# user_accounts

## POST /user_accounts/

**説明:** 新規登録

### リクエスト

None
#### ボディ (UserAccountCreate)

| フィールド | 型 | 必須 | 説明 |
|---|---|:--:|---|
| `login_id` | str | Y |  |
| `password` | str | Y |  |
| `name` | str | Y |  |

### レスポンス

**形式:** UserAccount

#### **モデル:** UserAccount

| フィールド | 型 | 必須 | 説明 |
|---|---|:--:|---|
| `id` | int | Y |  |
| `login_id` | str | Y |  |
| `name` | str | Y |  |

---
## GET /user_accounts/{id}

**説明:** IDで1件取得

### リクエスト

#### パスパラメータ

| パラメータ | 型 | 必須 | 説明 |
|---|---|:--:|---|
| `id` |  | Y |  |

### レスポンス

**形式:** UserAccount

#### **モデル:** UserAccount

| フィールド | 型 | 必須 | 説明 |
|---|---|:--:|---|
| `id` | int | Y |  |
| `login_id` | str | Y |  |
| `name` | str | Y |  |

---
## GET /user_accounts/

**説明:** 一覧取得

### リクエスト

#### クエリパラメータ

| パラメータ | 型 | 必須 | 説明 |
|---|---|:--:|---|
| `skip` |  |  |  |
| `limit` |  |  |  |

### レスポンス

**形式:** List[UserAccount]

#### **モデル:** UserAccount

| フィールド | 型 | 必須 | 説明 |
|---|---|:--:|---|
| `id` | int | Y |  |
| `login_id` | str | Y |  |
| `name` | str | Y |  |

---
## PUT /user_accounts/{id}

**説明:** 更新

### リクエスト

#### パスパラメータ

| パラメータ | 型 | 必須 | 説明 |
|---|---|:--:|---|
| `id` |  | Y |  |

#### ボディ (UserAccountUpdate)

| フィールド | 型 | 必須 | 説明 |
|---|---|:--:|---|
| `login_id` | str | Y |  |
| `password` | str | Y |  |
| `name` | str | Y |  |

### レスポンス

**形式:** UserAccount

#### **モデル:** UserAccount

| フィールド | 型 | 必須 | 説明 |
|---|---|:--:|---|
| `id` | int | Y |  |
| `login_id` | str | Y |  |
| `name` | str | Y |  |

---
## DELETE /user_accounts/{id}

**説明:** 削除

### リクエスト

#### パスパラメータ

| パラメータ | 型 | 必須 | 説明 |
|---|---|:--:|---|
| `id` |  | Y |  |

### レスポンス

**形式:** dict

**モデル:**  Any
# auth

## POST /login

**説明:** ログインID(login_id)とパスワードを受け取り、JWTを返す

### リクエスト

None
### レスポンス

**形式:** TokenResponse

#### **モデル:** TokenResponse

| フィールド | 型 | 必須 | 説明 |
|---|---|:--:|---|
| `access_token` | str | Y |  |
| `token_type` | str | Y |  |

---
## GET /user_accounts_with_auth/me

**説明:** ログイン中ユーザーの情報取得

### リクエスト

None
### レスポンス

**形式:** dict

**モデル:**  Any
# kartes

## POST /kartes/

**説明:** 新規登録

### リクエスト

None
#### ボディ (KarteSchema)

| フィールド | 型 | 必須 | 説明 |
|---|---|:--:|---|
| `karte_data_id` | str | Y |  |
| `karte_name` | str | Y |  |
| `data_type` | str | Y |  |
| `status` | str |  |  |

### レスポンス

**形式:** KarteResponse

#### **モデル:** KarteResponse

| フィールド | 型 | 必須 | 説明 |
|---|---|:--:|---|
| `karte_data_id` | str | Y |  |
| `karte_name` | str | Y |  |
| `data_type` | str | Y |  |
| `status` | str |  |  |
| `id` | int | Y |  |

---
## GET /kartes/{id}

**説明:** IDで1件取得

### リクエスト

#### パスパラメータ

| パラメータ | 型 | 必須 | 説明 |
|---|---|:--:|---|
| `id` |  | Y |  |

### レスポンス

**形式:** KarteResponse

#### **モデル:** KarteResponse

| フィールド | 型 | 必須 | 説明 |
|---|---|:--:|---|
| `karte_data_id` | str | Y |  |
| `karte_name` | str | Y |  |
| `data_type` | str | Y |  |
| `status` | str |  |  |
| `id` | int | Y |  |

---
## GET /kartes/

**説明:** 一覧取得

### リクエスト

#### クエリパラメータ

| パラメータ | 型 | 必須 | 説明 |
|---|---|:--:|---|
| `skip` |  |  |  |
| `limit` |  |  |  |

### レスポンス

**形式:** List[KarteResponse]

#### **モデル:** KarteResponse

| フィールド | 型 | 必須 | 説明 |
|---|---|:--:|---|
| `karte_data_id` | str | Y |  |
| `karte_name` | str | Y |  |
| `data_type` | str | Y |  |
| `status` | str |  |  |
| `id` | int | Y |  |

---
## PUT /kartes/{id}

**説明:** 更新

### リクエスト

#### パスパラメータ

| パラメータ | 型 | 必須 | 説明 |
|---|---|:--:|---|
| `id` |  | Y |  |

#### ボディ (KarteUpdate)

| フィールド | 型 | 必須 | 説明 |
|---|---|:--:|---|
| `karte_data_id` | str |  |  |
| `karte_name` | str |  |  |
| `data_type` | str |  |  |
| `status` | str |  |  |

### レスポンス

**形式:** KarteResponse

#### **モデル:** KarteResponse

| フィールド | 型 | 必須 | 説明 |
|---|---|:--:|---|
| `karte_data_id` | str | Y |  |
| `karte_name` | str | Y |  |
| `data_type` | str | Y |  |
| `status` | str |  |  |
| `id` | int | Y |  |

---
## DELETE /kartes/{id}

**説明:** 削除

### リクエスト

#### パスパラメータ

| パラメータ | 型 | 必須 | 説明 |
|---|---|:--:|---|
| `id` |  | Y |  |

### レスポンス

**形式:** dict

**モデル:**  Any
# DischargeSummaries

## POST /discharge_summaries/

**説明:** 新規登録

### リクエスト

None
#### ボディ (DischargeSummarySchema)

| フィールド | 型 | 必須 | 説明 |
|---|---|:--:|---|
| `karte_id` | int | Y |  |
| `registered_type` | str | Y |  |
| `registered_at` | datetime | Y |  |
| `registered_by` | int | Y |  |
| `patient_name` | str | Y |  |
| `patient_id` | str | Y |  |
| `taiin_summary_answerable` | int |  |  |
| `main_disease_1` | str |  |  |
| `main_disease_2` | str |  |  |
| `main_disease_3` | str |  |  |
| `main_disease_4` | str |  |  |
| `main_disease_5` | str |  |  |
| `surgery_1` | str |  |  |
| `surgery_2` | str |  |  |
| `surgery_3` | str |  |  |
| `chief_complaint` | str |  |  |
| `present_illness` | str |  |  |
| `past_history` | str |  |  |
| `family_history` | str |  |  |
| `life_history` | str |  |  |
| `main_condition` | str |  |  |
| `main_exam_finding` | str |  |  |
| `problem_list` | str |  |  |
| `hospital_course` | str |  |  |
| `prescription` | str |  |  |
| `future_plan` | str |  |  |
| `comment` | str |  |  |
| `referral_answerable` | int |  |  |
| `condition_1` | str |  |  |
| `disease_1` | str |  |  |
| `purpose_1` | str |  |  |
| `past_family_1` | str |  |  |
| `course_exam_1` | str |  |  |
| `treatment_1` | str |  |  |
| `current_med_1` | str |  |  |
| `note_1` | str |  |  |
| `annotation_comment_1` | str |  |  |
| `condition_2` | str |  |  |
| `disease_2` | str |  |  |
| `purpose_2` | str |  |  |
| `past_family_2` | str |  |  |
| `course_exam_2` | str |  |  |
| `treatment_2` | str |  |  |
| `current_med_2` | str |  |  |
| `note_2` | str |  |  |
| `annotation_comment_2` | str |  |  |
| `condition_3` | str |  |  |
| `disease_3` | str |  |  |
| `purpose_3` | str |  |  |
| `past_family_3` | str |  |  |
| `course_exam_3` | str |  |  |
| `treatment_3` | str |  |  |
| `current_med_3` | str |  |  |
| `note_3` | str |  |  |
| `annotation_comment_3` | str |  |  |
| `condition_4` | str |  |  |
| `disease_4` | str |  |  |
| `purpose_4` | str |  |  |
| `past_family_4` | str |  |  |
| `course_exam_4` | str |  |  |
| `treatment_4` | str |  |  |
| `current_med_4` | str |  |  |
| `note_4` | str |  |  |
| `annotation_comment_4` | str |  |  |

### レスポンス

**形式:** DischargeSummaryResponse

#### **モデル:** DischargeSummaryResponse

| フィールド | 型 | 必須 | 説明 |
|---|---|:--:|---|
| `karte_id` | int | Y |  |
| `registered_type` | str | Y |  |
| `registered_at` | datetime | Y |  |
| `registered_by` | int | Y |  |
| `patient_name` | str | Y |  |
| `patient_id` | str | Y |  |
| `taiin_summary_answerable` | int |  |  |
| `main_disease_1` | str |  |  |
| `main_disease_2` | str |  |  |
| `main_disease_3` | str |  |  |
| `main_disease_4` | str |  |  |
| `main_disease_5` | str |  |  |
| `surgery_1` | str |  |  |
| `surgery_2` | str |  |  |
| `surgery_3` | str |  |  |
| `chief_complaint` | str |  |  |
| `present_illness` | str |  |  |
| `past_history` | str |  |  |
| `family_history` | str |  |  |
| `life_history` | str |  |  |
| `main_condition` | str |  |  |
| `main_exam_finding` | str |  |  |
| `problem_list` | str |  |  |
| `hospital_course` | str |  |  |
| `prescription` | str |  |  |
| `future_plan` | str |  |  |
| `comment` | str |  |  |
| `referral_answerable` | int |  |  |
| `condition_1` | str |  |  |
| `disease_1` | str |  |  |
| `purpose_1` | str |  |  |
| `past_family_1` | str |  |  |
| `course_exam_1` | str |  |  |
| `treatment_1` | str |  |  |
| `current_med_1` | str |  |  |
| `note_1` | str |  |  |
| `annotation_comment_1` | str |  |  |
| `condition_2` | str |  |  |
| `disease_2` | str |  |  |
| `purpose_2` | str |  |  |
| `past_family_2` | str |  |  |
| `course_exam_2` | str |  |  |
| `treatment_2` | str |  |  |
| `current_med_2` | str |  |  |
| `note_2` | str |  |  |
| `annotation_comment_2` | str |  |  |
| `condition_3` | str |  |  |
| `disease_3` | str |  |  |
| `purpose_3` | str |  |  |
| `past_family_3` | str |  |  |
| `course_exam_3` | str |  |  |
| `treatment_3` | str |  |  |
| `current_med_3` | str |  |  |
| `note_3` | str |  |  |
| `annotation_comment_3` | str |  |  |
| `condition_4` | str |  |  |
| `disease_4` | str |  |  |
| `purpose_4` | str |  |  |
| `past_family_4` | str |  |  |
| `course_exam_4` | str |  |  |
| `treatment_4` | str |  |  |
| `current_med_4` | str |  |  |
| `note_4` | str |  |  |
| `annotation_comment_4` | str |  |  |
| `id` | int | Y |  |

---
## GET /discharge_summaries/{id}

**説明:** IDで1件取得

### リクエスト

#### パスパラメータ

| パラメータ | 型 | 必須 | 説明 |
|---|---|:--:|---|
| `id` |  | Y |  |

### レスポンス

**形式:** DischargeSummaryResponse

#### **モデル:** DischargeSummaryResponse

| フィールド | 型 | 必須 | 説明 |
|---|---|:--:|---|
| `karte_id` | int | Y |  |
| `registered_type` | str | Y |  |
| `registered_at` | datetime | Y |  |
| `registered_by` | int | Y |  |
| `patient_name` | str | Y |  |
| `patient_id` | str | Y |  |
| `taiin_summary_answerable` | int |  |  |
| `main_disease_1` | str |  |  |
| `main_disease_2` | str |  |  |
| `main_disease_3` | str |  |  |
| `main_disease_4` | str |  |  |
| `main_disease_5` | str |  |  |
| `surgery_1` | str |  |  |
| `surgery_2` | str |  |  |
| `surgery_3` | str |  |  |
| `chief_complaint` | str |  |  |
| `present_illness` | str |  |  |
| `past_history` | str |  |  |
| `family_history` | str |  |  |
| `life_history` | str |  |  |
| `main_condition` | str |  |  |
| `main_exam_finding` | str |  |  |
| `problem_list` | str |  |  |
| `hospital_course` | str |  |  |
| `prescription` | str |  |  |
| `future_plan` | str |  |  |
| `comment` | str |  |  |
| `referral_answerable` | int |  |  |
| `condition_1` | str |  |  |
| `disease_1` | str |  |  |
| `purpose_1` | str |  |  |
| `past_family_1` | str |  |  |
| `course_exam_1` | str |  |  |
| `treatment_1` | str |  |  |
| `current_med_1` | str |  |  |
| `note_1` | str |  |  |
| `annotation_comment_1` | str |  |  |
| `condition_2` | str |  |  |
| `disease_2` | str |  |  |
| `purpose_2` | str |  |  |
| `past_family_2` | str |  |  |
| `course_exam_2` | str |  |  |
| `treatment_2` | str |  |  |
| `current_med_2` | str |  |  |
| `note_2` | str |  |  |
| `annotation_comment_2` | str |  |  |
| `condition_3` | str |  |  |
| `disease_3` | str |  |  |
| `purpose_3` | str |  |  |
| `past_family_3` | str |  |  |
| `course_exam_3` | str |  |  |
| `treatment_3` | str |  |  |
| `current_med_3` | str |  |  |
| `note_3` | str |  |  |
| `annotation_comment_3` | str |  |  |
| `condition_4` | str |  |  |
| `disease_4` | str |  |  |
| `purpose_4` | str |  |  |
| `past_family_4` | str |  |  |
| `course_exam_4` | str |  |  |
| `treatment_4` | str |  |  |
| `current_med_4` | str |  |  |
| `note_4` | str |  |  |
| `annotation_comment_4` | str |  |  |
| `id` | int | Y |  |

---
## GET /discharge_summaries/

**説明:** 一覧取得

### リクエスト

#### クエリパラメータ

| パラメータ | 型 | 必須 | 説明 |
|---|---|:--:|---|
| `skip` |  |  |  |
| `limit` |  |  |  |

### レスポンス

**形式:** List[DischargeSummaryResponse]

#### **モデル:** DischargeSummaryResponse

| フィールド | 型 | 必須 | 説明 |
|---|---|:--:|---|
| `karte_id` | int | Y |  |
| `registered_type` | str | Y |  |
| `registered_at` | datetime | Y |  |
| `registered_by` | int | Y |  |
| `patient_name` | str | Y |  |
| `patient_id` | str | Y |  |
| `taiin_summary_answerable` | int |  |  |
| `main_disease_1` | str |  |  |
| `main_disease_2` | str |  |  |
| `main_disease_3` | str |  |  |
| `main_disease_4` | str |  |  |
| `main_disease_5` | str |  |  |
| `surgery_1` | str |  |  |
| `surgery_2` | str |  |  |
| `surgery_3` | str |  |  |
| `chief_complaint` | str |  |  |
| `present_illness` | str |  |  |
| `past_history` | str |  |  |
| `family_history` | str |  |  |
| `life_history` | str |  |  |
| `main_condition` | str |  |  |
| `main_exam_finding` | str |  |  |
| `problem_list` | str |  |  |
| `hospital_course` | str |  |  |
| `prescription` | str |  |  |
| `future_plan` | str |  |  |
| `comment` | str |  |  |
| `referral_answerable` | int |  |  |
| `condition_1` | str |  |  |
| `disease_1` | str |  |  |
| `purpose_1` | str |  |  |
| `past_family_1` | str |  |  |
| `course_exam_1` | str |  |  |
| `treatment_1` | str |  |  |
| `current_med_1` | str |  |  |
| `note_1` | str |  |  |
| `annotation_comment_1` | str |  |  |
| `condition_2` | str |  |  |
| `disease_2` | str |  |  |
| `purpose_2` | str |  |  |
| `past_family_2` | str |  |  |
| `course_exam_2` | str |  |  |
| `treatment_2` | str |  |  |
| `current_med_2` | str |  |  |
| `note_2` | str |  |  |
| `annotation_comment_2` | str |  |  |
| `condition_3` | str |  |  |
| `disease_3` | str |  |  |
| `purpose_3` | str |  |  |
| `past_family_3` | str |  |  |
| `course_exam_3` | str |  |  |
| `treatment_3` | str |  |  |
| `current_med_3` | str |  |  |
| `note_3` | str |  |  |
| `annotation_comment_3` | str |  |  |
| `condition_4` | str |  |  |
| `disease_4` | str |  |  |
| `purpose_4` | str |  |  |
| `past_family_4` | str |  |  |
| `course_exam_4` | str |  |  |
| `treatment_4` | str |  |  |
| `current_med_4` | str |  |  |
| `note_4` | str |  |  |
| `annotation_comment_4` | str |  |  |
| `id` | int | Y |  |

---
## PUT /discharge_summaries/{id}

**説明:** 更新

### リクエスト

#### パスパラメータ

| パラメータ | 型 | 必須 | 説明 |
|---|---|:--:|---|
| `id` |  | Y |  |

#### ボディ (DischargeSummaryUpdate)

| フィールド | 型 | 必須 | 説明 |
|---|---|:--:|---|
| `karte_id` | int |  |  |
| `registered_type` | str |  |  |
| `registered_at` | datetime |  |  |
| `registered_by` | int |  |  |
| `patient_name` | str |  |  |
| `patient_id` | str |  |  |
| `taiin_summary_answerable` | int |  |  |
| `main_disease_1` | str |  |  |
| `main_disease_2` | str |  |  |
| `main_disease_3` | str |  |  |
| `main_disease_4` | str |  |  |
| `main_disease_5` | str |  |  |
| `surgery_1` | str |  |  |
| `surgery_2` | str |  |  |
| `surgery_3` | str |  |  |
| `chief_complaint` | str |  |  |
| `present_illness` | str |  |  |
| `past_history` | str |  |  |
| `family_history` | str |  |  |
| `life_history` | str |  |  |
| `main_condition` | str |  |  |
| `main_exam_finding` | str |  |  |
| `problem_list` | str |  |  |
| `hospital_course` | str |  |  |
| `prescription` | str |  |  |
| `future_plan` | str |  |  |
| `comment` | str |  |  |
| `referral_answerable` | int |  |  |
| `condition_1` | str |  |  |
| `disease_1` | str |  |  |
| `purpose_1` | str |  |  |
| `past_family_1` | str |  |  |
| `course_exam_1` | str |  |  |
| `treatment_1` | str |  |  |
| `current_med_1` | str |  |  |
| `note_1` | str |  |  |
| `annotation_comment_1` | str |  |  |
| `condition_2` | str |  |  |
| `disease_2` | str |  |  |
| `purpose_2` | str |  |  |
| `past_family_2` | str |  |  |
| `course_exam_2` | str |  |  |
| `treatment_2` | str |  |  |
| `current_med_2` | str |  |  |
| `note_2` | str |  |  |
| `annotation_comment_2` | str |  |  |
| `condition_3` | str |  |  |
| `disease_3` | str |  |  |
| `purpose_3` | str |  |  |
| `past_family_3` | str |  |  |
| `course_exam_3` | str |  |  |
| `treatment_3` | str |  |  |
| `current_med_3` | str |  |  |
| `note_3` | str |  |  |
| `annotation_comment_3` | str |  |  |
| `condition_4` | str |  |  |
| `disease_4` | str |  |  |
| `purpose_4` | str |  |  |
| `past_family_4` | str |  |  |
| `course_exam_4` | str |  |  |
| `treatment_4` | str |  |  |
| `current_med_4` | str |  |  |
| `note_4` | str |  |  |
| `annotation_comment_4` | str |  |  |

### レスポンス

**形式:** DischargeSummaryResponse

#### **モデル:** DischargeSummaryResponse

| フィールド | 型 | 必須 | 説明 |
|---|---|:--:|---|
| `karte_id` | int | Y |  |
| `registered_type` | str | Y |  |
| `registered_at` | datetime | Y |  |
| `registered_by` | int | Y |  |
| `patient_name` | str | Y |  |
| `patient_id` | str | Y |  |
| `taiin_summary_answerable` | int |  |  |
| `main_disease_1` | str |  |  |
| `main_disease_2` | str |  |  |
| `main_disease_3` | str |  |  |
| `main_disease_4` | str |  |  |
| `main_disease_5` | str |  |  |
| `surgery_1` | str |  |  |
| `surgery_2` | str |  |  |
| `surgery_3` | str |  |  |
| `chief_complaint` | str |  |  |
| `present_illness` | str |  |  |
| `past_history` | str |  |  |
| `family_history` | str |  |  |
| `life_history` | str |  |  |
| `main_condition` | str |  |  |
| `main_exam_finding` | str |  |  |
| `problem_list` | str |  |  |
| `hospital_course` | str |  |  |
| `prescription` | str |  |  |
| `future_plan` | str |  |  |
| `comment` | str |  |  |
| `referral_answerable` | int |  |  |
| `condition_1` | str |  |  |
| `disease_1` | str |  |  |
| `purpose_1` | str |  |  |
| `past_family_1` | str |  |  |
| `course_exam_1` | str |  |  |
| `treatment_1` | str |  |  |
| `current_med_1` | str |  |  |
| `note_1` | str |  |  |
| `annotation_comment_1` | str |  |  |
| `condition_2` | str |  |  |
| `disease_2` | str |  |  |
| `purpose_2` | str |  |  |
| `past_family_2` | str |  |  |
| `course_exam_2` | str |  |  |
| `treatment_2` | str |  |  |
| `current_med_2` | str |  |  |
| `note_2` | str |  |  |
| `annotation_comment_2` | str |  |  |
| `condition_3` | str |  |  |
| `disease_3` | str |  |  |
| `purpose_3` | str |  |  |
| `past_family_3` | str |  |  |
| `course_exam_3` | str |  |  |
| `treatment_3` | str |  |  |
| `current_med_3` | str |  |  |
| `note_3` | str |  |  |
| `annotation_comment_3` | str |  |  |
| `condition_4` | str |  |  |
| `disease_4` | str |  |  |
| `purpose_4` | str |  |  |
| `past_family_4` | str |  |  |
| `course_exam_4` | str |  |  |
| `treatment_4` | str |  |  |
| `current_med_4` | str |  |  |
| `note_4` | str |  |  |
| `annotation_comment_4` | str |  |  |
| `id` | int | Y |  |

---
## DELETE /discharge_summaries/{id}

**説明:** 削除

### リクエスト

#### パスパラメータ

| パラメータ | 型 | 必須 | 説明 |
|---|---|:--:|---|
| `id` |  | Y |  |

### レスポンス

**形式:** dict

**モデル:**  Any
# stroke_patients

## POST /stroke_patients/

**説明:** 新規登録

### リクエスト

None
#### ボディ (StrokePatientSchema)

| フィールド | 型 | 必須 | 説明 |
|---|---|:--:|---|
| `karte_id` | int | Y |  |
| `registered_type` | str | Y |  |
| `registered_at` | datetime | Y |  |
| `registered_by` | int | Y |  |
| `age` | int |  |  |
| `sex` | int |  |  |
| `sitename` | str |  |  |
| `onset_dt` | date |  |  |
| `onset_tm` | time |  |  |
| `arrival_tm` | int |  |  |
| `admit_dt` | date |  |  |
| `admit_proc` | int |  |  |
| `admit_route` | int |  |  |
| `diagnosis` | int |  |  |
| `duration` | str |  |  |
| `subtype` | int |  |  |
| `location` | str |  |  |
| `culprit` | str |  |  |
| `culprit_ves` | str |  |  |
| `emb_source` | str |  |  |
| `symptom` | str |  |  |
| `rf_smoking` | int |  |  |
| `rf_alcohol` | int |  |  |
| `rf_allergy` | int |  |  |
| `rf_ht` | int |  |  |
| `rf_dm` | int |  |  |
| `rf_dl` | int |  |  |
| `rf_dialysis` | int |  |  |
| `rf_af` | int |  |  |
| `rf_renal` | int |  |  |
| `mh_stroke` | int |  |  |
| `mh_dementia` | int |  |  |
| `mh_ihd` | int |  |  |
| `pre_mrs` | int |  |  |
| `chief_comp` | str |  |  |
| `present_ill` | str |  |  |
| `hgt` | float |  |  |
| `wgt` | float |  |  |
| `abd_cir` | float |  |  |
| `bp` | str |  |  |
| `sbp` | int |  |  |
| `dbp` | int |  |  |
| `pulse` | int |  |  |
| `murmur` | int |  |  |
| `conscious` | int |  |  |
| `cortical` | int |  |  |
| `motor_dis` | int |  |  |
| `sensory_dis` | int |  |  |
| `nihss` | int |  |  |
| `lab_cbc` | str |  |  |
| `lab_chem` | str |  |  |
| `lab_ddimer` | float |  |  |
| `lab_hscrp` | float |  |  |
| `img_ct` | int |  |  |
| `img_mri` | int |  |  |
| `img_mra` | int |  |  |
| `img_spect` | int |  |  |
| `img_echo` | str |  |  |
| `reperfusion` | int |  |  |
| `rtpa` | int |  |  |
| `evt` | int |  |  |
| `pre_at` | int |  |  |
| `pre_ap` | int |  |  |
| `pre_ac` | int |  |  |
| `in_at` | int |  |  |
| `in_ap` | int |  |  |
| `in_ac` | int |  |  |
| `anti_ht_tx` | int |  |  |
| `progress` | str |  |  |
| `recur` | int |  |  |
| `cv_event` | int |  |  |
| `complication` | int |  |  |
| `dc_outcome` | int |  |  |
| `dc_nihss` | int |  |  |
| `dc_mrs` | int |  |  |
| `dc_dt` | date |  |  |
| `dc_med` | str |  |  |
| `fu_mrs` | int |  |  |
| `fu_recur` | int |  |  |
| `fu_cvevent` | int |  |  |
| `fu_death` | int |  |  |

### レスポンス

**形式:** StrokePatientResponse

#### **モデル:** StrokePatientResponse

| フィールド | 型 | 必須 | 説明 |
|---|---|:--:|---|
| `karte_id` | int | Y |  |
| `registered_type` | str | Y |  |
| `registered_at` | datetime | Y |  |
| `registered_by` | int | Y |  |
| `age` | int |  |  |
| `sex` | int |  |  |
| `sitename` | str |  |  |
| `onset_dt` | date |  |  |
| `onset_tm` | time |  |  |
| `arrival_tm` | int |  |  |
| `admit_dt` | date |  |  |
| `admit_proc` | int |  |  |
| `admit_route` | int |  |  |
| `diagnosis` | int |  |  |
| `duration` | str |  |  |
| `subtype` | int |  |  |
| `location` | str |  |  |
| `culprit` | str |  |  |
| `culprit_ves` | str |  |  |
| `emb_source` | str |  |  |
| `symptom` | str |  |  |
| `rf_smoking` | int |  |  |
| `rf_alcohol` | int |  |  |
| `rf_allergy` | int |  |  |
| `rf_ht` | int |  |  |
| `rf_dm` | int |  |  |
| `rf_dl` | int |  |  |
| `rf_dialysis` | int |  |  |
| `rf_af` | int |  |  |
| `rf_renal` | int |  |  |
| `mh_stroke` | int |  |  |
| `mh_dementia` | int |  |  |
| `mh_ihd` | int |  |  |
| `pre_mrs` | int |  |  |
| `chief_comp` | str |  |  |
| `present_ill` | str |  |  |
| `hgt` | float |  |  |
| `wgt` | float |  |  |
| `abd_cir` | float |  |  |
| `bp` | str |  |  |
| `sbp` | int |  |  |
| `dbp` | int |  |  |
| `pulse` | int |  |  |
| `murmur` | int |  |  |
| `conscious` | int |  |  |
| `cortical` | int |  |  |
| `motor_dis` | int |  |  |
| `sensory_dis` | int |  |  |
| `nihss` | int |  |  |
| `lab_cbc` | str |  |  |
| `lab_chem` | str |  |  |
| `lab_ddimer` | float |  |  |
| `lab_hscrp` | float |  |  |
| `img_ct` | int |  |  |
| `img_mri` | int |  |  |
| `img_mra` | int |  |  |
| `img_spect` | int |  |  |
| `img_echo` | str |  |  |
| `reperfusion` | int |  |  |
| `rtpa` | int |  |  |
| `evt` | int |  |  |
| `pre_at` | int |  |  |
| `pre_ap` | int |  |  |
| `pre_ac` | int |  |  |
| `in_at` | int |  |  |
| `in_ap` | int |  |  |
| `in_ac` | int |  |  |
| `anti_ht_tx` | int |  |  |
| `progress` | str |  |  |
| `recur` | int |  |  |
| `cv_event` | int |  |  |
| `complication` | int |  |  |
| `dc_outcome` | int |  |  |
| `dc_nihss` | int |  |  |
| `dc_mrs` | int |  |  |
| `dc_dt` | date |  |  |
| `dc_med` | str |  |  |
| `fu_mrs` | int |  |  |
| `fu_recur` | int |  |  |
| `fu_cvevent` | int |  |  |
| `fu_death` | int |  |  |
| `id` | int | Y |  |

---
## GET /stroke_patients/{id}

**説明:** IDで1件取得

### リクエスト

#### パスパラメータ

| パラメータ | 型 | 必須 | 説明 |
|---|---|:--:|---|
| `id` |  | Y |  |

### レスポンス

**形式:** StrokePatientResponse

#### **モデル:** StrokePatientResponse

| フィールド | 型 | 必須 | 説明 |
|---|---|:--:|---|
| `karte_id` | int | Y |  |
| `registered_type` | str | Y |  |
| `registered_at` | datetime | Y |  |
| `registered_by` | int | Y |  |
| `age` | int |  |  |
| `sex` | int |  |  |
| `sitename` | str |  |  |
| `onset_dt` | date |  |  |
| `onset_tm` | time |  |  |
| `arrival_tm` | int |  |  |
| `admit_dt` | date |  |  |
| `admit_proc` | int |  |  |
| `admit_route` | int |  |  |
| `diagnosis` | int |  |  |
| `duration` | str |  |  |
| `subtype` | int |  |  |
| `location` | str |  |  |
| `culprit` | str |  |  |
| `culprit_ves` | str |  |  |
| `emb_source` | str |  |  |
| `symptom` | str |  |  |
| `rf_smoking` | int |  |  |
| `rf_alcohol` | int |  |  |
| `rf_allergy` | int |  |  |
| `rf_ht` | int |  |  |
| `rf_dm` | int |  |  |
| `rf_dl` | int |  |  |
| `rf_dialysis` | int |  |  |
| `rf_af` | int |  |  |
| `rf_renal` | int |  |  |
| `mh_stroke` | int |  |  |
| `mh_dementia` | int |  |  |
| `mh_ihd` | int |  |  |
| `pre_mrs` | int |  |  |
| `chief_comp` | str |  |  |
| `present_ill` | str |  |  |
| `hgt` | float |  |  |
| `wgt` | float |  |  |
| `abd_cir` | float |  |  |
| `bp` | str |  |  |
| `sbp` | int |  |  |
| `dbp` | int |  |  |
| `pulse` | int |  |  |
| `murmur` | int |  |  |
| `conscious` | int |  |  |
| `cortical` | int |  |  |
| `motor_dis` | int |  |  |
| `sensory_dis` | int |  |  |
| `nihss` | int |  |  |
| `lab_cbc` | str |  |  |
| `lab_chem` | str |  |  |
| `lab_ddimer` | float |  |  |
| `lab_hscrp` | float |  |  |
| `img_ct` | int |  |  |
| `img_mri` | int |  |  |
| `img_mra` | int |  |  |
| `img_spect` | int |  |  |
| `img_echo` | str |  |  |
| `reperfusion` | int |  |  |
| `rtpa` | int |  |  |
| `evt` | int |  |  |
| `pre_at` | int |  |  |
| `pre_ap` | int |  |  |
| `pre_ac` | int |  |  |
| `in_at` | int |  |  |
| `in_ap` | int |  |  |
| `in_ac` | int |  |  |
| `anti_ht_tx` | int |  |  |
| `progress` | str |  |  |
| `recur` | int |  |  |
| `cv_event` | int |  |  |
| `complication` | int |  |  |
| `dc_outcome` | int |  |  |
| `dc_nihss` | int |  |  |
| `dc_mrs` | int |  |  |
| `dc_dt` | date |  |  |
| `dc_med` | str |  |  |
| `fu_mrs` | int |  |  |
| `fu_recur` | int |  |  |
| `fu_cvevent` | int |  |  |
| `fu_death` | int |  |  |
| `id` | int | Y |  |

---
## GET /stroke_patients/

**説明:** 一覧取得

### リクエスト

#### クエリパラメータ

| パラメータ | 型 | 必須 | 説明 |
|---|---|:--:|---|
| `skip` |  |  |  |
| `limit` |  |  |  |

### レスポンス

**形式:** List[StrokePatientResponse]

#### **モデル:** StrokePatientResponse

| フィールド | 型 | 必須 | 説明 |
|---|---|:--:|---|
| `karte_id` | int | Y |  |
| `registered_type` | str | Y |  |
| `registered_at` | datetime | Y |  |
| `registered_by` | int | Y |  |
| `age` | int |  |  |
| `sex` | int |  |  |
| `sitename` | str |  |  |
| `onset_dt` | date |  |  |
| `onset_tm` | time |  |  |
| `arrival_tm` | int |  |  |
| `admit_dt` | date |  |  |
| `admit_proc` | int |  |  |
| `admit_route` | int |  |  |
| `diagnosis` | int |  |  |
| `duration` | str |  |  |
| `subtype` | int |  |  |
| `location` | str |  |  |
| `culprit` | str |  |  |
| `culprit_ves` | str |  |  |
| `emb_source` | str |  |  |
| `symptom` | str |  |  |
| `rf_smoking` | int |  |  |
| `rf_alcohol` | int |  |  |
| `rf_allergy` | int |  |  |
| `rf_ht` | int |  |  |
| `rf_dm` | int |  |  |
| `rf_dl` | int |  |  |
| `rf_dialysis` | int |  |  |
| `rf_af` | int |  |  |
| `rf_renal` | int |  |  |
| `mh_stroke` | int |  |  |
| `mh_dementia` | int |  |  |
| `mh_ihd` | int |  |  |
| `pre_mrs` | int |  |  |
| `chief_comp` | str |  |  |
| `present_ill` | str |  |  |
| `hgt` | float |  |  |
| `wgt` | float |  |  |
| `abd_cir` | float |  |  |
| `bp` | str |  |  |
| `sbp` | int |  |  |
| `dbp` | int |  |  |
| `pulse` | int |  |  |
| `murmur` | int |  |  |
| `conscious` | int |  |  |
| `cortical` | int |  |  |
| `motor_dis` | int |  |  |
| `sensory_dis` | int |  |  |
| `nihss` | int |  |  |
| `lab_cbc` | str |  |  |
| `lab_chem` | str |  |  |
| `lab_ddimer` | float |  |  |
| `lab_hscrp` | float |  |  |
| `img_ct` | int |  |  |
| `img_mri` | int |  |  |
| `img_mra` | int |  |  |
| `img_spect` | int |  |  |
| `img_echo` | str |  |  |
| `reperfusion` | int |  |  |
| `rtpa` | int |  |  |
| `evt` | int |  |  |
| `pre_at` | int |  |  |
| `pre_ap` | int |  |  |
| `pre_ac` | int |  |  |
| `in_at` | int |  |  |
| `in_ap` | int |  |  |
| `in_ac` | int |  |  |
| `anti_ht_tx` | int |  |  |
| `progress` | str |  |  |
| `recur` | int |  |  |
| `cv_event` | int |  |  |
| `complication` | int |  |  |
| `dc_outcome` | int |  |  |
| `dc_nihss` | int |  |  |
| `dc_mrs` | int |  |  |
| `dc_dt` | date |  |  |
| `dc_med` | str |  |  |
| `fu_mrs` | int |  |  |
| `fu_recur` | int |  |  |
| `fu_cvevent` | int |  |  |
| `fu_death` | int |  |  |
| `id` | int | Y |  |

---
## PUT /stroke_patients/{id}

**説明:** 更新

### リクエスト

#### パスパラメータ

| パラメータ | 型 | 必須 | 説明 |
|---|---|:--:|---|
| `id` |  | Y |  |

#### ボディ (StrokePatientUpdate)

| フィールド | 型 | 必須 | 説明 |
|---|---|:--:|---|
| `karte_id` | int |  |  |
| `registered_type` | str |  |  |
| `registered_at` | datetime |  |  |
| `registered_by` | int |  |  |
| `age` | int |  |  |
| `sex` | int |  |  |
| `sitename` | str |  |  |
| `onset_dt` | date |  |  |
| `onset_tm` | time |  |  |
| `arrival_tm` | int |  |  |
| `admit_dt` | date |  |  |
| `admit_proc` | int |  |  |
| `admit_route` | int |  |  |
| `diagnosis` | int |  |  |
| `duration` | str |  |  |
| `subtype` | int |  |  |
| `location` | str |  |  |
| `culprit` | str |  |  |
| `culprit_ves` | str |  |  |
| `emb_source` | str |  |  |
| `symptom` | str |  |  |
| `rf_smoking` | int |  |  |
| `rf_alcohol` | int |  |  |
| `rf_allergy` | int |  |  |
| `rf_ht` | int |  |  |
| `rf_dm` | int |  |  |
| `rf_dl` | int |  |  |
| `rf_dialysis` | int |  |  |
| `rf_af` | int |  |  |
| `rf_renal` | int |  |  |
| `mh_stroke` | int |  |  |
| `mh_dementia` | int |  |  |
| `mh_ihd` | int |  |  |
| `pre_mrs` | int |  |  |
| `chief_comp` | str |  |  |
| `present_ill` | str |  |  |
| `hgt` | float |  |  |
| `wgt` | float |  |  |
| `abd_cir` | float |  |  |
| `bp` | str |  |  |
| `sbp` | int |  |  |
| `dbp` | int |  |  |
| `pulse` | int |  |  |
| `murmur` | int |  |  |
| `conscious` | int |  |  |
| `cortical` | int |  |  |
| `motor_dis` | int |  |  |
| `sensory_dis` | int |  |  |
| `nihss` | int |  |  |
| `lab_cbc` | str |  |  |
| `lab_chem` | str |  |  |
| `lab_ddimer` | float |  |  |
| `lab_hscrp` | float |  |  |
| `img_ct` | int |  |  |
| `img_mri` | int |  |  |
| `img_mra` | int |  |  |
| `img_spect` | int |  |  |
| `img_echo` | str |  |  |
| `reperfusion` | int |  |  |
| `rtpa` | int |  |  |
| `evt` | int |  |  |
| `pre_at` | int |  |  |
| `pre_ap` | int |  |  |
| `pre_ac` | int |  |  |
| `in_at` | int |  |  |
| `in_ap` | int |  |  |
| `in_ac` | int |  |  |
| `anti_ht_tx` | int |  |  |
| `progress` | str |  |  |
| `recur` | int |  |  |
| `cv_event` | int |  |  |
| `complication` | int |  |  |
| `dc_outcome` | int |  |  |
| `dc_nihss` | int |  |  |
| `dc_mrs` | int |  |  |
| `dc_dt` | date |  |  |
| `dc_med` | str |  |  |
| `fu_mrs` | int |  |  |
| `fu_recur` | int |  |  |
| `fu_cvevent` | int |  |  |
| `fu_death` | int |  |  |

### レスポンス

**形式:** StrokePatientResponse

#### **モデル:** StrokePatientResponse

| フィールド | 型 | 必須 | 説明 |
|---|---|:--:|---|
| `karte_id` | int | Y |  |
| `registered_type` | str | Y |  |
| `registered_at` | datetime | Y |  |
| `registered_by` | int | Y |  |
| `age` | int |  |  |
| `sex` | int |  |  |
| `sitename` | str |  |  |
| `onset_dt` | date |  |  |
| `onset_tm` | time |  |  |
| `arrival_tm` | int |  |  |
| `admit_dt` | date |  |  |
| `admit_proc` | int |  |  |
| `admit_route` | int |  |  |
| `diagnosis` | int |  |  |
| `duration` | str |  |  |
| `subtype` | int |  |  |
| `location` | str |  |  |
| `culprit` | str |  |  |
| `culprit_ves` | str |  |  |
| `emb_source` | str |  |  |
| `symptom` | str |  |  |
| `rf_smoking` | int |  |  |
| `rf_alcohol` | int |  |  |
| `rf_allergy` | int |  |  |
| `rf_ht` | int |  |  |
| `rf_dm` | int |  |  |
| `rf_dl` | int |  |  |
| `rf_dialysis` | int |  |  |
| `rf_af` | int |  |  |
| `rf_renal` | int |  |  |
| `mh_stroke` | int |  |  |
| `mh_dementia` | int |  |  |
| `mh_ihd` | int |  |  |
| `pre_mrs` | int |  |  |
| `chief_comp` | str |  |  |
| `present_ill` | str |  |  |
| `hgt` | float |  |  |
| `wgt` | float |  |  |
| `abd_cir` | float |  |  |
| `bp` | str |  |  |
| `sbp` | int |  |  |
| `dbp` | int |  |  |
| `pulse` | int |  |  |
| `murmur` | int |  |  |
| `conscious` | int |  |  |
| `cortical` | int |  |  |
| `motor_dis` | int |  |  |
| `sensory_dis` | int |  |  |
| `nihss` | int |  |  |
| `lab_cbc` | str |  |  |
| `lab_chem` | str |  |  |
| `lab_ddimer` | float |  |  |
| `lab_hscrp` | float |  |  |
| `img_ct` | int |  |  |
| `img_mri` | int |  |  |
| `img_mra` | int |  |  |
| `img_spect` | int |  |  |
| `img_echo` | str |  |  |
| `reperfusion` | int |  |  |
| `rtpa` | int |  |  |
| `evt` | int |  |  |
| `pre_at` | int |  |  |
| `pre_ap` | int |  |  |
| `pre_ac` | int |  |  |
| `in_at` | int |  |  |
| `in_ap` | int |  |  |
| `in_ac` | int |  |  |
| `anti_ht_tx` | int |  |  |
| `progress` | str |  |  |
| `recur` | int |  |  |
| `cv_event` | int |  |  |
| `complication` | int |  |  |
| `dc_outcome` | int |  |  |
| `dc_nihss` | int |  |  |
| `dc_mrs` | int |  |  |
| `dc_dt` | date |  |  |
| `dc_med` | str |  |  |
| `fu_mrs` | int |  |  |
| `fu_recur` | int |  |  |
| `fu_cvevent` | int |  |  |
| `fu_death` | int |  |  |
| `id` | int | Y |  |

---
## DELETE /stroke_patients/{id}

**説明:** 削除

### リクエスト

#### パスパラメータ

| パラメータ | 型 | 必須 | 説明 |
|---|---|:--:|---|
| `id` |  | Y |  |

### レスポンス

**形式:** dict

**モデル:**  Any