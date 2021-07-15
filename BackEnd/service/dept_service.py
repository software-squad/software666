from fastapi import status

from dao import dept_dao, job_dao, staff_dao
from util import message


def get_departments():
    """获取所有部门信息"""
    status_code, result = dept_dao.getall()
    msg_code = message.SEARCH_SUCCESS
    if status_code == status.HTTP_400_BAD_REQUEST:
        msg_code = message.SEARCH_FAILURE
    return status_code, result, msg_code


def add_department(dept):
    """添加部门"""
    status_code, result = dept_dao.select('DEPTNAME', dept.deptname)  # 通过部门名字查询部门
    msg_code = message.ADD_SUCCESS
    if status_code == status.HTTP_400_BAD_REQUEST:
        msg_code = message.ADD_FAILURE
    elif result:  # 如果查询到名字相同的部门，则返回数据重复的消息
        msg_code = message.DATA_REPEATED
    else:
        status_code = dept_dao.insert(dept)  # 数据库中添加新的部门信息
        if status_code == status.HTTP_400_BAD_REQUEST:
            msg_code = message.ADD_FAILURE
    return status_code, msg_code


def del_department(dept):
    """删除部门"""
    edit_index = ['DEPTID', 'DEPTNAME', 'JOBID', 'JOBNAME']  # 员工信息中要修改的索引
    edit_value = [1, '待定', 1, '待定']  # 如果删除部门，则员工信息中部门和职位名字要变为待定，索引也要修改为1
    status_code = staff_dao.edit('DEPTID', dept.deptid, edit_index, edit_value)
    msg_code = message.DEL_SUCCESS
    if status_code == status.HTTP_400_BAD_REQUEST:
        msg_code = message.DEL_FAILURE
    else:
        status_code = job_dao.delete('DEPTID', dept.deptid)  # 部门下的职位也要删除
        if status_code == status.HTTP_400_BAD_REQUEST:
            msg_code = message.DEL_FAILURE
        else:
            status_code = dept_dao.delete('DEPTID', dept.deptid)  # 最后删除部门
            if status_code == status.HTTP_400_BAD_REQUEST:
                msg_code = message.DEL_FAILURE
    return status_code, msg_code


def edit_department(dept):
    """编辑部门"""
    status_code, result = dept_dao.select('DEPTNAME', dept.deptname)  # 根据部门名字查询部门
    msg_code = message.UPD_SUCCESS
    if status_code == status.HTTP_400_BAD_REQUEST:
        msg_code = message.UPD_FAILURE
    elif result and result[0]['deptid'] != dept.deptid:  # 如果查出来的部门，deptid不同于传入参数的deptid，说明数据重复
        msg_code = message.DATA_REPEATED
    else:
        status_code = staff_dao.edit('DEPTID', dept.deptid,  # 由于修改部门涉及到员工信息变化，故修改员工信息
                                     ['DEPTNAME'], [dept.deptname])
        if status_code == status.HTTP_400_BAD_REQUEST:
            msg_code = message.UPD_FAILURE
        else:
            edit_index = ['DEPTNAME', 'DEPTURL', 'REMARK']  # 部门信息修改的索引
            edit_value = [dept.deptname, dept.depturl, dept.remark]  # 部门信息修改后的值
            status_code = dept_dao.edit('DEPTID', dept.deptid,  # 在数据库中修改部门信息
                                        edit_index, edit_value)
            if status_code == status.HTTP_400_BAD_REQUEST:
                msg_code = message.UPD_FAILURE
    return status_code, msg_code
