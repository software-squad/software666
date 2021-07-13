from pydantic import BaseModel


class DeptInf(BaseModel):
    deptid: int = None
    deptname: str
    depturl: str
    remark: str
