from fastapi import APIRouter, UploadFile, File, Form

from util import response_code

from service import loginService

from model import login_inf

# 构建api路由
router = APIRouter()


@router.post("/login", tags=["login"])
async def loginByNameAndPwd(user: login_inf.LoginInf):
    """账号密码登录"""
    status_code, result, msg_code = loginService.validateUserByAccount(user)
    return response_code.response(status_code, msg_code, result)


@router.post("/facelogin", tags=["login"])
async def loginByFace(faceImage: UploadFile = File(...),
                      loginname: str = Form(...)):
    """刷脸登录"""
    faceByte = await faceImage.read()  # 获得刷脸时上传照片的字节
    status_code, result, msg_code = loginService.validateUserByFace(faceByte,
                                                                    faceImage,
                                                                    loginname)
    return response_code.response(status_code, msg_code, result)
