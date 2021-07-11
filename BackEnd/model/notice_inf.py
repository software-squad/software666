from pydantic import BaseModel


class NoticeInf(BaseModel):
    id: int
    title: str
    content: str
    createdate: str
    userid: str
