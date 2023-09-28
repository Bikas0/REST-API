from pydantic import BaseModel


class LifeHistory(BaseModel):
    maritalStatus: str
    relation: str


class Information(BaseModel):
    fullName: str
    fatherName: str
    motherName: str
    brotherName: str
    sisterName: str
    maritalStatus: LifeHistory


class Result(BaseModel):
    roll: int
    mark: float
    userName: str
    email: str
    personDetails: Information

