import jwt


def jwtEncode(token, secret, algorithm):
    # token解析认证
    try:
        data = jwt.decode(token, secret, algorithms=[algorithm])
    except Exception as e:
        return e
    return data
