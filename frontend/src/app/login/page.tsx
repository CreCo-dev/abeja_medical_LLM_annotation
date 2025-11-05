"use client";

import { useState, FormEvent } from "react";
import { useRouter } from "next/navigation";
import { apiPost } from "@/lib/api";
import { saveToken, clearToken } from "@/lib/auth";

export default function LoginPage() {
  const [username, setUsername] = useState("");
  const [password, setPassword] = useState("");
  const [err, setErr] = useState<string | null>(null);
  const [loading, setLoading] = useState(false);
  const router = useRouter();

  async function onSubmit(e: FormEvent) {
    e.preventDefault();
    setErr(null);
    setLoading(true);
    try {
      const data = await apiPost<{ access_token: string; token_type: string }>(
        "/token",
        { username, password },
        { form: true }
      );
      saveToken(data.access_token);
      router.push("/annotation");
    } catch (e: any) {
      clearToken();
      setErr(e?.message ?? "ログインに失敗しました");
    } finally {
      setLoading(false);
    }
  }

  return (
    <div className="min-h-[100dvh] grid place-items-center bg-slate-50">
      <form
        onSubmit={onSubmit}
        className="w-[min(420px,90vw)] rounded-2xl bg-white p-6 shadow-lg space-y-4 border"
      >
        <h1 className="text-2xl font-semibold">ログイン</h1>

        <label className="block space-y-1">
          <span className="text-sm text-slate-600">ログインID</span>
          <input
            className="w-full rounded-xl border px-3 py-2 outline-none focus:ring-2"
            value={username}
            onChange={(e) => setUsername(e.target.value)}
            autoComplete="username"
            required
          />
        </label>

        <label className="block space-y-1">
          <span className="text-sm text-slate-600">パスワード</span>
          <input
            type="password"
            className="w-full rounded-xl border px-3 py-2 outline-none focus:ring-2"
            value={password}
            onChange={(e) => setPassword(e.target.value)}
            autoComplete="current-password"
            required
          />
        </label>

        {err && (
          <p className="text-sm text-red-600 bg-red-50 border border-red-200 rounded-lg p-2">
            {err}
          </p>
        )}

        <button
          type="submit"
          disabled={loading}
          className="w-full rounded-xl bg-sky-600 text-white py-2.5 font-medium hover:opacity-90 disabled:opacity-50"
        >
          {loading ? "サインイン中..." : "サインイン"}
        </button>
      </form>
    </div>
  );
}
