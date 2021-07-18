from fastapi import APIRouter

from util.response import response
from service import job_service
from model import job_inf

# 构建api路由
router = APIRouter()


@router.get("/showJobs", tags=["job"])
async def show_jobs():
    """展示职位"""
    status_code, result, msg_code = job_service.get_jobs()
    return response(status_code, msg_code, result)


@router.get("/search", tags=["job"])
async def search_job(jobname: str):
    """查询职位"""
    status_code, result, msg_code = job_service.search_job(jobname)
    return response(status_code, msg_code, result)


@router.post("/add", tags=["job"])
async def add_job(job: job_inf.JobInf):
    """增添职位"""
    status_code, msg_code = job_service.add_job(job)
    return response(status_code, msg_code)


@router.post("/del", tags=["job"])
async def del_job(job: job_inf.DelJobInf):
    """删除职位"""
    status_code, msg_code = job_service.del_job(job)
    return response(status_code, msg_code)


@router.post("/edit", tags=["job"])
async def edit_job(job: job_inf.JobInf):
    """编辑职位"""
    status_code, msg_code = job_service.edit_job(job)
    return response(status_code, msg_code)
