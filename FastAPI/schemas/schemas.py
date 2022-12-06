from typing import Optional
from pydantic import BaseModel, Field

class Create_Student(BaseModel):
    user_name: str= Field(min_length=1,max_length=12)
    class_id: int

class Student(Create_Student):
    student_id: int

    class Config:
        orm_mode = True


class Create_Class(BaseModel):
    teacher_name : str = Field(min_length=1,max_length=12)
    year:int


class Class(Create_Class):
    class_id:int

    class Config:
        orm_mode = True

class Update_Student(BaseModel):
    user_name: Optional[str]  = Field(min_length=1,max_length=12)
    class_id: Optional[int] 

    class Config:
        orm_mode = True

class Update_Class(BaseModel):
    teacher_name : Optional[str]  = Field(min_length=1,max_length=12)
    year : Optional[int]

    class Config:
        orm_mode = True