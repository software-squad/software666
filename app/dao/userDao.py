from util import database
import pymysql
import config
def selUserById(user_id):
    # XXX user_id
    print(user_id)
    sql = "SELECT * FROM EMPLOYEE \
       WHERE ID = %d"%(user_id)
    # db = database.getUserDB()
    # 打开数据库连接
    conn = pymysql.connect(host=config.url, user="root", passwd="123456", database="test")

    # 使用cursor()方法获取操作游标
    db = conn.cursor()
    try:
        # XXX 打印
        print('开始查找数据')
        db.execute(sql)
        res = db.fetchall()
        print(res)
    except Exception as e:
        db.rollback()
        print(e.args)
        print("发生错误已经回滚")

    # 关闭数据库连接
    db.close()
    return  res