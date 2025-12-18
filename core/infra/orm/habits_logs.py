from sqlalchemy import Column, DateTime, ForeignKey, Integer, String
from sqlalchemy.orm import relationship

from core.infra.orm.base import Base


class HabitLog(Base):
    __tablename__ = "habit_logs"

    id = Column(Integer, primary_key=True, index=True)

    habit_id = Column(String, ForeignKey("user_habits.id"))
    done_at = Column(DateTime)

    habit = relationship("UserHabit", back_populates="habit_logs")
