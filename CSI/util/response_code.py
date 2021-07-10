from fastapi import status
from fastapi.responses import JSONResponse, Response  # , ORJSONResponse
from typing import Union


def loginResponse(token, userid, userstatus, msg_code):
    return JSONResponse(
        content={
            'code': status.HTTP_200_OK,
            'msg': msg_code,
            'data': {
                'token': token,
                'userid': userid,
                'userstatus': userstatus
            }
        }
    )


def showResponse(items, msg_code):
    return JSONResponse(
        content={
            'code': status.HTTP_200_OK,
            'msg': msg_code,
            'data': items
        }
    )

def showResponseFail(items, msg_code):
    return JSONResponse(
        content={
            'code': status.HTTP_400_BAD_REQUEST,
            'msg': msg_code,
            'data': items
        }
    )


def updateResponse(msg_code):
    return JSONResponse(
        content={
            'code': status.HTTP_200_OK,
            'msg': msg_code,
            'data': None
        }
    )
