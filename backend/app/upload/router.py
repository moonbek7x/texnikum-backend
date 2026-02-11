from fastapi import APIRouter, UploadFile, File, Form
from typing import List


from backend.app.upload.servise import save_file

router = APIRouter(prefix="/upload", tags=["Upload"])


@router.post("/")
async def upload_files(
    folder: str = Form(...),
    files: List[UploadFile] = File(...)
):
    urls = []

    for file in files:
        path = await save_file(file, folder)
        urls.append(path)

    return {
        "count": len(urls),
        "files": urls
    }
