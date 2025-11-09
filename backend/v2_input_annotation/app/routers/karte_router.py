from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from app.db.database import get_db, engine
from app.db.entities import karte

router = APIRouter()

