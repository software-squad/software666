from fastapi import status
from dao import loginDao
from util import msg_code
import time
import jwt

token_dict = {
    'iat': time.time(),  # 时间戳
    'name': 'lowman'  # 自定义的参数
}

headers = {
    'aig': 'HS256'  # 声明所使用的的算法
}



def validateUserByAccount(user):
    status_code, result = loginDao.select("LOGINNAME", user.loginname)
    token = 0
    code = msg_code.ENTER_SUCCESS
    new_result = {}
    if status_code == status.HTTP_400_BAD_REQUEST or not result or \
       result[0]['password'] != user.password:
        new_result = None
        code = msg_code.PWD_WRONG
        return status_code, None, msg_code.PWD_WRONG
    else:
        result = result[0]
        token = jwt.encode(token_dict,  # payload 有效载体
                           "zhananbudanchou1234678",  # 进行加密签名的密钥
                           algorithm="HS256",  # 指明签名算法方式，默认也是HS256
                           headers=headers).decode('ascii')
        new_result['token'] = token
        new_result['userid'] = result['userid']
        new_result['status'] = result['status']
    return status_code, new_result, code


def validateUserByFace(user):
    status_code, result = loginDao.select("FACEPATH", user.image)
    token = 0
    code = msg_code.ENTER_SUCCESS
    new_result = {}
    if status_code == status.HTTP_400_BAD_REQUEST or not result or \
       result[0]['password'] != user.password:
        new_result = None
        code = msg_code.PWD_WRONG
        return status_code, None, msg_code.PWD_WRONG
    else:
        result = result[0]
        new_result['token'] = token
        new_result['userid'] = result['userid']
        new_result['status'] = result['status']
    return status_code, new_result, code
