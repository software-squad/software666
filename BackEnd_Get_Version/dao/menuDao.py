from fastapi import status
from util import database
import pymysql

datalist = "NOTICES"


def getNews():
    db, cursor = database.connectToDataBase()
    sql = "SELECT * FROM %s ORDER BY EDITDATE DESC LIMIT 2" % (datalist)
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
