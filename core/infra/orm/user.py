from sqlalchemy import Column, String
from sqlalchemy.orm import relationship

from core.infra.orm.base import Base


class User(Base):
    __tablename__ = "users"

    id = Column(String, primary_key=True, index=True)
    username = Column(String, index=True)
    email = Column(String, unique=True, index=True)
    password = Column(String)

    user_habits = relationship("UserHabit", back_populates="user")
