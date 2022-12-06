from sqlalchemy.orm import Session
from models import models
from schemas import schemas

# read
def get_clases(db: Session, skip:int = 0, limit: int = 100):
    return db.query(models.Class).offset(skip).limit(limit).all()

def get_class(db: Session, class_id: int):
    return db.query(models.Class).filter(models.Class.class_id == class_id).first()

# create
def create_class(db: Session, Class: schemas.Class):
    Class = models.Class(teacher_name = Class.teacher_name, year = Class.year )
    db.add(Class)
    db.commit()

    return Class

# update
def update_class(db: Session, class_id: int, value: schemas.Update_Class):

    Class = db.query(models.Class).filter(models.Class.class_id == class_id)
    Class.update(value.dict(exclude_unset=True))

    print(Class)
    db.commit()

    return Class.first()

# delete
def delete_class(db: Session, class_id: int):

    db.query(models.Class).filter(models.Class.class_id == class_id).delete()

    db.commit()

    return