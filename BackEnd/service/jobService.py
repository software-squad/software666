from fastapi import status
from dao import jobDao, deptDao, staffDao
from util import msg_code


def showJobs():
    """展示工作"""
    status_code, result = jobDao.getAll()
    code = msg_code.SEARCH_SUCCESS
    if status_code == status.HTTP_400_BAD_REQUEST:
        code = msg_code.SEARCH_FAILURE
    return status_code, result, code


def searchJob(jobname):
    """查询工作"""
    status_code, result = jobDao.selectLike('JOBNAME', jobname)
    code = msg_code.SEARCH_SUCCESS
    if status_code == status.HTTP_400_BAD_REQUEST:
        code = msg_code.SEARCH_FAILURE
    return status_code, result, code


def editJob(job):
    """编辑工作"""
    status_code, result = deptDao.select('DEPTNAME', job.deptname)
    code = msg_code.UPD_SUCCESS
    if status_code == status.HTTP_400_BAD_REQUEST:
        code = msg_code.UPD_FAILURE
    elif not result:
        code = msg_code.DATA_NOT_EXIT
    else:
        deptid = result[0]['deptid']
        status_code, result = jobDao.selectBy2('JOBNAME', job.jobname,
                                               'DEPTID', deptid)
        if status_code == status.HTTP_400_BAD_REQUEST:
            code = msg_code.UPD_FAILURE
        elif result and result[0]['jobid'] != job.jobid:
            code = msg_code.DATA_REPEATED
        else:
            edit_index = ['JOBNAME', 'REMARK', 'DEPTID']
            edit_value = [job.jobname, job.remark, deptid]
            status_code = jobDao.edit('JOBID', job.jobid,
                                      edit_index, edit_value)
            if status_code == status.HTTP_400_BAD_REQUEST:
                code = msg_code.UPD_FAILURE
            else:
                edit_index = ['JOBNAME', 'DEPTID', 'DEPTNAME']
                edit_value = [job.jobname, deptid, job.deptname]
                status_code = staffDao.edit('JOBID', job.jobid,
                                            edit_index, edit_value)
                if status_code == status.HTTP_400_BAD_REQUEST:
                    code = msg_code.UPD_FAILURE
    return status_code, code


def delJob(job):
    """删除工作"""
    edit_index = ['JOBID', 'JOBNAME']
    edit_value = [1, '待定']
    status_code = staffDao.edit('JOBID', job.jobid, edit_index, edit_value)
    code = msg_code.DEL_SUCCESS
    if status_code == status.HTTP_400_BAD_REQUEST:
        code = msg_code.DEL_FAILURE
    else:
        status_code = jobDao.delete('JOBID', job.jobid)
        if status_code == status.HTTP_400_BAD_REQUEST:
            code = msg_code.DEL_FAILURE
    return status_code, code


def addJob(job):
    """增添工作"""
    status_code, result = deptDao.select('DEPTNAME', job.deptname)
    code = msg_code.ADD_SUCCESS
    if status_code == status.HTTP_400_BAD_REQUEST:
        code = msg_code.UPD_FAILURE
    elif not result:
        code = msg_code.DATA_NOT_EXIT
    else:
        deptid = result[0]['deptid']
        status_code, result = jobDao.selectBy2('JOBNAME', job.jobname,
                                               'DEPTID', deptid)
        code = msg_code.ADD_SUCCESS
        if status_code == status.HTTP_400_BAD_REQUEST:
            code = msg_code.ADD_FAILURE
        elif result:
            code = msg_code.DATA_REPEATED
        else:
            status_code, result = deptDao.select("DEPTNAME", job.deptname)
            if status_code == status.HTTP_400_BAD_REQUEST:
                code = msg_code.ADD_FAILURE
            elif not result:
                code = msg_code.DATA_NOT_EXIT
            else:
                job.deptid = result[0]['deptid']
                status_code = jobDao.insert(job)
                if status_code == status.HTTP_400_BAD_REQUEST:
                    code = msg_code.ADD_FAILURE
    return status_code, code
