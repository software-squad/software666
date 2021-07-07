import pymysql
import config
def getUserDB():
    # 打开数据库连接
    conn = pymysql.connect(host=config.url, user="root", passwd="123456", database="test")

    # 使用cursor()方法获取操作游标
    db = conn.cursor()
    return db