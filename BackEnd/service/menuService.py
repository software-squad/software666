from dao import menuDao
from util import msg_code


def findNews():
    result = menuDao.getAll()
    return result, msg_code.SEARCH_SUCCESS
