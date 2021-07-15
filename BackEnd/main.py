import uvicorn
from fastapi import FastAPI, Request, status
from starlette.middleware.cors import CORSMiddleware

from api import menu_api
from api import user_api
from api import staff_api
from api import dept_api
from api import job_api
from api import notice_api
from api import file_api
from dao import staff_dao
from util import security, message
from util.response import response

app = FastAPI()

# 配置跨域
origins = ["*"]
app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"])

# 注册api路由
app.include_router(user_api.router, prefix="/api")
app.include_router(menu_api.router, prefix="/api/menu")
app.include_router(staff_api.router, prefix="/api/staff")
app.include_router(dept_api.router, prefix="/api/dept")
app.include_router(job_api.router, prefix="/api/job")
app.include_router(notice_api.router, prefix="/api/notice")
app.include_router(file_api.router, prefix="/api/file")


# 可接受请求的列表，若url中的最后部分位于如下列表中，则无需判断，请求直接执行
accept = ['login', 'facelogin', 'docs', 'openapi.json',
          'facelogin', 'download', 'upload']

# 拒绝的请求列表，如果请求来自普通员工，则拒绝请求
refuse = ['add', 'del', 'edit', 'upload']


@app.middleware('http')
async def request_judge(request: Request, call_next):
    """中间件，用于执行其他请求前获取请求信息，判断请求是否可接受"""
    url = str(request.url)
    flag = False
    for item in accept:
        if item in url:
            flag = True  # 如果url里含有可接受请求列表的元素，则请求直接可执行
            break
    if not flag and request.method != 'OPTIONS':  # 判断请求可否执行
        if 'token' not in request.headers.keys():
            return response(status.HTTP_401_UNAUTHORIZED,
                            'not allowed')  # 不可判断则返回401码
        payload = security.jwt_decode(request.headers['token'])
        if payload is None:
            return response(status.HTTP_401_UNAUTHORIZED,
                            'not allowed')  # 不可判断则返回401码
        userid = payload['userid']  # 取出userid
        status_code, result = staff_dao.select('USERID', userid)
        if status_code == status.HTTP_400_BAD_REQUEST:
            return response(status_code, 'error request')
        user_status = result[0]['status']  # 访问数据库得到用户权限
        flag = True
        for item in refuse:
            if item in url:  # 如果url里含有可拒绝请求列表的元素，则可能拒绝请求
                flag = False
                break
        if user_status == message.EMPLOYEE and not flag:  # 普通员工拒绝请求
            return response(status.HTTP_403_FORBIDDEN, message.NOT_ALLOWED)
    return await call_next(request)  # 若请求可接受，则执行请求


if __name__ == '__main__':
    uvicorn.run("main:app", reload=True, host='192.168.0.111', port=8082)
