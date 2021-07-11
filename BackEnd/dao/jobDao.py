import pymysql
import json
import sys
import database
from fastapi import status
sys.path.append('D:\\python and c++\\software666-master\\CSI\\util')  # 括号内容为文件的绝对路径

datalist = "JOBS"


def select(index, value):
    db, cursor = database.connectToDataBase()
    sql = "SELECT * FROM %s WHERE %s = '%s'" % (datalist, index, value)
    status_code = status.HTTP_200_OK
    try:
        cursor.execute(sql)
        results = cursor.fetchall()
    except pymysql.Error:
        status_code = status.HTTP_400_BAD_REQUEST
        db.rollback()
        results = None
    db.close()
    return status_code, results


def selAllJobs():
    "返回所有的职位信息"
    db, cursor = database.connectToDataBase()
    sql = "SELECT * FROM JOBS"
    # result=0  查询成功；
    # result=1  查询失败
    # result=2  数据不存在
    try:
        cursor.execute(sql)
        results = cursor.fetchall()
        print("所有职位信息：", results)
        if str(results) == '()':
            db.close()
            return None, 2
        else:
            return results, 0
    except pymysql.Error:
        print("Unable to fetch jobs' info")
        db.rollback()
    cursor.close()
    db.close()
    return None, 1


def searchOneJob(jobname):
    # result=0  查询成功；
    # result=1  查询失败
    # result=2  数据不存在
    "搜索单个职位信息"
    db, cursor = database.connectToDataBase()
    sql = "SELECT * FROM JOBS WHERE JOBNAME= '%s'" % (jobname)
    try:
        cursor.execute(sql)
        results = cursor.fetchall()
        print("搜索得职位信息：", results)
        # XXX 这里要字符串类型比较才出的来
        if str(results) == "()":
            db.close()
            return None, 2
        else:
            return results, 0
    except pymysql.Error as e:
        print(e.args[0], e.args[1])
        db.rollback()
    cursor.close()
    db.close()
    return None, 1


# def selOneJob(id):
#     "搜索单个职位信息"
#     db = pymysql.connect(host=host, user=user,
#                          passwd=passpwd, database=database)
#     cursor = db.cursor(pymysql.cursors.DictCursor)
#     sql = """SELECT * FROM JOBS WHERE JOBID=%d""" %(id)
#     try:
#         cursor.execute(sql)
#         results = cursor.fetchall()
#         print("搜索得职位信息：",results)
#         if str(results) == '()':
#             db.close()
#             return None,False
#         else:
#             #TODO 尚不知道这里的结果是个啥，还需测试一波
#             return results,True
#     except pymysql.Error as e:
#         print(e.args[0], e.args[1])
#         db.rollback()
#     cursor.close()
#     db.close()
#     return None,False

def editOneJob(jobid, jobname, remark):
    # result=0  更新成功
    # result=1  更新失败
    # result=2  数据重复
    db, cursor = database.connectToDataBase()
    # XXX 这里要加引号
    sql = "UPDATE JOBS SET JOBNAME = '%s', REMARK = '%s' \
             WHERE JOBID = '%d' " % (jobname, remark, jobid)
    # 包括自己只能有一个
    sql2 = "SELECT * FROM jobs WHERE jobname= '%s' " % (jobname)
    sql3 = "SELECT * FROM JOBS WHERE JOBID= '%d' " % (jobid)
    try:
        # 计算同名的有多少
        cursor.execute(sql2)
        sameName = cursor.fetchall()
        cursor.execute(sql3)
        result = cursor.fetchall()
        # dictJson=json.loads(result)
        for i in result:
            # 这里是原来的名字
            for k, v in i.items():
                if k == "jobname":
                    originName = v
        print("originName:", originName)
        print("同名职称数：", sameName)
        "可以更新的两种情况：跟原来一样的名字 || 原来没有这个名字"
        if (str(sameName) != '()' and originName == jobname) or (str(sameName) == '()'):
            cursor.execute(sql)
            db.commit()
            return 0
        else:
            print("因重复导致更新失败")
            return 2
    except pymysql.Error as e:
        print(e.args[0], e.args[1])
        db.rollback()
    cursor.close()
    db.close()
    return 1


def delOneJob(jobid):
    # 删除成员
    # 0 成功
    # 1 失败
    db, cursor = database.connectToDataBase()
    sql = "DELETE FROM JOBS WHERE JOBID = %d" % (jobid)
    try:
        cursor.execute(sql)
        db.commit()
        return 0
    except pymysql.Error as e:
        print(e.args[0], e.args[1])
        db.rollback()
    cursor.close()
    db.close()
    return 1


def addOneJob(jobname, remark):
    # 添加职位
    # result=0  新增成功
    # result=1  新增失败
    # result=2  数据重复
    db, cursor = database.connectToDataBase()
    # 计算这个表里这个新名字是不是已经存在的
    sql3 = "SELECT * FROM jobs WHERE jobname= '%s' " % (jobname)
    cursor.execute(sql3)
    info = cursor.fetchall()

    if str(info) == "()":
        sql = "INSERT INTO JOBS(JOBNAME, REMARK) \
                VALUES('%s','%s')" % (jobname, remark)
        try:
            cursor.execute(sql)
            db.commit()
            return 0
        except pymysql.Error as e:
            print(e.args[0], e.args[1])
            db.rollback()
    else:
        print("因为该职位名称已存在，所以增加失败")
        return 2
    cursor.close()
    db.close()
    return 1
