from pathlib import Path
from fastapi import UploadFile, HTTPException
import uuid

BASE_UPLOAD_DIR = Path("uploads")

ALLOWED_FOLDERS = {
    "teachers",
    "categories",
    "news",
    "deficiency"
}

MAX_FILE_SIZE = 10 * 1024 * 1024  # 10MB


async def save_file(file: UploadFile, folder: str) -> str:
    if folder not in ALLOWED_FOLDERS:
        raise HTTPException(400, "Invalid folder")

    upload_dir = BASE_UPLOAD_DIR / folder
    upload_dir.mkdir(parents=True, exist_ok=True)

    ext = file.filename.split(".")[-1].lower()
    filename = f"{uuid.uuid4()}.{ext}"
    path = upload_dir / filename

    content = await file.read()

    if len(content) > MAX_FILE_SIZE:
        raise HTTPException(400, "File too large")

    path.write_bytes(content)

    # DB uchun qaytariladi
    return f"{folder}/{filename}"
