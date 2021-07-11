from pydantic import BaseModel


class DocumentInf(BaseModel):
    fileid: int
    title: str
    filename: str
    remark: str
    createdate: str
    username: str
    filepath: str


class UploadDocumentInf(BaseModel):
    title: str
    remark: str
    createdate: str
    username: str
