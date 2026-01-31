from sqlalchemy.ext.asyncio import AsyncSession
from fastapi import APIRouter, Depends,status,Query,Path

from database.postgres.database import get_async_db
from backend.app.owner.service import OwnerService
from database.postgres.models.users import User
from backend.depensies import get_current_user
from backend.app.owner.schema.create import UserCreate,TeacherCreate,TeacherUpdate,NewsCreate,NewsUpdate,CategoryUpdate,CategoryCreate,DeficiencyUpdate,DeficiencyCreate

router = APIRouter(prefix="/owner", tags=["OWNER"])

@router.post("/teachers")
async def create_teacher(
    data:TeacherCreate,
    db: AsyncSession = Depends(get_async_db),
    current_user = Depends(get_current_user),
):
    data = TeacherCreate(
        first_name=data.first_name,
        last_name=data.last_name,
        middle_name=data.middle_name,
        photo_url=data.photo_url

    )

    return await OwnerService.teacher_create(data, db, current_user)


@router.get("/teachers")
async def get_teachers(
    page: int = Query(1, ge=1),
    limit: int = Query(10, ge=1, le=100),
    db: AsyncSession = Depends(get_async_db),
    current_user = Depends(get_current_user),
):
    return await OwnerService.teacher_list(
        db=db,
        current_user=current_user,
        page=page,
        limit=limit,
    )
@router.patch("/teachers/{teacher_id}")
async def update_teacher(
    teacher_id: int = Path(..., ge=1),
    data: TeacherUpdate = ...,
    db: AsyncSession = Depends(get_async_db),
    current_user = Depends(get_current_user),
):
    return await OwnerService.teacher_update(
        teacher_id=teacher_id,
        data=data,
        db=db,
        current_user=current_user,
    )
@router.delete("/teachers/{teacher_id}")
async def delete_teacher(
    teacher_id: int = Path(..., ge=1),
    db: AsyncSession = Depends(get_async_db),
    current_user = Depends(get_current_user),
):
    return await OwnerService.teacher_delete(
        teacher_id=teacher_id,
        db=db,
        current_user=current_user,
    )

# CREATE
@router.post("cree_news")
async def create_news(
    data: NewsCreate,
    db: AsyncSession = Depends(get_async_db),
    current_user = Depends(get_current_user),
):
    return await OwnerService.news_create(data, db, current_user)

# GET LIST (pagination)
@router.get("/news")
async def get_news(
    page: int = Query(1, ge=1),
    limit: int = Query(10, ge=1, le=100),
    db: AsyncSession = Depends(get_async_db),
    current_user = Depends(get_current_user),
):
    return await OwnerService.news_list(db, current_user, page, limit)

# PATCH
@router.patch("/news/{news_id}")
async def update_news(
    news_id: int = Path(..., ge=1),
    data: NewsUpdate = ...,
    db: AsyncSession = Depends(get_async_db),
    current_user = Depends(get_current_user),
):
    return await OwnerService.news_update(news_id, data, db, current_user)

# DELETE
@router.delete("/news/{news_id}")
async def delete_news(
    news_id: int = Path(..., ge=1),
    db: AsyncSession = Depends(get_async_db),
    current_user = Depends(get_current_user),
):
    return await OwnerService.news_delete(news_id, db, current_user)


# CREATE
@router.post("create_categories")
async def create_category(
    data: CategoryCreate,
    db: AsyncSession = Depends(get_async_db),
    current_user = Depends(get_current_user),
):
    return await OwnerService.category_create(data, db, current_user)

# GET LIST
@router.get("/categories")
async def get_categories(
    page: int = Query(1, ge=1),
    limit: int = Query(10, ge=1, le=100),
    db: AsyncSession = Depends(get_async_db),
    current_user = Depends(get_current_user),
):
    return await OwnerService.category_list(db, current_user, page, limit)

# PATCH
@router.patch("/categories/{category_id}")
async def update_category(
    category_id: int = Path(..., ge=1),
    data: CategoryUpdate = ...,
    db: AsyncSession = Depends(get_async_db),
    current_user = Depends(get_current_user),
):
    return await OwnerService.category_update(
        category_id, data, db, current_user
    )

# DELETE
@router.delete("/categories/{category_id}")
async def delete_category(
    category_id: int = Path(..., ge=1),
    db: AsyncSession = Depends(get_async_db),
    current_user = Depends(get_current_user),
):
    return await OwnerService.category_delete(
        category_id, db, current_user
    )

# CREATE
@router.post("create_deficiency")
async def create_deficiency(
    data: DeficiencyCreate,
    db: AsyncSession = Depends(get_async_db),
    current_user = Depends(get_current_user),
):
    return await OwnerService.deficiency_create(data, db, current_user)

# GET LIST
@router.get("/deficiency")
async def get_deficiencies(
    page: int = Query(1, ge=1),
    limit: int = Query(10, ge=1, le=100),
    db: AsyncSession = Depends(get_async_db),
    current_user = Depends(get_current_user),
):
    return await OwnerService.deficiency_list(db, current_user, page, limit)

# PATCH
@router.patch("/deficiency/{deficiency_id}")
async def update_deficiency(
    deficiency_id: int = Path(..., ge=1),
    data: DeficiencyUpdate = ...,
    db: AsyncSession = Depends(get_async_db),
    current_user = Depends(get_current_user),
):
    return await OwnerService.deficiency_update(
        deficiency_id, data, db, current_user
    )

# DELETE
@router.delete("/deficiency/{deficiency_id}")
async def delete_deficiency(
    deficiency_id: int = Path(..., ge=1),
    db: AsyncSession = Depends(get_async_db),
    current_user = Depends(get_current_user),
):
    return await OwnerService.deficiency_delete(
        deficiency_id, db, current_user
    )