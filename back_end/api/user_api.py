from fastapi import APIRouter

from util.response import response
from service import user_service
from model import user_inf

# 构建api路由
router = APIRouter()


@router.post("/login", tags=["login"])
async def login_by_account(user: user_inf.LoginInf):
    """账号密码登录"""
    status_code, result, msg_code = user_service.validate_by_account(user)
    return response(status_code, msg_code, result)


@router.post("/user/changePwd", tags=["user"])
async def change_pwd(user: user_inf.PwdChange):
    """更改密码"""
    status_code, msg_code = user_service.change_pwd(user)
    return response(status_code, msg_code)


@router.post("/admin/resetPwd", tags=["user"])
async def reset_pwd(user: user_inf.PwdReset):
    """重置密码"""
    status_code, msg_code = user_service.reset_pwd(user)
    return response(status_code, msg_code)
