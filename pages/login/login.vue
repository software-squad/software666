<template>
	<view>
		<u-toast ref="uToast" />
		<text class="title">CSI员工之家</text>
		<u-gap height="200"></u-gap>
		<!-- FIX 去掉之前的input change -->
		<u-input :border="true" v-model="loginname" placeholder="请输入用户名" />
		<u-gap height="10"></u-gap>
		<u-input type="password" :border="true" v-model="password" placeholder="请输入密码" />

		<u-gap height="80"></u-gap>

		<u-checkbox v-model="remember">记住密码</u-checkbox>
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
		loginSendData
	} from "../../api/api.js"
	export default {
		data() {
			return {
				loginname: '',
				password: '',
				remember: false,
				userid: '',
				status: '',
				token: '',
				username:''
			}
		},

		computed: {},
		onLoad() {},
		methods: {
			showFalseToast() {
				this.$refs.uToast.show({
					title: '用户名或密码错误',
					type: 'false',
				})
			},
			showSuccessToast() {
				this.$refs.uToast.show({
					title: '登录成功',
					type: 'success',
				})
				
				uni.setStorageSync("userid",this.userid)
				uni.setStorageSync("token",this.token)
				uni.setStorageSync("username", this.username)
				// #ifdef H5
				sessionStorage.setItem("userid", this.userid)
				sessionStorage.setItem("token", this.token)
				sessionStorage.setItem("username", this.username)
				// #endif
				
				//将登录成功的状态存入缓存
				if (this.remember) {
					//如果选择记住密码，将账号和密码存缓存
					//window.sessionStorage.setItem("user", obj),
					uni.setStorageSync('password',this.password)
					// #ifdef H5
					sessionStorage.setItem("password", this.password);
					// #endif
				}
			},
			submit() {
				let data = {
					loginname: this.loginname,
					password: this.password,
				}
				// TODO 部分逻辑修改
				// loginSendData(data)
				this.$request.request({
						url: '/api/login',
						method: "POST",
						data: data,
					})
					.then((response) => {
						this.userid = response.data.data.userid;
						this.token = response.data.data.token;
						this.username = response.data.data.username
						this.showSuccessToast();
						uni.switchTab({
							url: '/pages/menu/menu'
						})
					})
					// .catch((error) => {
					// 	console.log(error);
					// 	this.showFalseToast();
					// 	uni.switchTab({
					// 		url: '/pages/login/login'
					// 	})
					// })
			},
			//监听账号输入操作,如果输入账号，自动输入密码
			// change() {
			// 	let loginname = this.loginname
			// 	let password = JSON.parse(localStorage.getItem("password"))
			// 	if (loginname === "admin") {
			// 		this.password = password
			// 	}
			// },
			// checkboxChange(e) {
			// 	console.log(e);
			// },
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
	}

	.remember {
		margin-left: -50%;
		margin-top: 50%;
		color: #adadad;
	}
</style>
