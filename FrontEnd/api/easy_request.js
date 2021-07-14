const request = (config) => {
		// 处理 apiUrl  
		// config.url = '127.0.0.1/api' + config.url;  // => 已经进行跨域处理
		// console.log('封装请求中')
		if(!config.url.indexOf('login')>=0){  // 非登录请求
			// console.log('设置请求头')
			// console.log(uni.getStorageSync('token'))
			// console.log('请求头已找到')
			// console.log(config)
			config.header = {
				'token':sessionStorage.getItem('token')
			}
			// console.log('请求头已设置')
			// config.header.content-type = 'application/x-www-form-urlencoded'
		}
		if (!config.data) {
			config.data = {};
		}
		// console.log(JSON.stringify(config.data));
		let promise = new Promise(function(resolve, reject) {
				// console.log('异步请求中')
				console.log(config)
				uni.request({
					...config,
					success: (response) => {
						// console.log('已经响应')
						console.log('服务器响应结果',response)
						if(response.statusCode==200){
							resolve(response);
						}else{
							reject(response)
						}
					},
					fail: (error) => {
						// console.log('响应错误')
						console.log("服务器请求失败",error)
						reject(error);
					}
				})
			})
			return promise;
		};
export default {
	request:request
};
