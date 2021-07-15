import pymysql


def connect_to_database(host="192.168.0.101", user="root",
                        password="123456", database="software666666"):
    """连接数据库的函数，默认参数为当前服务器的数据库所需参数"""
    db = pymysql.connect(host=host, user=user,
                         passwd=password, database=database)
    cursor = db.cursor(pymysql.cursors.DictCursor)
    return db, cursor
