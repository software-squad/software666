import uvicorn
from fastapi import FastAPI, Request, status
from api import loginAPI
from api import menuAPI
from api import userAPI
from api import staffAPI
from api import deptAPI
from api import jobAPI
from api import noticeAPI
from api import fileAPI
from starlette.middleware.cors import CORSMiddleware
from util import jwt_decode, response_code

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
app.include_router(loginAPI.router, prefix="/api")
app.include_router(menuAPI.router, prefix="/api/menu")
app.include_router(userAPI.router, prefix="/api/user")
app.include_router(staffAPI.router, prefix="/api/staff")
app.include_router(deptAPI.router, prefix="/api/dept")
app.include_router(jobAPI.router, prefix="/api/job")
app.include_router(noticeAPI.router, prefix="/api/notice")
app.include_router(fileAPI.router, prefix="/api/file")


# 可接受请求，url最后部分位于如下列表中，则请求直接执行。
accept = ['login', 'facelogin', 'docs', 'openapi.json',
          'facelogin', 'download']


@app.middleware('http')
async def add_process_time_header(request: Request, call_next):
    """中间件，用于执行其他请求前获取请求信息，判断请求是否可接受"""
    url = str(request.url)
    try:
        last = url[url.rindex('/') + 1:]  # 截取url中最后部分，如login等。
        if last not in accept and request.method != 'OPTIONS':  # 请求是否可执行判断
            if 'token' not in request.headers.keys() or \
               jwt_decode.jwtEncode(request.headers['token']) is None:
                return response_code.response(status.HTTP_401_UNAUTHORIZED,
                                              'not allowed')  # 不可判断则返回401码
    except Exception:
        return response_code.response(status.HTTP_401_UNAUTHORIZED,
                                      'not allowed')  # 发生异常则返回401码
    response = await call_next(request)  # 若请求可接受，则执行请求。
    return response


if __name__ == '__main__':
    uvicorn.run("main:app", reload=True, host='192.168.0.101', port=8082)
