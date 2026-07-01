from datetime import datetime
from typing import TYPE_CHECKING

from sqlalchemy import ForeignKey, String, Text, func
from sqlalchemy.orm import Mapped, mapped_column, relationship

from database import Base

if TYPE_CHECKING:
    from auth.models import User

class Post(Base):
    __tablename__ = "posts"

    id: Mapped[int] = mapped_column(primary_key=True)
    title: Mapped[str] = mapped_column(String(50), nullable=False)
    content: Mapped[str | None] = mapped_column(Text)

    created_at: Mapped[datetime] = mapped_column(server_default=func.now(), nullable=False)

    author_id: Mapped[int] = mapped_column(ForeignKey("users.id"))

    author: Mapped["User"] = relationship("User", back_populates="posts")
    comments: Mapped[list["Comment"]] = relationship("Comment", back_populates="post")
    likes: Mapped[list["Like"]] = relationship("Like", back_populates="post")
    
class Comment(Base):
    __tablename__ = "comments"

    id: Mapped[int] = mapped_column(primary_key=True)
    content: Mapped[str] = mapped_column(Text, nullable=False)

    user_id: Mapped[int] = mapped_column(ForeignKey("users.id"))
    post_id: Mapped[int] = mapped_column(ForeignKey("posts.id"))

    created_at: Mapped[datetime] = mapped_column(server_default=func.now(), nullable=False)

    author: Mapped["User"] = relationship(back_populates="comments")
    post: Mapped["Post"] = relationship(back_populates="comments") 

class Like(Base):
    __tablename__ = "likes"

    user_id: Mapped[int] = mapped_column(ForeignKey("users.id"), primary_key=True)
    post_id: Mapped[int] = mapped_column(ForeignKey("posts.id"), primary_key=True)

    created_at: Mapped[datetime] = mapped_column(server_default=func.now(), nullable=False)

    author: Mapped["User"] = relationship(back_populates="likes")
    post: Mapped["Post"] = relationship(back_populates="likes")

