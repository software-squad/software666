import pymysql

from fastapi import status

from util import database

datalist = "NOTICES"


def getall():
    """获取 NOTICES 中所有行的数据"""
    db, cursor = database.connect_to_database()
    sql = "SELECT * FROM %s" % (datalist)  # 选取所有数据的数据库语句
    status_code = status.HTTP_200_OK
    try:
        cursor.execute(sql)  # 执行数据库语句
        results = cursor.fetchall()  # 获取所有数据
    except pymysql.Error:
        status_code = status.HTTP_400_BAD_REQUEST
        results = None  # 如果语句执行失败，则返回失败状态码和None
        db.rollback()
    db.close()
    return status_code, results  # 返回状态码和数据


def getnews():
    """寻找 NOTICES 数据库中最新修改的两条公告"""
    db, cursor = database.connect_to_database()
    sql = "SELECT * FROM %s ORDER BY EDITDATE DESC LIMIT 2" % (datalist)  # 选取修改时间最新的两条数据
    status_code = status.HTTP_200_OK
    try:
        cursor.execute(sql)  # 执行数据库语句
        results = cursor.fetchall()  # 获取所有数据
    except pymysql.Error:
        status_code = status.HTTP_400_BAD_REQUEST
        results = None  # 如果语句执行失败，则返回失败状态码和None
        db.rollback()
    db.close()
    return status_code, results  # 返回状态码和数据


def select(index, value):
    """选取 NOTICES 中 index = value 的行"""
    db, cursor = database.connect_to_database()
    sql = "SELECT * FROM %s WHERE %s = '%s'" % (datalist, index, value)
    status_code = status.HTTP_200_OK
    try:
        cursor.execute(sql)  # 执行数据库语句
        results = cursor.fetchall()  # 获取所有数据
    except pymysql.Error:
        status_code = status.HTTP_400_BAD_REQUEST
        results = None  # 如果语句执行失败，则返回失败状态码和None
        db.rollback()
    db.close()
    return status_code, results  # 返回状态码和数据


def insert(item):
    """在 NOTICES 中增加一行 item"""
    db, cursor = database.connect_to_database()
    sql = "INSERT INTO %s(TITLE,CONTENT,USERID,USERNAME) \
                VALUES('%s','%s','%d','%s')" % (  # 插入相关数据的数据库语句
                        datalist, item.title, item.content,
                        item.userid, item.username)
    status_code = status.HTTP_200_OK
    try:
        cursor.execute(sql)  # 执行数据库语句
        db.commit()
    except pymysql.Error:
        status_code = status.HTTP_400_BAD_REQUEST  # 如果语句执行失败，则返回失败状态码
        db.rollback()
    db.close()
    return status_code


def delete(index, value):
    """删除 NOTICES 中 index = value 的行"""
    db, cursor = database.connect_to_database()
    sql = "DELETE FROM %s WHERE %s = '%s'" % (datalist, index, value)
    status_code = status.HTTP_200_OK
    try:
        cursor.execute(sql)  # 执行数据库语句
        db.commit()
    except pymysql.Error:
        status_code = status.HTTP_400_BAD_REQUEST  # 如果语句执行失败，则返回失败状态码
        db.rollback()
    db.close()
    return status_code


def edit(index, value, edit_index: list, edit_value: list):
    """对 index = value 的行，将索引列表 edit_index 中索引对应值改为 edit_value"""
    db, cursor = database.connect_to_database()
    sql = "UPDATE %s SET %s = '%s'" % (datalist, edit_index[0], edit_value[0])  # 更新数据的数据库语句
    if len(edit_index) > 1:  # 由于edit_index传入的是列表，故需要判断在索引数大于1时，继续扩展语句
        for key, val in zip(edit_index[1:], edit_value[1:]):
            sql += ", %s = '%s'" % (key, val)
    sql += " WHERE %s = '%s'" % (index, value)
    status_code = status.HTTP_200_OK
    try:
        cursor.execute(sql)  # 执行数据库语句，将索引对应行数据修改
        db.commit()
    except pymysql.Error:
        status_code = status.HTTP_400_BAD_REQUEST  # 如果语句执行失败，则返回失败状态码
        db.rollback()
    db.close()
    return status_code
