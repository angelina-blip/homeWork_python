from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Column, Integer, String

Base = declarative_base()

class Student(Base):
    __tablename__ = 'student'
    user_id = Column(Integer, primary_key=True, index=True)
    level = Column(String)
    education_form = Column(String)
    subject_id = Column(Integer)