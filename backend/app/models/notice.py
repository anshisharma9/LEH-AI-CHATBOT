from sqlalchemy import Column, Integer, String, Text
from app.database.base import Base

class Notice(Base):
    __tablename__ = "notices"

    id = Column(Integer, primary_key=True, index=True)
    title = Column(String(255))
    description = Column(Text)