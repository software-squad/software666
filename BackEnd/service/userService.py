from fastapi import status
from dao import userDao
from util import msg_code


def changePassword(user):
    status_code, result = userDao.select("USERID", user.userid)[0]
    if status_code == status.HTTP_400_BAD_REQUEST or result['password'] != user.oldpwd:
        return status_code, msg_code.UPD_FAILURE
    else:
        userDao.edit('USERID', user.userid, 'PASSWORD', user.newpwd)
        return status_code, msg_code.UPD_SUCCESS


def faceRegister(user):
    status_code = userDao.edit('USERID', user.userid, 'FACEURL', user.image)
    code = msg_code.UPD_SUCCESS
    if status_code == msg_code.UPD_FAILURE:
        code = msg_code.UPD_FAILURE
    return status_code, code
