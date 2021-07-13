from pydantic import BaseModel


class PwdChange(BaseModel):
    userid: int
    oldpwd: str
    newpwd: str


class FaceReg(BaseModel):
    image: str
    userid: int
