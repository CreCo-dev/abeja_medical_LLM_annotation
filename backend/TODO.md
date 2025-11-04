
## TODO
# 全般
- 設定関係は環境編集に持つ    from dotenv import load_dotenv
    - ユーザー認証のキー 環境変数化 SECRET_KEY = "your-secret-key"  
    - database.py DATABASE_URL
    - utils/logger 使いやすいように変更する
# リファクタリング
- ルーターは1ファイルに統合
- cruds とmodel 統合
- 認証は、utils/security
# 認証
- ユーザーアカウント作成時 
    - login_id の重複チェック DBはユニーク制約が システム的にチェックしていない →する。
    - パスワード 72 文字を超えると 暗号化できない 入力時のチェック処理入れる。
# DB
- 時間経過でDBとの接続が切れていた場合に 再接続する。
# テスト
- テストコード実装(間に合わない場合は手動テストのみとする)