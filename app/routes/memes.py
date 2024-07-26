from fastapi import APIRouter, HTTPException, Depends, status
from sqlalchemy.orm import Session
from typing import List
from .. import crud, schemas
from ..dependencies import get_db

router = APIRouter()

@router.get("/memes", response_model=List[schemas.MemeInDB])
async def read_memes(skip: int = 0, limit: int = 10, db: Session = Depends(get_db)):
    memes = crud.get_memes(db, skip=skip, limit=limit)
    return memes

@router.get("/memes/{meme_id}", response_model=schemas.MemeInDB)
async def read_meme(meme_id: int, db: Session = Depends(get_db)):
    meme = crud.get_meme(db, meme_id=meme_id)
    if meme is None:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Meme not found")
    return meme

@router.post("/memes", response_model=schemas.MemeInDB)
async def create_meme(meme: schemas.MemeCreate, db: Session = Depends(get_db)):
    return crud.create_meme(db=db, meme=meme)

@router.put("/memes/{meme_id}", response_model=schemas.MemeInDB)
async def update_meme(meme_id: int, meme: schemas.MemeUpdate, db: Session = Depends(get_db)):
    db_meme = crud.update_meme(db=db, meme_id=meme_id, meme=meme)
    if db_meme is None:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Meme not found")
    return db_meme

@router.delete("/memes/{meme_id}", response_model=schemas.MemeInDB)
async def delete_meme(meme_id: int, db: Session = Depends(get_db)):
    db_meme = crud.delete_meme(db=db, meme_id=meme_id)
    if db_meme is None:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Meme not found")
    return db_meme
