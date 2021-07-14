from fastapi import APIRouter, UploadFile, File, Form

from util import response_code

from service import userService

from model import user_inf

# 构建api路由
router = APIRouter()


@router.post("/changepwd", tags=["user"])
async def changePassword(user: user_inf.PwdChange):
    """更改密码"""
    status_code, msg_code = userService.changePassword(user)
    return response_code.response(status_code, msg_code)


@router.post("/facereg", tags=["user"])
async def faceRegister(image: UploadFile = File(...), userid: int = Form(...)):
    """刷脸登记"""
    contentsByte = await image.read()
    status_code, msg_code = userService.faceRegister(contentsByte,
                                                     image,
                                                     userid)
    return response_code.response(status_code, msg_code)
