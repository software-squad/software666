<template>
	<view class="whole">
		<u-gap height="10"></u-gap>
		<!-- 搜索栏 -->
		<view class="search">
			<u-sticky bg-color="#f5f5f5">
				<u-search placeholder="请输入文件标题" v-model="searchFileTitle" shape="round" @change="search"
					bg-color="#ffffff" border-color='#fdfcfa' :show-action="false"></u-search>
			</u-sticky>
		</view>
		
		<!-- 文件信息展示 -->
		<view :index="index" :key="item.fileid" v-for="(item,index) in itemShows" @click="navToOne(index)"
			class="u-card-wrap">
			<view class="u-body-item">
				<!-- <image :src="item.faceurl" mode="aspectFill" class="avatar-item"></image> -->
				<u-row class="info-item-row">
					<u-col span="12">
						<view class="info-item" style="font-weight: bold;">{{item.title}}</view>
					</u-col>
				</u-row>
				<u-row>
					<u-col span="12">
						<view class="remark-item" style="float: left;">{{item.filename}}</view>
					</u-col>
				</u-row>
				<u-gap height="10"></u-gap>
				<u-tag :text="item.createdate" type="info" mode="plain" shape="circle" />
			</view>
		</view>
		<u-toast ref="uToast"></u-toast>
	</view>
</template>

<script>
	import util from "../../api/util.js"
	export default {
		data() {
			return {
				items: [],
				itemShows: [],
				searchFileTitle: '',
				options: util.options,
			}
		},

		onPullDownRefresh() {
			// 监听下拉刷新动作的执行方法，每次手动下拉刷新都会执行一次
			// FIXME 这个会清除返回信息
			// // #ifdef H5
			// window.location.reload()
			// // #endif
			console.log('开始刷新')
			this.myReload()
			// FIXME 这里的时限控制貌似不太成功诶
			// TODO 这里的时间会不会太长
			setTimeout(function() {
				uni.stopPullDownRefresh(); //停止下拉刷新动画
			}, 4000);
			console.log('刷新结束')
		},

		onLoad() {
			this.myReLoad()
		},

		methods: {
			// 自定义加载页面参数
			myReLoad() {
				// 获取文档列表
				this.$api.fileShowMany().then(res => {
					// 异常码判断
					if (res.data.msg == "10007") {
						this.items = res.data.data
						this.itemShows = res.data.data
						for (var i in this.itemShows) {
							this.itemShows[i].show = false
						}
					} else {
						this.$refs.uToast({
							title: `数据获取失败`
						})
					}
				}).catch(err => {})
			},

			// 文件查看
			navToOne(index) {
				let item = encodeURIComponent(JSON.stringify(this.itemShows[index]))
				uni.navigateTo({
					url: 'one?item=' + item
				})
			},

			// 文件搜索
			search() {
				if (this.searchFileTitle == "") {
					this.itemShows = this.items
				} else {
					this.itemShows = []
					this.items.forEach((item) => { // 实现动态搜索
						if (item.title.includes(this.searchFileTitle))
							this.itemShows.push(item)
					})
				}
			},
		}
	}
</script>

<style>
	/* 	.search{
		background-color:  #f5f5f5;
	} */
	.whole {
		background-color: #f5f5f5;
		height: calc(100vh);
		/* 	#ifdef H5*/
		height: calc(100vh - var(--window-top));
		/* #endif */
	}

	.u-card-wrap {
		background-color: $u-bg-color;
		padding: 1px;
		/* border-style: solid; */
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
		/* border-style: solid; */
		float: left;
	}

	.info-item {
		font-size: large;
		font-style: normal;
		float: left;
		/* font-weight:500; */
		text-align: left;
		/* padding-left: 10rpx; */
		/* border-style: solid;  /* TODO */
	}

	.info-item-row {
		margin-bottom: 5rpx;
	}

	.remark-item {
		font-size: larger;
		font-style: oblique;
		color: #699df3;
		float: left;
		text-align: justify;
		padding-left: 10rpx;
		/* padding-left: -60rpx; */
	}

	.avatar-item {}

	.u-card-wrap {
		background-color: #FFFFFF;
		margin: 20rpx 0rpx 0rpx 0rpx;
	}
</style>
