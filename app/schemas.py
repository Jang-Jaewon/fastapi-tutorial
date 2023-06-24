from datetime import date, datetime
from typing import List

from pydantic import BaseModel, EmailStr, constr


class UserBaseSchema(BaseModel):
    name: str
    email: EmailStr
    photo: str

    class Config:
        orm_mode = True


class CreateUserSchema(UserBaseSchema):
    password: constr(min_length=8)
    passwordConfirm: str
    role: str = "user"
    verified: bool = False


class LoginUserSchema(BaseModel):
    email: EmailStr
    password: constr(min_length=8)


class UserResponse(UserBaseSchema):
    id: int
    created_at: datetime
    updated_at: datetime


class FilteredUserResponse(UserBaseSchema):
    id: int


class ItemBaseSchema(BaseModel):
    title: str
    content: str
    category: str
    image: str
    user_id: int | None = None

    class Config:
        orm_mode = True


class CreateItemSchema(ItemBaseSchema):
    pass


class ItemResponse(ItemBaseSchema):
    id: int
    owner: FilteredUserResponse
    created_at: datetime
    updated_at: datetime


class UpdateItemSchema(BaseModel):
    title: str
    content: str
    category: str
    image: str
    user_id: int | None = None
    created_at: datetime | None = None
    updated_at: datetime | None = None

    class Config:
        orm_mode = True


class ListItemResponse(BaseModel):
    status: str
    results: int
    items: List[ItemBaseSchema]

