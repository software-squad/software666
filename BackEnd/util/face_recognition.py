from fastapi import UploadFile
import os
import requests
import base64

'''
人脸对比，图片传输
'''


request_url = "https://aip.baidubce.com/rest/2.0/face/v3/match"
access_token = '24.64eeb5e0b58c269905827436bf39d70e.'
access_token += '.2592000.1628345085.282335-24516115'
request_url = request_url + "?access_token=" + access_token
headers = {'content-type': 'application/json'}


def faceMatch(img1_path, img2_path):
    img1 = str(base64.b64encode(open(img1_path, 'rb').read()), 'utf-8')
    img2 = str(base64.b64encode(open(img2_path, 'rb').read()), 'utf-8')
    params = [{"image": img1, "image_type": "BASE64", "face_type": "LIVE",
               "quality_control": "NONE"},
              {"image": img2, "image_type": "BASE64", "face_type": "LIVE",
               "quality_control": "NONE"}]
    response = requests.post(request_url, json=params, headers=headers)
    if response:
        print(response.json())
    return response.json()['result']['score']


def createFacePath(faceByte, faceImage):
    with open("C:/tempFace/%s" % (faceImage.filename), 'wb') as f:
        f.write(faceByte)
    return "C:/tempFace/%s" % (faceImage.filename)


def uploadFile2ImageStr64(contentsByte, image: UploadFile, userid):
    with open("C:/faceImage/%d%s" % (userid, image.filename), 'wb') as f:
        f.write(contentsByte)
    # imageStr64 = str(base64.b64encode(open("./faceImage/%d%s" % (userid,
    #                  image.filename), 'rb').read()),'utf-8')
    return "C:/faceImage/%d%s" % (userid, image.filename)


def delFaceTemp(facePath):
    if os.path.exists(facePath):  # 如果文件存在
        # 删除文件，可使用以下两种方法。
        # os.unlink(path)
        os.remove(facePath)
    else:
        print('no such file: %s' % facePath)  # 如果文件不存在
