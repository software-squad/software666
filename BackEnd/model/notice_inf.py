from pydantic import BaseModel


class NoticeInf(BaseModel):
    noticeid: int
    title: str
    content: str
    userid: int
    username: str


class AddNoticeInf(BaseModel):
    title: str
    content: str
    userid: int
    username: str
