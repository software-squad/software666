<template>
	<view class="page-inner">

		<!-- 搜索框 -->
		<view class="u-search-box">
			<u-sticky bg-color="#fafafa">
							<u-search v-model='kw' :show-action="true" action-text="搜索" :animation="true" height="80"
								placeholder='请输入员工姓名' @search='getSearchList' @custom='getSearchList' @change="change">
							</u-search>
						</u-sticky>
		</view>

		<!-- 搜索建议列表 -->
		<view class="sugg-list" v-if="this.kw.length !== 0">
			<u-swipe-action :index="index" :key="item.userid" v-for="(item,index) in searchResults" :show="item.show"
				:options="options" btn-width="180" @click="click" @open="open(index)"
				@content-click="gotoOne(item.userid)" >
				<view class="u-body-item">
					<image :src="item.faceurl" mode="aspectFill" class="avatar-item"></image>

					<!-- TODO 调成u-image 有默认头像格式 -->
					<!-- shape="circle" -->
					<u-image width='120rpx' height='120rpx' slot="title" :src="item.faceurl" mode="aspectFill">
					</u-image>

					<view calss="info-item">
						<u-row class="info-item-row">
							<u-col span=12>
								<text style="font-size: larger;font-weight: bold;">{{item.username}}</text>
							</u-col>
						</u-row>
						<u-row class="info-item-row">
							<u-col span="12">
								<text>{{item.sex}}&nbsp;|&nbsp;{{item.deptname}}&nbsp;|&nbsp;{{item.jobname}}</text>
							</u-col>
						</u-row>
						<u-row class="info-item-row">
							<u-col span="12">
								<view class="u-line-2" style="color: #C0C4CC;">{{item.remark}}</view>
							</u-col>
						</u-row>
					</view>
				</view>
			</u-swipe-action>
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

		<!-- 模态框是否确认传输 -->
		<u-modal v-model="delShow" :content="delContent" :show-cancel-button="true" :async-close="true"
			@confirm="confirmDel"></u-modal>

		<!-- 提示 -->
		<u-toast ref="uToast" />
	</view>
</template>

<script>
	export default {
		data() {
			return {
				timer: null, // 定时器
				kw: '', // 搜索框中的关键词
				searchResults: [], // 搜索的结果列表
				historyList: [], // 搜索历史的数组
				delShow: false,
				delContent: '',
				delIndex: '',
				delId: '',
				options: [{
						text: '编辑',
						style: {
							backgroundColor: '#007aff'
						}
					},
					{
						text: '删除',
						style: {
							backgroundColor: '#dd524d'
						}
					}
				],
			};
		},
		onNavigationBarButtonTap: function(e) {
			uni.navigateTo({
				url: '/pages/staff/add'
			})
		},
		onLoad() {
			console.log("员工搜索中")
			this.historyList = JSON.parse(uni.getStorageSync('kw') || '[]')
		},
		methods: {
			// change 输入事件的处理函数
			change(e) {
				if (this.kw.length == 0) {
					this.searchResults = []
					return
				}
				// 动态搜索
				clearTimeout(this.timer)
				this.timer = setTimeout(() => {
					this.getSearchList()
				}, 500)
			},
			getSearchList() {
				console.log("获取搜索列表")
				// 判断搜索关键词是否为空
				if (this.kw.length === 0) {
					this.searchResults = []
					return
				}
				this.$request.request({
					url: '/api/staff/showUserByUsername',
					data: {
						username: this.kw,
					},
					method: 'GET',
				}).then(res => {
					if (res.data.code !== 200) alert(res.data.msg)
					this.searchResults = res.data.data
					for (var i in this.searchResults) {
						this.searchResults[i].show = false
						if (!this.searchResults[i].remark) {
							this.searchResults[i].remark = '无详细描述'
						}
						if (!this.searchResults[i].faceurl) {
							if (this.searchResults[i].sex == '男') {
								this.searchResults[i].faceurl = '/static/boy1.svg'
							} else if (this.searchResults[i].sex == '女') {
								this.searchResults[i].faceurl = '/static/girl1.svg'
							} else {
								this.searchResults[i].faceurl = '/static/头像.svg'
							}
						}
					}
					this.saveSearchHistory()
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
			},

			click(index, option) {
				if (option == 1) {
					this.delShow = true
					this.delContent = "确认删除" + this.searchResults[index].username + "？"
					this.delIndex = index
					this.delId = this.searchResults[index].userid
				} else {
					this.navToEdit(index)
					this.searchResults[index].show = false
				}
			},
			open(index) {
				// 先将正在被操作的swipeAction标记为打开状态，否则由于props的特性限制，
				// 原本为'false'，再次设置为'false'会无效
				console.log('打开中')
				console.log(index)
				console.log(this.searchResults[index])
				this.searchResults[index].show = true;
				this.searchResults.map((val, idx) => {
					if (index != idx) this.searchResults[idx].show = false;
				})
				console.log(this.searchResults)
			},
			gotoOne(userid) {
				console.log("即将跳转到个人信息页面")
				uni.navigateTo({
					url: '../staff/one?userid=' + userid
				})
			},
			navToEdit(index) {
				uni.navigateTo({
					url: '/pages/staff/edit?item=' + this.searchResults[index].userid,
				})
			},
			confirmDel() {
				let index = this.delIndex
				this.$request.request({
					url: '/api/staff/del',
					data: {
						userid: this.delId,
					},
					method: 'GET',
				}).then(res => {
					this.searchResults.splice(index, 1);
				})

				this.delShow = false
				this.$refs.uToast.show({
					title: '删除成功',
					type: 'success',
				})
			},
			cancel() {
				this.delShow = false;
				this.searchResults[this.delIndex].show = false;
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
	.page-inner {
		background-color: #fafafa;
		height: calc(100vh);
		/* #ifdef H5 */
		height: calc(100vh - var(--window-top));
		/* #endif */
		display: flex;
		flex-direction: column;
		/* border-style: solid; */
	}

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
		// margin: 30rpx 20rpx;
		// border-style: solid;
		/* TODO */
		overflow: hidden;
	}

	.u-body-item {
		font-size: 32rpx;
		color: #333;
		padding: 20rpx 20rpx;
		/* border-style: solid; */
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

	.avatar-item {
		margin-right: 10rpx;
	}

	.info-item-row {
		margin-bottom: 5rpx;
	}
</style>
