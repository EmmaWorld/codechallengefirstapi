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
def get_all_students() :
    all_student = session.query(Student).all()
    return all_student

# GET request to retrive students by ID

@app.get("/student/{student_id}")
def get_student(student_id: int):
    student = session.query(Student).filter(Student.StudentID == student_id).first()
    if student:
        return StudentResponse(
            student_id=student.StudentID,
            name=student.Name,
            email=student.Email,
            phone=student.Phone,
            address=student.Address
        )
    else:
        raise HTTPException(status_code=404, detail="Student not found")

# Delete the students by ID
@app.delete("/students/{student_id}")
def delete_student(student_id: int):
    student = session.query(Student).filter(Student.StudentID == student_id).first()
    if student:
        session.delete(student)
        session.commit()
        return {"message": "Student deleted successfully"}
    else:
        raise HTTPException(status_code=404, detail="Student not found")

#Post and Create the student
@app.post("/students")
def create_student(student: StudentRequest):
    new_student = Student(
        Name=student.name,
        Email=student.email,
        Phone=student.phone,
        Address=student.address
    )
    session.add(new_student)
    session.commit()
    session.refresh(new_student)
    return StudentResponse(
        student_id=new_student.StudentID,
        name=new_student.Name,
        email=new_student.Email,
        phone=new_student.Phone,
        address=new_student.Address
    )


# @app.patch("/students/{student_id}")
# def patch_student(student_id: int, patch_data: StudentPatchRequest):
#     student = session.query(Student).filter(Student.StudentID == student_id).first()
#     if student:
#         # Update the Student with the provided patch data
#         if patch_data.name:
#             student.Name = patch_data.name
#         if patch_data.email:
#             student.Email = patch_data.email
#         if patch_data.phone:
#             student.Phone = patch_data.phone
#         if patch_data.address:
#             student.Address = patch_data.address

#         session.commit()

#         return {"message": "Student updated successfully"}
#     else:
#         raise HTTPException(status_code=404, detail="Student not found")


@app.patch("/students/{student_id}")
def patch_student(student_id: int, patch_data: StudentPatchRequest):
    student = session.query(Student).filter(Student.StudentID == student_id).first()
    if student:
        # Update the Student with the provided patch data
        if patch_data.name is not None:
            student.Name = patch_data.name
        if patch_data.email is not None:
            student.Email = patch_data.email
        if patch_data.phone is not None:
            student.Phone = patch_data.phone
        if patch_data.address is not None:
            student.Address = patch_data.address

        session.commit()

        return {"message": "Student updated successfully"}
    else:
        raise HTTPException(status_code=404, detail="Student not found")
