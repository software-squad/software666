import axios from "axios";

//创建axios，赋给变量service
const BASEURL = process.env.NODE_ENV === "production" ? "" : "/";
const service = axios.create({
    baseURL: 'http://4097n16y34.zicp.vip/', //http://localhost:8080/devApi =='http://www.web-jshtml.cn/productapi'
    timeout: 15000, //超时时间，最好设大一点，不然请求接口时间如果超过超时时间就会无法返回
    headers: {
        "X-Custom-Header": "foobar",
    },
});

// 在这里拦截前端请求，添加token到请求头里
service.interceptors.request.use(
	
    function (config) {
		// console.log(config)
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

// 添加响应拦截器,请求接口，返回数据进行拦截
service.interceptors.response.use(
    function (response) {
        let data = response.data;
		// 在这里拦截后端发回的数据（响应response） 如果是200 才执行回调函数
        if (data.code != 200) {
            return Promise.reject(data);
        } else { // 对响应数据做点什么
            return response;
        }
    },
    function (error) {
        // 对响应错误做点什么
        return Promise.reject(error);
    }
);

export default service;

