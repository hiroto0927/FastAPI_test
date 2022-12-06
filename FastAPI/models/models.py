# coding: utf-8
from sqlalchemy import Column, ForeignKey, Integer, String
from sqlalchemy.orm import relationship
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()
metadata = Base.metadata


class Class(Base):
    __tablename__ = 'class'

    class_id = Column(Integer, primary_key=True)
    teacher_name = Column(String(12), index=True)
    year = Column(Integer, index=True)


class Student(Base):
    __tablename__ = 'student'

    student_id = Column(Integer, primary_key=True, index=True)
    user_name = Column(String(12), index=True)
    class_id = Column(ForeignKey('class.class_id'), nullable=False, index=True)

    _class = relationship('Class')
