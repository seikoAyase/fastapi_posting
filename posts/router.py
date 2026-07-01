from fastapi import APIRouter, HTTPException, Depends
from sqlalchemy.orm import Session

from src.database import get_db
from src.posts.models import Post, Like, Comment
from src.posts.schemas import PostCreate, PostResponse, CommentCreate, CommentResponse

router = APIRouter(prefix="/posts", tags=["posts"])

@router.post()