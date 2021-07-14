from fastapi import status
from dao import deptDao, jobDao, staffDao
from util import msg_code


def showDepartments():
    """展示所有部门"""
    status_code, result = deptDao.getAll()
    code = msg_code.SEARCH_SUCCESS
    if status_code == status.HTTP_400_BAD_REQUEST:
        code = msg_code.SEARCH_FAILURE
    return status_code, result, code


def addDepartment(dept):
    """添加部门"""
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


def editDepartment(dept):
    """编辑部门"""
    status_code, result = deptDao.select('DEPTNAME', dept.deptname)
    code = msg_code.UPD_SUCCESS
    if status_code == status.HTTP_400_BAD_REQUEST:
        code = msg_code.UPD_FAILURE
    elif result and result[0]['deptid'] != dept.deptid:
        code = msg_code.DATA_REPEATED
    else:
        status_code = staffDao.edit('DEPTID', dept.deptid,
                                    ['DEPTNAME'], [dept.deptname])
        if status_code == status.HTTP_400_BAD_REQUEST:
            code = msg_code.UPD_FAILURE
        else:
            edit_index = ['DEPTNAME', 'DEPTURL', 'REMARK']
            edit_value = [dept.deptname, dept.depturl, dept.remark]
            status_code = deptDao.edit('DEPTID', dept.deptid,
                                       edit_index, edit_value)
            if status_code == status.HTTP_400_BAD_REQUEST:
                code = msg_code.UPD_FAILURE
    return status_code, code


def delDepartment(dept):
    """删除部门"""
    edit_index = ['DEPTID', 'DEPTNAME', 'JOBID', 'JOBNAME']
    edit_value = [1, '待定', 1, '待定']
    status_code = staffDao.edit('DEPTID', dept.deptid, edit_index, edit_value)
    code = msg_code.DEL_SUCCESS
    if status_code == status.HTTP_400_BAD_REQUEST:
        code = msg_code.DEL_FAILURE
    else:
        status_code = jobDao.delete('DEPTID', dept.deptid)
        if status_code == status.HTTP_400_BAD_REQUEST:
            code = msg_code.DEL_FAILURE
        else:
            status_code = deptDao.delete('DEPTID', dept.deptid)
            if status_code == status.HTTP_400_BAD_REQUEST:
                code = msg_code.DEL_FAILURE
    return status_code, code
