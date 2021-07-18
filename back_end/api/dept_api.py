from fastapi import APIRouter

from util.response import response
from service import dept_service
from model import dept_inf

# 构建api路由
router = APIRouter()


@router.get("/showDepts", tags=["department"])
async def show_departments():
    """展示部门"""
    status_code, depts, msg_code = dept_service.get_departments()
    return response(status_code, msg_code, depts)


@router.post("/add", tags=["department"])
async def add_department(dept: dept_inf.DeptInf):
    """增添部门"""
    status_code, msg_code = dept_service.add_department(dept)
    return response(status_code, msg_code)


@router.post("/del", tags=["department"])
async def del_department(dept: dept_inf.DelDeptInf):
    """删除部门"""
    status_code, msg_code = dept_service.del_department(dept)
    return response(status_code, msg_code)


@router.post("/edit", tags=["department"])
async def edit_department(dept: dept_inf.DeptInf):
    """编辑部门"""
    status_code, msg_code = dept_service.edit_department(dept)
    return response(status_code, msg_code)
