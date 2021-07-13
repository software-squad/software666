from fastapi import status
from util import database
import pymysql

datalist = "DOCUMENTS"


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
        results = None
        status_code = status.HTTP_400_BAD_REQUEST
        db.rollback()
    db.close()
    return status_code, results


def insert(fileMsg, file):
    db, cursor = database.connectToDataBase()
    sql = """INSERT INTO %s (TITLE, FILENAME, REMARK, USERNAME, FILEPATH)
             VALUES ('%s','%s','%s','%s','%s');""" % (
             datalist, fileMsg['title'], file.filename, fileMsg['remark'],
             fileMsg['username'], './file/')
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
