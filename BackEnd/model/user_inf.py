from pydantic import BaseModel


class UserName(BaseModel):
    username: str


class Userid(BaseModel):
    userid: int


class PwdChange(BaseModel):
    userid: int
    oldpwd: str
    newpwd: str


class FaceReg(BaseModel):
    image: str
    userid: int
