from pydantic import BaseModel


class job_inf(BaseModel):
    jobid: str
    jobname: str
    remark: str
