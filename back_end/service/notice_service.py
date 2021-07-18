from fastapi import status

from dao import notice_dao
from util import message


def get_notices():
    """获取所有公告信息"""
    status_code, result = notice_dao.getall()
    msg_code = message.SEARCH_SUCCESS
    if status_code == status.HTTP_400_BAD_REQUEST:
        msg_code = message.SEARCH_FAILURE
    else:
        for item in result:  # 将datetime类型数据转换成str类型
            item['createdate'] = str(item['createdate'])
            item['editdate'] = str(item['editdate'])
    return status_code, result, msg_code


def add_notice(notice):
    """增加公告"""
    status_code, result = notice_dao.select('TITLE', notice.title)  # 根据新增公告名称查询公告
    msg_code = message.ADD_SUCCESS
    if status_code == status.HTTP_400_BAD_REQUEST:
        msg_code = message.ADD_FAILURE
    elif result:  # 如果存在数据，说明存在同名公告，要返回消息重复的消息
        msg_code = message.DATA_REPEATED
    else:
        status_code = notice_dao.insert(notice)
        if status_code == status.HTTP_400_BAD_REQUEST:
            msg_code = message.ADD_FAILURE
    return status_code, msg_code


def del_notice(notice):
    """删除公告"""
    status_code = notice_dao.delete('NOTICEID', notice.noticeid)
    msg_code = message.DEL_SUCCESS
    if status_code == status.HTTP_400_BAD_REQUEST:
        msg_code = message.DEL_FAILURE
    return status_code, msg_code


def edit_notice(notice):
    """编辑公告"""
    status_code, result = notice_dao.select('TITLE', notice.title)  # 根据名称查询公告
    msg_code = message.UPD_SUCCESS
    if status_code == status.HTTP_400_BAD_REQUEST:
        msg_code = message.UPD_FAILURE
    elif result and result[0]['noticeid'] != notice.noticeid:  # 如果存在同名公告且id不与参数中的相同，说明数据重复
        msg_code = message.DATA_REPEATED
    else:
        edit_index = ['TITLE', 'CONTENT', 'USERID', 'USERNAME']  # 要修改的索引
        edit_value = [notice.title, notice.content, notice.userid,  # 修改后的值
                      notice.username]
        status_code = notice_dao.edit('NOTICEID', notice.noticeid,  # 修改公告
                                      edit_index, edit_value)
        if status_code == status.HTTP_400_BAD_REQUEST:
            msg_code = message.UPD_FAILURE
    return status_code, msg_code
