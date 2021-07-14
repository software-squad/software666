import hashlib


def MD5(password, salt='154465441354651'):
    """MD5+盐加密，默认盐为154465441354651"""
    md = hashlib.md5(salt.encode('utf-8'))
    md.update(password.encode('utf-8'))
    return md.hexdigest()
