from fastapi import status

from dao import notice_dao
from util import message


def get_news():
    """获取最新两个公告"""
    status_code, result = notice_dao.getnews()
    for item in result:  # 只保留前端所需信息，并把datetime数据类型转换成str
        item['createdate'] = str(item['createdate'])
        item['editdate'] = str(item['editdate'])
    msg_code = message.SEARCH_SUCCESS
    if status_code == status.HTTP_400_BAD_REQUEST:
        msg_code = message.SEARCH_FAILURE
    return status_code, result, msg_code
