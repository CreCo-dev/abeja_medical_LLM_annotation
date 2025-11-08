from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from db.database import get_db, engine
from db.entities import stroke_patient
#from cruds import 
#from schemas import user_account_schema

router = APIRouter()

