from pydantic import BaseModel


class JobInf(BaseModel):
    jobid: int
    jobname: str
    remark: str
    deptid:int

class DelJobInf(BaseModel):
    jobid:int

class AddJobInf(BaseModel):
    jobname: str
    remark: str
    deptid:int
