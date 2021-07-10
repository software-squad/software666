from fastapi import APIRouter

from util import response_code

from service import noticeService

from model import notice_inf

# 构建api路由
router = APIRouter()


@router.post("/showmany", tags=["notice"])
async def showNotices(notice: notice_inf.notice_inf):
    # 展示所有公告
    result = noticeService.showNotices(notice)
    return response_code.response(result)


@router.post("/showone", tags=["notice"])
async def showOneNotice(notice: notice_inf.notice_inf):
    # 展示单个公告
    result = noticeService.showOneNotice(notice)
    return response_code.response(result)


@router.post("/edit", tags=["notice"])
async def editNotice(notice: notice_inf.notice_inf):
    # 编辑公告
    result = noticeService.editNotice(notice)
    return response_code.response(result)


@router.post("/del", tags=["notice"])
async def delNotice(notice: notice_inf.notice_inf):
    # 删除公告
    result = noticeService.delNotice(notice)
    return response_code.response(result)


@router.post("/add", tags=["notice"])
async def addNotice(notice: notice_inf.notice_inf):
    # 添加公告
    result = noticeService.addNotice(notice)
    return response_code.response(result)
