from pydantic import BaseModel


class LoginInf(BaseModel):
    loginname: str
    password: str


class FaceLoginInf(BaseModel):
    image: str
