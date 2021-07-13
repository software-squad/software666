from fastapi import status
from dao import loginDao
from util import msg_code, pwd_encode, face_recognition
import time
import jwt

headers = {
    'alg': 'HS256',  # 声明所使用的的算法
    'typ': 'JWT'  # 声明token的类型
}

secret = 'zhananbudanchou1234678'


def validateUserByAccount(user):
    # 通过用户名和密码登录
    status_code, result = loginDao.select('LOGINNAME', user.loginname)
    code = msg_code.ENTER_SUCCESS
    new_result = {}
    if status_code == status.HTTP_400_BAD_REQUEST or not result or \
       pwd_encode.MD5(user.password) != result[0]['password']:
        new_result = None
        code = msg_code.PWD_WRONG
        return status_code, None, msg_code.PWD_WRONG
    else:
        result = result[0]
        token_dict = {
            'iat': time.time(),  # 时间戳
            'name': result['loginname']  # loginname
        }
        token = jwt.encode(token_dict,  # payload 有效载体
                           secret,  # 进行加密签名的密钥
                           algorithm='HS256',  # 指明签名算法方式，默认也是HS256
                           headers=headers)
        new_result['token'] = token
        new_result['userid'] = result['userid']
        new_result['status'] = result['status']
    return status_code, new_result, code


def validateUserByFace(faceByte, faceImage, loginname):
    # 通过刷脸登录
    status_code, result = loginDao.select("loginname", loginname)  # 根据登录名获取对应的用户信息
    token = 0
    code = msg_code.ENTER_SUCCESS
    new_result = {}
    if status_code == status.HTTP_400_BAD_REQUEST or not result:
        new_result = None
        code = msg_code.PWD_WRONG
        return status_code, None, msg_code.PWD_WRONG
    else:
        userFacePath = result[0]['facepath']
        loginFacePath = face_recognition.createFacePath(faceByte, faceImage)  # 获取刷脸登录时上传的照片
        compResult = face_recognition.faceMatch(userFacePath, loginFacePath)  # 获取刷脸照片和数据库保存照片的比对结果
        face_recognition.delFaceTemp(loginFacePath)  # 清除刚才保存的文件
        if compResult < 80:  # 若比对结果分数小于80，则登录失败
            new_result = None
            code = msg_code.PWD_WRONG
            return status_code, None, msg_code.PWD_WRONG
        else:
            result = result[0]
            token_dict = {
                'iat': time.time(),  # 时间戳
                'name': result['loginname']  # loginname
            }
            token = jwt.encode(token_dict,  # payload 有效载体
                               secret,  # 进行加密签名的密钥
                               algorithm="HS256",  # 指明签名算法方式，默认也是HS256
                               headers=headers)
            new_result['token'] = token
            new_result['userid'] = result['userid']
            new_result['status'] = result['status']
    return status_code, new_result, code
