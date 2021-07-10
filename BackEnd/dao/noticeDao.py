from util import database


def select(name, pwd):
    # 判断用户名和密码的匹配
    db, cursor = database.connectToDataBase(database="test")
    sql = """SELECT * FROM USER \
             WHERE USERNAME = '%s'""" % (name)
    try:
        cursor.execute(sql)
        results = cursor.fetchall()
        print(results)
        if results == '()':
            db.close()
            return False
        else:
            for row in results:
                pwd1 = row[2]
                if pwd1 == pwd:
                    db.close()
                    return True
                return False
    except:
        db.rollback()
    db.close()
    return False


def insert(name, pwd, income):
    # 添加成员
    db, cursor = database.connectToDataBase(database="test")
    sql = """INSERT INTO USER(USERNAME, PWD, INCOME)
             VALUES('%s','%s','%s')""" % (name, pwd, income)
    try:
        cursor.execute(sql)
        db.commit()
        return True
    except:
        db.rollback()
    db.close()
    return False


def delete(name, pwd, income):
    # 删除成员
    db, cursor = database.connectToDataBase(database="test")
    sql = "DELETE FROM USER WHERE USERNAME = '%s'" % name
    try:
        cursor.execute(sql)
        db.commit()
        return True
    except:
        db.rollback()
    db.close()
    return False


def edit(name, pwd, income):
    # 修改成员
    db, cursor = database.connectToDataBase(database="test")
    sql = """UPDATE USER SET USERNAME = '%s', PWD = '%s', INCOME = '%s'
             WHERE USERNAME = '%s'""" % (name, pwd, income, name)
    try:
        cursor.execute(sql)
        db.commit()
        return True
    except:
        db.rollback()
    db.close()
    return False


def display():
    # 获取全部成员
    db, cursor = database.connectToDataBase(database="test")
    sql = """SELECT * FROM USER"""
    try:
        cursor.execute(sql)
        results = cursor.fetchall()
        db.close()
        return results
    except:
        db.rollback()
    db.close()
    return False
