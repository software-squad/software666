import axios from "axios";
let vm = null;

export function sendThis(_this){
	vm = _this
}

//创建axios，赋给变量service
const BASEURL = process.env.NODE_ENV === "production" ? "" : "/";
const service = axios.create({
    baseURL: 'http://192.168.0.117:8082/', //http://localhost:8080/devApi =='http://www.web-jshtml.cn/productapi'
    timeout: 15000, //超时时间，最好设大一点，不然请求接口时间如果超过超时时间就会无法返回
    headers: {
        "X-Custom-Header": "foobar",
    },
});

// 在这里拦截前端请求，添加token到请求头里
service.interceptors.request.use(
    function (config) {
        // 在发送请求之前做些什么
        //后台需要前端这边传相关的参数（在请求头添加参数）
        //Token userId sui
        //业务需求
        //向请求头添加参数： config.headers['userId']='xxx'
        //为请求头对象，添加token验证的Authorization字段
        config.headers.token = sessionStorage.getItem("token");
		// console.log(config.headers.token);
        return config;
    },
    function (error) {
        // 对请求错误做些什么
        return Promise.reject(error);
    }
);

service.interceptors.response.use(
    function (response) {
        let data = response.data;

        if (data.code != 200) {
            return Promise.reject(data);
        } else if(data.msg != 10013){ // 对响应数据做点什么
			switch (data.msg) {
				case 10001 :
					vm.showToast('增加成功','success')
					break;
				case 10002 :
					vm.showToast('增加失败','error')
					break;
				case 10003 :
					vm.showToast('删除成功','success')
					break;
				case 10004 :
					vm.showToast('删除失败','error')
					break;
				case 10005 :
					vm.showToast('更新成功','success')
					break;
				case 10006 :
					vm.showToast('更新失败','error')
					break;
				case 10007 :
					break;
				case 10008 :
					vm.showToast('查询失败','error')
					break;
				case 10010 :
					vm.showToast('登录成功','success')
					break;
				case 10011 :
					vm.showToast('数据不存在','error')
					break;
				case 10012 :
					vm.showToast('密码不正确','error')
					break;
				default :
					vm.showToast('未知错误','error')
				}
				return response;
			}else{
				vm.showToast('数据重复','error')
				return Promise.reject(data);
			}


    },
    function (error) {
        // 对响应错误做点什么
        return Promise.reject(error);
    }
);



export default service

