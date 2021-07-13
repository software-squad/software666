from fastapi import status
from dao import menuDao
from util import msg_code


def findNews():
    # 查询最新两个公告
    status_code, result = menuDao.getNews()
    for item in result:
        del item['userid']
        item['createdate'] = str(item['createdate'])
        item['editdate'] = str(item['editdate'])
    code = msg_code.SEARCH_SUCCESS
    if status_code == status.HTTP_400_BAD_REQUEST:
        code = msg_code.SEARCH_FAILURE
    return status_code, result, code
