<template>
	<view>
		<u-toast ref="uToast" />
		<view class="login-title-item">
			<text class="title">CSI员工之家</text>
		</view>
		<u-gap height="200"></u-gap>

		<u-input @change="change" :border="true" v-model="loginname" placeholder="请输入用户名" />
		<u-gap height="10"></u-gap>
		<u-input type="password" :border="true" v-model="password" placeholder="请输入密码" />

		<u-gap height="80"></u-gap>

		<u-checkbox v-model="remember" >记住密码</u-checkbox>
		<u-gap height="80"></u-gap>

		<u-col span="400">
			<u-row gutter="20">
				<button @click="submit" type="primary">登录</button>
				<button @click="submit" type="default">刷脸</button>
			</u-row>
		</u-col>
	</view>
</template>

<script>
	import {
		SendData
	} from "../../api/login.js"
	export default {
		data() {
			return {
				loginname: '',
				password: '',
				remember: false,
				userid: '',
				status: '',
			}
		},

		computed: {},
		onLoad() {},
		methods: {
			showFalseToast() {
				this.$refs.uToast.show({
					title: '用户名或密码错误',
					type: 'false'
				})
			},
			showSuccessToast() {
				this.$refs.uToast.show({
					title: '登录成功',
					type: 'success'
				})
				//将登录成功的状态存入缓存
				if (this.remember) {
					//如果选择记住密码，将账号和密码存缓存
					localStorage.setItem('loginname', this.loginname);
					localStorage.setItem('pwd', this.password);
					//window.localStorage.setItem("user", obj)
				}
			},
			submit() {
				let data = {
					loginname: this.loginname,
					password: this.password,
					userid: this.userid,
					status: this.status,
					remember: this.remember,
				}
				// SendData(data)
				// 	.then((response) => {
				// 		this.showSuccessToast();
				// 		uni.switchTab({
				// 		    url: '/pages/menu/menu'
				// 		})
				// 	})
				// 	.catch((error) => {
				// 		console.log(error);
				// 		this.showFalseToast();
				// 		uni.switchTab({
				// 		    url: '/pages/login/login'
				// 		})
				// 	})
				// TODO 页面跳转逻辑
				uni.request({
					url:'/api/login',
					method:'POST',
					data:{
						loginname: this.loginname,
						password: this.password,
					},
					success: (res) => {
						console.log(res)
						uni.setStorageSync('token',res.data.data.token)
						uni.setStorageSync('currentid',res.data.data.userid)
					}
				})
				console.log('开始跳转中')
				uni.switchTab({
					url:'../menu/menu',
				})
			},
			//监听账号输入操作,如果输入账号，自动输入密码
			change() {
				let loginname = this.loginname
				let password = JSON.parse(localStorage.getItem("password"))
				if (loginname === "admin") {
					this.password = password
				}
			},
			checkboxChange(e) {
				console.log(e);
			},
		}
	};
</script>

<style lang="scss" scoped>
	input {
		text-align: left;
		margin-bottom: 10rpx;
		padding-bottom: 6rpx
	}

	.title {
		font-size: 70rpx;
		position: absolute;
		right: 0px;
		width: 300px;
		padding: 10px;
		margin: 0 auto;
	}

	.remember {
		margin-left: -50%;
		margin-top: 50%;
		color: #adadad;
	}
	
	// .login-title-item{
	// 	border-style: solid;
	// 	margin: 0 auto;
	// 	height: 150rpx;
	// }
</style>
