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

export default function StrokePage() {
  // 左パネル：電子カルテ参照データ（モック）
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
        { k: "ADMIT_PROC", v: "緊急" },
        { k: "ADMIT_ROUTE", v: "救急搬送" },
      ],
    },
    {
      title: "診断情報",
      items: [
        { k: "DIAGNOSIS", v: "脳梗塞" },
        { k: "SUBTYPE", v: "心原性脳塞栓症" },
        { k: "LOCATION", v: "右大脳半球" },
        { k: "CULPRIT_VES", v: "中大脳動脈" },
      ],
    },
    {
      title: "危険因子",
      items: [
        { k: "RF_HT", v: "あり" },
        { k: "RF_DM", v: "なし" },
        { k: "RF_DL", v: "あり" },
        { k: "RF_AF", v: "あり" },
        { k: "MH_STROKE", v: "なし" },
      ],
    },
    {
      title: "現病歴・現症",
      items: [
        {
          k: "PRESENT_ILL",
          v: "起床時に左半身脱力・構音障害。前夜23:00就寝、起床まで異常なし。",
        },
        { k: "CONSCIOUS", v: "JCS I-1" },
        { k: "MOTOR_DIS", v: "左上下肢MMT 4/5" },
        { k: "NIHSS", v: "7点" },
      ],
    },
    {
      title: "検査情報",
      items: [
        { k: "IMG_CT", v: "早期虚血性変化なし" },
        { k: "IMG_MRI", v: "右MCA領域にDWI高信号" },
        { k: "IMG_MRA", v: "右M2閉塞" },
        { k: "LAB_DDIMER", v: "0.8 μg/mL" },
      ],
    },
    {
      title: "治療情報",
      items: [
        { k: "REPERFUSION", v: "なし" },
        { k: "RTPA", v: "なし(発症時刻不明のため)" },
        { k: "EVT", v: "なし" },
        { k: "IN_AC", v: "あり(アピキサバン)" },
      ],
    },
    {
      title: "退院時情報",
      items: [
        { k: "DC_OUTCOME", v: "自宅退院" },
        { k: "DC_NIHSS", v: "3点" },
        { k: "DC_MRS", v: "2" },
        { k: "DC_DT", v: "2025/11/15" },
      ],
    },
  ];

  // 右パネル：入力フォーム（モック）
  const fields: Field[] = [
    {
      label: "発症時間 (ONSET_TM)",
      inputType: "text",
      value: "23:00",
      confidence: 3,
      reason: "起床時発症のため、最後に正常確認された時刻(就寝時刻)を採用。",
      refs: {
        data:
          "現病歴: 起床時(6:30頃)に症状自覚。前夜23:00就寝、起床まで異常なし。",
        rule: "起床時発症では就寝時刻を採用。",
      },
    },
    {
      label: "主病名 (DIAGNOSIS)",
      inputType: "select",
      value: "脳梗塞",
      options: ["脳梗塞", "脳出血", "くも膜下出血", "一過性脳虚血発作"],
      confidence: 4,
      reason: "MRI所見で右MCA領域に高信号、脳梗塞と確定。",
      refs: {
        data: "診断情報: 主病名=脳梗塞、DWI高信号あり。",
        rule: "脳梗塞/脳出血/くも膜下出血/TIA から選択。",
      },
    },
    {
      label: "NIHSS",
      inputType: "text",
      value: "7",
      confidence: 4,
      reason: "来院時の神経学的所見から算出。",
      refs: {
        data: "NIHSS=7、意識JCS I-1、左上下肢MMT 4/5、構音障害あり。",
        rule: "0〜42点。各領域を評価して合算。",
      },
    },
    {
      label: "入院手順 (ADMIT_PROC)",
      inputType: "select",
      value: "緊急",
      options: ["緊急", "予定"],
      confidence: 4,
      reason: "救急搬送による緊急入院。",
      refs: {
        data: "入院経路: 救急搬送。",
        rule: "救急搬送は「緊急」。",
      },
    },
    {
      label: "再灌流療法 (REPERFUSION)",
      inputType: "select",
      value: "なし",
      options: ["あり(t-PA)", "あり(血管内治療)", "あり(両方)", "なし"],
      confidence: 4,
      reason: "発症時刻不明のためt-PA適応外。",
      refs: {
        data: "治療方針: t-PA適応外、抗凝固療法を開始。",
        rule: "t-PAは4.5h以内、血管内治療は8h以内実施で該当。",
      },
    },
  ];

  return (
    <main className="min-h-dvh bg-white">
      <div className="bg-blue-700 text-white px-6 py-4 rounded-b-lg">
        <h1 className="text-2xl font-bold">アノテーション(入力) - 脳卒中患者データ</h1>
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