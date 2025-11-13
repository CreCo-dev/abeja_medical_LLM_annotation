
## TODO
- テストコード
- スキーマから API設計書出力 生成できないエンドポイントも生成
- V1とV2でデータベース分ける
- DB rootでログインしているが userがよいか。 権限周り確認
- config.py  docker-compose.ymlで設定しているものはハードコーディング不要

- 退院時データ PDFから項目抽出、 確信度とコメントも、

- 複数テーブルをJoinして結果を返すrouterの作成 → カルテ一覧 想定

- 認証 ユーザーアカウント作成時 
    - login_id の重複チェック DBはユニーク制約が システム的にチェックしていない →する。
    - パスワード 72 文字を超えると 暗号化できない 入力時のチェック処理入れる。
    - ログイン以外のあくせすはデフォルトで認証必要にする

- DB 時間経過でDBとの接続が切れていた場合に 再接続する。
- 設定関係は環境変数にもたせた動作確認
    - 本番環境を想定したテスト .env

- 画面のプロタイプが完成後
    - 表示項目に合わせてDB･API変更
    - ボタン等の機能に合わせてAPI作成
 
- チケット
    - 外部設計確認 データ取り込み
    - 外部設計確認 データ出力
    - 外部設計確認 画面
    - DB設計書(詳細版)
    - API設計書
    - アーキテクチャ設計書
        インフラやFrontendもからみそうですが
        以下の図と 説明文くらいがあれば良いイメージでしょうか。
        https://marimokko.atlassian.net/wiki/spaces/ani/whiteboard/305364993?atl_f=PAGETREE

    MCPServer しらべる。

    - セキュリティ設計書
        インフラやFrontendもからみそうですが、特にインフラの要素が大きそうなイメージです。
        バックエンドだとログイン認証くらいでしょうか。

discharge_summary.py
    registered_type のEnum化
    Enum 型を使うとバリデーションや一貫性が高まります。例：Column(Enum(RegisteredTypeEnum))

discharge_summary_crud.py
    karte_id + registered_type の UniqueConstraint に違反した場合に IntegrityError
        try/exceptで補足し、HTTP 409(CONFLICT)を返すのが親切

## LOCAL
cd v2_input_annotation
docker compose up --build

http://localhost:82/docs

- ユーザーアカウント 1件登録

curl -X 'POST' \
  'http://localhost:70/user_accounts'   -H 'accept: application/json' -H 'Content-Type: application/json' \
   -d '{  "login_id": "test_id_1"
         ,"password": "test_password_1"
         ,"name": "test_name_1"}'

- カルテ 1件登録
curl -X 'POST' \
  'http://localhost:82/kartes/'   -H 'accept: application/json' -H 'Content-Type: application/json' \
  -d '{ "karte_data_id": "123",
        "karte_name": "test_name",
       "data_type": "DC"
      }'

→レスポンスのIDを記録し、以下の"karte_id"の値として設定する。

- 退院時サマリ 1件
curl -X 'POST' \
  'http://localhost:82/discharge_summaries/'   -H 'accept: application/json'   -H 'Content-Type: application/json' \
  -d '{  "karte_id": 1,
         "registered_type": "SUB",
         "registered_at": "2025-11-11T14:07:34.252Z",
         "registered_by": 1,
         "patient_name": "string",
         "patient_id": "string"
      }'

- カルテ 一覧
curl -X 'GET' \
  'http://localhost:82/kartes/?skip=0&limit=100' \
  -H 'accept: application/json'

- 退院時サマリ 一覧
curl -X 'GET' \
  'http://localhost:82/discharge_summaries/?skip=0&limit=100' \
  -H 'accept: application/json'


## TEST
cd v2_input_annotation
docker compose -f docker-compose.test.yml up --build --abort-on-container-exit



select * from kartes
select * from discharge_summaries
select * from stroke_patients;
select * from user_accounts;

delete from discharge_summaries;
delete from stroke_patients;
delete from kartes;
delete from user_accounts;

ALTER TABLE discharge_summaries AUTO_INCREMENT = 1;
ALTER TABLE stroke_patients AUTO_INCREMENT = 1;
ALTER TABLE kartes AUTO_INCREMENT = 1;
ALTER TABLE user_accounts AUTO_INCREMENT = 1;

drop table discharge_summaries;
drop table stroke_patients;
drop table kartes;
drop table user_accounts;


insert into user_accounts values (0,1,1,'test_name')
insert into kartes values (0,1,'test_name','DC',null)
insert into discharge_summaries values (0,1,'LLM','DC',null)

INSERT INTO `discharge_summaries`
(`karte_id`, `registered_type`, `registered_at`, `registered_by`,patient_name,patient_id)
VALUES
('1', 'LLM', '2025-11-09 10:30:00', 1,'test_name','test_id')
INSERT INTO `discharge_summaries`
(`karte_id`, `registered_type`, `registered_at`, `registered_by`,patient_name,patient_id)
VALUES
('1', 'MAIN', '2025-11-09 10:30:00', 1,'test_name','test_id')




http://localhost:82/docs

insert into user_accounts values (0,1,1,'test_name')
insert into kartes values (0,1,'test_name','DC',null)
insert into discharge_summaries values (0,1,'LLM','DC',null)




curl -X 'GET' \
  'http://localhost:82/discharge_summaries/?skip=0&limit=100' \
  -H 'accept: application/json'


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



