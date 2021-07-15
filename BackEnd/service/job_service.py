from fastapi import status

from dao import job_dao, dept_dao, staff_dao
from util import message


def get_jobs():
    """获取所有职位信息"""
    status_code, result = job_dao.getall()
    msg_code = message.SEARCH_SUCCESS
    if status_code == status.HTTP_400_BAD_REQUEST:
        msg_code = message.SEARCH_FAILURE
    else:
        for item in result:  # 对于所有查到的职位，需要添加上所属部门名字（职位数据表中没有）
            status_code, result1 = dept_dao.select('DEPTID', item['deptid'])
            if status_code == status.HTTP_400_BAD_REQUEST:
                msg_code = message.SEARCH_FAILURE
                break
            elif not result1:  # 如果没有查到相应部门，则返回数据不存在的消息
                msg_code = message.DATA_NOT_EXIT
                break
            else:
                item['deptname'] = result1[0]['deptname']
    return status_code, result, msg_code


def search_job(jobname):
    """查询职位"""
    status_code, result = job_dao.select_like('JOBNAME', jobname)  # 模糊搜索
    msg_code = message.SEARCH_SUCCESS
    if status_code == status.HTTP_400_BAD_REQUEST:
        msg_code = message.SEARCH_FAILURE
    return status_code, result, msg_code


def add_job(job):
    """增添职位"""
    status_code, result = dept_dao.select('DEPTNAME', job.deptname)  # 选取新增职位所属部门
    msg_code = message.ADD_SUCCESS
    if status_code == status.HTTP_400_BAD_REQUEST:
        msg_code = message.UPD_FAILURE
    elif not result:  # 如果不存在部门，则返回数据不存在的消息
        msg_code = message.DATA_NOT_EXIT
    else:
        deptid = result[0]['deptid']  # 取出部门的id
        status_code, result = job_dao.select_by_2('JOBNAME', job.jobname,
                                                  'DEPTID', deptid)  # 根据新增职位的名称和部门id选取职位
        msg_code = message.ADD_SUCCESS
        if status_code == status.HTTP_400_BAD_REQUEST:
            msg_code = message.ADD_FAILURE
        elif result:  # 如果能查到数据，说明部门下已存在该职位（名称重复）
            msg_code = message.DATA_REPEATED
        else:
            status_code = job_dao.insert(job)  # 最后，在数据库增添职位
            if status_code == status.HTTP_400_BAD_REQUEST:
                msg_code = message.ADD_FAILURE
    return status_code, msg_code


def del_job(job):
    """删除职位"""
    edit_index = ['JOBID', 'JOBNAME']  # 删除职位，则职位下员工信息要变化
    edit_value = [1, '待定']  # 员工的职位id置为1，职位名字置为待定
    status_code = staff_dao.edit('JOBID', job.jobid, edit_index, edit_value)
    msg_code = message.DEL_SUCCESS
    if status_code == status.HTTP_400_BAD_REQUEST:
        msg_code = message.DEL_FAILURE
    else:
        status_code = job_dao.delete('JOBID', job.jobid)  # 删除职位
        if status_code == status.HTTP_400_BAD_REQUEST:
            msg_code = message.DEL_FAILURE
    return status_code, msg_code


def edit_job(job):
    """编辑职位"""
    status_code, result = dept_dao.select('DEPTNAME', job.deptname)  # 编辑职位可能要修改部门，故先查询部门
    msg_code = message.UPD_SUCCESS
    if status_code == status.HTTP_400_BAD_REQUEST:
        msg_code = message.UPD_FAILURE
    elif not result:  # 如果没有相应部门，则返回数据不存在的消息
        msg_code = message.DATA_NOT_EXIT
    else:
        deptid = result[0]['deptid']  # 取出部门id
        status_code, result = job_dao.select_by_2('JOBNAME', job.jobname,
                                                  'DEPTID', deptid)  # 由部门和职位改动的信息查询职位
        if status_code == status.HTTP_400_BAD_REQUEST:
            msg_code = message.UPD_FAILURE
        elif result and result[0]['jobid'] != job.jobid:  # 如果存在数据且id不与参数中id相同，说明数据重复
            msg_code = message.DATA_REPEATED
        else:
            edit_index = ['JOBNAME', 'REMARK', 'DEPTID']  # 职位中要修改的索引
            edit_value = [job.jobname, job.remark, deptid]  # 职位中修改后的值
            status_code = job_dao.edit('JOBID', job.jobid,  # 调用dao层修改数据库
                                       edit_index, edit_value)
            if status_code == status.HTTP_400_BAD_REQUEST:
                msg_code = message.UPD_FAILURE
            else:
                edit_index = ['JOBNAME', 'DEPTID', 'DEPTNAME']  # 员工中要修改的索引
                edit_value = [job.jobname, deptid, job.deptname]  # 员工中要修改的值
                status_code = staff_dao.edit('JOBID', job.jobid,  # 调用员工的dao层修改数据库
                                             edit_index, edit_value)
                if status_code == status.HTTP_400_BAD_REQUEST:
                    msg_code = message.UPD_FAILURE
    return status_code, msg_code
