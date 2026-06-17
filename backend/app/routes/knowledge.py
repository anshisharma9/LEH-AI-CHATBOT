from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from pydantic import BaseModel

from app.database.session import get_db
from app.models.knowledge import Knowledge

router = APIRouter()


class KnowledgeCreate(BaseModel):
    question: str
    answer: str


@router.post("/")
def add_knowledge(
    data: KnowledgeCreate,
    db: Session = Depends(get_db)
):

    item = Knowledge(
        question=data.question,
        answer=data.answer
    )

    db.add(item)
    db.commit()

    return {
        "message": "Knowledge Added"
    }


@router.get("/")
def get_knowledge(
    db: Session = Depends(get_db)
):
    return db.query(Knowledge).all()


@router.delete("/{knowledge_id}")
def delete_knowledge(
    knowledge_id: int,
    db: Session = Depends(get_db)
):

    item = db.query(Knowledge).filter(
        Knowledge.id == knowledge_id
    ).first()

    if not item:
        return {
            "message": "Knowledge Not Found"
        }

    db.delete(item)
    db.commit()

    return {
        "message": "Knowledge Deleted"
    }