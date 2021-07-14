from fastapi import status
from dao import staffDao, deptDao, jobDao
from util import msg_code, pwd_encode


def getDept():
    """获取部门信息"""
    status_code, result = deptDao.getAll()  # 获取所有部门信息
    code = msg_code.SEARCH_SUCCESS
    if status_code == status.HTTP_400_BAD_REQUEST:
        code = msg_code.SEARCH_FAILURE
    new_result = []
    for item in result:
        temp = {}
        temp["value"] = item["deptid"]
        temp["label"] = item["deptname"]
        temp["children"] = []
        status_code1, result1 = jobDao.select('DEPTID', item['deptid'])
        for item1 in result1:
            temp1 = {}
            temp1["value"] = item1["jobid"]
            temp1["label"] = item1["jobname"]
            temp["children"].append(temp1)
        new_result.append(temp)
    return status_code, new_result, code


def searchByDept(deptid):
    """通过部门查询工作"""
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
    """通过部门和工作查询员工"""
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
        temp["faceurl"] = item["faceurl"]
        temp["deptname"] = item["deptname"]
        temp["sex"] = item["sex"]
        temp["remark"] = item["remark"]
        new_result.append(temp)
    return status_code, new_result, code


def searchByUsername(username):
    """通过用户名查询员工"""
    status_code, result = staffDao.selectLike('USERNAME', username)
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
        temp["faceurl"] = item["faceurl"]
        temp["deptname"] = item["deptname"]
        temp["sex"] = item["sex"]
        temp["remark"] = item["remark"]
        new_result.append(temp)
    return status_code, new_result, code


def showOneStaff(userid):
    """展示一个员工数据"""
    status_code, result = staffDao.select('USERID', userid)
    code = msg_code.SEARCH_SUCCESS
    if status_code == status.HTTP_400_BAD_REQUEST:
        code = msg_code.SEARCH_FAILURE
    else:
        result = result[0]
        del result['loginname']
        del result['password']
        del result['deptid']
        del result['jobid']
        del result['createdate']
    return status_code, result, code


def addStaff(staff):
    """添加员工"""
    status_code, result = staffDao.select('LOGINNAME', staff.loginname)
    code = msg_code.ADD_SUCCESS
    if status_code == status.HTTP_400_BAD_REQUEST:
        code = msg_code.ADD_FAILURE
    elif result:
        code = msg_code.DATA_REPEATED
    else:
        staff.password = pwd_encode.MD5(staff.password)
        status_code = staffDao.insert(staff)
        if status_code == status.HTTP_400_BAD_REQUEST:
            code = msg_code.ADD_FAILURE
    return status_code, code


def editStaffShow(userid):
    """编辑员工信息前，先传递原本信息"""
    status_code, result = staffDao.select('USERID', userid)
    code = msg_code.SEARCH_SUCCESS
    if status_code == status.HTTP_400_BAD_REQUEST:
        code = msg_code.SEARCH_FAILURE
    else:
        result = result[0]
        result['loginname'] = ''
        result['password'] = ''
        result['createdate'] = ''
    return status_code, result, code


def editStaffSubmit(staff):
    """修改员工信息"""
    edit_index = ['USERNAME', 'CARDID', 'SEX', 'JOBID', 'EDUCATION', 'EMAIL',
                  'DEPTID', 'TEL', 'PARTY', 'QQNUM', 'ADDRESS', 'POSTCODE',
                  'BIRTHDAY', 'FACEURL', 'DEPTNAME', 'JOBNAME']
    edit_value = [staff.username, staff.cardid, staff.sex, staff.jobid,
                  staff.education, staff.email, staff.deptid, staff.tel,
                  staff.party, staff.qqnum, staff.address, staff.postcode,
                  staff.birthday, staff.faceurl, staff.deptname, staff.jobname]
    status_code = staffDao.edit('USERID', staff.userid, edit_index, edit_value)
    code = msg_code.UPD_SUCCESS
    if status_code == status.HTTP_400_BAD_REQUEST:
        code = msg_code.UPD_FAILURE
    return status_code, code


def delStaff(userid):
    """删除员工"""
    status_code = staffDao.delete('USERID', userid)
    code = msg_code.DEL_SUCCESS
    if status_code == status.HTTP_400_BAD_REQUEST:
        code = msg_code.DEL_FAILURE
    return status_code, code
