from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session

from app.database.session import get_db
from app.models.class_timing import ClassTiming
from app.schemas.class_timing_schema import ClassTimingCreate

router = APIRouter()

@router.post("/")
def add_timing(
    timing: ClassTimingCreate,
    db: Session = Depends(get_db)
):

    new_timing = ClassTiming(
        course=timing.course,
        teacher=timing.teacher,
        timing=timing.timing
    )

    db.add(new_timing)
    db.commit()
    db.refresh(new_timing)

    return {
        "message": "Timing Added Successfully"
    }
    
@router.get("/")
def get_timings(
    db: Session = Depends(get_db)
):
    return db.query(ClassTiming).all()

@router.put("/{timing_id}")
def update_timing(
    timing_id: int,
    timing: ClassTimingCreate,
    db: Session = Depends(get_db)
):

    db_timing = db.query(ClassTiming).filter(
        ClassTiming.id == timing_id
    ).first()

    if not db_timing:
        return {
            "message": "Timing Not Found"
        }

    db_timing.course = timing.course
    db_timing.teacher = timing.teacher
    db_timing.timing = timing.timing

    db.commit()

    return {
        "message": "Timing Updated Successfully"
    }
@router.delete("/{timing_id}")
def delete_timing(
    timing_id: int,
    db: Session = Depends(get_db)
):

    db_timing = db.query(ClassTiming).filter(
        ClassTiming.id == timing_id
    ).first()

    if not db_timing:
        return {
            "message": "Timing Not Found"
        }

    db.delete(db_timing)
    db.commit()

    return {
        "message": "Timing Deleted Successfully"
    }