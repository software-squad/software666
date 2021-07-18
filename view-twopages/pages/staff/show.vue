<template>
	<view class="page-inner">

		<u-swipe-action :show="item.show" :index="index" :key="item.userid" v-for="(item,index) in searchResults"
			:options="options" btn-width="180" @click="click" @open="open(index)" @content-click="gotoOne(item.userid)"
			class="u-card-wrap">
			<view class="u-body-item">
				<!-- 头像 -->
				<image :src="item.faceurl" mode="aspectFill" class="avatar-item"></image>
				<!-- 信息栏 -->
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

		<!-- 是否删除的模态框 -->
		<u-modal v-model="delShow" :content="delContent" :show-cancel-button="true" :async-close="true"
			@confirm="confirmDel"></u-modal>
		<!-- 消息提示 -->
		<u-toast ref="uToast" />
	</view>

</template>

<script>
	import util from "../../api/util.js"
	export default {
		data() {
			return {
				item: null, // 带参跳转结果存储，部门id和职业id
				delShow: false, // 删除模态框展示
				delContent: '', // 模态框内容
				delIndex: '', // 选中删除对象的索引
				delId: '', // 选中删除对象的id
				searchResults: [], // 搜索员工列表
				options: util.options, // 员工操作功能
			};
		},

		// 增加员工跳转
		onNavigationBarButtonTap: function(e) {
			uni.navigateTo({
				url: '/pages/staff/add'
			})
			// TODO 返回刷新
		},

		// 根据部门和职业搜索员工初始化界面
		onLoad: function(item) {
			// console.log('根据部门和职业搜索员工',item)
			uni.setNavigationBarTitle({
				title: item.jobname
			})
			// 后端申请
			this.item = item
			this.myReload()
		},
		onShow() {
			this.myReload()
		},
		
		// 监听下拉刷新动作的执行方法，每次手动下拉刷新都会执行一次
		onPullDownRefresh() {
			// FIXME 这个会清除返回信息
			// // #ifdef H5
			// window.location.reload()
			// // #endif
			this.myReload(this.parm)
			setTimeout(function() {
				uni.stopPullDownRefresh(); //停止下拉刷新动画
			}, 1000);
		},

		methods: {
			// 获取页面渲染信息
			myReload() {
				this.$api.staffShowUserByDeptAndJob({
					deptid: this.item.deptid,
					jobid: this.item.jobid
				}).then(res => {
					this.searchResults = res.data.data
					for (var i in this.searchResults) {
						this.searchResults[i].show = false
						if (!this.searchResults[i].remark) {
							// 默认备注信息
							this.searchResults[i].remark = '无详细描述'
						}
						if (!this.searchResults[i].faceurl) {
							// 默认头像设置
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
			},
			
			// 点击查看员工信息
			gotoOne(userid) {
				uni.navigateTo({
					url: '../staff/one?userid=' + userid
				})
			},
			
			// 滑动块打开并点击
			click(index, option) {
				if (option == 1) {
					// 自己不能删除自己的逻辑实现
					let currUserid = uni.getStorageSync('userid')
					if (currUserid == this.searchResults[index].userid) {
						this.$refs.uToast.show({
							title: '您无法删除自己',
							type: 'warning',
						})
						return;
					}
					// 删除逻辑
					this.delShow = true
					this.delContent = "确认删除" + this.searchResults[index].username + "？"
					this.delIndex = index
					this.delId = this.searchResults[index].userid
				} else {
					// 编辑逻辑
					this.searchResults[index].show = false
					uni.navigateTo({
						url: '/pages/staff/edit?userid=' + this.searchResults[index].userid,
					})
					this.$forceUpdate() // 强制刷新
					// TODO
					// 方案一：监听navigateBack返回事件，自动刷新
					// 方案二：主页面和子页面数据交互
					// 方案三：下拉刷新（√）
				}
			},

			// 打开滑块
			open(index) {
				console.log('打开第', index, '用户')
				this.searchResults[index].show = true;
				this.searchResults.map((val, idx) => {
					if (index != idx) this.searchResults[idx].show = false;
				})
				this.$forceUpdate() // 强制刷新
			},

			// 确认删除员工
			confirmDel() {
				console.log('删除的id', this.delId)
				this.$api.staffDelData({
					userid: this.delId
				}).then(res => {
					this.searchResults.splice(this.delIndex, 1);
					this.delShow = false
					this.$refs.uToast.show({
						title: '删除成功',
						type: 'success',
					})
				})
			},
			
			// 取消删除
			cancel() {
				this.delShow = false;
				this.searchResults[this.delIndex].show = false;
				this.$forceUpdate()
			}
		}
	}
</script>

<style>
	.page-inner {
		background-color: #fafafa;
		height: calc(100vh);
		/* #ifdef H5 */
		height: calc(100vh - var(--window-top));
		/* #endif */
		display: flex;
		flex-direction: column;
	}

	.u-card-wrap {
		background-color: #FFFFFF;
		margin: 20rpx 0rpx 0rpx 0rpx;
	}

	.u-body-item {
		font-size: 32rpx;
		color: #333;
		padding: 20rpx 20rpx;
		overflow: hidden;
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
		float: left;
		text-align: left;
		padding-left: 20rpx;
	}

	.info-item-row {
		margin-bottom: 5rpx;
	}

	.avatar-item {
		margin-right: 10rpx;
	}
</style>
