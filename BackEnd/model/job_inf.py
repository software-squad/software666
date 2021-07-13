from pydantic import BaseModel


class JobInf(BaseModel):
    jobid: int = None
    jobname: str
    remark: str
    deptname: str
    deptid: int = None


class DelJobInf(BaseModel):
    jobid: int
