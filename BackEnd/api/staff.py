from fastapi import APIRouter

from util import response_code

from service import staffService

from model import staff_inf

# 构建api路由
router = APIRouter()


@router.get("/index", tags=["staff"])
async def showAllStaff(deptid: int = None):
    # 展示全体员工
    if deptid is None:
        status_code, staff, msg_code = staffService.getDept()
    else:
        status_code, staff, msg_code = staffService.searchByDept(deptid)
    return response_code.response(status_code, msg_code, staff)


@router.post("/showUserByDeptAndJob", tags=["staff"])
async def showByDeptAndJob(staff: staff_inf.StaffDeptAndJob):
    # 通过部门和工作查找员工
    status_code, staff, msg_code = staffService.searchByDeptAndJob(staff)
    return response_code.response(status_code, msg_code, staff)


@router.get("/showUserByUsername", tags=["staff"])
async def showByUsername(username: str):
    # 通过名字查找员工
    status_code, staff, msg_code = staffService.searchByUsername(username)
    return response_code.response(status_code, msg_code, staff)


@router.get("/oneByUserid", tags=["staff"])
async def showByUserid(userid: int):
    # 通过用户id查找员工
    status_code, staff, msg_code = staffService.showOneStaff(userid)
    return response_code.response(status_code, msg_code, staff)


@router.post("/add", tags=["staff"])
async def addStaff(staff: staff_inf.StaffInf):
    # 增添员工
    status_code, msg_code = staffService.addStaff(staff)
    return response_code.response(status_code, msg_code)


@router.get("/editByUserid", tags=["staff"])
async def editStaffByUserid(userid: int):
    # 编辑员工信息
    status_code, msg_code = staffService.editStaffShow(userid)
    return response_code.response(status_code, msg_code)


@router.post("/editSubmit", tags=["staff"])
async def editStaffSubmit(staff: staff_inf.StaffInf):
    # 编辑员工信息，提交环节
    print(staff.loginname)
    status_code, msg_code = staffService.editStaffSubmit(staff)
    return response_code.response(status_code, msg_code)


@router.post("/del", tags=["staff"])
async def delStaff(staff: staff_inf.StaffInf):
    # 删除员工
    status_code, msg_code = staffService.delStaff(staff)
    return response_code.response(status_code, msg_code)
