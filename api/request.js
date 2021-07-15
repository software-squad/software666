import axios from "axios";

//创建axios对象，赋给变量service，service为封装后对象

import util from "./util.js"

const service = axios.create({
	baseURL: util.requestBaseUrl,
	timeout: 15000, //超时时间，最好设大一点，不然请求接口时间如果超过超时时间就会无法返回
	headers: {
		//自定义请求头
	},
});

//=================统一请求拦截器================

// 在这里拦截前端请求，添加token到请求头里
service.interceptors.request.use(
	function(config) {
		let token = null
		if (config.url.indexOf('login') < 0) { // 非登录请求
			token = uni.getStorageSync('token')
			if (!token) {
				uni.showToast({
					title: '您尚未登录',
					icon: 'none',
					duration: 4000
				});
				uni.redirectTo({
					url: '/pages/login/login',
				})
				return;
			}
		}
		//后台需要前端这边传相关的参数（在请求头添加参数）
		//向请求头添加参数： config.headers['token']='xxx'
		config.headers.token = uni.getStorageSync("token");
		// console.log(config.headers.token);
		return config;
	},
	function(error) {
		// 对请求错误拒绝响应
		return Promise.reject(error);
	}
);


//=================异常码统一拦截处理部分===============

//定义指向当前页面的指针pointer
let pointer = null;

//获取指向当前页面的指针，并初始化pointer
export function sendThis(_this) {
	pointer = _this
}

//=================统一响应拦截器================

service.interceptors.response.use(
	function(response) {
		let data = response.data;
		if (data.code == 500) {
			pointer.showToast('服务器异常', 'false')
			return Promise.reject(data)
		} else if (data.code == 422) {
			pointer.showToast('访问数据格式错误', 'none')
			return Promise.reject(data)
		} else if (data.code == 403) {
			pointer.showToast('登录已过期', 'none')
			return Promise.reject(data)
		} else if (data.code == 404) {
			pointer.showToast('很抱歉，资源未找到!', 'none')
			return Promise.reject(data)
		} else if (data.code == 404) {
			pointer.showToast('传输方法错误', 'none')
			return Promise.reject(data)
		} else if (data.code == 504) {
			pointer.showToast('网络超时', 'none')
			return Promise.reject(data)
		} else if (data.code == 401) {
			pointer.showToast('未授权，请重新登录', 'none')
			return Promise.reject(data)
		}
		//检验返回码是否为200，若不是200，视作服务器未响应成功，拒绝进入相应回调函数
		else if (data.code != 200) {
			return Promise.reject(data);
		} else if (data.msg != 10013) { //若返回信息为100013，即为数据重复，拒绝进入回调函数，不进行相应跳转
			// 对响应数据判断返回信息，统一处理不同弹窗
			switch (data.msg) {
				case 10001:
					pointer.showToast('增加成功', 'success')
					break;
				case 10002:
					pointer.showToast('增加失败', 'error')
					break;
				case 10003:
					pointer.showToast('删除成功', 'success')
					break;
				case 10004:
					pointer.showToast('删除失败', 'error')
					break;
				case 10005:
					pointer.showToast('更新成功', 'success')
					break;
				case 10006:
					pointer.showToast('更新失败', 'error')
					break;
				case 10007:
					break;
				case 10008:
					pointer.showToast('查询失败', 'error')
					break;
				case 10010:
					pointer.showToast('登录成功', 'success')
					break;
				case 10011:
					pointer.showToast('数据不存在', 'error')
					break;
				case 10012:
					pointer.showToast('密码不正确', 'error')
					break;
				default:
					pointer.showToast('未知错误', 'error')
			}
			return response;
		} else {
			pointer.showToast('数据重复', 'error')
			return Promise.reject(data);
		}
	},
	function(error) {
		// 对响应错误拒绝进入回调函数
		return Promise.reject(error);
	}
);

export default service
