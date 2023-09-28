from fastapi import FastAPI, Path, HTTPException, status
from typing import List
import uvicorn
from examResult import Result, Information, LifeHistorys

app = FastAPI()
fake_user_db = []


@app.get(path="/users/", response_model=Result)
def get_user():
    status = LifeHistory(maritalStatus="Single", relation="None")
    familyInfo = Information(fullName="Md Biaksuzzaman", fatherName="Md Rafiqul Islam", motherName="Mst Halima Khatun",
                             brotherName="Md Lazimul Islam Latul", sisterName="Mst Romana Akter Sinthi",
                             maritalStatus=status)
    studentsInfo = Result(roll=4, mark=78.5, userName="bikas", email="bikasictiu1718@gmail.com",personDetails=familyInfo)
    return studentsInfo


@app.post(path="/users/", response_model=Result, status_code=status.HTTP_201_CREATED)
def CreateUser(student: Result):
    fake_user_db.append(student)
    return student


@app.get(path="/all_users/", response_model=List[Result])
def get_all_student_info():
    return fake_user_db


@app.get(path="/users/{student_id}", response_model=Result)
def read_Student_details(student_id: int = Path(..., title=f"Student details", ge=0)):
    for i, value in enumerate(fake_user_db):
        if value["roll"] == student_id:
            index = i
    return fake_user_db[index]
    # if student_id < len(fake_user_db):
    #     return fake_user_db[student_id]
    raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Student ID not found")


@app.delete(path="/users/{student_id}", response_model=List[Result])
def delete_student_id(student_id: int):
    if student_id > len(fake_user_db):
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=f" The {student_id} not exist in the Database")
    fake_user_db.pop(student_id)
    return fake_user_db


# @app.put(path="/users/{roll}", response_model=List[Result])
# def update_data(roll: int, post: Result):
#     for i, value in enumerate(fake_user_db):
#         if value["roll"] == roll:
#             index = i
#     fake_user_db[index] = roll
#     return fake_user_db


if __name__ == '__main__':
    uvicorn.run(app, host="0.0.0.0", port=8080)
