from pydantic import BaseModel

class KnowledgeCreate(BaseModel):

    title: str

    content: str