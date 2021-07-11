from fastapi import APIRouter

from util import response_code

from service import deptService

from model import dept_inf

# 构建api路由
router = APIRouter()


# DONE 高明
@router.get("/showAll", tags=["department"])
async def showAllDepartment():
    # 部门展示
    deptsList, isSuccess = deptService.showAllDepartmentService()
    if isSuccess:
        return response_code.showResponse(deptsList, "查询成功")
    else:
        return response_code.showResponseFail(deptsList, "查询失败")



# @router.post("/search", tags=["department"])
# async def searchDepartment(dept: dept_inf.dept_inf):
#     # 查询部门
#     result = deptService.searchDepartment(dept)
#     return response_code.response(result)


# DONE 高明
@router.post("/add", tags=["department"])
async def addDepartment(dept: dept_inf.AddDeptInf):
    # 增添部门
    isSuccess = deptService.addDepartmentService(dept)
    if isSuccess:
        return response_code.showResponse(None, "用户增加成功")
    else:
        return response_code.showResponseFail(None, "用户增加失败")


# @router.post("/one", tags=["department"])
# async def showOneDepartment(dept: dept_inf.dept_inf):
#     # 展示单个部门
#     result = deptService.showDepartment(dept)
#     return response_code.response(result)


# DONE 高明
@router.post("/edit", tags=["department"])
async def editDepartment(dept: dept_inf.DeptInf):
    # 编辑部门
    isRepeat, isOperaSuccess  = deptService.editDepartmentService(dept)
    if isRepeat or isOperaSuccess:
        if not isRepeat:
            if isOperaSuccess:
                return response_code.showResponse(None, "更新成功")
            else:
                return response_code.showResponseFail(None, "更新失败")
        else:
            return response_code.showResponse(None, "数据重复")
    else:
        return response_code.showResponseFail(None, "更新失败")


# DONE 高明
@router.post("/del", tags=["department"])
async def delDepartment(dept: dept_inf.DelDeptInf):
    # 删除部分
    isOperaSuccess = deptService.delDepartmentService(dept)
    if isOperaSuccess:
        return response_code.showResponse(None, "")
    else:
        return response_code.showResponseFail(None, "")
