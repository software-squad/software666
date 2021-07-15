from fastapi import status

from dao import staff_dao, dept_dao, job_dao
from util import message, security


def get_index():
    """获取所有职位和所属部门信息，以树状形式传回"""
    status_code, result = dept_dao.getall()  # 获取所有部门信息
    msg_code = message.SEARCH_SUCCESS
    if status_code == status.HTTP_400_BAD_REQUEST:
        msg_code = message.SEARCH_FAILURE
    new_result = []
    for item in result:  # 生成前端所需信息
        temp = {}
        temp["value"] = item["deptid"]  # 命名方式与前端同步，下同
        temp["label"] = item["deptname"]  # value表id，label表name，children中是job信息
        temp["children"] = []
        status_code1, result1 = job_dao.select('DEPTID', item['deptid'])
        for item1 in result1:  # chiledren的内容，是jobid和jobname
            temp1 = {}  # children中value表jobid，label表jobname
            temp1["value"] = item1["jobid"]
            temp1["label"] = item1["jobname"]
            temp["children"].append(temp1)
        new_result.append(temp)
    return status_code, new_result, msg_code


def search_by_dept_and_job(staff):
    """通过部门和工作查询员工"""
    status_code, result = staff_dao.select_by_2('DEPTID', staff.deptid,
                                                'JOBID', staff.jobid)
    msg_code = message.SEARCH_SUCCESS
    if status_code == status.HTTP_400_BAD_REQUEST:
        msg_code = message.SEARCH_FAILURE
    new_result = []
    for item in result:  # 生成前端所需信息
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
    return status_code, new_result, msg_code


def search_by_username(username):
    """通过用户名查询员工"""
    status_code, result = staff_dao.select_like('USERNAME', username)
    msg_code = message.SEARCH_SUCCESS
    if status_code == status.HTTP_400_BAD_REQUEST:
        msg_code = message.SEARCH_FAILURE
    new_result = []
    for item in result:  # 生成前端所需信息
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
    return status_code, new_result, msg_code


def search_by_userid(userid):
    """展示一个员工数据"""
    status_code, result = staff_dao.select('USERID', userid)
    msg_code = message.SEARCH_SUCCESS
    if status_code == status.HTTP_400_BAD_REQUEST:
        msg_code = message.SEARCH_FAILURE
    else:  # 只保留前端所需信息
        result = result[0]
        del result['loginname']
        del result['password']
        del result['createdate']
    return status_code, result, msg_code


def add_staff(staff):
    """添加员工"""
    status_code, result = staff_dao.select('LOGINNAME', staff.loginname)  # 查询新增员工loginname
    msg_code = message.ADD_SUCCESS
    if status_code == status.HTTP_400_BAD_REQUEST:
        msg_code = message.ADD_FAILURE
    elif result:  # loginname不允许重复，若有重复，则返回数据重复的消息
        msg_code = message.DATA_REPEATED
    else:
        staff.password = security.MD5(staff.password)
        status_code = staff_dao.insert(staff)
        if status_code == status.HTTP_400_BAD_REQUEST:
            msg_code = message.ADD_FAILURE
    return status_code, msg_code


def del_staff(userid):
    """删除员工"""
    status_code = staff_dao.delete('USERID', userid)
    msg_code = message.DEL_SUCCESS
    if status_code == status.HTTP_400_BAD_REQUEST:
        msg_code = message.DEL_FAILURE
    return status_code, msg_code


def edit_staff(staff):
    """修改员工信息"""
    # 要修改的索引
    edit_index = ['USERNAME', 'CARDID', 'SEX', 'JOBID', 'EDUCATION', 'EMAIL',
                  'DEPTID', 'TEL', 'PARTY', 'QQNUM', 'ADDRESS', 'POSTCODE',
                  'BIRTHDAY', 'FACEURL', 'DEPTNAME', 'JOBNAME', 'REMARK']
    # 要修改的值
    edit_value = [staff.username, staff.cardid, staff.sex, staff.jobid,
                  staff.education, staff.email, staff.deptid, staff.tel,
                  staff.party, staff.qqnum, staff.address, staff.postcode,
                  staff.birthday, staff.faceurl, staff.deptname,
                  staff.jobname, staff.remark]
    status_code = staff_dao.edit('USERID', staff.userid,
                                 edit_index, edit_value)
    msg_code = message.UPD_SUCCESS
    if status_code == status.HTTP_400_BAD_REQUEST:
        msg_code = message.UPD_FAILURE
    return status_code, msg_code
