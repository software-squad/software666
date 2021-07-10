from fastapi import APIRouter

from util import response_code

from service import loginService

from model import login_inf

# 构建api路由
router = APIRouter()


@router.post("/login", tags=["login"])
async def loginByNameAndPwd(user: login_inf.LoginInf):
    # 账号密码登录
    status_code, result, msg_code = loginService.validateUserByAccount(user)
    return response_code.response(status_code, msg_code, result)


@router.post("/facelogin", tags=["login"])
async def loginByFace(user: login_inf.FaceLoginInf):
    # 刷脸登录
    status_code, result, msg_code = loginService.validateUserByFace(user)
    return response_code.response(status_code, msg_code, result)
