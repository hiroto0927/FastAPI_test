from http.client import HTTPException
from fastapi import FastAPI,Depends
from sqlalchemy.orm import Session
from typing import List
from database import database
from models import models
from schemas import schemas
from crud import crud_class, crud_student

app = FastAPI()

models.Base.metadata.create_all(bind= database.engine)

def get_db():
    db = database.SessionLocal()
    try:
        yield db
    finally:
        db.close()

# read
@app.get('/student', response_model= List[schemas.Student])
async def  get_students(skip: int = 0, limit: int = 100, db: Session = Depends(get_db)):
    students = crud_student.get_students(db=db, skip=skip, limit= limit)
    return students

@app.get('/class', response_model= List[schemas.Class])
async def  get_clases(skip: int = 0, limit: int = 100, db: Session = Depends(get_db)):
    classes = crud_class.get_clases(db=db, skip=skip, limit=limit)
    return classes

@app.get('/student/{student_id}',response_model=schemas.Student)
async def get_student(student_id: int, db: Session = Depends(get_db)):
    student = crud_student.get_student(db=db, student_id= student_id)
    if student is None:
        raise HTTPException(status_code=404, detail="User not found")
    return student

@app.get('/class/{class_id}',response_model=schemas.Class)
async def get_student(class_id: int, db: Session = Depends(get_db)):
    Class = crud_class.get_class(db=db, class_id=class_id)
    if Class is None:
        raise HTTPException(status_code=404, detail="User not found")
    return Class

# create
@app.post('/student',response_model= schemas.Student)
async def create_student(student: schemas.Create_Student, db: Session = Depends(get_db)):
    return crud_student.create_student(db=db,student=student)

@app.post('/class',response_model= schemas.Class)
async def create_class(Class: schemas.Create_Class, db: Session = Depends(get_db)):
    return crud_class.create_class(db=db,Class=Class)

# update
@app.patch('/student/{student_id}', response_model=schemas.Student)
async def update_student(student_id: int , student: schemas.Update_Student ,db: Session = Depends(get_db)):
    return crud_student.update_student(db=db,student_id=student_id, value= student)

@app.patch('/class/{class_id}', response_model= schemas.Class)
async def update_class(class_id: int, Class: schemas.Update_Class, db: Session = Depends(get_db)):
    return crud_class.update_class(db=db, class_id = class_id, value=Class)

# delete
@app.delete('/student/{student_id}', status_code=204)
async def delete_student(student_id: int ,db: Session = Depends(get_db)):
    return crud_student.delete_student(db=db, student_id=student_id)

@app.delete('/class/{class_id}', status_code=204)
async def delete_class(class_id: int, db: Session = Depends(get_db)):
    return crud_class.delete_class(db=db, class_id=class_id)