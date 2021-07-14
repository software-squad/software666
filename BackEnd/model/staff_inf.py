from pydantic import BaseModel


class StaffInf(BaseModel):
    userid: int
    password: str = None
    status: int = None
    loginname: str = None
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
    deptname: str
    jobname: str
    remark: str


class StaffDeptAndJob(BaseModel):
    deptid: int
    jobid: int
