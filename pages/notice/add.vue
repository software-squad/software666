<!-- 公告添加界面 -->
<template>
	<view>
		<u-toast ref="uToast" />
		<view class="whole">
		<u-gap height="40"></u-gap>
		<text class="title">公告标题</text>
		<u-gap height="10"></u-gap>
		<u-input type="text" :border="true" placeholder="请输入文档标题" v-model="title" />
		<u-gap height="30"></u-gap>
		<text class="title">公告内容</text>
		<u-gap height="10"></u-gap>
		<u-input type="textarea" height="700" :border="true" placeholder="请输入文档描述" v-model="content" />
		<u-gap height="80"></u-gap>
		<u-col span="400">
			<u-row gutter="20">
				<u-modal v-model="show" :content="content1" :show-cancel-button="true" @confirm="submit"
					@cancel="cancel"></u-modal>
				<u-button @click="open" type="primary" shape="circle" class="custom-style">发布</u-button>
			</u-row>
		</u-col>
		</view>
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
			//打开确认是否发布的弹窗
			open() {
				this.show = true;
			},
			//取消发布，弹窗消失
			cancel() {
				this.show = false;
			},
			//确认发布
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
						// 返回上一页并刷新的方法
						let pages = getCurrentPages(); // 当前页面
						let beforePage = pages[pages.length - 2]; // 上一页就是show页面
						// console.log(pages);
						// console.log(beforePage);
						
						uni.navigateBack({
							// url: '/pages/notice/show',
							success: function() {
								console.log("返回上一页并刷新")
								beforePage.myReload() // 执行上一页的onLoad方法
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
	.whole{
		margin: 0 50rpx;
	}
	.title{
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

