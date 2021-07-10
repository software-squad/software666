from fastapi import APIRouter

from util import response_code

from service import deptService

from model import dept_inf

# 构建api路由
router = APIRouter()


@router.post("/search", tags=["department"])
async def searchDepartment(dept: dept_inf.dept_inf):
    # 查询部门
    result = deptService.searchDepartment(dept)
    return response_code.response(result)


@router.post("/add", tags=["department"])
async def addDepartment(dept: dept_inf.dept_inf):
    # 增添部分
    result = deptService.addDepartment(dept)
    return response_code.response(result)


@router.post("/one", tags=["department"])
async def showOneDepartment(dept: dept_inf.dept_inf):
    # 展示单个部门
    result = deptService.showDepartment(dept)
    return response_code.response(result)


@router.post("/edit", tags=["department"])
async def editDepartment(dept: dept_inf.dept_inf):
    # 编辑部门
    result = deptService.editDepartment(dept)
    return response_code.response(result)


@router.post("/del", tags=["department"])
async def delDepartment(dept: dept_inf.dept_inf):
    # 删除部分
    result = deptService.delDepartment(dept)
    return response_code.response(result)
