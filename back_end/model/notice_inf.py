from pydantic import BaseModel


class NoticeInf(BaseModel):
    noticeid: int = None
    title: str
    content: str
    userid: int
    username: str


class DelNoticeInf(BaseModel):
    noticeid: int
