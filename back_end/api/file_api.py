import datetime

from fastapi import APIRouter, UploadFile, File, Form, status
from starlette.responses import FileResponse

from util import message
from util.response import response
from service import file_service
from model import file_inf


# 构建api路由
router = APIRouter()


@router.get("/showFiles", tags=["file"])
async def show_files():
    """展示文件"""
    status_code, files, msg_code = file_service.get_files()
    return response(status_code, msg_code, files)


@router.post("/upload", tags=["file"])
async def upload_file(file: UploadFile = File(...), filemsg: str = Form(...)):
    """上传文件"""
    filemsg = eval(filemsg)  # 直接传JSON会报错，故采取传str然后转JSON的方式
    contents = await file.read()  # 直接在api层完成一部分业务逻辑，因为发现service中操作会出错，原因不明
    curr_time = datetime.datetime.strftime(datetime.datetime.now(),
                                           '%Y%m%d%H%M%S')
    filemsg['filename'] = curr_time + file.filename  # 完善filemsg的信息
    filemsg['filepath'] = 'C:/file/'  # 完善filemsg的信息
    with open("C:/file/%s" % filemsg['filename'], 'wb') as f:
        f.write(contents)  # 在固定地址写入文件
    status_code, msg_code = file_service.upload_file(filemsg)
    return response(status_code, msg_code)


@router.get("/download", tags=["file"])
async def download_file(fileid):
    """下载文件"""
    status_code, file_path, msg_code = file_service.download_file(fileid)
    if status_code == status.HTTP_200_OK and \
       msg_code == message.SEARCH_SUCCESS:
        return FileResponse(file_path,  # 如果文件下载成功则返回FileResponse型数据
                            filename=file_path[file_path.rindex('/') + 1:])
    else:
        return response(status_code, msg_code)


@router.get("/del", tags=["file"])
async def del_file(fileid: int):
    """删除文件"""
    status_code, msg_code = file_service.del_file(fileid)
    return response(status_code, msg_code)


@router.post("/edit", tags=["file"])
async def edit_file(file: file_inf.FileInf):
    """修改文件"""
    status_code, msg_code = file_service.edit_file(file)
    return response(status_code, msg_code)
