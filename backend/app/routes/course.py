from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session

from app.database.session import get_db
from app.models.course import Course
from app.schemas.course_schema import CourseCreate

router = APIRouter()

@router.post("/")
def add_course(
    course: CourseCreate,
    db: Session = Depends(get_db)
):

    new_course = Course(
        course_name=course.course_name,
        fees=course.fees,
        duration=course.duration,
        description=course.description
    )

    db.add(new_course)
    db.commit()
    db.refresh(new_course)

    return {
        "message": "Course Added Successfully"
    }
@router.get("/")
def get_courses(
    db: Session = Depends(get_db)
):
    return db.query(Course).all()


@router.put("/{course_id}")
def update_course(
    course_id: int,
    course: CourseCreate,
    db: Session = Depends(get_db)
):

    db_course = db.query(Course).filter(
        Course.id == course_id
    ).first()

    if not db_course:
        return {
            "message": "Course Not Found"
        }

    db_course.course_name = course.course_name
    db_course.fees = course.fees
    db_course.duration = course.duration
    db_course.description = course.description

    db.commit()

    return {
        "message": "Course Updated Successfully"
    }
    
@router.delete("/{course_id}")
def delete_course(
    course_id: int,
    db: Session = Depends(get_db)
):

    db_course = db.query(Course).filter(
        Course.id == course_id
    ).first()

    if not db_course:
        return {
            "message": "Course Not Found"
        }

    db.delete(db_course)
    db.commit()

    return {
        "message": "Course Deleted Successfully"
    }