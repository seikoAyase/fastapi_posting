from typing import TYPE_CHECKING

from sqlalchemy import String
from sqlalchemy.orm import Mapped, mapped_column, relationship

from database import Base

if TYPE_CHECKING:
    from posts.models import Comment, Like, Post

class User(Base):
    __tablename__ = "users"

    id: Mapped[int] = mapped_column(primary_key=True)
    username: Mapped[str] = mapped_column(String(20), nullable=False, unique=True)
    password: Mapped[str] = mapped_column(String(128), nullable=False)

    posts: Mapped[list["Post"]] = relationship("Post", back_populates="author")
    comments: Mapped[list["Comment"]] = relationship("Comment", back_populates="author")
    likes: Mapped[list["Like"]] = relationship("Like", back_populates="author")