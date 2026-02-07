from fastapi import HTTPException,status
from sqlalchemy.ext.asyncio import AsyncSession

from backend.depensies import hash_password
from common import auth
from sqlalchemy import select


from fastapi import HTTPException, status
from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy.future import select

from database.postgres.models.teacher import Teacher
from database.postgres.models.news import New
from database.postgres.models.categories import Category
from database.postgres.models.deficiency import Deficiency

from backend.depensies import hash_password
from backend.app.owner.schema.create import UserCreate,TeacherCreate,TeacherUpdate,NewsUpdate,NewsCreate,CategoryCreate,CategoryUpdate,DeficiencyCreate,DeficiencyUpdate


class OwnerService:
    @staticmethod
    async def teacher_create(
        data: TeacherCreate,
        db: AsyncSession,
        current_user,
    ):
        if current_user.id != 1:
            raise HTTPException(403)

        teacher = Teacher(
            first_name=data.first_name,
            last_name=data.last_name,
            middle_name=data.middle_name,
            photo=data.photo_url,
        )

        db.add(teacher)
        await db.commit()
        await db.refresh(teacher)

        return {"message":"succesfully"}
    @staticmethod
    async def teacher_list(
        db: AsyncSession,
        page: int = 1,
        limit: int = 10,
    ):


        if page < 1 or limit < 1:
            raise HTTPException(status_code=400, detail="Invalid pagination params")

        offset = (page - 1) * limit

        stmt = (
            select(Teacher)
            .offset(offset)
            .limit(limit)
            .order_by(Teacher.id.desc())
        )

        result = await db.execute(stmt)
        teachers = result.scalars().all()

        return teachers
    
    @staticmethod
    async def teacher_update(
        teacher_id: int,
        data: TeacherUpdate,
        db: AsyncSession,
        current_user,
    ):
        # owner tekshiruvi (senda role yo‘q, shuning uchun id=1)
        if current_user.id != 1:
            raise HTTPException(
                status_code=status.HTTP_403_FORBIDDEN,
                detail="Forbidden",
            )

        teacher = await db.get(Teacher, teacher_id)
        if not teacher:
            raise HTTPException(
                status_code=status.HTTP_404_NOT_FOUND,
                detail="Teacher not found",
            )

        update_data = data.model_dump(exclude_unset=True)

        for field, value in update_data.items():
            setattr(teacher, field, value)

        await db.commit()
        await db.refresh(teacher)

        return teacher
    
    @staticmethod
    async def teacher_delete(
        teacher_id: int,
        db: AsyncSession,
        current_user,
    ):
        # owner check (senda role yo‘q)
        if current_user.id != 1:
            raise HTTPException(
                status_code=status.HTTP_403_FORBIDDEN,
                detail="Forbidden",
            )

        teacher = await db.get(Teacher, teacher_id)
        if not teacher:
            raise HTTPException(
                status_code=status.HTTP_404_NOT_FOUND,
                detail="Teacher not found",
            )

        await db.delete(teacher)
        await db.commit()

        return {"message": "deleted successfully"}
    
        # CREATE
    @staticmethod
    async def news_create(
        data: NewsCreate,
        db: AsyncSession,
        current_user,
    ):
        if current_user.id != 1:
            raise HTTPException(status_code=403, detail="Forbidden")

        news = New(
            description=data.description,
            photo=data.photo,
        )

        db.add(news)
        await db.commit()
        await db.refresh(news)
        return {"message":"succesfully"}

    # GET LIST + PAGINATION
    @staticmethod
    async def news_list(
        db: AsyncSession,
        page: int = 1,
        limit: int = 10,
    ):


        offset = (page - 1) * limit

        stmt = (
            select(New)
            .order_by(New.created_date.desc())
            .offset(offset)
            .limit(limit)
        )

        result = await db.execute(stmt)
        return result.scalars().all()

    # PATCH
    @staticmethod
    async def news_update(
    news_id: int,
    data: NewsUpdate,
    db: AsyncSession,
    current_user,
):
        if current_user.id != 1:
            raise HTTPException(status_code=403, detail="Forbidden")

        news = await db.get(New, news_id)
        if not news:
            raise HTTPException(status_code=404, detail="News not found")

        update_data = data.model_dump(
        exclude_unset=True,
        exclude_none=True,  # 🔥 MUHIM
    )

        for field, value in update_data.items():
            setattr(news, field, value)

        await db.commit()
        await db.refresh(news)

        return {"message":"succesfully"}


    # DELETE
    @staticmethod
    async def news_delete(
        news_id: int,
        db: AsyncSession,
        current_user,
    ):
        if current_user.id != 1:
            raise HTTPException(status_code=403, detail="Forbidden")

        news = await db.get(New, news_id)
        if not news:
            raise HTTPException(status_code=404, detail="News not found")

        await db.delete(news)
        await db.commit()
        return {"message": "deleted successfully"}
    
        # CREATE
    @staticmethod
    async def category_create(
        data: CategoryCreate,
        db: AsyncSession,
        current_user,
    ):
        if current_user.id != 1:
            raise HTTPException(status_code=403, detail="Forbidden")

        category = Category(name=data.name)

        db.add(category)
        await db.commit()
        await db.refresh(category)

        return {"message":"succesfully"}

    # GET LIST + PAGINATION
    @staticmethod
    async def category_list(
        db: AsyncSession,
        page: int = 1,
        limit: int = 10,
    ):


        offset = (page - 1) * limit

        stmt = (
            select(Category)
            .order_by(Category.id.desc())
            .offset(offset)
            .limit(limit)
        )

        result = await db.execute(stmt)
        return result.scalars().all()

    # PATCH
    @staticmethod
    async def category_update(
        category_id: int,
        data: CategoryUpdate,
        db: AsyncSession,
        current_user,
    ):
        if current_user.id != 1:
            raise HTTPException(status_code=403, detail="Forbidden")

        category = await db.get(Category, category_id)
        if not category:
            raise HTTPException(status_code=404, detail="Category not found")

        update_data = data.model_dump(
            exclude_unset=True,
            exclude_none=True,
        )

        if not update_data:
            raise HTTPException(
                status_code=400,
                detail="No fields provided for update",
            )

        for field, value in update_data.items():
            setattr(category, field, value)

        await db.commit()
        await db.refresh(category)
        return {"message":"succesfully"}

    # DELETE
    @staticmethod
    async def category_delete(
        category_id: int,
        db: AsyncSession,
        current_user,
    ):
        if current_user.id != 1:
            raise HTTPException(status_code=403, detail="Forbidden")

        category = await db.get(Category, category_id)
        if not category:
            raise HTTPException(status_code=404, detail="Category not found")

        await db.delete(category)
        await db.commit()

        return {"message": "deleted successfully"}
    
        # CREATE
    @staticmethod
    async def deficiency_create(
        data: DeficiencyCreate,
        db: AsyncSession,
        current_user,
    ):
        if current_user.id != 1:
            raise HTTPException(status_code=403, detail="Forbidden")

        deficiency = Deficiency(
            description=data.description,
            photo=data.photo,
        )

        db.add(deficiency)
        await db.commit()
        await db.refresh(deficiency)
        return {"message":"succesfully"}

    # GET LIST + PAGINATION
    @staticmethod
    async def deficiency_list(
        db: AsyncSession,
        page: int = 1,
        limit: int = 10,
    ):


        offset = (page - 1) * limit

        stmt = (
            select(Deficiency)
            .order_by(Deficiency.created_date.desc())
            .offset(offset)
            .limit(limit)
        )

        result = await db.execute(stmt)
        return result.scalars().all()
    

    # PATCH
    @staticmethod
    async def deficiency_update(
        deficiency_id: int,
        data: DeficiencyUpdate,
        db: AsyncSession,
        current_user,
    ):
        if current_user.id != 1:
            raise HTTPException(status_code=403, detail="Forbidden")

        deficiency = await db.get(Deficiency, deficiency_id)
        if not deficiency:
            raise HTTPException(status_code=404, detail="Deficiency not found")

        update_data = data.model_dump(
            exclude_unset=True,
            exclude_none=True,
        )

        if not update_data:
            raise HTTPException(status_code=400, detail="No fields to update")

        for field, value in update_data.items():
            setattr(deficiency, field, value)

        await db.commit()
        await db.refresh(deficiency)
        return deficiency

    # DELETE
    @staticmethod
    async def deficiency_delete(
        deficiency_id: int,
        db: AsyncSession,
        current_user,
    ):
        if current_user.id != 1:
            raise HTTPException(status_code=403, detail="Forbidden")

        deficiency = await db.get(Deficiency, deficiency_id)
        if not deficiency:
            raise HTTPException(status_code=404, detail="Deficiency not found")

        await db.delete(deficiency)
        await db.commit()
        return {"message": "deleted successfully"}