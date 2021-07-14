<template>
	<view>
		<u-toast ref="uToast" />
		<u-gap height="40"></u-gap>
		<text>公告标题</text>
		<u-gap height="10"></u-gap>
		<u-input type="text" :border="true" placeholder="请输入文档标题" v-model="title" />
		<u-gap height="30"></u-gap>
		<text>公告内容</text>
		<u-gap height="10"></u-gap>
		<u-input type="textarea" height="700" :border="true" placeholder="请输入文档描述" v-model="content" />
		<u-gap height="80"></u-gap>
		<u-col span="400">
			<u-row gutter="20">
				<u-modal v-model="show" :content="content1" :show-cancel-button="true" @confirm="submit"
					@cancel="cancel"></u-modal>
				<button @click="open" type="primary">发布</button>
			</u-row>
		</u-col>
	</view>
</template>

<script>
	//import sendThis 函数，实现拦截器统一拦截msg码弹窗
	import {
		sendThis
	} from "../../api/request.js"
	import {
		noticeAddSendData
	} from "../../api/api.js"
	export default {
		data() {
			return {
				show: false,
				content1: '确认发布?',
				//noticeid: '',
				title: '',
				content: '',
				createdate: '',
				userid: 0,
				username: '',
				List: [],
			}
		},
		onLoad() {},
		methods: {
			//showToast方法，实现异常码弹窗
			showToast(TITLE, TYPE) {
				this.$refs.uToast.show({
					title: TITLE.toString(),
					type: TYPE.toString(),
				})
			},
			open() {
				this.show = true;
			},
			cancel() {
				this.show = false;
			},
			// navToShow() {
			// 	uni.redirectTo({
			// 		url: 'show?item=' + encodeURIComponent(JSON.stringify(this.item))
			// 	})
			// 	console.log(this.item.title)
			// 	console.log(this.item.content)
			// },

			showSuccessToast() {
				this.$refs.uToast.show({
					title: '发布成功',
					type: 'success'
				})
			},
			showFalseToast() {
				this.$refs.uToast.show({
					title: '发布失败',
					type: 'false'
				})
			},
			submit() {
				let data = {
					//noticeid: this.noticeid,
					title: this.title,
					content: this.content,
					//createdate: this.createdate,
					userid: this.userid,
					username: this.username,
					username: this.username,
				}
				noticeAddSendData(data)
					.then((response) => {
						this.showSuccessToast();
						uni.navigateBack({
							url: '/pages/notice/show'
						})
					})
					.catch((error) => {
						console.log(error);
						this.showFalseToast();
					})
			},

		},
	}
</script>

<style>

</style>
