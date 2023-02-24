from fastapi import Depends
from routers.schemas import PostBase
from sqlalchemy.orm.session import Session
from database.models import DbPost

import datetime


def create_post(db: Session, request: PostBase):
    new_post = DbPost(
        image_url = request.image_url,
        title = request.title,
        content = request.content,
        creator = request.creator,
        timestamp = datetime.datetime.now()
    )
    db.add(new_post)
    db.commit()
    db.refresh(new_post)
    return new_post