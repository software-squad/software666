from dao import noticeDao


# XXX 还要增加管理员权限的判断
def showNotices():
    print("====展示多个公告信息====")
    info, res = noticeDao.selAllNotices()
    for item in info:
        item['createdate'] = str(item['createdate'])
        item['editdate'] = str(item['editdate'])
    return info, res


# def showOneNotice(notice):
#     result = True
#     return result


def editNotice(notice):
    print("====编辑单个公告信息====")
    res = noticeDao.editOneNotice(notice.noticeid, notice.title,
                                  notice.content, notice.userid,
                                  notice.username)
    # 返回是否能成功编辑
    return res


def delNotice(notice):
    print("====删除单个公告信息====")
    res = noticeDao.delOneNotice(notice.noticeid)
    return res


def addNotice(notice):
    print("====增加单个公告信息====")
    res = noticeDao.addOneNotice(notice.title, notice.content,
                                 notice.userid, notice.username)
    return res
