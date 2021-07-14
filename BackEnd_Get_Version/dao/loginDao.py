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
        status_code = status.HTTP_400_BAD_REQUEST
        db.rollback()
        results = None
    db.close()
    return status_code, results