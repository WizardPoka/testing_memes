from pydantic import BaseModel, HttpUrl

class MemeBase(BaseModel):
    title: str
    description: str

class MemeCreate(MemeBase):
    image_url: HttpUrl

class MemeUpdate(MemeBase):
    image_url: HttpUrl

class MemeInDB(MemeBase):
    id: int
    image_url: HttpUrl

    class Config:
        orm_mode = True
