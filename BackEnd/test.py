import uvicorn
from fastapi import FastAPI
from starlette.middleware.cors import CORSMiddleware
from fastapi.encoders import jsonable_encoder
from fastapi.responses import JSONResponse
from model import dept_inf

from service import deptService

from api import dept

if __name__ == '__main__':
    # deptService.addDepartment(dept_inf.AddDeptInf(deptname = "人事部",remark = "里面全是人才"))
    # deptService.editDepartmentService(dept_inf.DeptInf(deptid = 2, deptname = "人事部", remark = "更改1：里面全是人才"))
    deptService.delDepartmentService(dept_inf.DelDeptInf(deptid = 4))