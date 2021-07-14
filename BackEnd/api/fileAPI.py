from fastapi import APIRouter, UploadFile, File, Form, status

from util import response_code, msg_code

from service import fileService

from model import file_inf

from starlette.responses import FileResponse

# 构建api路由
router = APIRouter()


@router.get("/showmany", tags=["file"])
async def showFiles():
    """展示大量文件"""
    status_code, files, msg_code = fileService.showFiles()
    return response_code.response(status_code, msg_code, files)


@router.post("/edit", tags=["file"])
async def editFile(file: file_inf.FileInf):
    """修改文件"""
    status_code, msg_code = fileService.editFile(file)
    return response_code.response(status_code, msg_code)


@router.get("/del", tags=["file"])
async def delFile(fileid: int):
    """删除文件"""
    status_code, msg_code = fileService.delFile(fileid)
    return response_code.response(status_code, msg_code)


@router.post("/upload", tags=["file"])
async def uploadFile(file: UploadFile = File(...), fileMsg: str = Form(...)):
    """上传文件"""
    fileMsg = eval(fileMsg)  # 直接传JSON会报错，故采取传str然后转JSON的方式
    contents = await file.read()
    with open("C:/file/%s" % (file.filename), 'wb') as f:
        f.write(contents)
    status_code, msg_code = fileService.uploadFile(fileMsg, file)
    return response_code.response(status_code, msg_code)


@router.get("/download", tags=["file"])
async def downloadFile(fileid):
    """下载文件"""
    status_code, file_path, msg_code1 = fileService.downloadFile(fileid)
    if status_code == status.HTTP_200_OK and \
       msg_code1 == msg_code.SEARCH_SUCCESS:
        return FileResponse(file_path,
                            filename=file_path[file_path.rindex('/') + 1:])
    else:
        return response_code.response(status_code, msg_code1)
