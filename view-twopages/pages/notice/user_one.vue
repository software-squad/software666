<!-- 普通用户单个公告展示界面 -->
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
			console.log("noticeOne")
			console.log(this.item.title);   //打印出上个页面传递的参数。
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
		}
	}
</script>

<style>
	.noticeOne{
		margin: 0 50rpx;
	}
	.title{
		font-size: larger;
		font-weight: bold;
		/* margin-left: 260rpx; */
	}
</style>