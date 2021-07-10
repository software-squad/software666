from dao import staffDao
from util import msg_code


def showStaff():
    result = staffDao.getAll()
    return result, msg_code.SEARCH_SUCCESS


def searchByDept(staff):
    result = staffDao.select('DEPTID', staff.dept)
    return result, msg_code.SEARCH_SUCCESS


def searchByDeptAndJob(staff):
    result1 = staffDao.select('DEPTID', staff.dept)
    result2 = staffDao.seletc('JOBID', staff.job)
    return [result1, result2], msg_code.SEARCH_SUCCESS


def searchByUsername(staff):
    result = staffDao.select('USERNAME', staff.username)
    return result, msg_code.SEARCH_SUCCESS


def showOneStaff(staff):
    result = staffDao.select('USERID'. staff.userid)
    return result, msg_code.SEARCH_SUCCESS


def addStaff(staff):
    staffDao.insert(staff)
    return msg_code.UPD_SUCCESS


def editStaff(staff):
    staffDao.edit('USERID', staff.userid, 'USERID', staff.userid)
    staffDao.edit('USERID', staff.userid, 'PASSWORD', staff.password)
    staffDao.edit('USERID', staff.userid, 'STAFFDAO', staff.status)
    staffDao.edit('USERID', staff.userid, 'USERNAME', staff.username)
    staffDao.edit('USERID', staff.userid, 'FACEURL', staff.faceurl)
    staffDao.edit('USERID', staff.userid, 'FACEPATH', staff.facepath)
    staffDao.edit('USERID', staff.userid, 'DEPTID', staff.deptid)
    staffDao.edit('USERID', staff.userid, 'JOBID', staff.jobid)
    staffDao.edit('USERID', staff.userid, 'NAME', staff.name)
    staffDao.edit('USERID', staff.userid, 'CARDID', staff.cardid)
    staffDao.edit('USERID', staff.userid, 'ADDRESS', staff.address)
    staffDao.edit('USERID', staff.userid, 'POSTCODE', staff.postcode)
    staffDao.edit('USERID', staff.userid, 'TEL', staff.tel)
    staffDao.edit('USERID', staff.userid, 'QQNUM', staff.qqnum)
    staffDao.edit('USERID', staff.userid, 'EMAIL', staff.email)
    staffDao.edit('USERID', staff.userid, 'SEX', staff.sex)
    staffDao.edit('USERID', staff.userid, 'PARTY', staff.party)
    staffDao.edit('USERID', staff.userid, 'BIRTHDAY', staff.birthday)
    staffDao.edit('USERID', staff.userid, 'EDUCATION', staff.education)
    staffDao.edit('USERID', staff.userid, 'CREATEDATE', staff.createdate)
    return msg_code.UPD_SUCCESS


def delStaff(staff):
    staffDao.delete('USERID', staff.userid)
    return msg_code.UPD_SUCCESS
