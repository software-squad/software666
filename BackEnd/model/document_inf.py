from pydantic import BaseModel


class DocumentInf(BaseModel):
    fileid: int
    title: str
    filename: str = None
    remark: str
    userid: int
    username: str
    filepath: str = None
