from fastapi import APIRouter

from util import response_code

from service import jobService

from model import job_inf

# 构建api路由
router = APIRouter()


@router.post("/show", tags=["job"])
async def showJobs(job: job_inf.job_inf):
    # 展示大量职位
    result = jobService.showJobs(job)
    return response_code.response(result)


@router.post("/search", tags=["job"])
async def searchJob(job: job_inf.job_inf):
    # 查询职位
    result = jobService.searchJob(job)
    return response_code.response(result)


@router.post("/one", tags=["job"])
async def showOneJob(job: job_inf.job_inf):
    # 展示一个职位
    result = jobService.showOneJob(job)
    return response_code.response(result)


@router.post("/edit", tags=["job"])
async def editJob(job: job_inf.job_inf):
    # 编辑职位
    result = jobService.editJob(job)
    return response_code.response(result)


@router.post("/del", tags=["job"])
async def delJob(job: job_inf.job_inf):
    # 删除职位
    result = jobService.delJob(job)
    return response_code.response(result)


@router.post("/add", tags=["job"])
async def addJob(job: job_inf.job_inf):
    # 增添职位
    result = jobService.addJob(job)
    return response_code.response(result)
