from fastapi import status
from dao import staffDao, deptDao, jobDao
from util import msg_code


def getDept():
    status_code, result = deptDao.getAll()
    code = msg_code.SEARCH_SUCCESS
    if status_code == status.HTTP_400_BAD_REQUEST:
        code = msg_code.SEARCH_FAILURE
    new_result = []
    temp = {}
    for item in result:
        temp["deptid"] = item["deptid"]
        temp["deptname"] = item["deptname"]
        new_result.append(temp)
    return status_code, new_result, code


def searchByDept(deptid):
    status_code, result = jobDao.select('DEPTID', deptid)
    code = msg_code.SEARCH_SUCCESS
    if status_code == status.HTTP_400_BAD_REQUEST:
        code = msg_code.SEARCH_FAILURE
    new_result = []
    temp = {}
    for item in result:
        temp["jobid"] = item["jobid"]
        temp["jobname"] = item["jobname"]
        new_result.append(temp)
    return status_code, new_result, code


def searchByDeptAndJob(staff):
    status_code, result = staffDao.selectBy2('DEPTID', staff.deptid,
                                             'JOBID', staff.jobid)
    code = msg_code.SEARCH_SUCCESS
    if status_code == status.HTTP_400_BAD_REQUEST:
        code = msg_code.SEARCH_FAILURE
    new_result = []
    temp = {}
    for item in result:
        temp["userid"] = item["userid"]
        temp["username"] = item["username"]
        temp["jobname"] = item["jobname"]
        temp["tel"] = item["tel"]
        new_result.append(temp)
    return status_code, new_result, code


def searchByUsername(username):
    status_code, result = staffDao.select('USERNAME', username)
    code = msg_code.SEARCH_SUCCESS
    if status_code == status.HTTP_400_BAD_REQUEST:
        code = msg_code.SEARCH_FAILURE
    new_result = []
    temp = {}
    for item in result:
        temp["userid"] = item["userid"]
        temp["username"] = item["username"]
        temp["jobname"] = item["jobname"]
        temp["tel"] = item["tel"]
        new_result.append(temp)
    return status_code, new_result, code


def showOneStaff(userid):
    status_code, result = staffDao.select('USERID', userid)
    code = msg_code.SEARCH_SUCCESS
    if status_code == status.HTTP_400_BAD_REQUEST:
        code = msg_code.SEARCH_FAILURE
    return status_code, result, code


def addStaff(staff):
    status_code, result = staffDao.select('LOGINNAME', staff.loginname)
    code = msg_code.ADD_SUCCESS
    if result and result['loginname'] == staff.loginname:
        code = msg_code.DATA_REPEATED
    else:
        status_code = staffDao.insert(staff)
    if status_code == status.HTTP_400_BAD_REQUEST:
        code = msg_code.ADD_FAILURE
    return status_code, code


def editStaff(staff):
    status_code = []
    status_code.append(staffDao.edit('USERID', staff.userid,
                                     'USERID', staff.userid))
    status_code.append(staffDao.edit('USERID', staff.userid,
                                     'PASSWORD', staff.password))
    status_code.append(staffDao.edit('USERID', staff.userid,
                                     'STAFFDAO', staff.status))
    status_code.append(staffDao.edit('USERID', staff.userid,
                                     'LOGINNAME', staff.loginname))
    status_code.append(staffDao.edit('USERID', staff.userid,
                                     'FACEURL', staff.faceurl))
    status_code.append(staffDao.edit('USERID', staff.userid,
                                     'FACEPATH', staff.facepath))
    status_code.append(staffDao.edit('USERID', staff.userid,
                                     'DEPTID', staff.deptid))
    status_code.append(staffDao.edit('USERID', staff.userid,
                                     'JOBID', staff.jobid))
    status_code.append(staffDao.edit('USERID', staff.userid,
                                     'USERNAME', staff.username))
    status_code.append(staffDao.edit('USERID', staff.userid,
                                     'CARDID', staff.cardid))
    status_code.append(staffDao.edit('USERID', staff.userid,
                                     'ADDRESS', staff.address))
    status_code.append(staffDao.edit('USERID', staff.userid,
                                     'POSTCODE', staff.postcode))
    status_code.append(staffDao.edit('USERID', staff.userid,
                                     'TEL', staff.tel))
    status_code.append(staffDao.edit('USERID', staff.userid,
                                     'QQNUM', staff.qqnum))
    status_code.append(staffDao.edit('USERID', staff.userid,
                                     'EMAIL', staff.email))
    status_code.append(staffDao.edit('USERID', staff.userid,
                                     'SEX', staff.sex))
    status_code.append(staffDao.edit('USERID', staff.userid,
                                     'PARTY', staff.party))
    status_code.append(staffDao.edit('USERID', staff.userid,
                                     'BIRTHDAY', staff.birthday))
    status_code.append(staffDao.edit('USERID', staff.userid,
                                     'EDUCATION', staff.education))
    status_code.append(staffDao.edit('USERID', staff.userid,
                                     'CREATEDATE', staff.createdate))
    if status.HTTP_400_BAD_REQUEST in status_code:
        status_code = status.HTTP_400_BAD_REQUEST
        code = msg_code.UPD_SUCCESS
    else:
        status_code = status.HTTP_200_OK
        code = msg_code.UPD_FAILURE
    return status_code, code


def delStaff(staff):
    status_code = staffDao.delete('USERID', staff.userid)
    code = msg_code.DEL_SUCCESS
    if status_code == status.HTTP_400_BAD_REQUEST:
        code = msg_code.DEL_FAILURE
    return status_code, code
