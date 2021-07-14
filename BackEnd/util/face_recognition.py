from fastapi import UploadFile
import os
import requests
import base64


def faceMatch(img1_path, img2_path):
    """人脸对比"""
    # host中client_id 为官网获取的AK,client_secret 为官网获取的SK.
    host = 'https://aip.baidubce.com/oauth/2.0/token?grant_type='
    host += 'client_credentials&client_id=bBdtji1hAx5h0VONFP1AS942'
    host += '&client_secret=auANLlS4mnRFDVUrz56t72Z9XrlRzALb'
    access_token = requests.get(host).json()['access_token']
    request_url = "https://aip.baidubce.com/rest/2.0/face/v3/match"
    request_url = request_url + "?access_token=" + access_token
    headers = {'content-type': 'application/json'}

    img1 = str(base64.b64encode(open(img1_path, 'rb').read()), 'utf-8')
    img2 = str(base64.b64encode(open(img2_path, 'rb').read()), 'utf-8')
    params = [{"image": img1, "image_type": "BASE64", "face_type": "LIVE",
               "quality_control": "NONE"},
              {"image": img2, "image_type": "BASE64", "face_type": "LIVE",
               "quality_control": "NONE"}]
    # 调用百度云API，参数已在以上代码获取，返回人脸对比信息。
    response = requests.post(request_url, json=params, headers=headers)
    if response:
        print(response.json())
    return response.json()['result']['score']  # 返回人脸对比分数。


def storeFaceTempFile(contentsByte, file):
    """刷脸登录时，暂存存储人脸图片"""
    with open("C:/tempFace/%s" % (file.filename), 'wb') as f:
        f.write(contentsByte)
    return "C:/tempFace/%s" % (file.filename)


def storeFaceFile(contentsByte, image: UploadFile, userid):
    """以userid+filname的命名方式存储图片"""
    with open("C:/faceImage/%d%s" % (userid, image.filename), 'wb') as f:
        f.write(contentsByte)
    return "C:/faceImage/%d%s" % (userid, image.filename)


def delFile(path):
    """删除文件，如人脸暂存的图片"""
    if os.path.exists(path):  # 如果文件存在
        # 删除文件，可使用以下两种方法。
        # os.unlink(path)
        os.remove(path)
    else:
        print('no such file: %s' % path)  # 如果文件不存在
