<template>
 	<view>
 		<u-toast ref="uToast" />
 		<u-gap height="40"></u-gap>
 		<view class="jobOne">
 			<text class="title">职位所属部门</text>
 			<u-gap height="10"></u-gap>
 			<u-select v-model="showSelect" :list="list" mode="single-column" @confirm="confirmSelect"></u-select>
 			<u-row>
					<u-input type="text" :border="true" placeholder="请选择部门" v-model="deptname" :disabled="true"/>
					<u-button @click="showSelect = true" style="width: 20%;">选择</u-button>
 			</u-row>

 			<u-gap height="30"></u-gap>
 			<text class="title">职位名称</text>
 			<u-gap height="10"></u-gap>
 			<u-input type="text" :border="true" placeholder="请输入职位名称" v-model="jobname"/>
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
		// 页面加载时
 		onLoad() {
			// 将当前页面的this传给request.js
 			sendThis(this)
			// 获取部门列表信息，用于列选择器
			this.DeptShowSendData()
 		},
 		methods: {
			// 获取部门列表信息，用于列选择器
			DeptShowSendData(){
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
			// 拦截器展示错误码时需要使用
 			showToast(TITLE, TYPE) {
 				this.$refs.uToast.show({
 					title: TITLE.toString(),
 					type: TYPE.toString(),
 				})
 			},
			// 提交后显示弹窗
 			submit() {
 				this.show = true;
 			},
			// 列选择器确认后修改全局部门名称
 			confirmSelect(e) {
 				console.log(e[0].label)
 				this.deptname = e[0].label
 			},
			// 确认添加职位后向后端发送添加职位的信息，在回调函数中根据msg显示toast提示
 			confirm() {
 				let data = {
 					deptname: this.deptname,
 					jobname: this.jobname,
 					remark: this.remark,
 				}
 				jobAddSendData(data)
 					.then((response) => {
 						this.showToast('提交成功','success')
 						// 回调函数里返回show页面并刷新
 						let pages = getCurrentPages(); // 当前页面
 						let beforePage = pages[pages.length - 2]; // 上一页
 						uni.navigateBack({
 							success: function() {
 								console.log("返回上一页并刷新")
 								beforePage.JobShowSendData() // 执行上一页的方法
 							}
 						});
 					})
 					.catch((error) => {
 						console.log(error)
 						this.showToast('提交失败','false')
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
	
	.info-item {
		font-size: large;
		font-style: normal;
		float: left;
		font-weight:500;
		text-align: left;
		padding-left: 10rpx;
		/* border-style: solid;  /* TODO */
	}
 </style>
