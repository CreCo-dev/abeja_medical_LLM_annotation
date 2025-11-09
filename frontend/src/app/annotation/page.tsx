"use client";
import { useMemo, useState } from "react";

type TabKey = "discharge" | "stroke";
const TABS: { key: TabKey; label: string; href: string }[] = [
  { key: "discharge", label: "退院時サマリー", href: "/annotation/discharge-summary" },
  { key: "stroke",    label: "脳卒中患者データ", href: "/annotation/stroke" },
];

export default function AnnotationIndex() {
  const [tab, setTab] = useState<TabKey>("discharge");
  const src = useMemo(() => TABS.find(t => t.key === tab)?.href ?? TABS[0].href, [tab]);

  return (
    <main className="min-h-dvh bg-white">
      <div className="bg-blue-700 text-white px-6 py-4 rounded-b-lg">
        <h1 className="text-2xl font-bold">アノテーション</h1>
      </div>

      <div className="mx-auto max-w-6xl p-4">
        {/* タブ */}
        <div className="mb-4 flex gap-2">
          {TABS.map(t => (
            <button
              key={t.key}
              onClick={() => setTab(t.key)}
              className={`rounded-md border px-3 py-2 text-sm font-medium
                ${tab === t.key
                  ? "bg-blue-600 text-white border-blue-600"
                  : "bg-white text-blue-700 border-blue-300 hover:bg-blue-50"}`}
            >
              {t.label}
            </button>
          ))}
        </div>

        {/* 本体：選択中タブのページを “そのまま” 表示 */}
        <div className="h-[calc(100dvh-200px)] overflow-hidden rounded-xl border">
          <iframe
            src={src}
            className="h-full w-full border-0"
            loading="lazy"
          />
        </div>
      </div>
    </main>
  );
}