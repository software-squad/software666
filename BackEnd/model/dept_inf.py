from pydantic import BaseModel


# 高明
class DeptInf(BaseModel):
    deptid: int
    deptname: str
    remark: str

# 高明
class AddDeptInf(BaseModel):
    deptname: str
    remark: str

# 高明
class DelDeptInf(BaseModel):
    deptid: int
