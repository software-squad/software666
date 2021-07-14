from fastapi import status
from util import database
import pymysql

datalist = "STAFFS"


def select(index, value):
    db, cursor = database.connectToDataBase()
    sql = """SELECT * FROM %s WHERE %s = '%s'""" % (datalist, index, value)
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
