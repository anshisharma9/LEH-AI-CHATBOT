from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session

from app.database.session import get_db
from app.models.faq import FAQ
from app.schemas.faq_schema import FAQCreate

router = APIRouter()
@router.post("/")
def add_faq(
    faq: FAQCreate,
    db: Session = Depends(get_db)
):

    new_faq = FAQ(
        question=faq.question,
        answer=faq.answer
    )

    db.add(new_faq)
    db.commit()
    db.refresh(new_faq)

    return {
        "message": "FAQ Added Successfully"
    }
    
@router.get("/")
def get_faqs(
    db: Session = Depends(get_db)
):
    return db.query(FAQ).all()
@router.get("/")
def get_faqs(
    db: Session = Depends(get_db)
):
    return db.query(FAQ).all()

@router.put("/{faq_id}")
def update_faq(
    faq_id: int,
    faq: FAQCreate,
    db: Session = Depends(get_db)
):

    db_faq = db.query(FAQ).filter(
        FAQ.id == faq_id
    ).first()

    if not db_faq:
        return {
            "message": "FAQ Not Found"
        }

    db_faq.question = faq.question
    db_faq.answer = faq.answer

    db.commit()

    return {
        "message": "FAQ Updated Successfully"
    }
@router.delete("/{faq_id}")
def delete_faq(
    faq_id: int,
    db: Session = Depends(get_db)
):

    db_faq = db.query(FAQ).filter(
        FAQ.id == faq_id
    ).first()

    if not db_faq:
        return {
            "message": "FAQ Not Found"
        }

    db.delete(db_faq)
    db.commit()

    return {
        "message": "FAQ Deleted Successfully"
    }