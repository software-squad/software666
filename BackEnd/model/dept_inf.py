from pydantic import BaseModel


class DeptInf(BaseModel):
    deptid: int
    deptname: str
    remark: str

class AddDeptInf(BaseModel):
    deptname: str
    remark: str

class DelDeptInf(BaseModel):
    deptid: int
