from fastapi import APIRouter, Depends, UploadFile, File
from fastapi.requests import Request
from routers.schemas import PostBase, PostDisplay
from sqlalchemy.orm.session import Session
from database.database import get_db
from database import db_post
import random
import string
import shutil

router = APIRouter(
    prefix='/post',
    tags=['post']
)


@router.post('')
def create_post(request:PostBase, db:Session = Depends(get_db)):
    return db_post.create_post(db, request)


@router.get('/all')
def get_all_posts(db:Session = Depends(get_db)):
    return db_post.get_all(db)


@router.delete("/{id}")
def delete_post(id:int, db:Session = Depends(get_db)):
    return db_post.delete(id, db)


@router.post("/image")
def upload_image(image: UploadFile = File(...)):
    letters = string.ascii_letters
    random_str = ''.join(random.choice(letters) for i in range(6))
    new = f"_{random_str}."
    filename = new.join(image.filename.rsplit('.',1))
    path = f"images/{filename}"

    with open(path, "w+b") as buffer:
        shutil.copyfileobj(image.file, buffer)

    return {
        "filename":path
    }