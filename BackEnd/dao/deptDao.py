from fastapi import status
from util import database
import pymysql
from model import dept_inf

datalist = "DEPARTMENTS"


def getAll():
    db, cursor = database.connectToDataBase()
    sql = "SELECT * FROM %s" % (datalist)
    status_code = status.HTTP_200_OK
    try:
        cursor.execute(sql)
        results = cursor.fetchall()
    except pymysql.Error:
        status_code = status.HTTP_400_BAD_REQUEST
        results = None
        db.rollback()
    db.close()
    return status_code, results

# DONE 高明
def selectAllDept():
    depts = dict()
    isSuccess = True
    db, cursor = database.connectToDataBase(database="software666")
    sql = """SELECT deptid, deptname, remark
        FROM departments"""
    try:
        cursor.execute(sql)
        depts = cursor.fetchall()
    except pymysql.Error as e:
        print(e.args[0], e.args[1])
        db.rollback()
        isSuccess = False
    db.close()
    return depts, isSuccess

# DONE 高明
def selectIdByName(deptname):
    # 判断用户名和密码的匹配
    deptid = dict()
    isOperaSuccess = True
    db, cursor = database.connectToDataBase(database="software666")
    sql = """SELECT deptid FROM departments \
            WHERE deptname = '%s'""" % (deptname)
    try:
        cursor.execute(sql)
        deptid = cursor.fetchall()
    except pymysql.Error as e:
        print(e.args[0], e.args[1])
        db.rollback()
        isOperaSuccess = False
    db.close()
    return deptid, isOperaSuccess

# DONE 高明
def insert(dept:dept_inf.AddDeptInf):
    # 添加部门
    db, cursor = database.connectToDataBase(database="software666")
    sql = """INSERT INTO departments(deptname, remark)
             VALUES('%s','%s')""" % (dept.deptname, dept.remark)
    try:
        cursor.execute(sql)
        db.commit()
        db.close()
        return True
    except pymysql.Error as e:
        print(e.args[0], e.args[1])
        db.rollback()
    db.close()
    return False

# DONE 高明
def delete(dept: dept_inf.DelDeptInf):
    # 删除成员
    isOperaSuccess = True
    db, cursor = database.connectToDataBase(database="software666")
    sql = "DELETE FROM departments WHERE deptid = %d" % dept.deptid
    try:
        cursor.execute(sql)
        db.commit()
    except pymysql.Error as e:
        print(e.args[0], e.args[1])
        isOperaSuccess = False
        db.rollback()
    db.close()
    return isOperaSuccess

# DONE 高明
def edit(dept: dept_inf.DeptInf):
    # 修改成员
    isOperaSuccess = True
    db, cursor = database.connectToDataBase(database="software666")

    sql = """UPDATE departments SET deptname = '%s', remark = '%s'
            WHERE deptid = %d""" % (dept.deptname, dept.remark, dept.deptid)
    try:
        cursor.execute(sql)
        db.commit()
    except pymysql.Error as e:
        print(e.args[0], e.args[1])
        db.rollback()
        isOperaSuccess = False
    db.close()
    return isOperaSuccess
