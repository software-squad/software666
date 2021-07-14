<template>
	<view>
		<u-toast ref="uToast" />
		<u-gap height="40"></u-gap>
		<text>公告标题</text>
		<u-gap height="10"></u-gap>
		<u-input type="text" :border="true" placeholder="请输入公告标题" v-model="item.title" />
		<u-gap height="30"></u-gap>
		<text>公告内容</text>
		<u-gap height="10"></u-gap>
		<u-input type="textarea" :border="true" placeholder="请输入公告内容" v-model="item.content" />
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
		noticeEditSendData
	} from "../../api/api.js"
	export default {
		data() {
			return {
				show: false,
				content1: '确认发布?',
				item: '',
				//noticeid: '',
				title: '',
				content: '',
				createdate: '',
				userid: '',
				username: '',
				List: [],
			}
		},
		onLoad: function(option) {
			this.item = JSON.parse(decodeURIComponent(option.item));
			console.log(this.item.title); //打印出上个页面传递的参数。
			console.log(this.item.content); //打印出上个页面传递的参数。
		},
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
					noticeid: this.item.noticeid,
					title: this.item.title,
					content: this.item.content,
					//createdate: this.item.createdate,
					userid: this.item.userid,
					username: this.item.username,
				}
				noticeEditSendData(data)
					.then((response) => {
						this.showSuccessToast();
						uni.navigateBack({
							delta: 2,
							url: '/pages/notice/show',

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
