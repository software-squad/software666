from fastapi import status
from util import database
import pymysql

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
