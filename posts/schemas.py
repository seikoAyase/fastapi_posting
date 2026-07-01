from pydantic import BaseModel, ConfigDict
from datetime import datetime
from sqlalchemy import Text, String


class PostCreate(BaseModel):
    title: str
    content: Text

class PostResponse(BaseModel):
    id: int 
    title: str
    content: Text
    author_id: int
    created_at: datetime

    
    model_config = ConfigDict(from_attributes = True)

class CommentCreate(BaseModel):
    content: str

class CommentResponse(BaseModel):
    id: int 
    content: str
    user_id: int
    post_id: int 

    model_config = ConfigDict(from_attributes = True)

# class LikeResponse(BaseModel):
#     user_id: int
#     post_id: int

#     model_config = ConfigDict(from_attributes=True)