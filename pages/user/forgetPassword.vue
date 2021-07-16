<template>
	<view>
		<u-field v-model="item.loginname" label="用户登录名" placeholder="请输入用户登录名" label-align="center">
		</u-field>
		<!-- <u-gap height="10" bg-color="#f9f9f9"></u-gap> -->
		<u-field v-model="item.newpwd" label="重置密码" placeholder="请输入重置密码" label-align="center"></u-field>
		<u-button type="primary" @click="modalShow = true">提交</u-button>
		<u-gap height="5"></u-gap>
		<!-- 模态框是否确认传输 -->
		<u-modal v-model="modalShow" content="确认提交" :show-cancel-button="true" :async-close="true" @confirm="confirm">
		</u-modal>
		<u-toast ref="uToast"></u-toast>
	</view>
</template>

<script>
	import {
		MD5
	} from "../../api/md5.js"
	export default {
		data() {
			return {
				item: {
					loginname: '',
					newpwd: '',
				},
				modalShow: false
			}
		},
		onLoad() {
			if (uni.getStorageSync('userid') != 1) {
				this.$refs.uToast.show({
					title: '您没有操作权限',
					type: 'error',
				})
				setTimeout(() => {
					uni.navigateBack();
				}, 1000)
			}
		},
		methods: {
			confirm() {
				if (uni.getStorageSync('userid') != 1) {
					this.$refs.uToast.show({
						title: '您没有操作权限',
						type: 'error',
					})
					return;
				}else{
					this.$api.resetPwd({
						loginname:this.item.loginname,
						newpwd:MD5(this.item.newpwd)
					}).then((res)=>{
						this.$refs.uToast.show({
							title: '重置成功',
							type: 'success',
						})
						setTimeout(() => {
							uni.navigateBack();
						}, 1000)
					}).catch((error)=>{
						this.$refs.uToast.show({
							title: '重置失败',
							type: 'error',
						})
					})
				}
			}
		}
	}
</script>

<style>

</style>
