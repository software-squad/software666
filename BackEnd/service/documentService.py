from dao import documentDao


# DONE 高明
def showFilesServie():
    data = dict()
    isOperaSuccess = True
    data, isOperaSuccess = documentDao.selectAllFiles()
    filesResult = {"filesList": data}
    return filesResult, isOperaSuccess


# DONE 高明
def editFileService(file):
    isOperaSuccess = documentDao.edit(file)
    return isOperaSuccess


# DONE 高明
def delFileService(file):
    isOperaSuccess = documentDao.delete(file)
    return isOperaSuccess


# def uploadFile(file):
#     result = True
#     return result


# def downloadFile():
#     result = True
#     return result
