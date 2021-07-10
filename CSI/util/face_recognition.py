
# encoding:utf-8
# import requests

# client_id 为官网获取的AK， client_secret 为官网获取的SK
# host = 'https://aip.baidubce.com/oauth/2.0/token?grant_type=client_credentials&client_id=bBdtji1hAx5h0VONFP1AS942&client_secret=auANLlS4mnRFDVUrz56t72Z9XrlRzALb'
# response = requests.get(host)
# if response:
#     print(response.json())

# https://aip.baidubce.com/rest/2.0/face/v1/merge?access_token=24.f9ba9c5341b67688ab4added8bc91dec.2592000.1485570332.282335-8574074


# encoding:utf-8

import requests
import base64

'''
人脸对比
'''


request_url = "https://aip.baidubce.com/rest/2.0/face/v3/match"
access_token = '24.64eeb5e0b58c269905827436bf39d70e.2592000.1628345085.282335-24516115'
request_url = request_url + "?access_token=" + access_token
headers = {'content-type': 'application/json'}

img1_path = r"C:\Users\15067\Desktop\face1.png"
img2_path = r"C:\Users\15067\Desktop\face2.png"


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
    return response.json()


def hash(s):
    pwd = ""
    for i in s:
        pwd += chr(ord(i)+1)
    print(pwd)

hash("good")
