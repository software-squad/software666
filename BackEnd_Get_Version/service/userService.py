from fastapi import status, UploadFile
from dao import userDao
from util import msg_code, pwd_encode, face_recognition


def changePassword(user):
    # 更改密码
    status_code, result = userDao.select("USERID", user.userid)
    if status_code == status.HTTP_400_BAD_REQUEST or \
       result[0]['password'] != pwd_encode.MD5(user.oldpwd):
        return status_code, msg_code.UPD_FAILURE
    else:
        userDao.edit('USERID', user.userid, 'PASSWORD',
                     pwd_encode.MD5(user.newpwd))
        return status_code, msg_code.UPD_SUCCESS


def faceRegister(contentsByte, image: UploadFile, userid: int):
    # 将上传的人脸图片保存在本地
    imagePath = face_recognition.uploadFile2ImageStr64(contentsByte,
                                                       image,
                                                       userid)
    status_code = userDao.edit('userid', userid, 'facepath', imagePath)
    # with open("./faceImage/%d%s"%(userid,image.filename), 'wb') as f:
    #     f.write(contentsByte)
    code = msg_code.UPD_SUCCESS
    if status_code == msg_code.UPD_FAILURE:
        code = msg_code.UPD_FAILURE
    return status_code, code
