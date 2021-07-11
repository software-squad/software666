from fastapi import status
from dao import documentDao
from util import msg_code


def showFilesService():
    # 展示所有文件
    status_code, result = documentDao.getAll()
    code = msg_code.SEARCH_SUCCESS
    if status_code == status.HTTP_400_BAD_REQUEST:
        code = msg_code.SEARCH_FAILURE
    return status_code, result, code


def editFileService(file):
    # 修改文件
    status_code = []
    status_code.append(documentDao.edit('FILEID', file.fileid,
                                        'TITLE', file.title))
    status_code.append(documentDao.edit('FILEID', file.fileid,
                                        'FILENAME', file.filename))
    status_code.append(documentDao.edit('FILEID', file.fileid,
                                        'REMARK', file.remark))
    status_code.append(documentDao.edit('FILEID', file.fileid,
                                        'CREATEDATE', file.createdate))
    status_code.append(documentDao.edit('FILEID', file.fileid,
                                        'USERNAME', file.username))
    status_code.append(documentDao.edit('FILEID', file.fileid,
                                        'FILEPATH', file.filepath))
    if status.HTTP_400_BAD_REQUEST in status_code:
        status_code = status.HTTP_400_BAD_REQUEST
        code = msg_code.UPD_FAILURE
    else:
        status_code = status.HTTP_200_OK
        code = msg_code.UPD_SUCCESS
    return status_code, code


def delFileService(file):
    # 删除文件
    status_code = documentDao.delete('FILEID', file.fileid)
    code = msg_code.DEL_SUCCESS
    if status_code == status.HTTP_400_BAD_REQUEST:
        code = msg_code.DEL_FAILURE
    return status_code, code


# def uploadFile(file):
#     result = True
#     return result


# def downloadFile():
#     result = True
#     return result
