from sqlalchemy import Column, Integer, String, Text
from app.database.base import Base

class Course(Base):
    __tablename__ = "courses"

    id = Column(Integer, primary_key=True, index=True)
    course_name = Column(String(100))
    fees = Column(String(50))
    duration = Column(String(50))
    description = Column(Text)