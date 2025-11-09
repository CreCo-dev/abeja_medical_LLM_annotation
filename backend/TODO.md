
## TODO
- 退院時データと脳卒中データの router作成

- 複数テーブルをJoinして結果を返すrouterの作成  カルテ一覧

- 設定関係は環境変数にもたせた動作確認

- 認証 ユーザーアカウント作成時 
    - login_id の重複チェック DBはユニーク制約が システム的にチェックしていない →する。
    - パスワード 72 文字を超えると 暗号化できない 入力時のチェック処理入れる。

- DB 時間経過でDBとの接続が切れていた場合に 再接続する。

- テスト テストコード実装(間に合わない場合は手動テストのみとする)

## TEST
select * FROM user_accounts
delete from user_accounts

curl http://localhost:82/

→"ok"%

curl -X GET http://localhost:82/user_accounts


curl -X POST http://localhost:82/user_accounts -H  'Content-Type: application/json' -d '{"login_id": "test_id_3","password": "test_password_3","name": "test_name_3"}'

→{"id":XX,"login_id":"XXXXXX","name":"XXXXXX"}% 

curl -X GET http://localhost:82/user_accounts_with_auth/me

(認証失敗)
→{"detail":"Not authenticated"}%

(ログイン)
curl -X POST http://localhost:82/login \
     -H 'Content-Type: application/x-www-form-urlencoded' \
     -d 'username=test_id_3&password=test_password_3'

(ログイン成功トークン取得)
→{"access_token":"ey･･････.･･････,"token_type":"bearer"}%
(上記で取得したaccess_tokenを利用する)
curl -X GET http://localhost:82/user_accounts_with_auth/me -H 'Authorization: Bearer ey･･････.･･････'

(認証成功)
→{"id":XX,"login_id":"XXXXXX","name":"XXXXXX"}%


curl -X GET http://localhost:82/user_accounts_with_auth/me -H 'Authorization: Bearer eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJzdWIiOiJ0ZXN0X2lkXzMiLCJleHAiOjE3NjI1OTE3NTV9.40d0kxqFUZBu4vI4vKTMRLkPpidmGDYWk6l-0TSEZ6c'


## メモ
リレーションの方法について
どちらのケースがよいか、複数の設計手法からメリデリおしえて、
また他によい設計方法があれば。

1．
StrokePatient やDischargeSummaryにkarte_idをもたせて
親テーブルである Karte とリレーションする
2．
親テーブルである Karte に
StrokePatient_id やDischargeSummary_id
をもたせてリレーションする。

※
Karte1レコードに対して、
StrokePatient、DischargeSummaryともに
RegisteredType別に最大4レコードしか存在しない。
RegisteredType
    LLM = "LLMが生成した初期データ"
    MAIN = "主担当アノテーター"
    SUB = "副担当アノテーター"
    CHK = "Check者のデータ"


FastAPIを利用ししたAPIでは、
カルテ一覧の情報に、Karteのレコードのカラムだけでなく
StrokePatientの、registered_atや、registered_byや
DischargeSummaryの、registered_atや、registered_byを
一緒に提供する可能性がたかい
その場合、sqlalchemy.orm をりようして
Karteのリレーションを利用して、StrokePatientやDischargeSummaryにアクセスした場合
必要なregistered_atや、registered_byだけでなく、他のサイズの大きいからむも取得してしまい
リソースのコストが高くならないか？
ORMを活用せず、複数テーブルを結合し、特定のカラムだけをSelectするような個別のSQLを実装する必要があるか。
画面に合わせてDB設計(Karteに、registered_atや、registered_bを何個もからむとしてもたせる)したほうがよいか。


with_entities() or load_only() を活用した軽量クエリのサンプルをもう一度
ただし以下の条件で。

欲しい情報は Karteの全カラム 
と{
 KarteのDataTypeがSTR = "脳卒中患者"の場合は、
  →StrokePatientの registered_atとregistered_by について RegisteredTypeごとの値
  
 KarteのDataTypeがDC = "退院時サマリー"の場合は、
  →DischargeSummaryの registered_atとregistered_by について RegisteredTypeごとの値
} → 2*4項目

ただし、StrokePatientやDischargeSummaryのレコードがない場合はNullとする。





```mermaid
erDiagram
    Karte ||--o{ DischargeSummary : "カルテID"
    Karte ||--o{ StrokePatient : "カルテID"

    Karte {
        int id PK "ID"
        string karte_id "カルテID"
        string data_type "データタイプ (退院時サマリー / 脳卒中患者)"
        String status "ステータス"
    }
    DischargeSummary {
        int id PK "ID"
        string karte_id FK,UK"カルテID"
        string registered_type UK "登録タイプ(LLM,MAIN,SUB,CHK)"
    }
    StrokePatient {
        int id PK "ID"
        string karte_id FK,UK"カルテID"
        string registered_type UK "登録タイプ(LLM,MAIN,SUB,CHK)"
    }
    USER_ACCOUNTS {
        int id PK "ID"
        string login_id UK "ログインID"
        string name "氏名"
    }

```
