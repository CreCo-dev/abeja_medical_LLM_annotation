
## TODO
- 退院時データと脳卒中データの router作成
- V2のデータベースわける
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

