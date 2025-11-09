// frontend/src/app/login/page.tsx
"use client";

import { useState } from "react";
import { useRouter } from "next/navigation";
import { loginAndGetToken, saveToken, clearToken } from "@/lib/api";

export default function LoginPage() {
  const router = useRouter();
  const [loginId, setLoginId] = useState("");
  const [password, setPassword] = useState("");
  const [busy, setBusy] = useState(false);
  const [error, setError] = useState<string | null>(null);

  async function onSubmit(e: React.FormEvent) {
    e.preventDefault();
    setError(null);
    setBusy(true);
    try {
      const token = await loginAndGetToken({ username: loginId, password });
      saveToken(token);
      router.push("/annotation"); // ログイン後はアノテーションへ
    } catch (err: any) {
      setError(err?.message ?? "Login failed");
      clearToken();
    } finally {
      setBusy(false);
    }
  }

  return (
    <main className="min-h-dvh bg-white">
      {/* 共通ヘッダー（他画面と統一） */}
      <div className="bg-blue-700 text-white px-6 py-4 rounded-b-lg">
        <h1 className="text-2xl font-bold">アノテーション ログイン</h1>
      </div>

      <div className="mx-auto max-w-6xl p-4">
        {/* セクション見出し（他画面と統一） */}
        <div className="mb-3 rounded-md bg-blue-50 text-blue-900 font-semibold px-3 py-2">
          ログイン
        </div>

        {/* 本体カード（他画面と統一） */}
        <div className="rounded-xl border bg-gray-50 p-4">
          <form onSubmit={onSubmit} className="space-y-4">
            <div>
              <label className="block text-sm text-gray-700 mb-1">ログインID</label>
              <input
                value={loginId}
                onChange={(e) => setLoginId(e.target.value)}
                className="w-full rounded-md border p-2 focus:outline-none focus:ring-2 focus:ring-blue-300"
                placeholder="test_login など"
                required
              />
            </div>

            <div>
              <label className="block text-sm text-gray-700 mb-1">パスワード</label>
              <input
                type="password"
                value={password}
                onChange={(e) => setPassword(e.target.value)}
                className="w-full rounded-md border p-2 focus:outline-none focus:ring-2 focus:ring-blue-300"
                placeholder="test_pass など"
                required
              />
            </div>

            {error && (
              <p className="text-sm text-red-600 whitespace-pre-wrap">{error}</p>
            )}

            <button
              type="submit"
              disabled={busy}
              className="w-full rounded-md border border-blue-700 bg-blue-700 px-4 py-2 text-white font-medium hover:bg-blue-800 disabled:opacity-50"
            >
              {busy ? "送信中..." : "ログイン"}
            </button>
          </form>

          <div className="mt-6 text-xs text-gray-600 space-y-1">
            <p>※ 事前に <code>POST /user_accounts</code> でユーザー作成が必要です。</p>
            <p>　例: login_id=<code>test_login</code> / password=<code>test_pass</code></p>
          </div>
        </div>
      </div>
    </main>
  );
}