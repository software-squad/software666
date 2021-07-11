from pydantic import BaseModel


#高明
class document_inf(BaseModel):
    fileid: int
    title: str
    filename: str
    remark: str
    createdate: str
    username: str
    filepath: str


#高明
class DelDocumentInf(BaseModel):
    fileid: int
