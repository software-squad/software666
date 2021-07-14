from pydantic import BaseModel


class FileInf(BaseModel):
    fileid: int
    title: str
    filename: str = None
    remark: str
    userid: int
    username: str
    filepath: str = None
