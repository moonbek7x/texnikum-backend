import uuid
from pathlib import Path
from fastapi import UploadFile

UPLOAD_DIR = Path("uploads")  
async def save_teacher_photo(file: UploadFile) -> str:
    UPLOAD_DIR.mkdir(parents=True, exist_ok=True)

    ext = file.filename.split(".")[-1]
    filename = f"{uuid.uuid4()}.{ext}"
    path = UPLOAD_DIR / filename

    content = await file.read()
    path.write_bytes(content)

    return f"teachers/{filename}"