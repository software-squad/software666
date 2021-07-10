from dao import documentDao

# DONE
def showFilesServie():
    data = dict()
    isOperaSuccess = True
    data, isOperaSuccess = documentDao.selectAllFiles()
    filesResult = {"filesList": data}
    return filesResult, isOperaSuccess


# DONE
def editFileService(file):
    isOperaSuccess = documentDao.edit(file)
    return isOperaSuccess

# DONE
def delFileService(file):
    isOperaSuccess = documentDao.delete(file)
    return isOperaSuccess


def uploadFile(file):
    result = True
    return result


def downloadFile():
    result = True
    return result
