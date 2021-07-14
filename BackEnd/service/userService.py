from fastapi import status, UploadFile
from dao import userDao
from util import msg_code, pwd_encode, face_recognition


def changePassword(user):
    """更改密码"""
    status_code, result = userDao.select("USERID", user.userid)
    code = msg_code.UPD_SUCCESS
    # 检查该userid下，旧密码是否输入正确
    if status_code == status.HTTP_400_BAD_REQUEST or \
       result[0]['password'] != pwd_encode.MD5(user.oldpwd):
        return status_code, msg_code.UPD_FAILURE
    else:
        # 旧密码正确的分支，修改密码
        status_code = userDao.edit('USERID', user.userid, ['PASSWORD'],
                                   [pwd_encode.MD5(user.newpwd)])
        if status_code == status.HTTP_400_BAD_REQUEST:
            code = msg_code.UPD_FAILURE
    return status_code, code


def faceRegister(contentsByte, image: UploadFile, userid: int):
    """将上传的人脸图片保存在本地"""
    imagePath = face_recognition.storeFaceFile(contentsByte,
                                               image,
                                               userid)
    # 修改文件
    status_code = userDao.edit('userid', userid, ['facepath'], [imagePath])
    code = msg_code.UPD_SUCCESS
    if status_code == msg_code.UPD_FAILURE:
        code = msg_code.UPD_FAILURE
    return status_code, code
