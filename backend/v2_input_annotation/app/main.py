# Standard Library
import os
# Third Party
from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
# app
from config import get_settings

settings = get_settings()
print(f"[main] Loaded settings for environment: {settings.app_env}", flush=True)

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=settings.allow_origins,
    allow_credentials=settings.allow_credentials,
    allow_methods=settings.allow_methods,
    allow_headers=settings.allow_headers,
)

# ルーターのインポート--------------------------------
from routers import (
    user_accounts_router,
    auth_router
)

@app.get("/")
async def root():
    return "ok"

# ルーター
app.include_router(user_accounts_router.router)
app.include_router(auth_router.router)