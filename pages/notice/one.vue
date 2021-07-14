<template>
	<view>
		<u-toast ref="uToast" />
		<uni-group title="公告标题" top="20">
			<view>{{item.title}}</view>
		</uni-group>
		<uni-group title="公告内容" top="20">
			<view>{{item.content}}</view>
		</uni-group>

		<u-col span="400" justify="center">
			<u-row gutter="20">
				<button @click="submit" type="primary">编辑</button>
				<u-modal v-model="show" :content="content1" :show-cancel-button="true" @confirm="delet"
					@cancel="cancel"></u-modal>
				<button @click="open" type="warn">删除</button>
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
			this.item = JSON.parse(decodeURIComponent(option.item));
			console.log("noticeOne")
			console.log(this.item.title); //打印出上个页面传递的参数。
			console.log(this.item.content); //打印出上个页面传递的参数。
			uni.setNavigationBarTitle({
				title: this.item.title,
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
			// navToEdit() {
			// 	uni.navigateTo({
			// 		url: 'edit?item=' + encodeURIComponent(JSON.stringify(this.item))
			// 	})
			// 	console.log(this.item.title)
			// 	console.log(this.item.content)
			// },
			// navToShow() {
			// 	uni.navigateTo({
			// 		url: 'show?item=' + encodeURIComponent(JSON.stringify(this.item))
			// 	})
			// 	console.log(this.item.title)
			// 	console.log(this.item.content)
			// },

			showDeletSuccessToast() {
				this.$refs.uToast.show({
					title: '删除成功',
					type: 'success'
				})
			},
			showEditSuccessToast() {
				this.$refs.uToast.show({
					title: '编辑成功',
					type: 'success'
				})
			},
			showDeletFalseToast() {
				this.$refs.uToast.show({
					title: '删除失败',
					type: 'false'
				})
			},
			showEditFalseToast() {
				this.$refs.uToast.show({
					title: '编辑失败',
					type: 'false'
				})
			},
			submit() {
				let data = {
					noticeid: this.item.noticeid,
					title: this.item.title,
					content: this.item.content,
					createdate: this.item.createdate,
					userid: this.item.userid,
					username: this.item.username,
				}
				noticeEditSendData(data)
					.then((response) => {
						this.showEditSuccessToast();
						uni.navigateTo({
							url: 'edit?item=' + encodeURIComponent(JSON.stringify(this.item))
						})
					})
					.catch((error) => {
						console.log(error);
						this.showEditFalseToast();
					})
			},

			delet() {
				let data = {
					noticeid: this.item.noticeid,
				}
				noticeDeletSendData(data)
					.then((response) => {
						this.showDeletSuccessToast();
						uni.navigateBack({
							url: '/pages/notice/show'
						})
					})
					.catch((error) => {
						console.log(error);
						this.showDeletFalseToast();
					})
			},

		}
	}
</script>

<style>

</style>
