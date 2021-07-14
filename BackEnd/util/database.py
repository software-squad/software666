import pymysql


# def connectToDataBase(host="4097n16y34.zicp.vip", user="root",
#                       password="123456", database="software666", port=80):
#     db = pymysql.connect(host=host, user=user,
#                          passwd=password, database=database, port=port)
#     cursor = db.cursor(pymysql.cursors.DictCursor)
#     return db, cursor


def connectToDataBase(host="192.168.0.113", user="root",
                      password="123456", database="software666"):
    db = pymysql.connect(host=host, user=user,
                         passwd=password, database=database)
    cursor = db.cursor(pymysql.cursors.DictCursor)
    return db, cursor
