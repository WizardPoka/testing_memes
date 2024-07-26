from minio import Minio
from .config import MINIO_ENDPOINT, MINIO_ACCESS_KEY, MINIO_SECRET_KEY, BUCKET_NAME

minio_client = Minio(
    MINIO_ENDPOINT,
    access_key=MINIO_ACCESS_KEY,
    secret_key=MINIO_SECRET_KEY,
    secure=False
)

def create_bucket():
    if not minio_client.bucket_exists(BUCKET_NAME):
        minio_client.make_bucket(BUCKET_NAME)

def upload_image(file_name: str, file_data: bytes):
    minio_client.put_object(
        BUCKET_NAME, file_name, file_data, length=len(file_data)
    )

def get_image_url(file_name: str) -> str:
    return minio_client.presigned_get_object(BUCKET_NAME, file_name)
