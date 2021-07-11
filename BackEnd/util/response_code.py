from fastapi.responses import JSONResponse, Response # , ORJSONResponse
from starlette.status import HTTP_200_OK,HTTP_400_BAD_REQUEST
from fastapi import status
from typing import Union

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

# 高明
def showResponse(items, msg_code):
    return JSONResponse(
        content={
            'code': status.HTTP_200_OK,
            'msg': msg_code,
            'data': items
        }
    )

# 高明
def showResponseFail(items, msg_code):
    return JSONResponse(
        content={
            'code': status.HTTP_400_BAD_REQUEST,
            'msg': msg_code,
            'data': items
        }
    )
