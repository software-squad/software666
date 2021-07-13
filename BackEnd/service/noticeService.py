from fastapi import status
from dao import noticeDao
from util import msg_code


def showNotices():
    # 展示公告
    status_code, result = noticeDao.getAll()
    code = msg_code.SEARCH_SUCCESS
    if status_code == status.HTTP_400_BAD_REQUEST:
        code = msg_code.SEARCH_FAILURE
    else:
        for item in result:
            item['createdate'] = str(item['createdate'])
            item['editdate'] = str(item['editdate'])
    return status_code, result, code


def editNotice(notice):
    # 编辑公告
    status_code, result = noticeDao.select('TITLE', notice.title)
    if status_code == status.HTTP_400_BAD_REQUEST:
        code = msg_code.UPD_FAILURE
    elif result and result[0]['noticeid'] != notice.noticeid:
        code = msg_code.DATA_REPEATED
    else:
        status_code = []
        status_code.append(noticeDao.edit('NOTICEID', notice.noticeid,
                                          'TITLE', notice.title))
        status_code.append(noticeDao.edit('NOTICEID', notice.noticeid,
                                          'CONTENT', notice.content))
        status_code.append(noticeDao.edit('NOTICEID', notice.noticeid,
                                          'USERID', notice.userid))
        status_code.append(noticeDao.edit('NOTICEID', notice.noticeid,
                                          'USERNAME', notice.username))
        if status.HTTP_400_BAD_REQUEST in status_code:
            status_code = status.HTTP_400_BAD_REQUEST
            code = msg_code.UPD_FAILURE
        else:
            status_code = status.HTTP_200_OK
            code = msg_code.UPD_SUCCESS
    return status_code, code


def delNotice(notice):
    # 删除公告
    status_code = noticeDao.delete('NOTICEID', notice.noticeid)
    code = msg_code.DEL_SUCCESS
    if status_code == status.HTTP_400_BAD_REQUEST:
        code = msg_code.DEL_FAILURE
    return status_code, code


def addNotice(notice):
    # 增加公告
    status_code, result = noticeDao.select('TITLE', notice.title)
    code = msg_code.ADD_SUCCESS
    if status_code == status.HTTP_400_BAD_REQUEST:
        code = msg_code.ADD_FAILURE
    elif result:
        code = msg_code.DATA_REPEATED
    else:
        status_code = noticeDao.insert(notice)
        if status_code == status.HTTP_400_BAD_REQUEST:
            code = msg_code.ADD_FAILURE
    return status_code, code
