<template>
 	<view>
 		<u-toast ref="uToast" />
 		<u-gap height="40"></u-gap>
 		<view class="jobOne">
 			<text class="title">职位所属部门</text>
 			<u-gap height="10"></u-gap>
 			<u-select v-model="showSelect" :list="list" mode="single-column" @confirm="confirmSelect"></u-select>
 			<u-row>
 				<text>{{deptname}}</text>
 				<u-button @click="showSelect = true" style="width: 80%;">选择</u-button>

 			</u-row>

 			<u-gap height="30"></u-gap>
 			<text class="title">职位名称</text>
 			<u-gap height="10"></u-gap>
 			<u-input type="text" :border="true" placeholder="请输入职位名称" v-model="jobname" />
 			<u-gap height="30"></u-gap>
 			<text class="title">职位描述</text>
 			<u-gap height="10"></u-gap>
 			<u-input type="textarea" height="700" :border="true" placeholder="请输入职位描述" v-model="remark" />
 			<u-gap height="30"></u-gap>
 			<u-col span="400">
 				<u-row gutter="20">
 					<u-modal v-model="show" :content="content" :show-cancel-button="true" @confirm="confirm"
 						@cancel="cancel"></u-modal>
 					<button @click="submit" type="primary" class="but">提交</button>
 				</u-row>
 			</u-col>
 			<u-gap height="30"></u-gap>
 		</view>
 	</view>
 </template>

 <script>
 	import {
 		sendThis
 	} from "../../api/request.js"
 	import {
 		jobAddSendData,
 		deptShowSendData
 	} from "../../api/api.js"
 	export default {
 		data() {
 			return {
 				deptname: '',
 				jobname: '',
 				remark: '',
 				show: false,
 				content: '确认提交？',
 				showSelect: false,
 				list: [],
 			}
 		},
 		onLoad() {
 			sendThis(this)
 			deptShowSendData()
 				.then((response) => {
 					this.list = []
 					for (let i = 0; i < response.data.data.length; i++) {
 						let d = {
 							value: i,
 							label: response.data.data[i].deptname,
 						}
 						this.list.push(d)
 					}
 				})
 				.catch((error) => {
 					console.log(error);
 				})
 		},
 		methods: {
 			showToast(TITLE, TYPE) {
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
 			submit() {
 				this.show = true;
 			},
 			confirmSelect(e) {
 				console.log(e[0].label)
 				this.deptname = e[0].label
 			},
 			confirm() {
 				let data = {
 					deptname: this.deptname,
 					jobname: this.jobname,
 					remark: this.remark,
 				}
 				jobAddSendData(data)
 					.then((response) => {
 						this.showSuccessToast();
 						uni.redirectTo({
 							url: '/pages/job/show'
 						})
 					})
 					.catch((error) => {
 						console.log(error)
 						this.showFalseToast()
 					})
 			},
 			cancel() {
 				this.show = false;
 			}


 		}
 	}
 </script>

 <style>
 	.jobOne {
 		margin: 0 50rpx;
 	}

 	.title {
 		font-size: larger;
 		font-weight: bold;
 	}
 </style>
