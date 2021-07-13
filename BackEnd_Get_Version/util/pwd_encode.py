import hashlib


def MD5(password, salt='154465441354651'):
    # MD5加密
    md = hashlib.md5(salt.encode('utf-8'))
    md.update(password.encode('utf-8'))
    return md.hexdigest()
