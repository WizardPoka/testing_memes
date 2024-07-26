from sqlalchemy.orm import Session
from typing import List, Optional
import models, schemas

def get_meme(db: Session, meme_id: int) -> Optional[models.Meme]:
    return db.query(models.Meme).filter(models.Meme.id == meme_id).first()

def get_memes(db: Session, skip: int = 0, limit: int = 10) -> List[models.Meme]:
    return db.query(models.Meme).offset(skip).limit(limit).all()

def create_meme(db: Session, meme: schemas.MemeCreate) -> models.Meme:
    db_meme = models.Meme(
        title=meme.title,
        description=meme.description,
        image_url=meme.image_url
    )
    db.add(db_meme)
    db.commit()
    db.refresh(db_meme)
    return db_meme

def update_meme(db: Session, meme_id: int, meme: schemas.MemeUpdate) -> Optional[models.Meme]:
    db_meme = get_meme(db, meme_id)
    if not db_meme:
        return None
    db_meme.title = meme.title
    db_meme.description = meme.description
    db_meme.image_url = meme.image_url
    db.commit()
    db.refresh(db_meme)
    return db_meme

def delete_meme(db: Session, meme_id: int) -> Optional[models.Meme]:
    db_meme = get_meme(db, meme_id)
    if not db_meme:
        return None
    db.delete(db_meme)
    db.commit()
    return db_meme
