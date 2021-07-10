from util import database
import pymysql
from model import dept_inf

# DONE
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

# DONE
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

# DONE
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


# DONE
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


# DONE
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


def display():
    # 获取全部成员
    db, cursor = database.connectToDataBase(database="test")
    sql = """SELECT * FROM USER"""
    try:
        cursor.execute(sql)
        results = cursor.fetchall()
        db.close()
        return results
    except:
        db.rollback()
    db.close()
    return False
