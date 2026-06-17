from sqlalchemy import Column, Integer, String, Text
from app.database.base import Base

class Knowledge(Base):
    __tablename__ = "knowledge"

    id = Column(Integer, primary_key=True, index=True)
    question = Column(String(500))
    answer = Column(Text)