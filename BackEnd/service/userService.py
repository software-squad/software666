from fastapi import status
from dao import userDao
from util import msg_code, pwd_encode


def changePassword(user):
    # 更改密码
    status_code, result = userDao.select("USERID", user.userid)
    if status_code == status.HTTP_400_BAD_REQUEST or \
       result[0]['password'] != pwd_encode.MD5(user.oldpwd):
        return status_code, msg_code.UPD_FAILURE
    else:
        userDao.edit('USERID', user.userid, 'PASSWORD',
                     pwd_encode.MD5(user.newpwd))
        return status_code, msg_code.UPD_SUCCESS


def faceRegister(user):
    # 刷脸登记
    status_code = userDao.edit('USERID', user.userid, 'FACEURL', user.image)
    code = msg_code.UPD_SUCCESS
    if status_code == msg_code.UPD_FAILURE:
        code = msg_code.UPD_FAILURE
    return status_code, code
