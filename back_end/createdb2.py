import pymysql

db = pymysql.connect(host="192.168.1.16", user="root", passwd="123456", database="software666666")
cursor = db.cursor()
cursor.execute("SELECT VERSION()")
data = cursor.fetchone()
print ("Database version : %s " % data)

# 建部门表
sql_buildDept = """CREATE TABLE `departments` (
  `deptid` int(10) unsigned NOT NULL AUTO_INCREMENT,
  `deptname` varchar(50) NOT NULL,
  `depturl` varchar(200) ,
  `remark` varchar(500) NOT NULL,
  PRIMARY KEY (`deptid`)
) ENGINE=InnoDB AUTO_INCREMENT=6 DEFAULT CHARSET=utf8;"""

sql_buildZhiwei = """CREATE TABLE `jobs` (
  `jobid` int(10) unsigned NOT NULL AUTO_INCREMENT,
  `jobname` varchar(50) NOT NULL,
  `remark` varchar(500) NOT NULL,
  `deptid` int(10) unsigned DEFAULT NULL,
  PRIMARY KEY (`jobid`),
  CONSTRAINT `fk_job_deptid` FOREIGN KEY (`deptid`) REFERENCES `departments` (`deptid`)
) ENGINE=InnoDB AUTO_INCREMENT=3 DEFAULT CHARSET=utf8;"""

sql_buildStaff = """CREATE TABLE `staffs` (
  `userid` int(10) unsigned NOT NULL AUTO_INCREMENT,
  `username` varchar(50) NOT NULL,
  `cardid` varchar(50) DEFAULT NULL,
  `sex` varchar(10) NOT NULL,
  `jobid` int(10) unsigned NOT NULL,
  `education` varchar(10) DEFAULT NULL,
  `email` varchar(50) DEFAULT NULL,
  `deptid` int(10) unsigned NOT NULL,
  `tel` varchar(16) NOT NULL,
  `party` varchar(10) DEFAULT NULL,
  `qqnum` varchar(50) DEFAULT NULL,
  `address` varchar(50) DEFAULT NULL,
  `postcode` varchar(50) DEFAULT NULL,
  `birthday` varchar(50) DEFAULT NULL,
  `loginname` varchar(50) NOT NULL,
  `password` varchar(50) NOT NULL,
  `status` int(10) unsigned NOT NULL,
  `createdate` timestamp NULL DEFAULT CURRENT_TIMESTAMP,
  `faceurl` varchar(255) DEFAULT NULL,
  `facepath` varchar(255) DEFAULT NULL,
  `deptname` varchar(50) NOT NULL,
  `jobname` varchar(50) NOT NULL,
  `remark` varchar(200) DEFAULT NULL,
  PRIMARY KEY (`userid`),
  CONSTRAINT `fk_staff_deptid` FOREIGN KEY (`deptid`) REFERENCES `departments` (`deptid`),
  CONSTRAINT `fk_staff_jobid` FOREIGN KEY (`jobid`) REFERENCES `jobs` (`jobid`)
) ENGINE=InnoDB AUTO_INCREMENT=5 DEFAULT CHARSET=utf8;"""

sql_buildNotice = """CREATE TABLE `notices` (
  `noticeid` int(10) unsigned NOT NULL AUTO_INCREMENT,
  `title` varchar(50) NOT NULL,
  `content` varchar(100) DEFAULT NULL,
  `createdate` timestamp NULL DEFAULT CURRENT_TIMESTAMP,
  `editdate` timestamp NULL DEFAULT current_timestamp() ON UPDATE CURRENT_TIMESTAMP,
  `userid` int(10) unsigned NOT NULL,
  `username` varchar(50) NOT NULL,
  PRIMARY KEY (`noticeid`)
) ENGINE=InnoDB AUTO_INCREMENT=2 DEFAULT CHARSET=utf8;"""

sql_buildFile = """CREATE TABLE `documents` (
  `fileid` int(10) unsigned NOT NULL AUTO_INCREMENT,
  `title` varchar(50) NOT NULL,
  `filename` varchar(50) NOT NULL,
  `remark` varchar(100) DEFAULT NULL,
  `createdate` timestamp NULL DEFAULT CURRENT_TIMESTAMP,
  `username` varchar(50) NOT NULL,
  `filepath` varchar(255) DEFAULT NULL,
  PRIMARY KEY (`fileid`)
) ENGINE=InnoDB AUTO_INCREMENT=3 DEFAULT CHARSET=utf8;"""

# cursor.execute(sql_buildDept)

# cursor.execute(sql_buildZhiwei)
cursor.execute(sql_buildStaff)
# cursor.execute(sql_buildFile)
# cursor.execute(sql_buildNotice)

#删表：
sql_del_tb_departments = """DROP TABLE departments ;"""
sql_del_tb_jobs = """DROP TABLE jobs ;"""
sql_del_tb_notice = """DROP TABLE notices ;"""
sql_del_tb_documents = """DROP TABLE documents ;"""
# cursor.execute(sql_del_tb_documents)

#插入数据
sql_insert_dept = """INSERT INTO departments(
         deptname, remark)
         VALUES ('技术部', '技术部技术部')"""

sql_insert_job = """INSERT INTO jobs(
         jobname, remark, deptid)
         VALUES ('干饭工程师', '主职干饭，副职摸鱼', 2)"""

sql_insert_staff = """INSERT INTO staffs(
         username
, cardid
, sex
, jobid
, jobname
, education
, email
, deptid
, deptname
, tel
, party
, qqnum
, address
, postcode
, birthday
, loginname
, password
, status)
         VALUES ('李华', '44990473907', '男', 1, '项目经理' '本科', '1234567890@**.com', 1, '技术部', '1234567890', '共青团员', '12345678', '重庆市', '2000', '20000-12-20', '小华', '123456', 1)"""

sql_insert_notice = """INSERT INTO notices(
         title
, content
, userid
, username)
         VALUES ('放假通知', '从即日起，公司全员带薪休假', 1, 'string')"""

sql_insert_document = """INSERT INTO documents(
         title
, filename
, createdate
, username
, filepath)
         VALUES ('更新2：《干饭：从入职到加薪》', '《干饭：从入职到加薪》', '2021-07-09', '小明', 'C:/公司资料')"""

sql_insert_document2 = """INSERT INTO documents(title,
                            filename,
                            remark,
                            createdate,
                            username,
                            filepath)
                                    VALUES('测试', '《mips1.asm》', 'string', 'string', 'string', 'D:/file/');"""

# 更加属性
sql_add_shuxing = """ALTER TABLE departments ADD depturl VARCHAR(200) AFTER remark; """
sql_add_shuxing2 = """ALTER TABLE notices ADD editdate timestamp NULL DEFAULT current_timestamp() ON UPDATE CURRENT_TIMESTAMP AFTER createdate; """

# 更改列名
sql_edit_lieming = """ALTER TABLE staffs CHANGE jobtname jobname VARCHAR(50);"""

# ALTER  TABLE 表名 CHANGE [column] 旧字段名 新字段名 新数据类型;	
# sql_edit_lieshuxing = """ALTER  TABLE staffs CHANGE createdate createdate timestamp NULL DEFAULT current_timestamp();	"""
# try:
#    # 执行sql语句
#    cursor.execute(sql_add_shuxing2)
#    # 提交到数据库执行
#    db.commit()
# except pymysql.Error as e:
#    # 如果发生错误则回滚
#    db.rollback()
#    print(e)

db.close()