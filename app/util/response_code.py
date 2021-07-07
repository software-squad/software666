from fastapi import status
from fastapi.responses import JSONResponse, Response  # , ORJSONResponse
from typing import Union

from starlette.status import HTTP_200_OK

def res_200(data:object = None,msg:str="Succeed") -> Response:
    return JSONResponse(
        status_code=status.HTTP_200_OK,
        content={
            'code': 200,
            'message': msg,
            'data': data,
        }
    )
    
def res_400(data:object = None, msg: str="BAD REQUEST") -> Response:
    return JSONResponse(
        status_code=status.HTTP_400_OK,
        content={
            'code': 400,
            'message': msg,
            'data': data,
        }
    )