from dao import loginDao
from util import msg_code


def validateUserByAccount(user):
    result = loginDao.select("LOGINNAME", user.loginname)
    print(result)
    if not result or result['password'] != user.password:
        return None, None, None, msg_code.PWD_WRONG
    else:
        return None, result['userid'], result['userstatus'], msg_code.ENTER_SUCCESS        


def validateUserByFace(user):
    result = loginDao.select("FACEPATH", user.image)
    if result is None or result['password'] != user.password:
        return None, None, None, msg_code.PWD_WRONG
    else:
        return None, result['userid'], result['userstatus'], msg_code.ENTER_SUCCESS 
