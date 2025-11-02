This is a [Next.js](https://nextjs.org) project bootstrapped with [`create-next-app`](https://nextjs.org/docs/app/api-reference/cli/create-next-app).

## Getting Started

First, run the development server:

```bash
npm run dev
# or
yarn dev
# or
pnpm dev
# or
bun dev
```

Open [http://localhost:3000](http://localhost:3000) with your browser to see the result.

You can start editing the page by modifying `app/page.tsx`. The page auto-updates as you edit the file.

This project uses [`next/font`](https://nextjs.org/docs/app/building-your-application/optimizing/fonts) to automatically optimize and load [Geist](https://vercel.com/font), a new font family for Vercel.

## Learn More

To learn more about Next.js, take a look at the following resources:

- [Next.js Documentation](https://nextjs.org/docs) - learn about Next.js features and API.
- [Learn Next.js](https://nextjs.org/learn) - an interactive Next.js tutorial.

You can check out [the Next.js GitHub repository](https://github.com/vercel/next.js) - your feedback and contributions are welcome!

## Deploy on Vercel

The easiest way to deploy your Next.js app is to use the [Vercel Platform](https://vercel.com/new?utm_medium=default-template&filter=next.js&utm_source=create-next-app&utm_campaign=create-next-app-readme) from the creators of Next.js.

Check out our [Next.js deployment documentation](https://nextjs.org/docs/app/building-your-application/deploying) for more details.


# フロントエンド

開発環境（ローカル）
前提

Docker Desktop が起動していること

Node.js 20+ / npm がインストール済み

Windows の場合は PowerShell か cmd

Backend（FastAPI + MySQL）
# リポジトリ直下
docker compose up -d


# docker compose up -d で起動しない場合
まず DBだけ先に起動→安定するのを待つ

cd C:\Users\youyouryou\Desktop\abeja_medical_LLM_annotation
docker compose up -d db
docker compose logs -f db   # 「ready for connections」が出るまで眺める（Ctrl+Cで抜ける）

その後 バックエンドを再起動
 docker compose up -d backend
または
 docker compose restart backend_fastapi_sample



# 状態確認
docker compose ps

docker compose logs -f

docker compose down

FastAPI の自動ドキュメントは **http://localhost:80/docs**（Swagger UI）です。

Frontend（Next.js）
cd frontend
# 初回のみ
npm i
# 環境変数
  PowerShell: cp .env.example .env.local
  cmd:        copy .env.example .env.local
  Devサーバ
npm run dev → http://localhost:3000 をURL入力


# 環境変数
frontend/.env.local
 
 例：
NEXT_PUBLIC_API_BASE_URL=http://localhost:80

NEXT_PUBLIC_ で始まる変数はクライアント（ブラウザ）にバンドルされます（公開前提の値のみ）。 


# 動作確認（Quick Verify）

http://localhost:80/docs
 が開く（バックエンド起動確認） 
fastapi.tiangolo.com

http://localhost:3000
 が表示される
ブラウザのコンソールで文字列が表示されるので、それをクリック
→ OKなのが出るのを確認する。

トラブルシュート

3306番ポートが使用中で DB が起動できない → 既存 MySQL を停止するか、docker-compose.yml の ports を 3307:3306 に変更

フロントから 405（Method Not Allowed） → ブラウザURL直打ちは GET になるため、/sample_post には POST で送る

フロントから BE へ届かない → NEXT_PUBLIC_API_BASE_URL 値、rewrites 設定、npm run dev の再起動を確認