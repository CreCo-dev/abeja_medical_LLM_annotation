# Standard Library
import os

# Third Party
from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=[os.getenv('FRONTEND_URL', 'http://localhost:3000')],
    allow_credentials=True,
    allow_methods=['*'],
    allow_headers=['*']
)

# ルーターのインポート--------------------------------
from routers import (
    sample_router,
    user_accounts_router,
    auth_router
)

@app.get("/")
async def root():
    return "ok"

# ルーター
app.include_router(sample_router.router)
app.include_router(user_accounts_router.router)
app.include_router(auth_router.router)