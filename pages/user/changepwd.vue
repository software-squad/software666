<template>
	<view>
		<u-toast ref="uToast" />
		<view class="userimage">
			<u-image width="250rpx" height="250rpx" :src="imageSrc" shape="circle"></u-image>
		</view>
		<u-gap height="200"></u-gap>
		<view class="password">
			<u-input type="password" :border="true" v-model="oldpwd" placeholder="请输入原密码" />
			<u-gap height="30"></u-gap>
			<u-input type="password" :border="true" v-model="newpwd" placeholder="请输入新密码" />
			<u-gap height="30"></u-gap>
			<u-input type="password" :border="true" v-model="confirmpwd" placeholder="请再次输入新密码" />
			<u-gap height="180"></u-gap>
		</view>
		<u-row>
			<u-button type="primary" @click="confirm">确认</u-button>
			<u-button type="error" @click="cancel">取消</u-button>
		</u-row>
	</view>
</template>

<script>
	import {
		MD5
	} from "../../api/md5.js"
	import {
		changePwdSendData
	} from "../../api/api.js"
	import {
		sendThis
	} from "../../api/request.js"
	export default {
		data() {
			return {
				userid: '',
				imageSrc: '',
				oldpwd: '',
				newpwd: '',
				confirmpwd: ''
			}
		},
		// 页面加载时
		onLoad: function(option) {
			// 将当前页面的this传给request
			sendThis(this)
			// 获取带参跳转的图片路径
			this.imageSrc = JSON.parse(decodeURIComponent(option.pic))
			// 获取存在前端的userid
			this.userid = sessionStorage.getItem("userid")
		},
		methods: {
			// 拦截器调用显示错误码
			showToast(TITLE, TYPE) {
				this.$refs.uToast.show({
					title: String(TITLE),
					type: String(TYPE),
				})
			},
			// 先验证两次密码是否一致
			confirm() {
				if (this.confirmpwd != this.newpwd) {
					this.showToast('两次输入的密码不一致','error');
					this.oldpwd = '';
					this.newpwd = '';
					this.confirmpwd = '';
				} else {
					this.submit();
				}
			},
			// 若一致，将账号密码发至后端，在回调中将token存入前端
			submit() {
				let data = {
					userid: this.userid,
					oldpwd: MD5(this.oldpwd),
					newpwd:  MD5(this.newpwd),
				}
				changePwdSendData(data)
					.then((response) => {
						this.showToast('修改成功','success');
						setTimeout(() => {
							uni.navigateBack();
						}, 1000)
					})
					.catch((error) => {
						console.log(error);
					})
			},
			// 点击取消回到user页面
			cancel() {
				uni.navigateBack()
			}

		}
	}
</script>

<style>
	.userimage {
		align-items: center;
		display: flex;
		justify-content: center;
	}

	,
	.password {
		align-items: center;
		width: 100%;
		padding: 0 50rpx;
	}
</style>
