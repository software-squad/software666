from fastapi import APIRouter
from fastapi import status
from fastapi.responses import JSONResponse, Response 

from util  import  response_code

from fastapi.responses import JSONResponse, Response 

# 构建api路由
router = APIRouter()

from service import userService

# @router.post("/user",tags=['user'])
# async def read_users(item_id:int):
#     #调用 用户是否存在的用户服务
#     # print("hello")
#     print(type(item_id))
#     if not item_id:
#         return response_code.res_400()
#     res = userService.validataUser(item_id)
#     if res:
#         return response_code.res_200(res)
#     else:
#         return response_code.res_400(res)

@router.get("/user",tags=['user'])
async def read_users(item_id:int):
    #调用 用户是否存在的用户服务
    # print("hello")
    print(type(item_id))
    if not item_id:
        return response_code.res_400()
    res = userService.validataUser(item_id)
    # XXX res
    print(res)
    if res:
        return response_code.res_200(res)
    else:
        return response_code.res_400(res)