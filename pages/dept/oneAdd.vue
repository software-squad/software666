<template>
 	<view>
		<u-toast ref="uToast" />
 		<u-gap height="40"></u-gap>
 		<view class="deptOne">
 			<text>部门名字</text>
 			<u-input type="text" :border="true" placeholder="请输入部门名字" v-model="deptname"/>
 			<u-gap height="30"></u-gap>
 			<text>部门描述</text>
 			<u-gap height="10"></u-gap>
 			<u-input type="textarea" height="700" :border="true" placeholder="请输入部门描述" v-model="remark"/>
 			<u-gap height="80"></u-gap>
			<text>部门照片</text>
			<u-gap height="10"></u-gap>
			<u-input type="textarea" height="700" :border="true" placeholder="请输入部门照片网址" v-model="url"/>
			<u-gap height="80"></u-gap>
 			<u-col span="400">
 				<u-row gutter="20">
					<u-modal v-model="show" :content="content" :show-cancel-button="true" @confirm="confirm" @cancel="cancel"></u-modal>
 					<button @click="submit" >提交</button>
 				</u-row>
 			</u-col>
 		</view>
 	</view>
 </template>
 
 <script>
	 import {sendThis} from "../../api/request.js"
	import {deptAddSendData} from "../../api/api.js"
 	export default {
 		data() {
 			return {
 				value: '',
 				deptname:'',
 				remark:'',
				url:'',
				show: false,
				content: '确认提交？'
 			}
 		},
		onLoad(){
			sendThis(this)
		},
 		methods: {
			showToast(TITLE,TYPE) {
							this.$refs.uToast.show({
								title: TITLE.toString(),
								type: TYPE.toString(),
							})
			},
 			showSuccessToast() {
 				this.$refs.uToast.show({
 					title: '提交成功',
 					type: 'success'
 				})
 			},
 			showFalseToast() {
 				this.$refs.uToast.show({
 					title: '提交失败',
 					type: 'false'
 				})
 			},
 			submit(){
 				this.show = true;
 			},
			confirm(){
				let data = {
					deptname:this.deptname,
					remark:this.remark,
					depturl:this.url
				}
				deptAddSendData(data)
					.then((response) => {
						this.showSuccessToast();
						uni.navigateBack()
					})
					.catch((error) => {
						console.log(error);
						this.showFalseToast();
					})		
			},
			cancel(){
				this.show = false;
			}
 			
 			
 		}
 	}
 </script>
 
 <style>
 	.deptOne{
 		margin: 0 50rpx;
 	}
 
 </style>
