from pydantic import BaseModel


class DocumentInf(BaseModel):
    fileid: int
    title: str
    filename: str
    remark: str
    username: str
    filepath: str
