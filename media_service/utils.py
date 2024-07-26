from fastapi import UploadFile
import os

def save_upload_file(upload_file: UploadFile) -> str:
    file_path = f"temp/{upload_file.filename}"
    with open(file_path, "wb") as buffer:
        buffer.write(upload_file.file.read())
    return file_path

def remove_file(file_path: str):
    if os.path.exists(file_path):
        os.remove(file_path)
