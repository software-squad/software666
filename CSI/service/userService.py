from dao import userDao
from util import msg_code


def changePassword(user):
    result = userDao.select("USERID", user.userid)
    if result['password'] != user.oldpwd:
        return msg_code.UPD_FAILURE
    else:
        userDao.edit('USERID', user.userid, 'PASSWORD', user.newpwd)
        return msg_code.UPD_SUCCESS


def faceRegister(user):
    userDao.edit('USERID', user.userid, 'FACEURL', user.image)
    return msg_code.UPD_SUCCESS
