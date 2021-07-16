<template>
	<view>
		<!-- 引入uview弹窗组件，实现异常码拦截弹窗 -->
		<u-toast ref="uToast" />
		<u-gap height="40"></u-gap>
		<view class="whole">
			<!-- 实现用户键入新建部门的信息组件 -->
			<text class="title">部门名字</text>
			<u-gap height="10"></u-gap>
			<u-input type="text" :border="true" placeholder="请输入部门名字" v-model="deptname" />
			<u-gap height="30"></u-gap>
			<text class="title">部门描述</text>
			<u-gap height="10"></u-gap>
			<u-input type="textarea" height="400" :border="true" placeholder="请输入部门描述" v-model="remark" />
			<u-gap height="30"></u-gap>
			<text class="title">部门照片</text>
			<!-- 上传照片组件 -->
			<u-gap height="10"></u-gap>
			<uni-file-picker  fileMediatype="image" limit="1" ref='imagePick' @select="select"
				@success="success" @fail="fail" @progress="progress" />
			<u-gap height="50"></u-gap>
			<u-col span="400">
				<u-row gutter="20">
					<u-modal v-model="show" :content="content" :show-cancel-button="true" @confirm="confirm"
						@cancel="cancel"></u-modal>
					<u-button @click="submit" type="primary" shape="circle" class="custom-style">提交</u-button>
				</u-row>
			</u-col>
		</view>
	</view>
</template>

<script>
	// 引入request里封装的返回指向当前页面的指针的函数sendThis
	import {
		sendThis
	} from "../../api/request.js"
	// 引入api统一管理文档里的deptAddSendData接口，实现展示新建部门的请求
	import {
		deptAddSendData
	} from "../../api/api.js"
	export default {
		data() {
			return {
				deptname: '',
				remark: '',
				url: '',
				show: false,
				content: '确认提交？'
			}
		},
		onLoad() {
			// 把当前指向当前页面的指针发给request.js
			sendThis(this)
		},
		methods: {
			//定义弹窗函数接受request.js的参数，实现弹窗
			showToast(TITLE, TYPE) {
				this.$refs.uToast.show({
					title: TITLE.toString(),
					type: TYPE.toString(),
				})
			},
			select(e) {},
			progress(e) {},
			fail(e) {},
			success(e) {
				console.log('上传成功', e)
				this.url = e.tempFilePaths[0]
				console.log('部门新照片', this.url)
			},
			// 点击添加事件，弹出给用户再次选择是否添加的模态框
			submit() {
				this.show = true;
			},
			// 模态框确认事件，定义传给后端的data，并调用deptAddSendData接口向后端发出请求
			confirm() {
				let data = {
					deptname: this.deptname,
					remark: this.remark,
					depturl: this.url
				}
				deptAddSendData(data)
					.then((response) => {
						// 回调函数里返回show页面并刷新
						let pages = getCurrentPages(); // 当前页面
						let beforePage = pages[pages.length - 2]; // 上一页
						uni.navigateBack({
							success: function() {
								console.log("返回上一页并刷新")
								beforePage.DeptShowSendData() // 执行上一页的方法
							}
						});
					})
					.catch((error) => {
						console.log(error);
					})
			},
			cancel() {
				this.show = false;
			}


		}
	}
</script>

<style>
	.whole {
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
