from sqlalchemy import Column, DateTime, ForeignKey, String
from sqlalchemy.orm import relationship

from core.infra.orm.base import Base


class UserHabit(Base):
    __tablename__ = "user_habits"

    id = Column(String, primary_key=True, index=True)
    user_id = Column(String, ForeignKey("users.id"))
    description = Column(String, index=True)
    created_at = Column(DateTime)
    updated_at = Column(DateTime)

    user = relationship("User", back_populates="user_habits")
    habit_logs = relationship("HabitLog", back_populates="habit")
