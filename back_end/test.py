"""JWT测试"""

import time
import jwt

# token的headers
headers = {
    'alg': 'HS256',  # 声明所使用的的算法
    'typ': 'JWT'  # 声明token的类型
}

# token的密钥
secret = 'zhananbudanchou1234678'

# token的加密算法
algorithm = 'HS256'


def jwt_encode(loginname, userid):
    """根据userid生成token"""
    # token的payload
    payload = {
        'iat': time.time(),  # 时间戳
        'exp': time.time()+24*60*60,  # 销毁时间，24小时后
        'loginname': loginname,  # payload中假如loginname
        'userid': userid  # payload中加入userid
    }
    token = jwt.encode(payload=payload,  # payload 有效载体
                       key=secret,  # 进行加密签名的密钥
                       algorithm=algorithm,  # 指明签名算法方式，默认也是HS256
                       headers=headers)
    return token


def jwt_decode(token, secret=secret, algorithm=algorithm):
    """JWT中token的解析认证，若token不正确，则返回None"""
    try:
        data = jwt.decode(token, secret, algorithms=[algorithm])
    except Exception:
        return None
    return data


if __name__ == '__main__':
    token = jwt_encode('哈哈', 5)
    token = jwt_decode(token)
    print(token['userid'])
