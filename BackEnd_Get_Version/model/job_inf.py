from pydantic import BaseModel


class JobInf(BaseModel):
    jobid: int = None
    jobname: str
    remark: str
    deptname: str = None
    deptid: int = None
