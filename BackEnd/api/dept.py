from fastapi import APIRouter

from util import response_code

from service import deptService

from model import dept_inf

# 构建api路由
router = APIRouter()


@router.get("/showAll", tags=["department"])
async def showDepartments():
    # 展示所有部门
    status_code, depts, msg_code = deptService.showDepartments()
    return response_code.response(status_code, msg_code, depts)


@router.post("/add", tags=["department"])
async def addDepartment(dept: dept_inf.DeptInf):
    # 增添部门
    status_code, msg_code = deptService.addDepartment(dept)
    return response_code.response(status_code, msg_code)


@router.post("/edit", tags=["department"])
async def editDepartment(dept: dept_inf.DeptInf):
    # 编辑部门
    status_code, msg_code = deptService.editDepartment(dept)
    return response_code.response(status_code, msg_code)


@router.post("/del", tags=["department"])
async def delDepartment(dept: dept_inf.DelDeptInf):
    # 删除部门
    status_code, msg_code = deptService.delDepartment(dept)
    return response_code.response(status_code, msg_code)
