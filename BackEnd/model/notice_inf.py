from pydantic import BaseModel


class NoticeInf(BaseModel):
    noticeid: int
    title: str
    content: str
    createdate: str
    userid: int
    username: str

class DelNoticeInf(BaseModel):
    noticeid:int

class AddNoticeInf(BaseModel):
    title:str
    content:str
    createdate:str
    userid:int
    username:str
