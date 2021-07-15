import util from "./util.js"

const request = (config) => {
	// 处理 apiUrl  
	config.url = util.easyRequestUrl + config.url; // => 已经进行跨域处理
	console.log('封装请求中', config.url)
	if (config.url.indexOf('login') < 0) { // 非登录请求
		console.log('非登录请求，token验证中')
		let token = ""
		// token = sessionStorage.getItem('token')
		token = uni.getStorageSync('token')
		console.log('请求token', token)

		// FIXME 根据token测试
		if (!token) {
			// console.log('重定向', token)
			// 添加重定向提示
			uni.showToast({
				title: '您尚未登录',
				icon: 'none',
				duration: 4000
			});
			uni.reLaunch({
				url: '/pages/login/login',
			})
			return;
		}
		
		// 请求头设置
		config.header = {
			'token': token,
			'userid':uni.getStorageSync('userid')
			// 'userid':sessionStorage.getItem('userid')
			// 'content-type':'application/x-www-form-urlencoded'
		}
	}
	if (!config.data) {
		config.data = {};
	}
	var hideLoading = config.hideLoading || false;
	//加载圈
	if (!hideLoading) {
		uni.showLoading({
			title: '加载中...'
		});
	}
	// console.log(JSON.stringify(config.data));
	let promise = new Promise(function(resolve, reject) {
		console.log('请求数据', config)
		uni.request({
			...config,
			// 请求成功
			success: (response) => {
				console.log('服务器响应结果', response)
				showError(response)
				if (response.statusCode == 200) {
					resolve(response);
				} else {
					reject(response)
				}
			},
			// 请求失败
			fail: (error) => {
				// console.log("服务器请求失败", error)
				uni.showToast({
					title: '服务器请求失败',
					icon: 'none',
					duration: 4000
				});
				reject(error);
			},
			//请求完成
			complete() {
				//隐藏加载
				if (!hideLoading) {
					uni.hideLoading();
				}
			}
		})
	})
	return promise;
};
export default {
	request: request
};


// 异常码处理
const showError = (res) => {
	if (res) {
		switch (res.statusCode) {
			case 422:
				uni.showToast({
					title: '访问数据格式错误',
					icon: 'none',
					duration: 4000
				});
				break
			case 403:
			uni.showToast({
				title: '您没有操作权限',
				icon: 'none',
				duration: 4000
			});
				// uni.showModal({
				// 	title: '登录已过期',
				// 	content: '很抱歉，登录已过期，请重新登录',
				// 	confirmText: '重新登录',
				// 	success: function(res) {
				// 		if (res.confirm) {
				// 			// TODO 记得解除注释
				// 			// 注销token
				// 			// sessionStorage.setItem("token", '')
				// 			uni.setStorageSync('token', '')
				// 			//去我的页面登录
				// 			uni.reLaunch({
				// 				url: '/pages/login/login'
				// 			})
				// 		} else if (res.cancel) {
				// 			console.log('用户点击取消');
				// 		}
				// 	}
				// })
				break
			case 404:
				uni.showToast({
					title: '很抱歉，资源未找到!',
					icon: 'none',
					duration: 4000
				});
				break
			case 405:
				uni.showToast({
					title: '传输方法错误',
					icon: 'none',
					duration: 4000
				});
				break
			case 504:
				uni.showToast({
					title: '网络超时',
					icon: 'none',
					duration: 2000
				});
				break
			case 500:
				uni.showToast({
					title: '服务器异常',
					icon: 'none',
					duration: 2000
				});
				break
			case 401:
				uni.showToast({
					title: '未授权，请重新登录',
					icon: 'none',
					duration: 4000
				});
				setTimeout(() => {
					//去我的页面登录
					uni.reLaunch({
						url: '/pages/login'
					})
				}, 1500)
				break
			default:
				break
		}
	}

	if (res.statusCode == 200) {
		switch (res.data.msg) {
			case 10002:
				uni.showToast({
					title: '添加失败',
					icon: 'none',
					duration: 4000
				});
				break
			case 10004:
				uni.showToast({
					title: '删除失败',
					icon: 'none',
					duration: 4000
				});
				break
			case 10006:
				uni.showToast({
					title: '更新失败',
					icon: 'none',
					duration: 4000
				});
				break
			case 10008:
				uni.showToast({
					title: '查询失败',
					icon: 'none',
					duration: 4000
				});
				break
			case 10011:
				uni.showToast({
					title: '数据不存在',
					icon: 'none',
					duration: 4000
				});
				break
			case 10012:
				uni.showToast({
					title: '用户名或密码错误',
					icon: 'none',
					duration: 4000
				});
				break
			case 10013:
				uni.showToast({
					title: '账户名已存在',
					icon: 'none',
					duration: 4000
				});
				break
		}
	}
	return null
};
