from fastapi import FastAPI,Path,Query,HTTPException
from typing import Optional
from pydantic import BaseModel
app=FastAPI()

students= {
    1: {"name": "John", "dept": "Computer Science", "student_id": "CS12345"},
    2: {"name": "Jane Smith", "dept": "Electrical Engineering", "student_id": "EE67890"},
    3: {"name": "Bob Johnson", "dept": "Mechanical Engineering", "student_id": "ME54321"},
    4: {"name": "Alice Brown", "dept": "Physics", "student_id": "PH98765"},
    5: {"name": "Charlie Davis", "dept": "Mathematics", "student_id": "MA45678"},
    6: {"name": "Eva White", "dept": "Chemistry", "student_id": "CH23456"},
    7: {"name": "Frank Miller", "dept": "Biology", "student_id": "BI78901"},
    8: {"name": "Bob Turner", "dept": "Civil Engineering", "student_id": "CE34567"},
    9: {"name": "Henry Evansbob", "dept": "Environmental Science", "student_id": "ES89012"},
    10: {"name": "Isabel Carter", "dept": "Geology", "student_id": "GL12389"}
}

class Student(BaseModel):
    name:str
    dept:str
    student_id:str


class UpdateStudnet(BaseModel):
    name:Optional[str]=None
    dept:Optional[str]=None
    student_id:Optional[str]=None


class Student(BaseModel):
    name:str
    dept:str
    student_id:str


@app.get("/")
def index():
    return {"name":"Momin"}


#List data
@app.get("/all/students")
def all_students():
    return students


#Get by Id
@app.get("/get-student/{student_id}")
def get_student(student_id:int= Path(...,description="The ID of the student you want to view.",gt=0,lt=10)):
    #gt=Greater than, lt=less than, ge=Greater than equal ,le=less than equal
    return students[student_id]

#Get by fullname

#Get by full name
@app.get("/get-by-name/{student_id}")
def get_student(*,student_id:int,name:Optional[str]=None,test:int):
    for student_id in students:
        if students[student_id]["name"]==name:
            return students[student_id]
        return {"Message":"Data not found"}
    


#Get by character
@app.get("/get-by-name-character/")
async def search_students_by_name(query_name: str = Query(..., description="Search students by name")):
    matching_students = [
        student for student in students.values() if query_name.lower() in student["name"].lower()
    ]
    if not matching_students:
        raise HTTPException(status_code=404, detail="No student found")
    return {"matching_students": matching_students}


#Create
@app.post("/create-student/{student_id}")
def create_student(student_id:int ,student:Student):
    if student_id in students:
        return {"Error":"This Student is already exist"}
    students[student_id]=student
    return students[student_id]


#Update
@app.put("/update-student/{student_id}")
def update_student(student_id:int, student:UpdateStudnet):
    if student_id not in students:
        return{"Error":"Student is not found"}
    
    if student.name !=None:
        students[student_id].name=student.name

    if student.dept !=None:
        students[student_id].dept=student.dept

    if student.student_id !=None:
        students[student_id].student_id=student.student_id
         
    return students[student_id]
    


#Delete
@app.delete("/delete-student/{student_id}")
def delete_student(student_id:int):
    if student_id not in students:
        return{"Error":"This student does dot in List"}
    del students[student_id]
    return{"Message":"Student deleted Successfully"}
