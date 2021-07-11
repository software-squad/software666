from fastapi import status
from util import database
import pymysql

datalist = "STAFFS"


def select(index, value):
    db, cursor = database.connectToDataBase()
    sql = "SELECT * FROM %s WHERE %s = '%s'" % (datalist, index, value)
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


def insert(item):
    db, cursor = database.connectToDataBase()
    sql = """INSERT INTO %s VALUES(DEFAULT,'%s','%s','%s','%s','%s','%s','%s','%s','%s',
             '%s','%s','%s','%s','%s','%s','%s','%s','%s','%s','%s','%s')""" %\
          (datalist, item.username, item.cardid, item.sex, item.jobid,
           item.education, item.email, item.deptid, item.tel, item.party,
           item.qqnum, item.address, item.postcode, item.birthday,
           item.loginname, item.password, item.status, item.createdate,
           item.faceurl, item.facepath, item.deptname, item.jobname)
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


def edit(index, value, edit_index, edit_value):
    db, cursor = database.connectToDataBase()
    sql = "UPDATE %s SET %s = '%s' WHERE %s = '%s'" % \
          (datalist, edit_index, edit_value, index, value)
    status_code = status.HTTP_200_OK
    try:
        cursor.execute(sql)
        db.commit()
    except pymysql.Error:
        status_code = status.HTTP_400_BAD_REQUEST
        db.rollback()
    db.close()
    return status_code
