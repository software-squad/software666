import pymysql

from fastapi import status

from util import database

datalist = "STAFFS"


def select(index, value):
    """选取 STAFFS 中 index = value 的行"""
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


def select_like(index, value):
    """选取 STAFFS 中 index = value 的行(不同于select，这是模糊搜索)"""
    db, cursor = database.connect_to_database()
    sql = "SELECT * FROM %s WHERE %s LIKE '%%%s%%'" % (datalist, index, value)  # 选取一些数据的数据库语句
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


def select_by_2(index1, value1, index2, value2):
    """选取 STAFFS 中 index1 = value1, index2 = value2 的行"""
    db, cursor = database.connect_to_database()
    sql = "SELECT * FROM %s WHERE %s = '%s' AND %s = '%s'" % (  # 选取某行数据的数据库语句
                    datalist, index1, value1, index2, value2)
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
    """在 STAFFS 中增加一行 item (即员工信息)"""
    db, cursor = database.connect_to_database()
    sql = """INSERT INTO %s VALUES(DEFAULT,'%s','%s','%s','%s','%s','%s','%s',
             '%s','%s','%s','%s','%s','%s','%s','%s','%s',DEFAULT,'%s',DEFAULT,
             '%s','%s','%s')""" % (  # 插入相关数据的数据库语句
                datalist, item.username, item.cardid, item.sex, item.jobid,
                item.education, item.email, item.deptid, item.tel, item.party,
                item.qqnum, item.address, item.postcode, item.birthday,
                item.loginname, item.password, item.status, item.faceurl,
                item.deptname, item.jobname, item.remark)
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
    """删除 STAFFS 中 index = value 的行"""
    db, cursor = database.connect_to_database()
    sql = "DELETE FROM %s WHERE %s = '%s'" % (datalist, index, value)  # 删除某行数据的数据库语句
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
