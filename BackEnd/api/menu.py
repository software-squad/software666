from fastapi import APIRouter

from util import response_code

from service import menuService

# 构建api路由
router = APIRouter()


@router.get("/showNews", tags=["menu"])
async def showNews():
    # 展示最新公告
    result, msg_code = menuService.findNews()
    return response_code.showResponse(result, msg_code)
