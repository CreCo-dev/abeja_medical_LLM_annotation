type FetchOptions = {
  method?: "GET" | "POST" | "PUT" | "PATCH" | "DELETE";
  body?: any;
  form?: boolean;
  token?: string | null;
};

const API_BASE =
  process.env.NEXT_PUBLIC_API_BASE_URL?.replace(/\/$/, "") || "http://localhost:70";

async function request<T>(path: string, opts: FetchOptions = {}): Promise<T> {
  const url = `${API_BASE}${path.startsWith("/") ? path : `/${path}`}`;
  const headers: Record<string, string> = {};

  const t =
    opts.token ?? (typeof window !== "undefined" ? localStorage.getItem("token") : null);
  if (t) headers["Authorization"] = `Bearer ${t}`;

  let body: BodyInit | undefined;
  if (opts.body != null) {
    if (opts.form) {
      const params = new URLSearchParams();
      Object.entries(opts.body).forEach(([k, v]) => params.append(k, String(v)));
      body = params;
      headers["Content-Type"] = "application/x-www-form-urlencoded";
    } else {
      body = JSON.stringify(opts.body);
      headers["Content-Type"] = "application/json";
    }
  }

  const res = await fetch(url, {
    method: opts.method ?? (opts.body != null ? "POST" : "GET"),
    headers,
    body,
  });

  if (!res.ok) {
    const text = await res.text().catch(() => "");
    throw new Error(text || `HTTP ${res.status}`);
  }
  const ct = res.headers.get("content-type") || "";
  if (ct.includes("application/json")) return (await res.json()) as T;
  // @ts-ignore
  return (await res.text()) as T;
}

export function apiGet<T>(path: string) {
  return request<T>(path, { method: "GET" });
}

export function apiPost<T>(path: string, body: any, extra?: { form?: boolean }) {
  return request<T>(path, { method: "POST", body, form: extra?.form });
}
