from util import database

datalist = "NOTICES"


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
