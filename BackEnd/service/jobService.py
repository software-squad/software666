import sys
sys.path.append('D:\\python and c++\\software666-master\\CSI\\dao')   #括号内容为文件的绝对路径
import jobDao


def showJobs():
    print("====展示单个职位信息====")
    # 调用dao层  从数据库获取的数据封装到对象中。所以可能会涉及到在model中构建模型 
    info,res = jobDao.selAllJobs()
    return info,res


def searchJob(jobname):
    print("====搜索单个职位信息====")
    info,res=jobDao.searchOneJob(jobname)
    return info,res


# def showOneJob(job):
#     print("====展示单个职位信息====")
#     info,res=jobDao.selOneJob(job.jobid)
#     return info,res


def editJob(jobid,jobname,remark):
    print("====编辑单个职位信息====")
    res=jobDao.editOneJob(jobid,jobname,remark)
    #返回是否能成功编辑
    return res


def delJob(jobid):
    print("====删除单个职位信息====")
    res=jobDao.delOneJob(jobid)
    #返回是否能成功删除
    return res


def addJob(jobname,remark):
    print("====增加单个职位信息====")
    res=jobDao.addOneJob(jobname,remark)
    #返回是否能成功增加
    return res

