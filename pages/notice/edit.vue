<!-- 公告编辑界面 -->
<template>
	<view class="noticeEdit">
		<u-toast ref="uToast" />
		<u-gap height="40"></u-gap>
		<text class="title">公告标题</text>
		<u-gap height="20"></u-gap>
		<u-input type="text" :border="true" placeholder="请输入公告标题" v-model="item.title" />
		<u-gap height="30"></u-gap>
		<text class="title">公告内容</text>
		<u-gap height="20"></u-gap>
		<u-input type="textarea" :border="true" placeholder="请输入公告内容" v-model="item.content" />
		<u-gap height="80"></u-gap>
		<u-col span="400">
			<u-row gutter="20">
				<u-modal v-model="show" :content="content1" :show-cancel-button="true" @confirm="submit"
					@cancel="cancel"></u-modal>
				<u-button @click="open" type="primary" shape="circle" class="custom-style">发布</u-button>
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
			sendThis(this)
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
			//打开确认是否发布的弹窗
			open() {
				this.show = true;
			},
			//取消编辑，弹窗消失
			cancel() {
				this.show = false;
			},
			//确认编辑
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
						// 返回上一页并刷新的方法
						let pages = getCurrentPages(); // 当前页面
						let beforePage = pages[pages.length - 3]; // 上上页
						// TODO
						uni.navigateBack({
							delta: 2,
							url: '/pages/notice/show',
							success: function() {
								console.log("返回上一页并刷新")
								beforePage.submit() // 执行上一页的onLoad方法
							}
						});
					})
					.catch((error) => {
						console.log(error);
					})
			},

		},
	}
</script>

<style>
	.noticeEdit {
		margin: 0 50rpx;
	}

	.title {
		font-size: larger;
		font-weight: bold;
	}

	.custom-style {
		color: #ffffff;
		background-color: #0167ff;
		font-weight: 550;
		font-size: larger;
		width: 100%;
		height: 90rpx;
	}
</style>
