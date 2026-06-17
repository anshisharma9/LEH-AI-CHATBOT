from pydantic import BaseModel

class ClassTimingCreate(BaseModel):
    course: str
    teacher: str
    timing: str