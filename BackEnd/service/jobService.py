from dao import deptDao, jobDao


def showJobs():
    print("====展示单个职位信息====")
    # 调用dao层，从数据库获取的数据封装到对象中。所以可能会涉及到在model中构建模型
    info, res = jobDao.selAllJobs()
    return info, res


def searchJob(jobname):
    print("====搜索单个职位信息====")
    info, res = jobDao.searchOneJob(jobname)
    return info, res


# def showOneJob(job):
#     print("====展示单个职位信息====")
#     info,res=jobDao.selOneJob(job.jobid)
#     return info,res


def editJob(job):
    print("====编辑单个职位信息====")
    res = jobDao.editOneJob(job.jobid, job.jobname, job.remark, job.deptid)
    # 返回是否能成功编辑
    return res


def delJob(job):
    print("====删除单个职位信息====")
    res = jobDao.delOneJob(job.jobid)
    # 返回是否能成功删除
    return res


def addJob(job):
    print("====增加单个职位信息====")
    status_code, result = deptDao.select('DEPTNAME', job.deptname)
    res = jobDao.addOneJob(job.jobname, job.remark, result[0]['deptid'])
    # 返回是否能成功增加
    return res
