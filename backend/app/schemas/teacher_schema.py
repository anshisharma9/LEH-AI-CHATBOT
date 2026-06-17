from pydantic import BaseModel
from typing import Optional


class TeacherCreate(BaseModel):
    name: str
    course: str
    experience: Optional[str] = None