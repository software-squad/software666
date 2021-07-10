from util import database

datalist = "STAFFS"


def select(index, value):
    db, cursor = database.connectToDataBase()
    sql = """SELECT * FROM %s \
             WHERE %s = '%s'""" % (datalist, index, value)
    try:
        cursor.execute(sql)
        results = cursor.fetchall()
    except:
        results = None
        db.rollback()
    db.close()
    return results


def insert(item):
    # 添加成员
    db, cursor = database.connectToDataBase()
    sql = """INSERT INTO %s VALUES(0, '%s','%s','%s'.'%s','%s','%s','%s','%s'.'%s','%s'
             '%s','%s','%s'.'%s','%s','%s','%s','%s'.'%s')""" % \
          (datalist, item.username, item.cardid, item.sex,
           item.jobid, item.education, item.email, item.deptid,
           item.tel, item.party, item.qqnum, item.address, item.postcode,
           item.birthday, item.loginname, item.password, item.status,
           item.createdate, item.faceurl, item.facepath)
    try:
        cursor.execute(sql)
        db.commit()
        return True
    except:
        db.rollback()
    db.close()
    return False


def delete(index, value):
    db, cursor = database.connectToDataBase()
    sql = "DELETE FROM %s WHERE %s = '%s'" % (datalist, index, value)
    try:
        cursor.execute(sql)
        db.commit()
        return True
    except:
        db.rollback()
    db.close()


def edit(index, value, edit_index, edit_value):
    db, cursor = database.connectToDataBase()
    sql = "UPDATE %s SET %s = '%s' WHERE %s = '%s'" % \
          (datalist, edit_index, edit_value, index, value)
    try:
        cursor.execute(sql)
        db.commit()
    except:
        db.rollback()
    db.close()


def getAll():
    db, cursor = database.connectToDataBase()
    sql = "SELECT * FROM %s" % (datalist)
    try:
        cursor.execute(sql)
        results = cursor.fetchall()
    except:
        results = None
        db.rollback()
    db.close()
    return results
