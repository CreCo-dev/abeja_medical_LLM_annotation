"use client";
import { useState } from "react";
import { apiGet, apiPost } from "@/lib/api";

export default function Home() {
  const [root, setRoot] = useState(""), [getMsg, setGetMsg] = useState(""), [postMsg, setPostMsg] = useState("");
  return (
    <main className="p-6 space-y-4">
      <h1 className="text-2xl font-semibold">Medical LLM UI – Frontend scaffold</h1>
      <button onClick={async()=>setRoot(JSON.stringify(await apiGet("/")))}>GET /</button> <span>{root}</span><br/>
      <button onClick={async()=>setGetMsg(JSON.stringify(await apiGet("/sample_get")))}>GET /sample_get</button> <span>{getMsg}</span><br/>
      <button onClick={async()=>setPostMsg(JSON.stringify(await apiPost("/sample_post",{hello:"world"})))}>POST /sample_post</button> <span>{postMsg}</span>
    </main>
  );
}