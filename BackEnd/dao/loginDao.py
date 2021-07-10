from util import database

datalist = "STAFFS"


def select(index, value):
    db, cursor = database.connectToDataBase()
    sql = """SELECT * FROM %s WHERE %s = '%s'""" % (datalist, index, value)
    try:
        cursor.execute(sql)
        results = cursor.fetchall()
    except:
        db.rollback()
        results = None
    db.close()
    return results
