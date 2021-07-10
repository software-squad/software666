from pydantic import BaseModel


class StaffInf(BaseModel):
    userid: int
    password: str
    status: str
    username: str
    faceurl: str
    facepath: str
    deptid: int
    jobid: int
    name: str
    cardid: int
    address: str
    postcode: str
    tel: str
    qqnum: str
    email: str
    sex: str
    party: str
    birthday: str
    education: str
    createdate: str


class StaffDept(BaseModel):
    dept: str


class StaffDeptAndJob(BaseModel):
    dept: str
    job: str
