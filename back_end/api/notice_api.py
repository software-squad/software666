from fastapi import APIRouter

from util.response import response
from service import notice_service
from model import notice_inf

# 构建api路由
router = APIRouter()


@router.get("/showNotices", tags=["notice"])
async def show_notices():
    """展示公告"""
    status_code, jobs, msg_code = notice_service.get_notices()
    return response(status_code, msg_code, jobs)


@router.post("/add", tags=["notice"])
async def add_notice(notice: notice_inf.NoticeInf):
    """添加公告"""
    status_code, msg_code = notice_service.add_notice(notice)
    return response(status_code, msg_code)


@router.post("/del", tags=["notice"])
async def del_notice(notice: notice_inf.DelNoticeInf):
    """删除公告"""
    status_code, msg_code = notice_service.del_notice(notice)
    return response(status_code, msg_code)


@router.post("/edit", tags=["notice"])
async def edit_notice(notice: notice_inf.NoticeInf):
    """编辑公告"""
    status_code, msg_code = notice_service.edit_notice(notice)
    return response(status_code, msg_code)
