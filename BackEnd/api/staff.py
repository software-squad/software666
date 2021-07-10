from fastapi import APIRouter

from util import response_code

from service import staffService

from model import staff_inf

from model import user_inf

# 构建api路由
router = APIRouter()


@router.get("/index", tags=["staff"])
async def showAllStaff(staff: staff_inf.StaffDept = None):
    # 展示全体员工
    if staff is None:
        staff, msg_code = staffService.showStaff()
    else:
        staff, msg_code = staffService.searchByDept(staff)
    return response_code.showResponse(staff, msg_code)


@router.post("/showUserByDeptAndJob", tags=["staff"])
async def showByDeptAndJob(staff: staff_inf.StaffDeptAndJob):
    # 通过部门和工作查找员工
    staff, msg_code = staffService.searchByDeptAndJob(staff)
    return response_code.showResponse(staff, msg_code)


@router.post("/showUserByUsername", tags=["staff"])
async def showByUsername(staff: user_inf.UserName):
    # 通过名字查找员工
    staff, msg_code = staffService.searchByUsername(staff)
    return response_code.showResponse(staff, msg_code)


@router.get("/oneByUserid", tags=["staff"])
async def showByUserid(staff: user_inf.Userid):
    # 通过用户id查找员工
    staff, msg_code = staffService.showOneStaff(staff)
    return response_code.showResponse(staff, msg_code)


@router.post("/add", tags=["staff"])
async def addStaff(staff: staff_inf.StaffInf):
    # 增添员工
    msg_code = staffService.addStaff(staff)
    return response_code.updateResponse(msg_code)


@router.post("/edit", tags=["staff"])
async def editStaff(staff: staff_inf.StaffInf):
    # 编辑员工信息
    msg_code = staffService.editStaff(staff)
    return response_code.updateResponse(msg_code)


@router.post("/del", tags=["staff"])
async def delStaff(staff: staff_inf.StaffInf):
    # 删除员工
    msg_code = staffService.delStaff(staff)
    return response_code.updateResponse(msg_code)
