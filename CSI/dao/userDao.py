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
