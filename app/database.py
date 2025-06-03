from app import db,login_manager
from datetime import datetime, timezone
from typing import Optional
from sqlalchemy import ForeignKey
from sqlalchemy import String
from sqlalchemy.orm import DeclarativeBase
from sqlalchemy.orm import Mapped
from sqlalchemy.orm import mapped_column
from sqlalchemy.orm import relationship
from sqlalchemy.orm import WriteOnlyMapped
from werkzeug.security import generate_password_hash, check_password_hash
from flask_login import LoginManager,UserMixin

class User(db.Model,UserMixin):
    __tablename__ = "user_account"

    id: Mapped[int] = mapped_column(primary_key=True,autoincrement=True)
    login: Mapped[str] = mapped_column(String(30),unique=True,nullable=False)
    password: Mapped[str] = mapped_column(String(250),unique=True,nullable=False)
    posts: WriteOnlyMapped['Post'] = relationship(back_populates='author')

    def set_password(self,password):
        self.password = generate_password_hash(password)
    
    def check_password(self,password):
        return check_password_hash(self.password,password)


    def __repr__(self) -> str:
        return f"User(id={self.id!r}, name={self.login!r}, fullname={self.password!r})"

@login_manager.user_loader
def load_user(user_id):
    return db.session.get(User,int(user_id))

class Post(db.Model):
    id: Mapped[int] = mapped_column(primary_key=True)
    body: Mapped[str] = mapped_column(String(80),unique=True,index=True)
    timestamp: Mapped[datetime] = mapped_column(
        index=True, default=lambda: datetime.now(timezone.utc))
    user_id: Mapped[int] = mapped_column(ForeignKey(User.id))
    author: Mapped[User] = relationship(back_populates='posts')