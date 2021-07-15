<template>
	<view>
		<u-toast ref="uToast" />
		<view class="login-title-item">
			<text class="title">CSI员工之家</text>
		</view>
		<view class="welcome">
			<text>Welcome to House</text>
		</view>
		<u-gap height="200"></u-gap>
		<view class="nameInput">
			<!-- FIX 去掉之前的input change -->
			<u-input :border="true" v-model="loginname" placeholder="请输入用户名" />
			<u-gap height="10"></u-gap>
			<u-input type="password" :border="true" v-model="password" placeholder="请输入密码" />
		</view>
		<u-gap height="50"></u-gap>
		<u-checkbox v-model="remember" style="margin-left: 40rpx;">记住密码</u-checkbox>
		<u-gap height="80"></u-gap>

		<u-col span="400">
			<u-row gutter="20">
				<button @click="submit" type="primary">登录</button>
			</u-row>
		</u-col>
	</view>
</template>

<script>
	import tabber from '../../util/tabBar.js'
	//import sendThis 函数，实现拦截器统一拦截msg码弹窗
	import {
		sendThis
	} from "../../api/request.js"
	import {
		loginSendData
	} from "../../api/api.js"
	import {
		MD5
	} from "../../api/md5.js"

	export default {
		data() {
			return {
				loginname: '',
				password: '',
				remember: false,
				userid: '',
				status: '',
				token: '',
				username: ''
			}
		},

		computed: {},
		onLoad() {
			sendThis(this)
		},
		methods: {
			//showToast方法，实现异常码弹窗
			showToast(TITLE, TYPE) {
				this.$refs.uToast.show({
					title: TITLE.toString(),
					type: TYPE.toString(),
				})
			},
			showSuccessToast() {
		
				uni.setStorageSync("userid", this.userid)
				uni.setStorageSync("token", this.token)
				uni.setStorageSync("username", this.username)
				// #ifdef H5
				sessionStorage.setItem("userid", this.userid)
				sessionStorage.setItem("token", this.token)
				sessionStorage.setItem("username", this.username)
				// #endif

				//将登录成功的状态存入缓存
				if (this.remember) {
					//如果选择记住密码，将账号和密码存缓存
					uni.setStorageSync('password', this.password)
					// #ifdef H5
					sessionStorage.setItem("password", this.password);
					// #endif
				}
			},
			submit() {
				let data = {
					loginname: this.loginname,
					password: MD5(this.password),//对password进行md5加密
				}
				loginSendData(data)
					.then((response) => {
						this.userid = response.data.data.userid;
						this.token = response.data.data.token;
						this.status = response.data.data.status;
						this.username = response.data.data.username;
						console.log(this.status)
						this.showSuccessToast();
						if (this.status) {
							this.$store.commit('tabBer/add', tabber.testBBar)
							console.log(this.$store.getters.tabBerList)
							uni.switchTab({
								url: '/pages/menu/menu'
							})
						} else {
							this.$store.commit('tabBer/add', tabber.testABar)
							console.log(this.$store.getters.tabBerList)
							uni.switchTab({
								url: '/pages/menu/user_menu'
							})
						}
					})
					.catch((error) => {
						console.log(error);
						uni.redirectTo({
							url: '/pages/login/login'
						})
					})
			},
		},
	}
</script>

<style lang="scss" scoped>
	input {
		text-align: left;
		margin-bottom: 10rpx;
		padding-bottom: 6rpx
	}

	.welcome {
		font-size: 50rpx;
		font-style: oblique;
		margin: 20rpx 20rpx -60rpx 150rpx;
	}

	.nameInput {
		margin: 0rpx 30rpx 10rpx 30rpx;
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

	.login-title-item {
		// border-style: solid;
		margin: 100rpx 0rpx 30rpx 30rpx;
		height: 150rpx;
	}
</style>
