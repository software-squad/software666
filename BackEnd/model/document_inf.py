from pydantic import BaseModel


class document_inf(BaseModel):
    fileid: int
    title: str
    filename: str
    remark: str
    createdate: str
    username: str
    filepath: str


class DelDocumentInf(BaseModel):
    fileid: int
