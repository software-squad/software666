import pymysql
import sys
import database
sys.path.append('D:\\python and c++\\software666-master\\CSI\\util')  # 括号内容为文件的绝对路径
# 后续要修改


def selAllNotices():
    "返回所有的职位信息"
    db, cursor = database.connectToDataBase()
    sql = "SELECT * FROM NOTICES"
    # result=0  查询成功；
    # result=1  查询失败
    # result=2  数据不存在
    try:
        cursor.execute(sql)
        results = cursor.fetchall()
        print("所有公告信息：", results)
        if str(results) == '()':
            db.close()
            return None, 2
        else:
            return results, 0
    except pymysql.Error as e:
        print(e.args[0], e.args[1])
        print("Unable to fetch notices' info")
        db.rollback()
    cursor.close()
    db.close()
    return None, 1


def editOneNotice(noticeid, title, createdate, content, userid):
    # 修改公告信息
    # result=0  更新成功
    # result=1  更新失败
    # result=2  数据重复
    db, cursor = database.connectToDataBase()
    sql = "UPDATE NOTICES SET TITLE = '%s', CONTENT= '%s',CREATEDATE= '%s',USERID= '%d' \
             WHERE NOTICEID = '%d' " % (title, content, createdate, userid, noticeid)
    # TODO 这里能不能行呢？
    # 包括自己只能有一个
    sql2 = "SELECT COUNT(noticeid) AS nums FROM NOTICES WHERE title= '%s' " % (title)
    sql3 = "SELECT * FROM NOTICES WHERE NOTICEID= '%d' " % (noticeid)
    try:
        # 计算同名的有多少
        count = cursor.execute(sql2)
        cursor.execute(sql3)
        result = cursor.fetchall()
        print(result)
        # dictJson=json.loads(result)
        for i in result:
            # 这里是原来的名字
            for k, v in i.items():
                if k == "title":
                    originTitle = v
                    print(originTitle)
        "可以更新的两种情况：跟原来一样的名字 || 原来没有这个名字"
        if (count == 1 and originTitle == title) or count == 0:
            cursor.execute(sql)
            db.commit()
            return 0
        else:
            print("因重复导致更新失败")
            return 2
    except pymysql.Error as e:
        print(e.args[0], e.args[1])
        db.rollback()
    cursor.close()
    db.close()
    return 1


def delOneNotice(noticeid):
    # 删除公告
    # 0 成功
    # 1 失败
    db, cursor = database.connectToDataBase()
    sql = "DELETE FROM NOTICES WHERE NOTICEID = %d" % (noticeid)
    try:
        cursor.execute(sql)
        db.commit()
        return 0
    except pymysql.Error as e:
        print(e.args[0], e.args[1])
        db.rollback()
    cursor.close()
    db.close()
    return 1


def addOneNotice(title, content, createdate, userid):
    # 新增公告
    # result=0  新增成功
    # result=1  新增失败
    # result=2  数据重复
    db, cursor = database.connectToDataBase()

    # 计算这个表里这个新标题是不是已经存在的
    sql3 = "SELECT * FROM notices WHERE title= '%s' " % (title)
    cursor.execute(sql3)
    info = cursor.fetchall()
    if str(info) == "()":
        sql = "INSERT INTO NOTICES(TITLE, CONTENT,CREATEDATE,USERID) \
                VALUES('%s','%s','%s','%d')" % (title, content, createdate, userid)
        try:
            cursor.execute(sql)
            db.commit()
            return 0
        except pymysql.Error as e:
            print(e.args[0], e.args[1])
            db.rollback()
    else:
        print("因为该公告名称已存在，所以增加失败")
        return 2
    cursor.close()
    db.close()
    return 1
