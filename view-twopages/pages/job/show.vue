<template>
	<view class="whole">
			<view class="search">
				<u-sticky bg-color="#f5f5f5">
					<u-search placeholder="请输入职位名称" v-model="searchJobName" shape="round" @change="search"
						bg-color="#ffffff" border-color='#fdfcfa' :show-action="false"></u-search>
				</u-sticky>
			</view>
			<u-gap height="20" bg-color="#f5f5f5"></u-gap>
			<!-- 循环展示所有要显示的职位信息 -->
			<view :index="index" v-for="(item,index) in jobsShow" @click="navToEdit(item,index)">
				<view class="u-body-item">
					<u-row class="info-item-row">
						<u-col span="12">
							<view class="info-item" style="font-weight: bold;">{{item.jobname}}</view>
							<view class="info-item" style="font-weight: lighter;">| {{item.deptname}}</view>
						</u-col>
						
					</u-row>
					<u-row>
						<u-col span="12">
							<view class="remark-item">详情:{{item.remark}}</view>
						</u-col>
					</u-row>
				</view>
				<u-gap height="10" bg-color="#f5f5f5"></u-gap>
				</navigator>
			</view>
		</view>
	</template>
</template>

<script>
	import {sendThis} from "../../api/request.js"
	import {jobShowSendData} from "../../api/api.js"
	export default {
		data() {
			return {
				searchJobName:'',
				keyword:'',
				jobs: [],
				jobsShow:[],
				
			}
		},
		// 页面加载时
		onLoad() {
			// 将当前页面的this发送到js函数便于拦截错误码
			sendThis(this)
			// 初始化职位显示信息
			this.myReload()
		},
		onShow() {
			this.myReload()
		},
		methods: {
			// 请求职位信息接口并在前端展示响应结果
			myReload(){
				jobShowSendData().then((response) => {
					this.jobs = []
					console.log("response")
					console.log(response.data.data)
					// 遍历响应中的职位信息，全部加入到前端缓存的数组中
					for (let i = 0; i < response.data.data.length; i++) {
						let d = {
							jobid: response.data.data[i].jobid,
							jobname: response.data.data[i].jobname,
							deptname:response.data.data[i].deptname,
							remark: response.data.data[i].remark,
						}
						this.jobs.push(d)
					}
					console.log("jobs")
					console.log(this.jobs)
					// 将缓存数组的值赋值给显示数组中
					this.jobsShow = this.jobs
				})
				.catch((error) => {
					console.log(error);
				})
			},
			// 跳转到添加职位页面
			onNavigationBarButtonTap:function(e){
			    uni.navigateTo({
			    	url:"oneAdd"
			    })
			},
			// 拦截错误码并显示时会调用的函数
			showToast(TITLE,TYPE) {
							this.$refs.uToast.show({
								title: TITLE.toString(),
								type: TYPE.toString(),
							})
			},
			// 动态搜索框
			search(){
				// 如果搜索框内容为空，表示用户不使用该组件，显示全部内容
				if(this.searchJobName == ""){
					this.jobsShow = this.jobs
				}
				// 否则根据搜索关键字修改显示内容
				else {
					this.jobsShow = []
					this.jobs.forEach((item) => {
						// 如果职位名字包含关键字，添加进展示的数组中
						if(item.jobname.includes(this.searchJobName))
						this.jobsShow.push(item)
					})
				}
			},
			// 跳转到查看单个职位信息的页面
			navToEdit(item,index){
				uni.navigateTo({
					// 带参跳转，将选中职位的信息传至目标页面
					// TODO 记得检验一下登录逻辑
					url: "one?item="+encodeURIComponent(JSON.stringify(item))
				}),
				console.log("show")
			},
		}
	}
</script>

<style>
	.whole {
		background-color: #f5f5f5;
		height: calc(100vh);
		/* 	#ifdef H5*/
		height: calc(100vh - var(--window-top));
		/* #endif */
	}

	/* 	.search{
		margin: 0 50rpx;
		margin-top: 30rpx;
	} */

	.u-card-wrap {
		background-color: $u-bg-color;
		padding: 1rpx;
		margin: 0 50rpx;
	}

	.u-body-item {
		font-size: 32rpx;
		color: #333;
		padding: 20rpx 20rpx;
		margin-top: -10rpx;
		margin-bottom: 16rpx;
		background-color: #ffffff;
		/* TODO*/
		overflow: hidden;
	}

	.u-body-item image {
		width: 120rpx;
		flex: 0 0 120rpx;
		height: 120rpx;
		border-radius: 8rpx;
		margin-left: 12rpx;
		/* border-style: solid;  /* TODO */
		float: left;
	}

	.u-search-box {
		padding: 18rpx 30rpx;
	}

	.u-search-inner {
		background-color: rgb(234, 234, 234);
		border-radius: 100rpx;
		display: flex;
		align-items: center;
		padding: 10rpx 16rpx;
	}

	.u-search-text {
		font-size: 26rpx;
		color: $u-tips-color;
		margin-left: 10rpx;
	}
	.info-item-row{
		margin-bottom: 5rpx;
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
	.remark-item{
		font-size: 35rpx;
		/* color: #a8a7ab; */
		color: #4d669e;
		float: left;
		text-align: justify;
		padding-left: 10rpx;
		/* padding-left: -60rpx; */
	}
	.avatar-item {}
</style>

