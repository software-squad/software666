<!-- 管理员单个公告展示界面 -->
<template>
	<view>
		<u-toast ref="uToast" />
		<u-gap height="20"></u-gap>
		<view class="noticeOne">
			<text class="title">公告内容</text>
			<u-gap height="60"></u-gap>
			<text style="font-size: larger; height: 200;">{{item.content}}</text>
			<u-gap height="40" ></u-gap>
			<u-line color="#bbb" />
			<u-gap height="100" ></u-gap>

		<u-col span="400" justify="center">
			<u-row gutter="20">
				<u-button @click="submit" type="primary" shape="circle" class="custom-style">编辑</u-button>
				<u-modal v-model="show" :content="content1" :show-cancel-button="true" @confirm="delet"
					@cancel="cancel"></u-modal>
				<u-button @click="open" type="error" shape="circle" class="custom1-style">删除</u-button>
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
		noticeEditSendData
	} from "../../api/api.js"
	import {
		noticeDeletSendData
	} from "../../api/api.js"
	export default {
		data() {
			return {
				show: false,
				item: '',
				noticeid: 0,
				title: '',
				content: '',
				createdate: '',
				userid: '',
				username: '',
				content1: '确认删除?',
			}
		},
		onLoad: function(option) {
			sendThis(this)
			this.item = JSON.parse(decodeURIComponent(option.item));
			console.log(this.item.title); //打印出上个页面传递的参数。
			console.log(this.item.content); //打印出上个页面传递的参数。
			uni.setNavigationBarTitle({
				title: this.item.title
			})
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
			submit() {
				// BUG 关闭当前页面跳转
				uni.navigateTo({
					url: 'edit?item=' + encodeURIComponent(JSON.stringify(this.item))
				})
				// })
			},

			delet() {
				let data = {
					noticeid: this.item.noticeid,
				}
				noticeDeletSendData(data)
					.then((response) => {
						// 返回上一页并刷新的方法
						let pages = getCurrentPages(); // 当前页面
						let beforePage = pages[pages.length - 2]; // 上一页
						uni.navigateBack({
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

		}
	}
</script>

<style>
	.noticeOne{
		margin: 0 50rpx;
	}
	.name{
		text-align: center;
		margin-left: 285rpx;
		font-size: larger;
		font-weight: 550;
	}
	.title{
		font-size: larger;
		font-weight: bold;
		/* margin-left: 260rpx; */
	}
	.custom-style {
		color: #ffffff;
		background-color: #0167ff;
		font-weight: 550;
		font-size: larger;
		width: 50%;;
		height: 90rpx;
	}
	.custom1-style {
		color: #241c32;
		background-color: #e6e6e6;
		font-size: larger;
		font-weight: 550;
		width: 50%;
		height: 90rpx;
	}
</style>
