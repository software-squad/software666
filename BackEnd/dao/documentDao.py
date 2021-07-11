from util import database

import pymysql


# DONE 高明
def selectAllFiles():
    # 查询所有的文件信息
    data = dict()
    isOperaSuccess = True
    db, cursor = database.connectToDataBase(database="software666")
    sql = """SELECT * FROM documents"""
    try:
        cursor.execute(sql)
        data = cursor.fetchall()
    except pymysql.Error as e:
        print(e.args[0], e.args[1])
        isOperaSuccess = False
        db.rollback()
    db.close()
    return data, isOperaSuccess


def insert(name, pwd, income):
    # 添加成员
    db, cursor = database.connectToDataBase(database="test")
    sql = """INSERT INTO USER(USERNAME, PWD, INCOME)
             VALUES('%s','%s','%s')""" % (name, pwd, income)
    try:
        cursor.execute(sql)
        db.commit()
        return True
    except pymysql.Error:
        db.rollback()
    db.close()
    return False


# DONE 高明
def delete(file):
    # 删除成员
    isOperaSuccess = True
    db, cursor = database.connectToDataBase(database="software666")
    sql = "DELETE FROM documents WHERE fileid = %d" % file.fileid
    try:
        cursor.execute(sql)
        db.commit()
        return True
    except pymysql.Error as e:
        print(e.args[0], e.args[1])
        isOperaSuccess = False
        db.rollback()
    db.close()
    return isOperaSuccess


# DONE 高明
def edit(file):
    # 修改成员
    isOperaSuccess = True
    db, cursor = database.connectToDataBase(database="software666")
    sql = """UPDATE documents SET fileid = %d
            , title = '%s'
            , filename = '%s'
            , remark = '%s'
            , createdate = '%s'
            , username = '%s'
            , filepath = '%s'
             WHERE fileid = %d""" % (file.fileid,
                                     file.title,
                                     file.filename,
                                     file.remark,
                                     file.createdate,
                                     file.username,
                                     file.filepath,
                                     file.fileid)
    try:
        cursor.execute(sql)
        db.commit()
    except pymysql.Error as e:
        print(e.args[0], e.args[1])
        isOperaSuccess = False
        db.rollback()
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
    except pymysql.Error:
        db.rollback()
    db.close()
    return False
