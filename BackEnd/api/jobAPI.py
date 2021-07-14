from fastapi import APIRouter

from util import response_code

from service import jobService

from model import job_inf

# 构建api路由
router = APIRouter()


@router.get("/show", tags=["job"])
async def showJobs():
    """展示大量职位"""
    status_code, result, msg_code = jobService.showJobs()
    return response_code.response(status_code, msg_code, result)


@router.get("/search", tags=["job"])
async def searchJob(jobname: str):
    """查询职位"""
    status_code, result, msg_code = jobService.searchJob(jobname)
    return response_code.response(status_code, msg_code, result)


@router.post("/edit", tags=["job"])
async def editJob(job: job_inf.JobInf):
    """编辑职位"""
    status_code, msg_code = jobService.editJob(job)
    return response_code.response(status_code, msg_code)


@router.post("/del", tags=["job"])
async def delJob(job: job_inf.DelJobInf):
    """删除职位"""
    status_code, msg_code = jobService.delJob(job)
    return response_code.response(status_code, msg_code)


@router.post("/add", tags=["job"])
async def addJob(job: job_inf.JobInf):
    """增添职位"""
    status_code, msg_code = jobService.addJob(job)
    return response_code.response(status_code, msg_code)
