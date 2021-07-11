from fastapi.responses import JSONResponse
from starlette.status import HTTP_200_OK,HTTP_400_BAD_REQUEST

def response(status_code, msg_code, items=None):
    return JSONResponse(
        status_code=status_code,
        content={
            'code': status_code,
            'msg': msg_code,
            'data': items
        }
    )

#这里把data=None放前面要报错，所以把它放后面了
def res_200(msg:str,data:object = None) -> Response:
    return JSONResponse(
        status_code=status.HTTP_200_OK,
        content={
            'code': 200,
            'message': msg,
            'data': data,
        }
    )
    
def res_400(msg:str,data:object = None) -> Response:
    return JSONResponse(
        status_code=status.HTTP_400_BAD_REQUEST,
        content={
            'code': 400,
            'message': msg,
            'data': data,
        }
    )
