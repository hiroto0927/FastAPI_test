from sqlalchemy.orm import Session
from models import models
from schemas import schemas

# read
def get_students(db: Session, skip:int = 0, limit: int = 100):
    return db.query(models.Student).offset(skip).limit(limit).all()

def get_student(db: Session, student_id: int):
    return db.query(models.Student).filter(models.Student.student_id == student_id).first()

# create
def create_student(db: Session, student: schemas.Student):
    db_student = models.Student(user_name = student.user_name, class_id = student.class_id)
    db.add(db_student)
    db.commit()

    return db_student

# update
def update_student(db: Session, student_id: int, value: schemas.Update_Student):

    student = db.query(models.Student).filter(models.Student.student_id == student_id)
    student.update(value.dict(exclude_unset=True))

    print(student)
    db.commit()

    return student.first()

# delete
def delete_student(db: Session, student_id: int):

    db.query(models.Student).filter(models.Student.student_id == student_id).delete()

    db.commit()

    return