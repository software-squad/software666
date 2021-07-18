<template>
	<view>
		<!-- 引入uview弹窗组件，实现异常码拦截弹窗 -->
		<u-toast ref="uToast" />
		<view class="whole">
			<!-- 循环展示部门信息 -->
			<view :index="index" v-for="(item,index) in dept" @click="navToOne(item,index)">
				<view class="u-body-item">
					<image :src="item.depturl" mode="aspectFill" class="avatar-item"></image>
					<u-row class="info-item-row">
						<u-col span="12">
							<view class="info-item">{{item.deptname}}</view>
						</u-col>
					</u-row>
					<u-row>
						<u-col span="12">
							<view class="remark-item">简介:{{item.remark}}</view>
						</u-col>
					</u-row>
					<u-gap height="10"></u-gap>
				</view>
			</view>
		</view>
	</view>
</template>

<script>
	// 引入request里封装的返回指向当前页面的指针的函数sendThis
	import {
		sendThis
	} from "../../api/request.js"
	// 引入api统一管理文档里的deptShowSendData接口，实现展示所有部门的请求
	import {
		deptShowSendData
	} from "../../api/api.js"

	export default {
		data() {
			return {
				dept: []
			}
		},
		// 页面的加载生命周期开始
		onLoad() {
			// 把当前指向当前页面的指针发给request.js
			sendThis(this)
			// 调用函数myReload，请求展示所有部门及其信息
			this.myReload()
		},
		methods: {
			// 调用函数myReload，请求并在其回调中展示所有部门及其信息
			myReload:function(){
				deptShowSendData()
					.then((response) => {
						// 该回调函数将响应的数据中的部门信息存入dept数组，dept里为所有部门的所有信息
						this.dept = []
						// 循环取出response里的data
						for (let i = 0; i < response.data.data.length; i++) {
							let d = {
								deptid: response.data.data[i].deptid,
								deptname: response.data.data[i].deptname,
								depturl: response.data.data[i].depturl,
								remark: response.data.data[i].remark,
							}
							this.dept.push(d)
						}
					})
					.catch((error) => {
						console.log(error);
					})
			},
			// 点击导航栏右上方加号跳转到新增部门的页面
			onNavigationBarButtonTap: function(e) {
				uni.navigateTo({
					url: "oneAdd"
				})
			},
			//定义弹窗函数接受request.js的参数，实现弹窗
			showToast(TITLE, TYPE) {
				this.$refs.uToast.show({
					title: TITLE.toString(),
					type: TYPE.toString(),
				})
			},
			//页面带参跳转函数，进入单独部门的展示页
			navToOne(item, index) {
				console.log("========deptshow页面==========")
				console.log("选中跳转的部门名字：", item.deptname),
					console.log("该部门的描述：", item.remark)
				// 实现带参跳转，由于参数过长，用encodeURIComponent处理
				uni.navigateTo({
					url: "one?item=" + encodeURIComponent(JSON.stringify(item))
				})
			},
		}
	}
</script>

<style>
	.whole {
		background-color: #f5f5f5;
		height: calc(100vh);
		weight: calc(100vw);
		height: calc(100vh - var(--window-top));
	}

	.u-card-wrap {
		background-color: $u-bg-color;
		padding: 1rpx;
		margin: 0 50rpx;
	}

	.u-body-item {
		font-size: 32rpx;
		padding: 20rpx 20rpx;
		margin-bottom: 16rpx;
		overflow: hidden;
		background-color: #ffffff;
	}

	.u-body-item image {
		width: 120rpx;
		flex: 0 0 120rpx;
		height: 120rpx;
		border-radius: 8rpx;
		margin-left: 12rpx;
		float: left;
	}

	.info-item {
		font-size: large;
		font-style: normal;
		float: left;
		font-weight: 500;
		text-align: left;
		padding-left: 10rpx;
	}

	.remark-item {
		font-size: large;
		color: #a8a7ab;
		float: left;
		text-align: justify;
		padding-left: 10rpx;
	}

	.avatar-item {}

	.info-item-row {
		margin-bottom: 5rpx;
	}
</style>
