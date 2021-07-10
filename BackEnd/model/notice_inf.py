from pydantic import BaseModel


class notice_inf(BaseModel):
    noticeid: str
    title: str
    content: str
    createdate: str
    userid: str
