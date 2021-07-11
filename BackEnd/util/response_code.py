from fastapi.responses import JSONResponse, Response
from fastapi import status


def response(status_code, msg_code, items=None):
    return JSONResponse(
        status_code=status_code,
        content={
            'code': status_code,
            'msg': msg_code,
            'data': items
        }
    )


def res_200(msg: str, data: object = None) -> Response:
    return JSONResponse(
        status_code=status.HTTP_200_OK,
        content={
            'code': status.HTTP_200_OK,
            'message': msg,
            'data': data,
        }
    )


def res_400(msg: str, data: object = None) -> Response:
    return JSONResponse(
        status_code=status.HTTP_400_BAD_REQUEST,
        content={
            'code': status.HTTP_400_BAD_REQUEST,
            'message': msg,
            'data': data,
        }
    )
