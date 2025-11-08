from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from db.database import get_db, engine
from db.entities import karte
#from cruds import 
#from schemas import 

router = APIRouter()

