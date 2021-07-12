import uvicorn
from fastapi import FastAPI, Request, status
from api import login
from api import menu
from api import user
from api import staff
from api import dept
from api import job
from api import notice
from api import document
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
app.include_router(login.router, prefix="/api")
app.include_router(menu.router, prefix="/api/menu")
app.include_router(user.router, prefix="/api/user")
app.include_router(staff.router, prefix="/api/staff")
app.include_router(dept.router, prefix="/api/dept")
app.include_router(job.router, prefix="/api/job")
app.include_router(notice.router, prefix="/api/notice")
app.include_router(document.router, prefix="/api/file")


@app.middleware('http')
async def add_process_time_header(request: Request, call_next):
    response = await call_next(request)
    url = str(request.url)
    try:
        last = url[url.rindex('/') + 1:]
        print(last)
        if last != 'login' and last != 'docs' and last != 'openapi.json':
            if 'token' not in request.headers.keys() or \
               jwt_decode.jwtEncode(request.headers['token']) is None:
                return response_code.response(status.HTTP_401_UNAUTHORIZED,
                                              'not allowed')
    except Exception:
        return response_code.response(status.HTTP_401_UNAUTHORIZED,
                                      'not allowed')
    return response

if __name__ == '__main__':
    uvicorn.run("main:app", reload=False, host='192.168.0.106', port=8082)
