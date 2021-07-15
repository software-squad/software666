import os

from fastapi import status

from dao import file_dao
from util import message


def get_files():
    """获取所有文件信息"""
    status_code, result = file_dao.getall()  # 从数据库获取所有文件信息
    msg_code = message.SEARCH_SUCCESS
    if status_code == status.HTTP_400_BAD_REQUEST:
        msg_code = message.SEARCH_FAILURE
    else:
        for item in result:  # 将文件信息中createdate转换为str类型
            item['createdate'] = str(item['createdate'])
    return status_code, result, msg_code


def upload_file(filemsg, file):
    """上传文件"""
    filemsg['filename'] = file.filename  # 完善filemsg的信息
    filemsg['filepath'] = 'C:/file/'  # 完善filemsg的信息
    status_code = file_dao.insert(filemsg)  # 修改数据库
    msg_code = message.ADD_SUCCESS
    if status_code == status.HTTP_400_BAD_REQUEST:
        msg_code = message.ADD_FAILURE
    return status_code, msg_code


def download_file(fileid):
    """下载文件"""
    status_code, result = file_dao.select('FILEID', fileid)  # 获取要下载的文件信息
    msg_code = message.SEARCH_SUCCESS
    if status_code == status.HTTP_400_BAD_REQUEST:
        msg_code = message.SEARCH_FAILURE
    elif not result:  # 如果没获取到，则返回数据不存在的消息
        msg_code = message.DATA_NOT_EXIT
    else:
        result = result[0]['filepath'] + result[0]['filename']  # 文件路径
    return status_code, result, msg_code


def del_file(fileid):
    """删除文件"""
    status_code, result = file_dao.select('FILEID', fileid)  # 根据fileid选择要改的文件
    msg_code = message.DEL_SUCCESS
    if status_code == status.HTTP_400_BAD_REQUEST:
        msg_code = message.DEL_FAILURE
    elif not result:  # 如果result为空，说明数据不存在（尽管这种情况较少见）
        msg_code = message.DATA_NOT_EXIT
    else:
        status_code = file_dao.delete('FILEID', fileid)  # 调用dao层函数修改数据库
        if status_code == status.HTTP_400_BAD_REQUEST:
            msg_code = message.DEL_FAILURE
        else:
            filepath = result[0]['filepath'] + result[0]['filename']  # 文件路径
            if os.path.exists(filepath):
                os.remove(filepath)  # 删除文件
    return status_code, msg_code


def edit_file(file):
    """修改文件"""
    edit_index = ['TITLE', 'REMARK', 'USERID', 'USERNAME']  # 要修改的索引
    edit_value = [file.title, file.remark, file.userid, file.username]  # 修改后的值
    status_code = file_dao.edit('FILEID', file.fileid, edit_index,
                                edit_value)  # 调用dao层函数修改数据库
    msg_code = message.UPD_SUCCESS
    if status_code == status.HTTP_400_BAD_REQUEST:
        msg_code = message.UPD_FAILURE
    return status_code, msg_code
