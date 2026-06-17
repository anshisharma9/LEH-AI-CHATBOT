from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session

from app.database.session import get_db
from app.models.teacher import Teacher
from app.schemas.teacher_schema import TeacherCreate

# JWT security (optional for now)


router = APIRouter()


# Add Teacher
@router.post("/")
def add_teacher(
    teacher: TeacherCreate,
    db: Session = Depends(get_db),
    
):

    new_teacher = Teacher(
        name=teacher.name,
        course=teacher.course,
        experience=teacher.experience,
        
    )

    db.add(new_teacher)
    db.commit()
    db.refresh(new_teacher)

    return {
        "message": "Teacher Added Successfully",
        "teacher": {
            "id": new_teacher.id,
            "name": new_teacher.name,
            "course": new_teacher.course
        }
    }


# Get All Teachers
@router.get("/")
def get_teachers(
    db: Session = Depends(get_db)
):
    return db.query(Teacher).all()


# Update Teacher
@router.put("/{teacher_id}")
def update_teacher(
    teacher_id: int,
    teacher: TeacherCreate,
    db: Session = Depends(get_db),
):

    db_teacher = db.query(Teacher).filter(
        Teacher.id == teacher_id
    ).first()

    if not db_teacher:
        return {
            "message": "Teacher Not Found"
        }

    db_teacher.name = teacher.name
    db_teacher.course = teacher.course
    db_teacher.experience = teacher.experience
   

    db.commit()

    return {
        "message": "Teacher Updated Successfully"
    }


# Delete Teacher
@router.delete("/{teacher_id}")
def delete_teacher(
    teacher_id: int,
    db: Session = Depends(get_db),
   
):

    db_teacher = db.query(Teacher).filter(
        Teacher.id == teacher_id
    ).first()

    if not db_teacher:
        return {
            "message": "Teacher Not Found"
        }

    db.delete(db_teacher)
    db.commit()

    return {
        "message": "Teacher Deleted Successfully"
    }