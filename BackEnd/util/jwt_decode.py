import jwt


def jwtEncode(token, secret='zhananbudanchou1234678', algorithm='HS256'):
    """JWT中token的解析认真，若token不正确，则返回None。"""
    try:
        data = jwt.decode(token, secret, algorithms=[algorithm])
    except Exception:
        return None
    return data
