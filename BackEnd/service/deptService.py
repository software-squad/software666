from fastapi import status
from dao import deptDao
from util import msg_code


def showAllDepartments():
    # 展示所有部门
    status_code, result = deptDao.getAll()
    code = msg_code.SEARCH_SUCCESS
    if status_code == status.HTTP_400_BAD_REQUEST:
        code = msg_code.SEARCH_FAILURE
    return status_code, result, code


def addDepartment(dept):
    # 添加部门
    status_code, result = deptDao.select('DEPTNAME', dept.deptname)
    code = msg_code.ADD_SUCCESS
    if status_code == status.HTTP_400_BAD_REQUEST:
        code = msg_code.ADD_FAILURE
    elif result:
        code = msg_code.DATA_REPEATED
    else:
        status_code = deptDao.insert(dept)
        if status_code == status.HTTP_400_BAD_REQUEST:
            code = msg_code.ADD_FAILURE
    return status_code, code


def editDepartmentService(dept):
    # 编辑部门
    status_code, result = deptDao.select('DEPTNAME', dept.deptname)
    if status_code == status.HTTP_400_BAD_REQUEST:
        code = msg_code.UPD_FAILURE
    elif result:
        code = msg_code.DATA_REPEATED
    else:
        status_code = []
        status_code.append(deptDao.edit('DEPTID', dept.deptid,
                                        'DEPTNAME', dept.deptname))
        status_code.append(deptDao.edit('DEPTID', dept.deptid,
                                        'REMARK', dept.remark))
        if status.HTTP_400_BAD_REQUEST in status_code:
            status_code = status.HTTP_400_BAD_REQUEST
            code = msg_code.UPD_FAILURE
        else:
            status_code = status.HTTP_200_OK
            code = msg_code.UPD_SUCCESS
    return status_code, code


def delDepartmentService(dept):
    # 删除部门
    status_code = deptDao.delete('DEPTID', dept.deptid)
    code = msg_code.DEL_SUCCESS
    if status_code == status.HTTP_400_BAD_REQUEST:
        code = msg_code.DEL_FAILURE
    return status_code, code
