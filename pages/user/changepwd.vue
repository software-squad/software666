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
		onLoad: function(option) {
			sendThis(this)
			this.imageSrc = JSON.parse(decodeURIComponent(option.pic));
			// this.userid = sessionStorage.getItem("userid");
			this.userid = uni.getStorageSync("userid");
		},
		methods: {
			showToast(TITLE, TYPE) {
				this.$refs.uToast.show({
					title: TITLE.toString(),
					type: TYPE.toString(),
				})
			},
			// showFalseToast() {
			// 				this.$refs.uToast.show({
			// 					title: '修改失败',
			// 					type: 'error',
			// 				})
			// },
			// showSuccessToast() {
			// 				this.$refs.uToast.show({
			// 					title: '修改成功',
			// 					type: 'success'
			// 				})
			// },
			showWarningToast() {
				this.$refs.uToast.show({
					title: '两次输入的新密码不一致',
					type: 'error'
				})
			},
			confirm() {
				if (this.confirmpwd != this.newpwd) {
					this.showWarningToast();
					this.oldpwd = '';
					this.newpwd = '';
					this.confirmpwd = '';
				} else {
					this.submit();
				}
			},
			submit() {
				let data = {
					userid: this.userid,
					oldpwd: this.oldpwd,
					newpwd: this.newpwd,
				}
				changePwdSendData(data)
					.then((response) => {
						// this.showToast()
						// this.showSuccessToast()
						uni.navigateTo({
							url: "user"
						})
					})
					.catch((error) => {
						console.log(error);
						// this.showFalseToast()
					})
			},
			cancel() {
				uni.navigateTo({
					url: "user"
				})
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
