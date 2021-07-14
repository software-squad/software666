<template>
	<view>
			<u-toast ref="uToast" />
			<view class="jobOne">
				<u-gap height="15"></u-gap>
				<text class="title">职位名字</text>
				<u-gap height="30"></u-gap>
				<text>{{item.jobname}}</text>
				<u-gap height="40"></u-gap>
				<u-line color="#bbb" />
				<u-gap height="15"></u-gap>
				<text class="title">职位描述</text>
				<u-gap height="30"></u-gap>
				<text>{{item.remark}}</text>
				<u-gap height="40"></u-gap>
				<u-line color="#bbb" />
				<u-gap height="40"></u-gap>
			</view>
		</view>
</template>

<script>
	//import sendThis 函数，实现拦截器统一拦截msg码弹窗
	import {
		sendThis
	} from "../../api/request.js"
	import {
		jobOneDelSendData
	} from "../../api/api.js"
	export default {
		data() {
			return {
				jobid: '',
				value: '',
				jobname: '',
				remark: '',
				item: '',
				show: false,
				content: '确认删除？'
			}
		},
		onLoad: function(option) {
			sendThis(this)
			this.item = JSON.parse(decodeURIComponent(option.item));
			// console.log("one");
			// console.log(this.item.name);
			// console.log(this.item.remark);
		},
		methods: {
			//showToast方法，实现异常码弹窗
			showToast(TITLE, TYPE) {
				this.$refs.uToast.show({
					title: TITLE.toString(),
					type: TYPE.toString(),
				})
			},
			// 		showDelSuccessToast() {
			// 			this.$refs.uToast.show({
			// 				title: '删除成功',
			// 				type: 'success'
			// 			})
			// 		},
			// 		showDelFalseToast() {
			// 			this.$refs.uToast.show({
			// 				title: '删除失败',
			// 				type: 'false'
			// 			})
			// 		},
			// 		del(){
			// 			this.show = true;	
			// 		},
			// 		confirm(){
			// 			let data = {
			// 				jobid:this.item.jobid		
			// 			}
			// 			jobOneDelSendData(data)
			// 				.then((response) => {
			// 					this.showDelSuccessToast();
			// 					uni.navigateBack({
			// 						url: '/pages/job/show'
			// 					})
			// 				})
			// 				.catch((error) => {
			// 					console.log(error);
			// 					this.showDelFalseToast();
			// 				})	
			// 		},
			// 		cancel(){
			// 			this.show = false;
			// 		},
			// 		navToEdit(){
			// 			uni.navigateTo({
			// 				url: "edit?item="+encodeURIComponent(JSON.stringify(this.item))
			// 			}),
			// 			console.log("one")
			// 			// console.log(this.item.name),
			// 			// console.log(this.item.dcrpt)
			// 		}


		}
	}
</script>

<style>
	.jobOne{
		margin: 0 50rpx;
	},
	.title{
		font-size: larger;
		font-weight: bold;
		margin-left: 260rpx;
	}
	.custom-style{
		color: #241c32;
		font-weight: bold;
		/* background-color: #a8a7ab; ; */
		width: 150rpx;
		height: 90rpx;
	}
	.custom1-style{
		color: #241c32;
		font-weight: bold;
		background-color: #e6e6e6; 
		width: 150rpx;
		height: 90rpx;
	}
</style>

