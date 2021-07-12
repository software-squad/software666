// import axios from "axios";

// //创建axios，赋给变量service
// const BASEURL = process.env.NODE_ENV === "production" ? "" : "/";
// const service = axios.create({
//     baseURL: BASEURL, //http://localhost:8080/devApi =='http://www.web-jshtml.cn/productapi'
//     timeout: 15000, //超时时间，最好设大一点，不然请求接口时间如果超过超时时间就会无法返回
//     headers: {
//         "X-Custom-Header": "foobar",
//     },
// });

// // 在这里拦截前端请求，添加token到请求头里
// service.interceptors.request.use(
//     function (config) {
//         // 在发送请求之前做些什么
//         //后台需要前端这边传相关的参数（在请求头添加参数）
//         //Token userId sui
//         //业务需求
//         //向请求头添加参数： config.headers['userId']='xxx'
//         //为请求头对象，添加token验证的Authorization字段
//         config.headers.token = window.sessionStorage.getItem("token");
//         // config.headers.username = window.sessionStorage.getItem("username");
//         return config;
//     },
//     function (error) {
//         // 对请求错误做些什么
//         return Promise.reject(error);
//     }
// );

// // 添加响应拦截器,请求接口，返回数据进行拦截
// service.interceptors.response.use(
//     function (response) {
//         let data = response.data;
// 		// 在这里拦截后端发回的数据（响应response） 如果是200 才执行回调函数
//         if (data.code != 200) {
//             return Promise.reject(data);
//         } else { // 对响应数据做点什么
//             return response;
//         }
//     },
//     function (error) {
//         // 对响应错误做点什么
//         return Promise.reject(error);
//     }
// );

// export default service;

// uni.setStorageSync('token') = "eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJpYXQiOjE2MjYwNjQyMDMuNDI1Mjg3NywibmFtZSI6InN1cGVybWFuIn0.cvNLYSAhGBP3RLQkV4359GhRGoUgwMwCBTOH1q5v77w";

const request = (config) => {
		// 处理 apiUrl  
		// config.url = '127.0.0.1/api' + config.url;  // => 已经进行跨域处理
		console.log('封装请求中')
		// if(!config.url.indexOf('login')>=0){  // 非登录请求
		// 	console.log('设置请求头')
		// 	console.log(uni.getStorageSync('token'))
		// 	console.log('请求头已找到')
		// 	console.log(config)
		// 	config.header = {
		// 		'token':uni.getStorageSync('token')
		// 	}
		// 	console.log('请求头已设置')
		// 	// config.header.content-type = 'application/x-www-form-urlencoded'
		// }
		if (!config.data) {
			config.data = {};
		}
		// console.log(JSON.stringify(config.data));
		let promise = new Promise(function(resolve, reject) {
				console.log('异步请求中')
				console.log(config)
				uni.request({
					...config,
					success: (response) => {
						console.log('已经响应')
						console.log(response)
						resolve(response);
						// if (responses[0]) {
						// 	reject({
						// 		message: "网络超时"
						// 	});
						// } else {
						// 	let response = responses[1].data; // 如果返回的结果是data.data的，嫌麻烦可以用这个，return res,这样只返回一个data
							
						// }
					},
					fail: (error) => {
						console.log('响应错误')
						console.log(error)
						reject(error);
					}
				})
			})
			return promise;
		};
		export default request;
