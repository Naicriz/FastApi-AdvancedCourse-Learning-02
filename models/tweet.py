from models import UUID, Optional, datetime
# Pydantic
from models import BaseModel, Field

from models import User

# Models


class Tweet(BaseModel):
    tweet_id: UUID = Field(..., description="Tweet ID")
    content: str = Field(...,
                         min_length=1,
                         max_length=256,
                         description="Tweet Content")
    created_at: datetime = Field(default=datetime.now(),
                                 description="Tweet Created At")
    updated_at: Optional[datetime] = Field(default=datetime.now())
    created_by: User = Field(..., description="Tweet Created By")
