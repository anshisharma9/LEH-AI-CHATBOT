from sqlalchemy import Column, Integer, String
from app.database.base import Base

class ClassTiming(Base):
    __tablename__ = "class_timings"

    id = Column(Integer, primary_key=True, index=True)
    course = Column(String(100))
    teacher = Column(String(100))
    timing = Column(String(100))