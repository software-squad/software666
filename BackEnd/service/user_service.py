import time

import jwt
from fastapi import status

from dao import staff_dao
from util import security, message


def validate_by_account(user):
    """通过用户名和密码登录"""
    status_code, result = staff_dao.select('LOGINNAME', user.loginname)
    msg_code = message.ENTER_SUCCESS
    new_result = {}  # 用于存放前端需要返回的数据
    if status_code == status.HTTP_400_BAD_REQUEST or not result or \
       security.MD5(user.password) != result[0]['password']:  # 判断账号是否存在或密码是否正确
        new_result = None
        msg_code = message.PWD_WRONG
        return status_code, None, message.PWD_WRONG
    else:
        result = result[0]
        token = security.jwt_encode(result['loginname'], result['userid'])  # 生成token
        new_result['token'] = token
        new_result['userid'] = result['userid']
        new_result['status'] = result['status']
        new_result['username'] = result['username']
    return status_code, new_result, msg_code


def change_pwd(user):
    """更改密码"""
    status_code, result = staff_dao.select("USERID", user.userid)
    msg_code = message.UPD_SUCCESS
    # 检查该用户旧密码是否输入正确
    if status_code == status.HTTP_400_BAD_REQUEST or \
       result[0]['password'] != security.MD5(user.oldpwd):
        return status_code, message.UPD_FAILURE
    else:
        # 如果旧密码输入正确，则修改密码
        status_code = staff_dao.edit('USERID', user.userid, ['PASSWORD'],
                                     [security.MD5(user.newpwd)])
        if status_code == status.HTTP_400_BAD_REQUEST:
            msg_code = message.UPD_FAILURE
    return status_code, msg_code
