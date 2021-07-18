from fastapi.responses import JSONResponse


def response(status_code, message, items=None):
    """返回给前端的response，以JSON的格式，
    包含status_code和请求处理后需要返回的具体内容。
    """
    return JSONResponse(
        status_code=status_code,
        content={
            'code': status_code,
            'msg': message,
            'data': items
        }
    )
