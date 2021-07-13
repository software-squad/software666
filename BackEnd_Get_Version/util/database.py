import pymysql


def connectToDataBase(host="192.168.0.102", user="root",
                      password="123456", database="software666"):
    db = pymysql.connect(host=host, user=user,
                         passwd=password, database=database)
    cursor = db.cursor(pymysql.cursors.DictCursor)
    return db, cursor
