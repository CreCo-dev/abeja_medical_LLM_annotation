// src/lib/api.ts
import { z } from "zod";

// Next.js の rewrites で /api/* -> BE に中継する前提
const API_PREFIX = "/api";

export class ApiError extends Error {
  status: number;
  info?: unknown;
  constructor(message: string, status: number, info?: unknown) {
    super(message);
    this.name = "ApiError";
    this.status = status;
    this.info = info;
  }
}

type BaseInit = RequestInit & {
  /** 失敗時に自動 Abort するタイムアウト(ms)。既定: 10s */
  timeoutMs?: number;
};

// 実装: fetch ラッパ（JSON前提）
// - 成功なら JSON を返す
// - 失敗なら ApiError を throw
// - schema 指定時は Zod で実行時バリデーション
async function requestImpl<T>(
  path: string,
  init: BaseInit = {}
): Promise<T> {
  const {
    timeoutMs = 10_000,
    headers,
    // cache/no-store 等は呼び出し側で上書き可
    ...rest
  } = init;

  // タイムアウト: AbortSignal.timeout() を利用（Baseline 2024 で各ブラウザ対応）
  // https://developer.mozilla.org/docs/Web/API/AbortSignal/timeout_static
  const timeoutSignal = AbortSignal.timeout(timeoutMs);

  const res = await fetch(`${API_PREFIX}${path}`, {
    headers: { "Content-Type": "application/json", ...(headers ?? {}) },
    signal: timeoutSignal,
    ...rest,
  });

  // 204などボディ無しの考慮
  if (!res.ok) {
    let info: unknown;
    try {
      info = await res.json();
    } catch {
      info = await res.text().catch(() => undefined);
    }
    throw new ApiError(`HTTP ${res.status}`, res.status, info);
  }

  // JSON を安全に読む（空ボディでも落とさない）
  const text = await res.text();
  return (text ? JSON.parse(text) : undefined) as T;
}

// ---------- 型安全な公開API（Zod対応のオーバーロード） ----------

// schema 指定あり: 返り値は z.infer<S>
export async function apiGet<S extends z.ZodTypeAny>(
  path: string,
  init: Omit<BaseInit, "method" | "body"> & { schema: S }
): Promise<z.infer<S>>;
// schema なし: 呼び出し側の <T> で受ける
export async function apiGet<T = unknown>(
  path: string,
  init?: Omit<BaseInit, "method" | "body">
): Promise<T>;
export async function apiGet(
  path: string,
  init: Omit<BaseInit, "method" | "body"> & { schema?: z.ZodTypeAny } = {}
): Promise<unknown> {
  const data = await requestImpl<unknown>(path, { method: "GET", cache: "no-store", ...init });
  if (init.schema) {
    const r = init.schema.safeParse(data);
    if (!r.success) throw new ApiError("Response validation failed", 200, r.error.format());
    return r.data;
  }
  return data;
}

export async function apiPost<S extends z.ZodTypeAny, B = unknown>(
  path: string,
  body: B,
  init: Omit<BaseInit, "method" | "body"> & { schema: S }
): Promise<z.infer<S>>;
export async function apiPost<T = unknown, B = unknown>(
  path: string,
  body: B,
  init?: Omit<BaseInit, "method" | "body">
): Promise<T>;
export async function apiPost(
  path: string,
  body: unknown,
  init: Omit<BaseInit, "method" | "body"> & { schema?: z.ZodTypeAny } = {}
): Promise<unknown> {
  const data = await requestImpl<unknown>(path, {
    method: "POST",
    body: JSON.stringify(body ?? {}),
    ...init,
  });
  if (init.schema) {
    const r = init.schema.safeParse(data);
    if (!r.success) throw new ApiError("Response validation failed", 200, r.error.format());
    return r.data;
  }
  return data;
}

export async function apiPut<T = unknown, B = unknown>(
  path: string,
  body: B,
  init?: Omit<BaseInit, "method" | "body">
): Promise<T> {
  return requestImpl<T>(path, { method: "PUT", body: JSON.stringify(body ?? {}), ...init });
}

export async function apiDelete<T = unknown>(
  path: string,
  init?: Omit<BaseInit, "method" | "body">
): Promise<T> {
  return requestImpl<T>(path, { method: "DELETE", ...init });
}
