<!-- 普通用户单个公告展示界面 -->
<template>
	<view>
		<!-- 根据所点击公告内容动态改变公告标题和内容 -->
		<u-toast ref="uToast" />
		<uni-group title="公告标题" top="20">
			<view>{{item.title}}</view>
		</uni-group>
		<uni-group title="公告内容" top="20">
			<view>{{item.content}}</view>
		</uni-group>
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

</style>
