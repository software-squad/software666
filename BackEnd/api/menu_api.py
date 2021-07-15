from fastapi import APIRouter

from util.response import response
from service import menu_service

# 构建api路由
router = APIRouter()


@router.get("/showNews", tags=["menu"])
async def show_news():
    """展示最新公告"""
    status_code, result, msg_code = menu_service.get_news()
    return response(status_code, msg_code, result)
