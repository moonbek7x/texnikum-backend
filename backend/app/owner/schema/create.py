from pydantic import BaseModel,model_validator


class UserCreate(BaseModel):
    login :str
    password:str


class TeacherCreate(BaseModel):
    first_name: str
    last_name: str
    middle_name: str | None = None
    photo_url: str


class TeacherUpdate(BaseModel):
    first_name: str | None = None
    last_name: str | None = None
    middle_name: str | None = None
    photo_url: str | None = None


class NewsCreate(BaseModel):
    description: str
    photo: str | None = None


class NewsUpdate(BaseModel):
    description: str | None = None
    photo: str | None = None


class CategoryCreate(BaseModel):
    name: str


class CategoryUpdate(BaseModel):
    name: str | None = None


class DeficiencyCreate(BaseModel):
    description: str
    photo: str | None = None


class DeficiencyUpdate(BaseModel):
    description: str | None = None
    photo: str | None = None

