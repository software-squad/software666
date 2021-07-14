from pydantic import BaseModel


class StaffInf(BaseModel):
    userid: int
    password: str
    status: int
    loginname: str
    faceurl: str
    facepath: str
    deptid: int
    jobid: int
    username: str
    cardid: str
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
    deptname: str
    jobname: str
    remark: str


class StaffDeptAndJob(BaseModel):
    deptid: int
    jobid: int
