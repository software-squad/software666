import jwt


def jwtEncode(token, secret='zhananbudanchou1234678', algorithm='HS256'):
    # token解析认证
    try:
        data = jwt.decode(token, secret, algorithms=[algorithm])
    except Exception:
        return None
    return data
