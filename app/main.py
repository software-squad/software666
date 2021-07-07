import uvicorn
from fastapi import FastAPI
from api import user
from api import item
from starlette.middleware.cors import CORSMiddleware
from fastapi.encoders import jsonable_encoder
from fastapi.responses import JSONResponse

app = FastAPI()

#配置跨域
origins = ["*"]
app.add_middleware(
    CORSMiddleware, 
    allow_origins=origins,  
    allow_credentials=True,
    allow_methods=["*"], 
    allow_headers=["*"]
    )  

# 注册api路由
app.include_router(user.router,prefix="/api")
app.include_router(item.router,prefix="/api")


if __name__ == '__main__':
    uvicorn.run("main:app", reload=True, host='localhost', port=8082)

    
   