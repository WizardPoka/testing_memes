from fastapi import FastAPI
from .routes import memes
from .models import Base
from .database import engine

Base.metadata.create_all(bind=engine)

app = FastAPI(title="Meme API", description="API для управления мемами", version="1.0.0")

app.include_router(memes.router, prefix="/api/v1", tags=["memes"])
