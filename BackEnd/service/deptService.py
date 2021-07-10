from dao import deptDao

# DONE
def showAllDepartmentService():
    # 实现展示所有部门的业务逻辑
    depts, isSuccess = deptDao.selectAllDept()
    deptsResult = {"deptsList": depts}
    print(deptsResult)
    return deptsResult, isSuccess

def searchDepartment(dept):
    result = True
    return result


# DONE
def addDepartmentService(dept):
    # 实现添加部门的业务逻辑
    isSuccess = deptDao.insert(dept)
    return isSuccess


def showDepartment(dept):
    result = True
    return result

# DONE
def editDepartmentService(dept):
    # 实现添加部门的业务逻辑
    isRepeat = False
    isOperaSuccess = True
    deptid, isOperaSuccess = deptDao.selectIdByName(dept.deptname)
    if isOperaSuccess:
        if not deptid or (deptid[0]['deptid']==dept.deptid):
            isRepeat = False
            isOperaSuccess = deptDao.edit(dept)
            return isRepeat, isOperaSuccess
        else:
            isRepeat = True
            return isRepeat, isOperaSuccess
    else:
        return isRepeat, isOperaSuccess
    

# DONE
def delDepartmentService(dept):
    isOperaSuccess = deptDao.delete(dept)
    return isOperaSuccess
