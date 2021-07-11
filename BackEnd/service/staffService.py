from fastapi import status
from dao import staffDao, deptDao, jobDao
from util import msg_code


def getDept():
    # 获取部门
    status_code, result = deptDao.getAll()
    code = msg_code.SEARCH_SUCCESS
    if status_code == status.HTTP_400_BAD_REQUEST:
        code = msg_code.SEARCH_FAILURE
    new_result = []
    for item in result:
        temp = {}
        temp["deptid"] = item["deptid"]
        temp["deptname"] = item["deptname"]
        new_result.append(temp)
    return status_code, new_result, code


def searchByDept(deptid):
    # 通过部门查询工作
    status_code, result = jobDao.select('DEPTID', deptid)
    code = msg_code.SEARCH_SUCCESS
    if status_code == status.HTTP_400_BAD_REQUEST:
        code = msg_code.SEARCH_FAILURE
    new_result = []
    for item in result:
        temp = {}
        temp["jobid"] = item["jobid"]
        temp["jobname"] = item["jobname"]
        new_result.append(temp)
    return status_code, new_result, code


def searchByDeptAndJob(staff):
    # 通过部门和工作查询员工
    status_code, result = staffDao.selectBy2('DEPTID', staff.deptid,
                                             'JOBID', staff.jobid)
    code = msg_code.SEARCH_SUCCESS
    if status_code == status.HTTP_400_BAD_REQUEST:
        code = msg_code.SEARCH_FAILURE
    new_result = []
    for item in result:
        temp = {}
        temp["userid"] = item["userid"]
        temp["username"] = item["username"]
        temp["jobname"] = item["jobname"]
        temp["tel"] = item["tel"]
        new_result.append(temp)
    return status_code, new_result, code


def searchByUsername(username):
    # 通过用户名查询员工
    status_code, result = staffDao.select('USERNAME', username)
    code = msg_code.SEARCH_SUCCESS
    if status_code == status.HTTP_400_BAD_REQUEST:
        code = msg_code.SEARCH_FAILURE
    new_result = []
    for item in result:
        temp = {}
        temp["userid"] = item["userid"]
        temp["username"] = item["username"]
        temp["jobname"] = item["jobname"]
        temp["tel"] = item["tel"]
        new_result.append(temp)
    return status_code, new_result, code


def showOneStaff(userid):
    # 展示一个员工数据
    status_code, result = staffDao.select('USERID', userid)
    code = msg_code.SEARCH_SUCCESS
    if status_code == status.HTTP_400_BAD_REQUEST:
        code = msg_code.SEARCH_FAILURE
    return status_code, result, code


def addStaff(staff):
    # 添加员工
    status_code, result = staffDao.select('LOGINNAME', staff.loginname)
    code = msg_code.ADD_SUCCESS
    if status_code == status.HTTP_400_BAD_REQUEST:
        code = msg_code.ADD_FAILURE
    elif result:
        code = msg_code.DATA_REPEATED
    else:
        status_code = deptDao.insert(staff)
        if status_code == status.HTTP_400_BAD_REQUEST:
            code = msg_code.ADD_FAILURE
    return status_code, code


def editStaff(staff):
    # 修改员工信息
    status_code = []
    status_code.append(staffDao.edit('USERID', staff.userid,
                                     'USERID', staff.userid))
    status_code.append(staffDao.edit('USERID', staff.userid,
                                     'USERNAME', staff.username))
    status_code.append(staffDao.edit('USERID', staff.userid,
                                     'CARDID', staff.cardid))
    status_code.append(staffDao.edit('USERID', staff.userid,
                                     'SEX', staff.sex))
    status_code.append(staffDao.edit('USERID', staff.userid,
                                     'JOBID', staff.jobid))
    status_code.append(staffDao.edit('USERID', staff.userid,
                                     'EDUCATION', staff.education))
    status_code.append(staffDao.edit('USERID', staff.userid,
                                     'EMAIL', staff.email))
    status_code.append(staffDao.edit('USERID', staff.userid,
                                     'DEPTID', staff.deptid))
    status_code.append(staffDao.edit('USERID', staff.userid,
                                     'TEL', staff.tel))
    status_code.append(staffDao.edit('USERID', staff.userid,
                                     'PARTY', staff.party))
    status_code.append(staffDao.edit('USERID', staff.userid,
                                     'QQNUM', staff.qqnum))
    status_code.append(staffDao.edit('USERID', staff.userid,
                                     'ADDRESS', staff.address))
    status_code.append(staffDao.edit('USERID', staff.userid,
                                     'POSTCODE', staff.postcode))
    status_code.append(staffDao.edit('USERID', staff.userid,
                                     'BIRTHDAY', staff.birthday))
    status_code.append(staffDao.edit('USERID', staff.userid,
                                     'LOGINNAME', staff.loginname))
    status_code.append(staffDao.edit('USERID', staff.userid,
                                     'PASSWORD', staff.password))
    status_code.append(staffDao.edit('USERID', staff.userid,
                                     'STATUS', staff.status))
    status_code.append(staffDao.edit('USERID', staff.userid,
                                     'CREATEDATE', staff.createdate))
    status_code.append(staffDao.edit('USERID', staff.userid,
                                     'FACEURL', staff.faceurl))
    status_code.append(staffDao.edit('USERID', staff.userid,
                                     'FACEPATH', staff.facepath))
    status_code.append(staffDao.edit('USERID', staff.userid,
                                     'DEPTNAME', staff.deptname))
    status_code.append(staffDao.edit('USERID', staff.userid,
                                     'JOBNAME', staff.jobname))
    if status.HTTP_400_BAD_REQUEST in status_code:
        status_code = status.HTTP_400_BAD_REQUEST
        code = msg_code.UPD_FAILURE
    else:
        status_code = status.HTTP_200_OK
        code = msg_code.UPD_SUCCESS
    return status_code, code


def delStaff(staff):
    # 删除员工
    status_code = staffDao.delete('USERID', staff.userid)
    code = msg_code.DEL_SUCCESS
    if status_code == status.HTTP_400_BAD_REQUEST:
        code = msg_code.DEL_FAILURE
    return status_code, code
