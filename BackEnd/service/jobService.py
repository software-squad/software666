from fastapi import status
from dao import jobDao, deptDao
from util import msg_code


def showJobs():
    # 展示工作
    status_code, result = jobDao.getAll()
    code = msg_code.SEARCH_SUCCESS
    if status_code == status.HTTP_400_BAD_REQUEST:
        code = msg_code.SEARCH_FAILURE
    return status_code, result, code


def searchJob(jobname):
    # 查询工作
    status_code, result = jobDao.selectLike('JOBNAME', jobname)
    code = msg_code.SEARCH_SUCCESS
    if status_code == status.HTTP_400_BAD_REQUEST:
        code = msg_code.SEARCH_FAILURE
    return status_code, result, code


def editJob(job):
    # 编辑工作
    status_code, result = jobDao.select('JOBNAME', job.jobname)
    if status_code == status.HTTP_400_BAD_REQUEST:
        code = msg_code.UPD_FAILURE
    elif result and result[0]['jobid'] != job.deptid:
        code = msg_code.DATA_REPEATED
    else:
        status_code = []
        status_code.append(jobDao.edit('JOBID', job.jobid,
                                       'JOBNAME', job.jobname))
        status_code.append(jobDao.edit('JOBID', job.jobid,
                                       'REMARK', job.remark))
        if status.HTTP_400_BAD_REQUEST in status_code:
            status_code = status.HTTP_400_BAD_REQUEST
            code = msg_code.UPD_FAILURE
        else:
            status_code = status.HTTP_200_OK
            code = msg_code.UPD_SUCCESS
    return status_code, code


def delJob(job):
    # 删除工作
    status_code = jobDao.delete(job.jobid)
    code = msg_code.DEL_SUCCESS
    if status_code == status.HTTP_400_BAD_REQUEST:
        code = msg_code.DEL_FAILURE
    return status_code, code


def addJob(job):
    # 增添工作
    status_code, result = jobDao.select("JOBNAME", job.jobname)
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
