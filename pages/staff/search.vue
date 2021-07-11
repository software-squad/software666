<template>
	<view>
		<!-- TODO 上一个页面的搜索框，可以保证页面跳转一致性，但是不能正常输入 -->
		<!-- <view class="u-search-box">
			<view class="u-search-inner">
				<u-icon name="search" color="#909399" :size="28"></u-icon>
				<text @change="gotoSearch" class="u-search-text">请输入员工姓名，不支持模糊搜索</text>
			</view>
		</view> -->

		<view class="u-search-box">
			<u-search v-model='kw' :show-action="true" action-text="搜索" :animation="true" placeholder='请输入员工姓名，不支持模糊搜索'
				@search='gotoSearch' @custom='gotoSearch'></u-search>
		</view>

		<!-- 搜索建议列表 -->
		<!-- <uni-icons type="arrowright" size="16"></uni-icons> -->
		<!-- <view class="sugg-list" v-if="this.kw.length !== 0">
			<view class="sugg-item" v-for="(item, i) in searchResults" :key="i" @click="gotoOne(item)">
				<view class="goods-name">{{item.username}}</view>
			</view>
		</view> -->
		<view class="" v-if="this.kw.length !== 0">
			<view :key="index" v-for="(item,index) in searchResults" @click="gotoOne(item)">
				<view class="u-body-item">
					<image :src="item.faceurl" mode="aspectFill" class="avatar-item"></image>
					<view class="info-item" style="font-weight: bold;">{{item.username}}</view>
					<view class="info-item" style="float: left;">Tel:{{item.tel}}</view>
					<u-tag :text="item.jobname" type="primary" />
				</view>
			</view>
		</view>
		<!-- 搜索历史 -->
		<view class="history-box" v-else>
			<!-- 标题区域 -->
			<view class="history-title">
				<text style="font-size: 30rpx">搜索历史</text>
				<!-- <uni-icons type="trash" size="17" @click="clean"></uni-icons> -->
				<u-icon name="trash" size="40rpx" style="padding-right: 10rpx;" @click="clean"></u-icon>
			</view>
			<!-- 列表区域 -->
			<view class="history-list">
				<u-tag :text="item" v-for="(item, i) in histories" :key="i" @click="gotoUserList(item)" type="info"
					style="margin: 10rpx;padding: 10rpx;" />
			</view>
		</view>
	</view>
</template>

<script>
	export default {
		data() {
			return {
				// 定时器
				timer: null,
				// 搜索框中的关键词
				kw: '',
				// 搜索的结果列表
				searchResults: [],
				// 搜索历史的数组
				historyList: []
			};
		},
		onLoad() {
			console.log("员工搜索中")
			this.historyList = JSON.parse(uni.getStorageSync('kw') || '[]')
		},
		methods: {
			// gotoSearch 输入事件的处理函数
			gotoSearch(e) {
				console.log('搜索中')
				console.log(this.kw)
				if (this.kw.length == 0) {
					return
				}
				this.getSearchList()
				// clearTimeout(this.timer)
				// this.timer = setTimeout(() => {
				// 	this.kw = e.value
				// 	console.log(this.kw)
				// 	this.getSearchList()
				// }, 500)
			},
			getSearchList() {
				console.log("获取搜索列表")

				// 判断搜索关键词是否为空
				if (this.kw.length === 0) {
					this.searchResults = []
					return
				}

				uni.request({
					url: '/api/staff/showUserByUsername',
					method: 'GET',
					data: {
						username: this.kw
					},
					success: (res) => {
						console.log(res)
						if (res.data.code !== 200) alert(res.data.msg)
						this.searchResults = res.data.data
						this.saveSearchHistory()
					}
				})

				// const {
				// 	data: res
				// } = await uni.$http.get('/api/staff/showUserByUsername', {
				// 	query: this.kw
				// })
				// if (res.data.data.code !== 200) return uni.$showMsg()
				// this.searchResults = res.message
				// this.saveSearchHistory()
			},
			gotoOne(item) {
				console.log("即将跳转到个人信息页面")
				console.log(item)
				uni.navigateTo({
					url: '../staff/one?userid=' + item.userid
				})
			},
			saveSearchHistory() {
				console.log("存储搜索历史")
				console.log(this.kw)
				// 重复存储
				// this.historyList.push(this.kw)

				// 不重复存储
				const set = new Set(this.historyList)
				set.delete(this.kw)
				set.add(this.kw)
				this.historyList = Array.from(set)

				// 对搜索历史数据，进行持久化的存储
				uni.setStorageSync('kw', JSON.stringify(this.historyList))
			},

			clean() {
				console.log("清除历史中")
				this.historyList = []
				uni.setStorageSync('kw', '[]')
			},

			gotoUserList(kw) {
				console.log("获取搜索list" + kw)
				this.kw = kw
				this.getSearchList()
			}
		},
		computed: {
			histories() {
				return [...this.historyList].reverse()
			}
		}
	}
</script>

<style lang="scss">
	.u-search-box {
		padding: 15rpx 30rpx;
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

	.search-box {
		position: sticky;
		top: 0;
		z-index: 999;
	}

	.sugg-list {
		padding: 0 5px;

		.sugg-item {
			display: flex;
			align-items: center;
			justify-content: space-between;
			font-size: 12px;
			padding: 13px 0;
			border-bottom: 1px solid #efefef;

			.goods-name {
				white-space: nowrap;
				overflow: hidden;
				text-overflow: ellipsis;
				margin-right: 3px;
			}
		}
	}

	.history-box {
		padding: 0 5px;

		.history-title {
			display: flex;
			justify-content: space-between;
			height: 40px;
			align-items: center;
			font-size: 13px;
			border-bottom: 1px solid #efefef;
		}

		.history-list {
			display: flex;
			flex-wrap: wrap;

			.uni-tag {
				margin-top: 5px;
				margin-right: 5px;
			}
		}
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

	.info-item {
		font-size: large;
		float: left;
		text-align: left;

		padding-left: 10rpx;
		/* border-style: solid;  /* TODO */
	}
</style>
