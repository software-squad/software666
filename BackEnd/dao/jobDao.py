import pymysql
from util import database
from fastapi import status

datalist = "JOBS"


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


def selectBy2(index1, value1, index2, value2):
    db, cursor = database.connectToDataBase()
    sql = "SELECT * FROM %s WHERE %s = '%s' AND %s = '%s'" % \
          (datalist, index1, value1, index2, value2)
    status_code = status.HTTP_200_OK
    try:
        cursor.execute(sql)
        results = cursor.fetchall()
    except pymysql.Error:
        results = None
        status_code = status.HTTP_400_BAD_REQUEST
        db.rollback()
    db.close()
    return status_code, results


def selectLike(index, value):
    db, cursor = database.connectToDataBase()
    sql = "SELECT * FROM %s WHERE %s LIKE '%%%s%%'" % (datalist, index, value)
    status_code = status.HTTP_200_OK
    try:
        cursor.execute(sql)
        results = cursor.fetchall()
    except pymysql.Error:
        results = None
        status_code = status.HTTP_400_BAD_REQUEST
        db.rollback()
    db.close()
    return status_code, results


def insert(item):
    db, cursor = database.connectToDataBase()
    sql = "INSERT INTO %s(JOBNAME,REMARK,DEPTID) \
                VALUES('%s','%s','%s')" % \
          (datalist, item.jobname, item.remark, item.deptid)
    status_code = status.HTTP_200_OK
    try:
        cursor.execute(sql)
        db.commit()
    except pymysql.Error:
        status_code = status.HTTP_400_BAD_REQUEST
        db.rollback()
    db.close()
    return status_code


def delete(index, value):
    db, cursor = database.connectToDataBase()
    sql = "DELETE FROM %s WHERE %s = '%s'" % (datalist, index, value)
    status_code = status.HTTP_200_OK
    try:
        cursor.execute(sql)
        db.commit()
    except pymysql.Error:
        status_code = status.HTTP_400_BAD_REQUEST
        db.rollback()
    db.close()
    return status_code


def edit(index, value, edit_index: list, edit_value: list):
    db, cursor = database.connectToDataBase()
    sql = "UPDATE %s SET %s = '%s'" % (datalist, edit_index[0], edit_value[0])
    if len(edit_index) > 1:
        for key, val in zip(edit_index[1:], edit_value[1:]):
            sql += ", %s = '%s'" % (key, val)
    sql += " WHERE %s = '%s'" % (index, value)
    status_code = status.HTTP_200_OK
    try:
        cursor.execute(sql)
        db.commit()
    except pymysql.Error:
        status_code = status.HTTP_400_BAD_REQUEST
        db.rollback()
    db.close()
    return status_code
