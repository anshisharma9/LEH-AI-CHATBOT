from sqlalchemy import Column, Integer, String
from app.database.base import Base

class Teacher(Base):
    __tablename__ = "teachers"

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String(100))
    course = Column(String(100))
    experience = Column(String(100))
    