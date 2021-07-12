from pydantic import BaseModel


class DeptInf(BaseModel):
    deptid: int
    deptname: str
    depturl: str
    remark: str


class AddDeptInf(BaseModel):
    deptname: str
    depturl: str
    remark: str


class DelDeptInf(BaseModel):
    deptid: int
