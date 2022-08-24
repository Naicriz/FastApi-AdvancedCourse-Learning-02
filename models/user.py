# Python Native Library
from typing import Optional
from datetime import date
from uuid import UUID

# Pydantic
from pydantic import BaseModel, EmailStr, Field

# Models


class PasswordMixin(BaseModel):
    password: str = Field(...,
                          min_length=8,
                          max_length=60,
                          description="User Password")


class UserBase(BaseModel):
    user_id: UUID = Field(..., description="User ID")
    email: EmailStr = Field(..., description="User Email")
    username: str = Field(...,
                          min_length=4,
                          max_length=20,
                          description="User Username")


class User(UserBase):
    first_name: str = Field(...,
                            min_length=4,
                            max_length=30,
                            description="User First Name")
    last_name: str = Field(...,
                           min_length=4,
                           max_length=30,
                           description="User Last Name")
    birth_day: Optional[date] = Field(default=None,
                                      description="User Birth Day")


class UserLogin(PasswordMixin, UserBase):
    pass


class UserUpdateReg(PasswordMixin, User):
    pass
