from fastapi import APIRouter

from util import response_code

from service import userService

from model import user_inf

# 构建api路由
router = APIRouter()


@router.post("/changepwd", tags=["user"])
async def changePassword(user: user_inf.PwdChange):
    # 更改密码
    msg_code = userService.changePassword(user)
    return response_code.updateResponse(msg_code)


@router.post("/facereg", tags=["user"])
async def faceRegister(user: user_inf.FaceReg):
    # 刷脸登记
    msg_code = userService.faceRegister(user)
    return response_code.updateResponse(msg_code)
