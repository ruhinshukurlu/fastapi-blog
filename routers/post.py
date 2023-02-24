from fastapi import APIRouter, Depends
from fastapi.requests import Request
from routers.schemas import PostBase, PostDisplay
from sqlalchemy.orm.session import Session
from database.database import get_db
from database import db_post


router = APIRouter(
    prefix='/post',
    tags=['post']
)


@router.post('')
def create_post(request:PostBase, db:Session = Depends(get_db)):
    return db_post.create_post(db, request)