from fastapi import APIRouter, UploadFile, File, Depends
from sqlalchemy.ext.asyncio import AsyncSession

from backend.app.upload.servise import save_teacher_photo

router = APIRouter(prefix="/upload", tags=["Upload"])

@router.post("/teacher-photo")
async def upload_teacher_photo(
    file: UploadFile = File(...),
):
    photo_url = await save_teacher_photo(file)

    return {
        "url": photo_url
    }