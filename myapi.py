from fastapi import FastAPI,Path

app=FastAPI()

students= {
    1: {"name": "John", "dept": "Computer Science", "student_id": "CS12345"},
    2: {"name": "Jane Smith", "dept": "Electrical Engineering", "student_id": "EE67890"},
    3: {"name": "Bob Johnson", "dept": "Mechanical Engineering", "student_id": "ME54321"},
    4: {"name": "Alice Brown", "dept": "Physics", "student_id": "PH98765"},
    5: {"name": "Charlie Davis", "dept": "Mathematics", "student_id": "MA45678"},
    6: {"name": "Eva White", "dept": "Chemistry", "student_id": "CH23456"},
    7: {"name": "Frank Miller", "dept": "Biology", "student_id": "BI78901"},
    8: {"name": "Grace Turner", "dept": "Civil Engineering", "student_id": "CE34567"},
    9: {"name": "Henry Evans", "dept": "Environmental Science", "student_id": "ES89012"},
    10: {"name": "Isabel Carter", "dept": "Geology", "student_id": "GL12389"}
}


@app.get("/")
def index():
    return {"name":"Momin"}
#List data
@app.get("/all/students")
def all_students():
    return students
#retrive by Id
@app.get("/get-student/{student_id}")
def get_student(student_id:int= Path(...,description="The ID of the student you want to view.",gt=0,lt=10)):
    #gt=Greater than, lt=less than, ge=Greater than equal ,le=less than equal
    return students[student_id]

@app.get("/get-by-name")
def get_student(name:str):
    for student_id in students:
        if students[student_id]["name"]==name:
            return students[student_id]
        return {"Message":"Data not found"}
    
