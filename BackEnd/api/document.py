from fastapi import APIRouter

from util import response_code

from service import documentService

from model import document_inf

# 构建api路由
router = APIRouter()


@router.post("/showmany", tags=["document"])
async def showFiles(file: document_inf.document_inf):
    # 展示大量文件
    result = documentService.showFiles(file)
    return response_code.response(result)


@router.post("/edit", tags=["document"])
async def editFile(file: document_inf.document_inf):
    # 修改文件
    result = documentService.editFile(file)
    return response_code.response(result)


@router.post("/del", tags=["document"])
async def delFile(file: document_inf.document_inf):
    # 删除文件
    result = documentService.delFile(file)
    return response_code.response(result)


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
