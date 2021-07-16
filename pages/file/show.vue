<template>
	<view class="whole">
		<!-- 搜索框 -->
		<u-gap height="10"></u-gap>
		<view class="search">
			<u-sticky bg-color="#f5f5f5">
				<u-search placeholder="请输入文件标题" v-model="searchFileTitle" shape="round" @change="search"
					bg-color="#ffffff" border-color='#fdfcfa' :show-action="false"></u-search>
			</u-sticky>
		</view>
		<!-- 展示页面 -->
		<u-swipe-action :show="item.show" :index="index" :key="item.fileid" v-for="(item,index) in itemShows"
			:options="options" btn-width="180" @click="click" @open="open(index)" @content-click="navToOne(index)"
			class="u-card-wrap">
			<view class="u-body-item">
				<u-row class="info-item-row">
					<u-col span="12">
						<view class="info-item" style="font-weight: bold;">{{item.title}}</view>
					</u-col>
				</u-row>
				<u-row>
					<u-col span="12">
						<view class="remark-item">简介:{{item.remark}}</view>
					</u-col>
				</u-row>
				<u-gap height="10"></u-gap>
				<u-tag :text="item.createdate" type="info" mode="plain" shape="circle" />
			</view>
		</u-swipe-action>
		<u-modal v-model="delShow" :content="delContent" :show-cancel-button="true" :async-close="true"
			@confirm="confirmDel"></u-modal>
		<u-toast ref="uToast"></u-toast>
	</view>
</template>

<script>
	import util from "../../api/util.js"
	export default {
		data() {
			return {
				delShow: false,
				delContent: '',
				delIndex: '',
				delId: '',
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
			// TODO 编辑后必须重新获取数据，这里为啥刷新不了
			console.log('开始刷新')
			this.myReload()
			// FIXME 这里的时限控制貌似不太成功诶
			setTimeout(function() {
				uni.stopPullDownRefresh(); //停止下拉刷新动画
				console.log('刷新结束')
			}, 1000);
		},

		onLoad() {
			this.myReload()
		},

		onNavigationBarButtonTap() {
			uni.navigateTo({
				url: "upload"
			})
		},

		methods: {
			// 自定义加载页面参数
			myReload() {
				// 获取文档列表
				// console.log('文件刷新成功啦')
				this.$api.fileShowMany().then(res => {
					// 异常码判断
					if (res.data.msg == "10007") {
						this.items = res.data.data
						this.itemShows = res.data.data
						
						for (var i in this.itemShows) {
							var str = this.itemShows[i].filename.split(14)
							console.log('字符串切片',str)
							this.itemShows[i].filename = str
							this.items[i].filename = str
							this.itemShows[i].show = false
							this.items[i].show = false
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

			// 右滑
			click(index, option) {
				if (option == 1) {
					// 删除功能
					this.delShow = true
					this.delContent = "确认删除" + this.itemShows[index].title + "？"
					this.delIndex = index
					this.delId = this.itemShows[index].fileid
				} else {
					// 编辑功能
					this.itemShows[index].show = false
					uni.navigateTo({
						url: '/pages/file/edit?item=' + encodeURIComponent(JSON.stringify(this.itemShows[index]))
					})
					this.$forceUpdate() // 页面强制渲染
				}
			},

			// 关闭其他滑块
			open(index) {
				// 先将正在被操作的swipeAction标记为打开状态，否则由于props的特性限制，
				// 原本为'false'，再次设置为'false'会无效
				console.log(this.itemShows[index])
				this.itemShows[index].show = true;
				this.itemShows.map((val, idx) => {
					if (index != idx) this.itemShows[idx].show = false;
				})
				this.$forceUpdate() // 页面强制渲染
			},

			// 确认删除后即可
			confirmDel() {
				let index = this.delIndex
				this.$api.fileDel({
					fileid: this.delId,
				}).then(res => {
					console.log('回调成功')
					if (res.data.msg == 10003) {
						// TODO 删除会重复index
						console.log('删除成功啦')
						for (var i in this.itemShows) {
							if (this.itemShows[i].fileid == this.delId) {
								this.itemShows.splice(i, 1);
								console.log('itemShows删除了第',i,'个')
							}
							if (this.items[i].fileid == this.delId) {
								this.items.splice(i, 1);
								console.log('items删除了第',i,'个')
							}
						}
						this.$refs.uToast({
							title: `删除成功`
						})
						this.myReload()
					}
				})
				this.delShow = false
			},

			// 取消文件删除
			cancel() {
				this.delShow = false;
				this.itemShows[this.delIndex].show = false;
				this.$forceUpdate() // 页面强制渲染
			}

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
		font-size: large;
		color: #a8a7ab;
		float: left;
		text-align: justify;
		padding-left: 10rpx;
	}

	.avatar-item {}

	.u-card-wrap {
		background-color: #FFFFFF;
		margin: 20rpx 0rpx 0rpx 0rpx;
	}
</style>
