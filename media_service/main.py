from fastapi import FastAPI, UploadFile, HTTPException, status
from .minio_client import create_bucket, upload_image, get_image_url
from .utils import save_upload_file, remove_file

app = FastAPI(title="Media Service", description="Service for handling media files", version="1.0.0")

create_bucket()

@app.post("/upload", status_code=status.HTTP_201_CREATED)
async def upload_media(file: UploadFile):
    try:
        file_path = save_upload_file(file)
        with open(file_path, "rb") as f:
            upload_image(file.filename, f.read())
        remove_file(file_path)
        return {"url": get_image_url(file.filename)}
    except Exception as e:
        raise HTTPException(status_code=status.HTTP_500_INTERNAL_SERVER_ERROR, detail=str(e))
