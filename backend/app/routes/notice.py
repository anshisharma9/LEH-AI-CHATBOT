from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session

from app.database.session import get_db
from app.models.notice import Notice
from app.schemas.notice_schema import NoticeCreate

router = APIRouter()
@router.post("/")
def add_notice(
    notice: NoticeCreate,
    db: Session = Depends(get_db)
):

    new_notice = Notice(
        title=notice.title,
        description=notice.description
    )

    db.add(new_notice)
    db.commit()
    db.refresh(new_notice)

    return {
        "message": "Notice Added Successfully"
    }
@router.get("/")
def get_notices(
    db: Session = Depends(get_db)
):
    return db.query(Notice).all()

@router.put("/{notice_id}")
def update_notice(
    notice_id: int,
    notice: NoticeCreate,
    db: Session = Depends(get_db)
):

    db_notice = db.query(Notice).filter(
        Notice.id == notice_id
    ).first()

    if not db_notice:
        return {
            "message": "Notice Not Found"
        }

    db_notice.title = notice.title
    db_notice.description = notice.description

    db.commit()

    return {
        "message": "Notice Updated Successfully"
    }
@router.delete("/{notice_id}")
def delete_notice(
    notice_id: int,
    db: Session = Depends(get_db)
):

    db_notice = db.query(Notice).filter(
        Notice.id == notice_id
    ).first()

    if not db_notice:
        return {
            "message": "Notice Not Found"
        }

    db.delete(db_notice)
    db.commit()

    return {
        "message": "Notice Deleted Successfully"
    }