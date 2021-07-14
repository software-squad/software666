from fastapi import status
from dao import documentDao
from util import msg_code


def showFiles():
    # 展示所有文件
    status_code, result = documentDao.getAll()
    code = msg_code.SEARCH_SUCCESS
    if status_code == status.HTTP_400_BAD_REQUEST:
        code = msg_code.SEARCH_FAILURE
    else:
        for item in result:
            item['createdate'] = str(item['createdate'])
    return status_code, result, code


def editFile(file):
    # 修改文件
    edit_index = ['TITLE', 'FILENAME', 'REMARK', 'USERNAME', 'FILEPATH']
    edit_value = [file.title, file.filename, file.remark, file.username,
                  file.filepath]
    status_code = documentDao.edit('FILEID', file.fileid, edit_index,
                                   edit_value)
    if status_code == status.HTTP_400_BAD_REQUEST:
        code = msg_code.UPD_FAILURE
    return status_code, code


def delFile(fileid):
    # 删除文件
    status_code = documentDao.delete('FILEID', fileid)
    code = msg_code.DEL_SUCCESS
    if status_code == status.HTTP_400_BAD_REQUEST:
        code = msg_code.DEL_FAILURE
    return status_code, code


def uploadFile(fileMsg, file):
    # 上传文件
    status_code = documentDao.insert(fileMsg, file)
    code = msg_code.ADD_SUCCESS
    if status_code == status.HTTP_400_BAD_REQUEST:
        code = msg_code.ADD_FAILURE
    return status_code, code


def downloadFile(fileid):
    # 下载文件
    status_code, result = documentDao.select('FILEID', fileid)
    code = msg_code.SEARCH_SUCCESS
    if status_code == status.HTTP_400_BAD_REQUEST:
        code = msg_code.SEARCH_FAILURE
    else:
        result = result[0]
    return status_code, result['filepath'] + result['filename'], code
