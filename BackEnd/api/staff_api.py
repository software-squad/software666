from fastapi import APIRouter

from util.response import response
from service import staff_service
from model import staff_inf

# 构建api路由
router = APIRouter()


@router.get("/index", tags=["staff"])
async def index():
    """职位和所属部门以树状层次结构陈列，职位之下则对应员工"""
    status_code, staff, msg_code = staff_service.get_index()
    return response(status_code, msg_code, staff)


@router.post("/searchByDeptAndJob", tags=["staff"])
async def search_by_dept_and_job(staff: staff_inf.StaffDeptAndJob):
    """通过部门和工作查找员工"""
    status_code, staff, msg_code = staff_service.search_by_dept_and_job(staff)
    return response(status_code, msg_code, staff)


@router.get("/searchByUsername", tags=["staff"])
async def search_by_username(username: str):
    """通过名字查找员工"""
    status_code, staff, msg_code = staff_service.search_by_username(username)
    return response(status_code, msg_code, staff)


@router.get("/searchByUserid", tags=["staff"])
async def search_by_userid(userid: int):
    """通过用户id查找员工"""
    status_code, staff, msg_code = staff_service.search_by_userid(userid)
    return response(status_code, msg_code, staff)


@router.post("/add", tags=["staff"])
async def add_staff(staff: staff_inf.StaffInf):
    """增添员工"""
    status_code, msg_code = staff_service.add_staff(staff)
    return response(status_code, msg_code)


@router.get("/del", tags=["staff"])
async def del_staff(userid: int):
    """删除员工"""
    status_code, msg_code = staff_service.del_staff(userid)
    return response(status_code, msg_code)


@router.post("/edit", tags=["staff"])
async def edit_staff(staff: staff_inf.StaffInf):
    """编辑员工信息，提交环节"""
    status_code, msg_code = staff_service.edit_staff(staff)
    return response(status_code, msg_code)
