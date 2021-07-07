from  dao  import userDao




def validataUser(item_id):
    # XXX 打印
    print("开始验证数据")
    # 调用dao层  从数据库获取的数据封装到对象中。所以可能会涉及到在model中构建模型 
    res = userDao.selUserById(item_id)
    return res
    