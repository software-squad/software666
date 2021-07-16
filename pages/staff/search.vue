<template>
	<view class="page-inner">

		<!-- 搜索框 -->
		<view class="u-search-box">
			<u-sticky bg-color="#fafafa">
				<u-search v-model='kw' :show-action="true" action-text="搜索" :animation="true" placeholder='请输入员工姓名,支持模糊搜索'
					@search='search' @custom='search' @change="change">
				</u-search>
			</u-sticky>
		</view>

		<!-- 搜索建议列表 -->
		<view class="sugg-list" v-if="this.kw.length !== 0">
			<u-swipe-action :index="index" :key="item.userid" v-for="(item,index) in searchResults" :show="item.show"
				:options="options" btn-width="180" @click="click" @open="open(index)"
				@content-click="gotoOne(item.userid)">
				<view class="u-body-item">
					<image :src="item.faceurl" mode="aspectFill" class="avatar-item"></image>
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
	import util from "../../api/util.js"
	export default {
		data() {
			return {
				timer: null, // 定时器
				kw: '', // 搜索框中的关键词
				searchResults: [], // 搜索的结果列表
				historyList: [], // 搜索历史的数组
				delShow: false, // 删除模态框展示
				delContent: '', // 模态框内容
				delIndex: '', // 选中删除对象的索引
				delId: '', // 选中删除对象的id
				options: util.options, // 滑动框的功能按钮
			};
		},

		onNavigationBarButtonTap: function(e) {
			uni.navigateTo({
				url: '/pages/staff/add'
			})
		},

		onPullDownRefresh() {
			this.myReload()
			setTimeout(function() {
				uni.stopPullDownRefresh(); //停止下拉刷新动画
			}, 1000);
		},

		onLoad() {
			console.log("员工搜索中")
			this.historyList = JSON.parse(uni.getStorageSync('kw') || '[]')
		},

		methods: {

			// change 动态处理触发搜索事件
			change(e) {
				if (this.kw.length == 0) {
					this.searchResults = []
					return
				}
				// 动态搜索
				clearTimeout(this.timer)
				this.timer = setTimeout(() => {
					this.myReload()
				}, 500)
			},

			// enter触发或点击搜索触发搜索事件
			search() {
				this.myReload()
				this.saveSearchHistory()
			},

			// 点击搜索历史标签，触发搜索历史
			gotoUserList(kw) {
				console.log("点击搜索历史标签" + kw)
				this.kw = kw
				this.myReload()
			},

			// 获取搜索列表
			myReload() {
				// console.log("获取搜索列表")
				// 判断搜索关键词是否为空
				if (this.kw.length === 0) {
					this.searchResults = []
					return
				}
				this.$api.staffShowUserByUsername({
					username: this.kw,
				}).then(res => {
					// 非200信息提示
					// if (res.data.code !== 200) alert(res.data.msg)
					this.searchResults = res.data.data
					for (var i in this.searchResults) {
						this.searchResults[i].show = false
						if (!this.searchResults[i].remark) {
							// 备注信息默认展示
							this.searchResults[i].remark = '无详细描述'
						}

						if (!this.searchResults[i].faceurl) {
							// 默认头像展示
							if (this.searchResults[i].sex == '男') {
								this.searchResults[i].faceurl = '/static/boy1.svg'
							} else if (this.searchResults[i].sex == '女') {
								this.searchResults[i].faceurl = '/static/girl1.svg'
							} else {
								this.searchResults[i].faceurl = '/static/头像.svg'
							}
						}
					}
				})
				// this.saveSearchHistory()
			},

			// 存储搜索历史
			saveSearchHistory() {
				// console.log("存储搜索历史:",this.kw)

				// 关键字不判重
				// this.historyList.push(this.kw)

				// 关键字判重
				const set = new Set(this.historyList)
				set.delete(this.kw)
				set.add(this.kw)
				this.historyList = Array.from(set)

				// 对搜索历史数据，进行持久化的存储
				uni.setStorageSync('kw', JSON.stringify(this.historyList))
			},

			// 清空搜索历史
			clean() {
				this.historyList = []
				uni.setStorageSync('kw', '[]')
			},
			
			// 查看一个用户具体信息
			gotoOne(userid) {
				console.log("即将跳转到个人信息页面", userid)
				uni.navigateTo({
					url: '../staff/one?userid=' + userid
				})
			},
			
			// 用户滑块功能点击
			click(index, option) {
				if (option == 1) {
					// ==========点击删除==========
					// // #ifdef H5
					// let currUserid = sessionStorage.getItem('userid')
					// // #endif

					// 自己不能删除自己的逻辑实现
					let currUserid = uni.getStorageSync('userid')
					if (currUserid == this.searchResults[index].userid) {
						this.$refs.uToast.show({
							title: '您无法删除自己',
							type: 'warning',
						})
						return;
					}
					// 触发删除确认模态框
					this.delShow = true
					this.delContent = "确认删除" + this.searchResults[index].username + "？"
					this.delIndex = index
					this.delId = this.searchResults[index].userid
				} else {
					// ==========点击编辑==========
					this.searchResults[index].show = false
					uni.navigateTo({
						url: '/pages/staff/edit?userid=' + this.searchResults[index].userid,
					})
					this.$forceUpdate()
					// TODO 
					// 方案一：监听navigateBack返回事件，自动刷新
					// 方案二：主页面和子页面数据交互
					// 方案三：下拉刷新（√）
				}
			},

			// 其他员工的功能键隐藏
			open(index) {
				// 先将正在被操作的swipeAction标记为打开状态，否则由于props的特性限制，
				// 原本为'false'，再次设置为'false'会无效
				console.log('打开第', index, '用户')
				this.searchResults[index].show = true;
				this.searchResults.map((val, idx) => {
					if (index != idx) this.searchResults[idx].show = false;
				})
				this.$forceUpdate()
			},

			
			// 删除用户
			confirmDel() {
				let index = this.delIndex
				this.$api.staffDelData({
					userid: this.delId,
				}).then(res => {
					this.searchResults.splice(index, 1);
				})

				this.delShow = false
				this.$refs.uToast.show({
					title: '删除成功',
					type: 'success',
				})
			},

			// 取下删除操作
			cancel() {
				this.delShow = false;
				this.searchResults[this.delIndex].show = false;
				this.$forceUpdate()
			}
		},

		// 历史按时间顺序取反
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
