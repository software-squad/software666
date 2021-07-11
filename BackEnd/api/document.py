from fastapi import APIRouter, UploadFile, File, Form

from util import response_code

from service import documentService

from model import document_inf

# 构建api路由
router = APIRouter()


@router.get("/showmany", tags=["document"])
async def showFiles():
    # 展示大量文件
    status_code, files, msg_code = documentService.showFiles()
    return response_code.response(status_code, msg_code, files)


@router.post("/edit", tags=["document"])
async def editFile(file: document_inf.DocumentInf):
    # 修改文件
    status_code, msg_code = documentService.editFile(file)
    return response_code.response(status_code, msg_code)


@router.get("/del", tags=["document"])
async def delFile(fileid: int):
    # 删除文件
    status_code, msg_code = documentService.delFile(fileid)
    return response_code.response(status_code, msg_code)


@router.post("/upload", tags=["document"])
async def uploadFile(file: UploadFile = File(...), fileMsg: str = Form(...)):
    # 上传文件
    fileMsgJson = '{%s}' % (fileMsg)
    fileMsg = eval(fileMsgJson)
    contents = await file.read()
    with open("./file/%s" % (file.filename), 'wb') as f:
        f.write(contents)
    status_code, msg_code = documentService.uploadFile(fileMsg, file)
    return response_code.response(status_code, msg_code)