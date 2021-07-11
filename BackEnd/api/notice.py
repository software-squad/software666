from fastapi import APIRouter

from util import response_code

from service import noticeService

from model import notice_inf

from util import msg_code
# 构建api路由
router = APIRouter()


@router.get("/showmany", tags=["notice"])
async def showNotices():
    # 展示所有公告
    data, result = noticeService.showNotices()
    if result == 0:
        return response_code.res_200(msg_code.SEARCH_SUCCESS, data)
    if result == 1:
        return response_code.res_400(msg_code.SEARCH_FAILURE, data)
    if result == 2:
        return response_code.res_200(msg_code.DATA_NOT_EXIT, data)


# @router.post("/showone", tags=["notice"])
# async def showOneNotice(notice: notice_inf.notice_inf):
#     # 展示单个公告
#     result = noticeService.showOneNotice(notice)
#     return response_code.response(result)


@router.post("/edit", tags=["notice"])
async def editNotice(notice: notice_inf.NoticeInf):
    # 编辑公告
    result = noticeService.editNotice(notice)
    if result == 0:
        return response_code.res_200(msg_code.UPD_SUCCESS)
    if result == 1:
        return response_code.res_400(msg_code.UPD_FAILURE)
    if result == 2:
        return response_code.res_200(msg_code.DATA_REPEATED)


@router.get("/del", tags=["notice"])
async def delNotice(noticeid: int):
    # 删除公告
    result = noticeService.delNotice(noticeid)
    if result == 0:
        return response_code.res_200(msg_code.DEL_SUCCESS)
    if result == 1:
        return response_code.res_400(msg_code.DEL_FAILURE)


@router.post("/add", tags=["notice"])
async def addNotice(notice: notice_inf.AddNoticeInf):
    # 添加公告
    # result=0  新增成功
    # result=1  新增失败
    # result=2  数据重复
    result = noticeService.addNotice(notice)
    if result == 0:
        return response_code.res_200(msg_code.ADD_SUCCESS)
    if result == 1:
        return response_code.res_400(msg_code.ADD_FAILURE)
    if result == 2:
        return response_code.res_200(msg_code.DATA_REPEATED)
