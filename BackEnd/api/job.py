from fastapi import APIRouter

from util import response_code

from service import jobService

from model import job_inf

from util import msg_code

# 构建api路由
router = APIRouter()


@router.get("/show", tags=["job"])
async def showJobs():
    # 展示大量职位
    "service应该返回是否查询成功和查询结果"
    data, result = jobService.showJobs()
    # result=0  查询成功；
    # result=1  查询失败
    # result=2  数据不存在
    if result == 0:
        return response_code.res_200(msg_code.SEARCH_SUCCESS, data)
    if result == 1:
        return response_code.res_400(msg_code.SEARCH_FAILURE, data)
    if result == 2:
        return response_code.res_200(msg_code.DATA_NOT_EXIT, data)


@router.get("/search", tags=["job"])
async def searchJob(jobname: str):
    # 查询职位
    # result=0  查询成功；
    # result=1  查询失败
    # result=2  数据不存在
    data, result = jobService.searchJob(jobname)
    if result == 0:
        return response_code.res_200(msg_code.SEARCH_SUCCESS, data)
    if result == 1:
        return response_code.res_400(msg_code.SEARCH_FAILURE, data)
    if result == 2:
        return response_code.res_200(msg_code.DATA_NOT_EXIT, data)


# @router.get("/one", tags=["job"])
# async def showOneJob(job: job_inf.JobInf):
#     # 展示一个职位
#     data,result = jobService.showOneJob(job)
#     if result:
#         return response_code.response('10007',data)
#     else:
#         return response_code.response('10008',data)


@router.post("/edit", tags=["job"])
async def editJob(job:job_inf.JobInf):
    # 编辑职位
    # result=0  更新成功
    # result=1  更新失败
    # result=2  数据重复
    result = jobService.editJob(job)
    if result == 0:
        return response_code.res_200(msg_code.UPD_SUCCESS)
    if result == 1:
        return response_code.res_400(msg_code.UPD_FAILURE)
    if result == 2:
        return response_code.res_200(msg_code.DATA_REPEATED)


@router.post("/del", tags=["job"])
async def delJob(job:job_inf.DelJobInf):
    # 删除职位
    # 0 成功
    # 1 失败
    result = jobService.delJob(job)
    if result == 0:
        return response_code.res_200(msg_code.DEL_SUCCESS)
    if result == 1:
        return response_code.res_400(msg_code.DEL_FAILURE)


@router.post("/add", tags=["job"])
async def addJob(job:job_inf.AddJobInf):
    # 增添职位
    # result=0  新增成功
    # result=1  新增失败
    # result=2  数据重复
    result = jobService.addJob(job)
    if result == 0:
        return response_code.res_200(msg_code.ADD_SUCCESS)
    if result == 1:
        return response_code.res_400(msg_code.ADD_FAILURE)
    if result == 2:
        return response_code.res_200(msg_code.DATA_REPEATED)
