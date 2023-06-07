from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from models import create_database, Student, session
from typing import List
from datetime import datetime
app = FastAPI()

# Define request/response models
class StudentRequest(BaseModel):
    name: str
    email: str
    phone: int
    address: str

class StudentResponse(BaseModel):
    student_id: int
    name: str
    email: str
    phone: int
    address: str
    
    
    class Config:
        orm_mode = True
        
# Define request/response models
class StudentPatchRequest(BaseModel):
    name: str = None
    email: str = None
    phone: str = None
    address: str = None

# GET request to retrieve all students
@app.get("/")
def get_all_stdents() :
    all_student = session.query(Student).all()
    return all_student

    
@app.delete("/students/{student_id}")
def delete_student(student_id: int):
    student = session.query(Student).filter(Student.StudentID == student_id).first()
    if student:
        session.delete(student)
        session.commit()
        return {"message": "Customer deleted successfully"}
    else:
        raise HTTPException(status_code=404, detail="Customer not found")

