"use client";

import { useEffect, useMemo, useState } from "react";
import { useRouter } from "next/navigation";
import { apiGet } from "@/lib/api";
import { getToken, clearToken } from "@/lib/auth";

type Item = {
  id: string;
  title: string;
  text: string;
};

const MOCK_ITEMS: Item[] = Array.from({ length: 24 }).map((_, i) => ({
  id: `mock-${i + 1}`,
  title: `レポート #${i + 1}`,
  text:
    "70代男性のハノイの塔プロトコル記録（ダミー）です。観察テキストがここに入ります。" +
    "作業順序、迷い、言い換え、自己修正などを含む想定。",
}));

export default function AnnotationPage() {
  const router = useRouter();
  const [ready, setReady] = useState(false);
  const [selectedId, setSelectedId] = useState(MOCK_ITEMS[0].id);
  const selected = useMemo(
    () => MOCK_ITEMS.find((x) => x.id === selectedId)!,
    [selectedId]
  );

  useEffect(() => {
    const token = getToken();
    if (!token) {
      router.replace("/login");
      return;
    }
    apiGet("/user_accounts_with_auth/me")
      .then(() => setReady(true))
      .catch(() => {
        clearToken();
        router.replace("/login");
      });
  }, [router]);

  const [label, setLabel] = useState<string>("正常");
  const [tags, setTags] = useState<string[]>([]);
  const [note, setNote] = useState("");

  function toggleTag(t: string) {
    setTags((prev) =>
      prev.includes(t) ? prev.filter((x) => x !== t) : [...prev, t]
    );
  }

  function onSave() {
    console.log("save", { id: selectedId, label, tags, note });
    alert("モック保存しました（コンソールに出力）");
  }

  if (!ready) {
    return (
      <div className="min-h-[100dvh] grid place-items-center">
        <p className="text-slate-500">認証確認中...</p>
      </div>
    );
  }

  return (
    <div className="min-h-[100dvh] grid grid-cols-[360px_1fr]">
      <aside className="border-r bg-slate-50/60">
        <div className="px-4 py-3 border-b bg-white">
          <h2 className="font-semibold">アノテーション対象</h2>
        </div>
        <ul className="divide-y max-h-[calc(100dvh-52px)] overflow-auto">
          {MOCK_ITEMS.map((item) => (
            <li
              key={item.id}
              className={
                "p-3 cursor-pointer hover:bg-slate-100 " +
                (selectedId === item.id ? "bg-sky-50" : "")
              }
              onClick={() => setSelectedId(item.id)}
            >
              <div className="text-sm font-medium">{item.title}</div>
              <div className="text-xs text-slate-500 line-clamp-2">
                {item.text}
              </div>
            </li>
          ))}
        </ul>
      </aside>

      <main className="grid grid-rows-[52px_1fr_auto]">
        <div className="px-5 py-3 border-b flex items-center justify-between">
          <div className="font-semibold">詳細</div>
          <button
            className="rounded-lg border px-3 py-1.5 text-sm hover:bg-slate-50"
            onClick={() => router.push("/login")}
            title="ログアウト（トークンは保持したまま）"
          >
            ログインへ
          </button>
        </div>

        <div className="p-5 grid grid-cols-1 gap-5 overflow-auto">
          <section className="space-y-2">
            <h3 className="font-medium">本文</h3>
            <div className="rounded-xl border bg-white p-4 text-sm leading-relaxed whitespace-pre-wrap">
              {selected.text}
            </div>
          </section>

          <section className="space-y-3">
            <h3 className="font-medium">ラベル</h3>
            <div className="flex gap-2 flex-wrap">
              {["正常", "注意", "要確認"].map((name) => (
                <button
                  key={name}
                  onClick={() => setLabel(name)}
                  className={
                    "px-3 py-1.5 rounded-full border text-sm " +
                    (label === name
                      ? "bg-sky-600 text-white border-sky-600"
                      : "bg-white hover:bg-slate-50")
                  }
                >
                  {name}
                </button>
              ))}
            </div>
          </section>

          <section className="space-y-3">
            <h3 className="font-medium">タグ</h3>
            <div className="flex gap-2 flex-wrap">
              {["言い換え", "迷い", "自己修正", "要約", "外れ値"].map((t) => {
                const active = tags.includes(t);
                return (
                  <button
                    key={t}
                    onClick={() => toggleTag(t)}
                    className={
                      "px-3 py-1.5 rounded-full border text-sm " +
                      (active
                        ? "bg-emerald-600 text-white border-emerald-600"
                        : "bg-white hover:bg-slate-50")
                    }
                  >
                    {t}
                  </button>
                );
              })}
            </div>
          </section>

          <section className="space-y-2">
            <h3 className="font-medium">ノート</h3>
            <textarea
              className="w-full h-28 rounded-xl border p-3 text-sm"
              value={note}
              onChange={(e) => setNote(e.target.value)}
              placeholder="補足・理由など"
            />
          </section>
        </div>

        <div className="px-5 py-3 border-t bg-white flex justify-end">
          <button
            onClick={onSave}
            className="px-5 py-2 rounded-xl bg-sky-600 text-white font-medium hover:opacity-90"
          >
            保存（モック）
          </button>
        </div>
      </main>
    </div>
  );
}