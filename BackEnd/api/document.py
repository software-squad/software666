from fastapi import APIRouter

from util import response_code, msg_code

from service import documentService

from model import document_inf

# 构建api路由
router = APIRouter()


# DONE
@router.get("/showmany", tags=["document"])
async def showFiles():
    # 展示大量文件
    data, isOperaSuccess = documentService.showFilesServie()
    if isOperaSuccess:
        return response_code.showResponse(data, msg_code.SEARCH_SUCCESS)
    else:
        return response_code.showResponseFail(data, msg_code.SEARCH_FAILURE)


# DONE
@router.post("/edit", tags=["document"])
async def editFile(file: document_inf.document_inf):
    # 修改文件
    isOperaSuccess = documentService.editFileService(file)
    if isOperaSuccess:
        return response_code.showResponse(None, msg_code.UPD_SUCCESS)
    else:
        return response_code.showResponseFail(None, msg_code.UPD_FAILURE)


# DONE
@router.post("/del", tags=["document"])
async def delFile(file: document_inf.DelDocumentInf):
    # 删除文件
    isOperaSuccess = documentService.delFileService(file)
    if isOperaSuccess:
        return response_code.showResponse(None, msg_code.DEL_SUCCESS)
    else:
        return response_code.showResponseFail(None, msg_code.DEL_FAILURE)


@router.post("/upload", tags=["document"])
async def uploadFile(file: document_inf.document_inf):
    # 上传文件
    result = documentService.uploadFile(file)
    return response_code.response(result)


@router.post("/download", tags=["document"])
async def downloadFile(file: document_inf.document_inf):
    # 下载文件
    result = documentService.downloadFile(file)
    return response_code.response(result)
