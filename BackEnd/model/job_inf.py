from pydantic import BaseModel


class JobInf(BaseModel):
    id: int
    name: str
    remark: str
