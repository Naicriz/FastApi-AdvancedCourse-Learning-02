from models import UUID, Optional, date
# Pydantic
from pydantic import BaseModel, EmailStr, Field

# Models


class UserBase(BaseModel):
    user_id: UUID = Field(..., description="User ID")
    email: EmailStr = Field(..., description="User Email")
    username: str = Field(...,
                          min_length=4,
                          max_length=20,
                          description="User Username")


class User(UserBase):
    password: str = Field(...,
                          min_length=8,
                          max_length=60,
                          description="User Password")
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


class userLogin(UserBase):
    password: str = Field(...,
                          min_length=8,
                          max_length=60,
                          description="User Password")
