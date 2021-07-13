from fastapi import APIRouter

from util import response_code

from service import noticeService

from model import notice_inf

# 构建api路由
router = APIRouter()


@router.get("/showmany", tags=["notice"])
async def showNotices():
    # 展示所有公告
    status_code, jobs, msg_code = noticeService.showNotices()
    return response_code.response(status_code, msg_code, jobs)


@router.post("/edit", tags=["notice"])
async def editNotice(notice: notice_inf.NoticeInf):
    # 编辑公告
    status_code, msg_code = noticeService.editNotice(notice)
    return response_code.response(status_code, msg_code)


@router.get("/del", tags=["notice"])
async def delNotice(noticeid: int):
    # 删除公告
    status_code, msg_code = noticeService.delNotice(noticeid)
    return response_code.response(status_code, msg_code)


@router.post("/add", tags=["notice"])
async def addNotice(notice: notice_inf.NoticeInf):
    # 添加公告
    status_code, msg_code = noticeService.addNotice(notice)
    return response_code.response(status_code, msg_code)
