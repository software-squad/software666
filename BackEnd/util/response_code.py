from fastapi.responses import JSONResponse


def response(status_code, msg_code, items=None):
    return JSONResponse(
        status_code=status_code,
        content={
            'code': status_code,
            'msg': msg_code,
            'data': items
        }
    )
