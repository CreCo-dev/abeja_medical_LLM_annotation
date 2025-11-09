"use client";

type RefPanels = { data: string; rule: string };
type Field = {
  label: string;
  inputType: "text" | "select";
  value: string;
  options?: string[];
  confidence: 0 | 1 | 2 | 3 | 4;
  reason: string;
  refs: RefPanels;
};

function FieldBlock({ f }: { f: Field }) {
  return (
    <div className="mb-6 rounded-lg border bg-white p-4">
      <div className="mb-2 text-blue-900 font-semibold">{f.label} [必須]</div>
      <div className="flex gap-4">
        <div className="w-1/3 space-y-2">
          {f.inputType === "text" ? (
            <input className="w-full rounded-md border p-2" defaultValue={f.value} />
          ) : (
            <select className="w-full rounded-md border p-2" defaultValue={f.value}>
              {f.options?.map((o) => (
                <option key={o} value={o}>{o}</option>
              ))}
            </select>
          )}
          <select className="w-full rounded-md border p-2" defaultValue={String(f.confidence)}>
            <option value="0">確信度: 0（情報なし）</option>
            <option value="1">確信度: 1（低い確信）</option>
            <option value="2">確信度: 2（やや確信）</option>
            <option value="3">確信度: 3（確信）</option>
            <option value="4">確信度: 4（完全に確信）</option>
          </select>
        </div>

        <div className="w-2/3 space-y-2">
          <div className="text-gray-600 font-medium">📋 判断理由に対するコメント</div>
          <textarea className="h-20 w-full rounded-md border p-2" defaultValue={f.reason} />
          <div className="rounded-md bg-gray-100 p-3">
            <div className="text-gray-600 font-medium mb-1">📄 参照データ(読み取り専用)</div>
            <p className="text-sm text-gray-700">{f.refs.data}</p>
          </div>
          <div className="rounded-md bg-gray-100 p-3">
            <div className="text-gray-600 font-medium mb-1">📖 レジストリルール</div>
            <p className="text-sm text-gray-700">{f.refs.rule}</p>
          </div>
        </div>
      </div>
    </div>
  );
}

export default function DischargeSummaryPage() {
  // --- 左パネル（電子カルテ参照データ）のモック ---
  const leftSections: { title: string; items: { k: string; v: string }[] }[] = [
    {
      title: "患者情報",
      items: [
        { k: "AGE", v: "65歳" },
        { k: "SEX", v: "男性" },
      ],
    },
    {
      title: "入院基本情報",
      items: [
        { k: "SITENAME", v: "中央病院" },
        { k: "ONSET_DT", v: "2025/10/28" },
        { k: "ONSET_TM", v: "6:30頃(起床時)" },
        { k: "ARRIVAL_TM", v: "7:15" },
        { k: "ADMIT_DT", v: "2025/10/28" },
      ],
    },
    {
      title: "診断情報",
      items: [
        { k: "DIAGNOSIS", v: "脳梗塞" },
        { k: "SUBTYPE", v: "心原性脳塞栓症" },
        { k: "CULPRIT_VES", v: "中大脳動脈" },
      ],
    },
    {
      title: "危険因子",
      items: [
        { k: "RF_HT", v: "あり" },
        { k: "RF_DM", v: "なし" },
        { k: "RF_AF", v: "あり" },
      ],
    },
    {
      title: "現病歴・現症",
      items: [
        {
          k: "PRESENT_ILL",
          v: "2025年10月28日朝、起床時(6:30頃)に左半身の脱力。構音障害あり。昨晩23:00就寝。",
        },
        { k: "NIHSS", v: "7点" },
      ],
    },
    {
      title: "治療情報",
      items: [
        { k: "REPERFUSION", v: "なし" },
        { k: "RTPA", v: "なし(発症時刻不明のため)" },
        { k: "EVT", v: "なし" },
      ],
    },
  ];

  // --- 右パネル（入力フォーム）のモック ---
  const fields: Field[] = [
    {
      label: "発症時間 (ONSET_TM)",
      inputType: "text",
      value: "23:00",
      confidence: 3,
      reason: "起床時発症のため、最後に正常確認された時刻(就寝時刻)を採用。",
      refs: {
        data:
          "現病歴: 起床時に症状出現、前夜23:00就寝。起床まで異常の自覚なし。",
        rule:
          "「起床時発症」の場合は最後に正常確認された時刻(就寝時刻)を採用。",
      },
    },
    {
      label: "診断名 (DIAGNOSIS)",
      inputType: "select",
      value: "脳梗塞",
      options: ["脳梗塞", "脳出血", "くも膜下出血", "一過性脳虚血発作"],
      confidence: 4,
      reason: "MRI所見で右MCA領域に高信号、脳梗塞と確定。",
      refs: {
        data: "画像所見: MRIにて右中大脳動脈領域に高信号。",
        rule: "放射線所見で確定診断がなされた場合はその診断を採用。",
      },
    },
    {
      label: "高血圧 (RF_HT)",
      inputType: "select",
      value: "あり",
      options: ["あり", "なし", "不明"],
      confidence: 3,
      reason: "既往歴に高血圧の記載・降圧薬内服あり。",
      refs: {
        data: "既往歴: 高血圧症、内服: アムロジピン5mg。",
        rule: "降圧薬内服中または医師診断ありは「あり」。",
      },
    },
    {
      label: "NIHSS",
      inputType: "text",
      value: "7",
      confidence: 4,
      reason: "入院時の神経学的所見より算出。",
      refs: {
        data: "意識清明、左上下肢不全麻痺、構音障害あり。NIHSS 7点。",
        rule: "0〜42点。入院時の値を記載。",
      },
    },
    {
      label: "t-PA治療 (RTPA)",
      inputType: "select",
      value: "なし",
      options: ["あり", "なし"],
      confidence: 4,
      reason: "起床時発症で発症時刻特定できず適応外。",
      refs: {
        data:
          "治療方針: 起床時発症で発症時刻不明のためt-PA適応外。抗凝固療法開始。",
        rule: "t-PA静注は発症4.5時間以内実施で「あり」。",
      },
    },
  ];

  return (
    <main className="min-h-dvh bg-white">
      <div className="bg-blue-700 text-white px-6 py-4 rounded-b-lg">
        <h1 className="text-2xl font-bold">アノテーション(入力) - 退院時サマリー</h1>
      </div>

      <div className="mx-auto max-w-6xl p-4">
        <div className="grid grid-cols-12 gap-4">
          {/* 左：参照データ */}
          <section className="col-span-12 lg:col-span-5">
            <div className="mb-3 rounded-md bg-blue-50 text-blue-900 font-semibold px-3 py-2">
              電子カルテ参照データ
            </div>
            <div className="rounded-xl border bg-gray-50 p-3">
              {leftSections.map((s) => (
                <div key={s.title} className="mb-4">
                  <h3 className="mb-2 text-gray-700 font-semibold">{s.title}</h3>
                  <div className="divide-y">
                    {s.items.map((it) => (
                      <div key={it.k} className="py-2">
                        <span className="font-medium text-blue-900 mr-2">{it.k}</span>
                        <span className="text-gray-800">{it.v}</span>
                      </div>
                    ))}
                  </div>
                </div>
              ))}
            </div>
          </section>

          {/* 右：入力フォーム */}
          <section className="col-span-12 lg:col-span-7">
            <div className="mb-3 rounded-md bg-blue-50 text-blue-900 font-semibold px-3 py-2">
              入力フォーム
            </div>
            {fields.map((f) => (
              <FieldBlock key={f.label} f={f} />
            ))}
          </section>
        </div>
      </div>
    </main>
  );
}