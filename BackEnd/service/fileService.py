from fastapi import status
from dao import fileDao
from util import msg_code, face_recognition


def showFiles():
    """展示所有文件"""
    status_code, result = fileDao.getAll()
    code = msg_code.SEARCH_SUCCESS
    if status_code == status.HTTP_400_BAD_REQUEST:
        code = msg_code.SEARCH_FAILURE
    else:
        for item in result:
            item['createdate'] = str(item['createdate'])
    return status_code, result, code


def editFile(file):
    """修改文件"""
    edit_index = ['TITLE', 'REMARK', 'USERID', 'USERNAME']
    edit_value = [file.title, file.remark, file.userid, file.username]
    status_code = fileDao.edit('FILEID', file.fileid, edit_index,
                               edit_value)
    if status_code == status.HTTP_400_BAD_REQUEST:
        code = msg_code.UPD_FAILURE
    return status_code, code


def delFile(fileid):
    """删除文件"""
    status_code, result = fileDao.select('FILEID', fileid)
    code = msg_code.DEL_SUCCESS
    if status_code == status.HTTP_400_BAD_REQUEST:
        code = msg_code.DEL_FAILURE
    elif not result:
        code = msg_code.DATA_NOT_EXIT
    else:
        status_code = fileDao.delete('FILEID', fileid)
        if status_code == status.HTTP_400_BAD_REQUEST:
            code = msg_code.DEL_FAILURE
        else:
            face_recognition.delFile(result[0]['filepath']
                                     + result[0]['filename'])
    return status_code, code


def uploadFile(fileMsg, file):
    """上传文件"""
    status_code = fileDao.insert(fileMsg, file)
    code = msg_code.ADD_SUCCESS
    if status_code == status.HTTP_400_BAD_REQUEST:
        code = msg_code.ADD_FAILURE
    return status_code, code


def downloadFile(fileid):
    """下载文件"""
    status_code, result = fileDao.select('FILEID', fileid)
    code = msg_code.SEARCH_SUCCESS
    if status_code == status.HTTP_400_BAD_REQUEST:
        code = msg_code.SEARCH_FAILURE
    elif not result:
        code = msg_code.DATA_NOT_EXIT
    else:
        result = result[0]['filepath'] + result[0]['filename']
    return status_code, result, code
