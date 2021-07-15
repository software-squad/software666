from pydantic import BaseModel


class LoginInf(BaseModel):
    loginname: str
    password: str


class PwdChange(BaseModel):
    userid: int
    oldpwd: str
    newpwd: str
