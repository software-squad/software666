<template>
	<view>
		<u-toast ref="uToast" />
		<view class="search">
			<u-search placeholder="请输入职位名称" v-model="searchJobName" shape="round" @change="search" :show-action="false">
			</u-search>
		</view>
		<view :index="index" v-for="(item,index) in jobsShow" @click="navToEdit(item,index)">
			<view class="u-body-item">
				<view class="info-item" style="font-weight: bold;">职位名称:{{item.jobname}}</view>
				<view class="info-item">职位描述:{{item.remark}}</view>
			</view>
			</navigator>
		</view>
	</view>
</template>

<script>
	//import sendThis 函数，实现拦截器统一拦截msg码弹窗
	import {
		sendThis
	} from "../../api/request.js"
	import {
		jobShowSendData
	} from "../../api/api.js"
	export default {
		data() {
			return {
				searchJobName: '',
				keyword: '',
				jobs: [],
				jobsShow: [],

			}
		},
		onLoad() {
			sendThis(this)
			jobShowSendData()
				.then((response) => {
					this.jobs = []
					console.log("response")
					console.log(response.data.data)
					for (let i = 0; i < response.data.data.length; i++) {
						let d = {
							jobid: response.data.data[i].jobid,
							jobname: response.data.data[i].jobname,
							remark: response.data.data[i].remark,
						}
						this.jobs.push(d)
					}
					console.log("jobs")
					console.log(this.jobs)
					this.jobsShow = this.jobs
				})
				.catch((error) => {
					console.log(error);
				})
		},
		onNavigationBarButtonTap: function(e) {
			uni.navigateTo({
				url: "oneAdd"
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
			search() {
				if (this.searchJobName == "") {
					this.jobsShow = this.jobs
				} else {
					this.jobsShow = []
					this.jobs.forEach((item) => {
						if (item.jobname.includes(this.searchJobName))
							this.jobsShow.push(item)
					})
				}
			},

			navToEdit(item, index) {
				uni.navigateTo({
						url: "user_one?item=" + encodeURIComponent(JSON.stringify(item))
					}),
					console.log("show")
				// console.log(item.name),
				// console.log(item.dcrpt)
			},
		}
	}
</script>

<style>
	.search {
		margin: 0 50rpx;
		margin-top: 30rpx;
	}

	.u-card-wrap {
		background-color: $u-bg-color;
		padding: 1rpx;
		margin: 0 50rpx;
	}

	.u-body-item {
		font-size: 32rpx;
		color: #333;
		padding: 20rpx 20rpx;
		margin: 30rpx 20rpx;
		border-style: solid;
		/* TODO */
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

	.info-item {
		font-size: large;
		float: left;
		text-align: left;

		padding-left: 10rpx;
		/* border-style: solid;  /* TODO */
	}

	.avatar-item {}
</style>
