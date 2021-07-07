from fastapi import status
from fastapi.responses import JSONResponse, Response  # , ORJSONResponse
from typing import Union

# 注意有个 * 号 不是笔误， 意思是调用的时候要指定参数 e.g.resp_200（data=xxxx)
def res_200(data:object = None,msg:str="Succeed") -> Response:
    return result(200,msg,data)
    
def res_400(data:object = None, msg: str="Error") -> Response:
    return result(400,msg,data)

def result(code:int, msg: str = None, data:object = None) -> Response:
    return JSONResponse(
        status_code=status.HTTP_400_BAD_REQUEST,
        content={
            'code': code,
            'message': msg,
            'data': data,
        }
    )
