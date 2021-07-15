<template>
	<view class="page-inner">
		<view :index="index" :key="item.userid" v-for="(item,index) in searchResults"
			 @click="gotoOne(item.userid)"
			 class="u-card-wrap">
			<view class="u-body-item">
				<image :src="item.faceurl" mode="aspectFill" class="avatar-item"></image>
				
				<!-- TODO 调成u-image 有默认头像格式 -->
				<!-- shape="circle" -->
				<u-image width='120rpx' height='120rpx' slot="title" :src="item.faceurl" 
				mode="aspectFill"></u-image>
				
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
		</view>
	</view>

</template>

<script>
	export default {
		data() {
			return {
				item:null,
				delShow: false, 
				delContent: '',
				delIndex: '',
				searchResults: [],
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
		// 增加员工
		onNavigationBarButtonTap: function(e) {
			uni.navigateTo({
				url: '/pages/staff/add'
			})
			// TODO 返回刷新
		},
		onLoad: function(item) {
			// console.log('根据部门和职业搜索员工',item)
			uni.setNavigationBarTitle({
				title: item.jobname
			})
			// 后端申请
			this.parm = item
			this.myReload(item)
		},
		onPullDownRefresh() {
			// 监听下拉刷新动作的执行方法，每次手动下拉刷新都会执行一次
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
			myReload(item){
				this.$api.staffShowUserByDeptAndJob({
					deptid: item.deptid,
					jobid: item.jobid
				}).then(res => {
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
				})
			},
			
			// 点击进入
			gotoOne(userid) {
				uni.navigateTo({
					url: '../staff/one?userid=' + userid
				})
			},
		}
	}
</script>

<style>
	
	.page-inner{
		background-color: #fafafa;
		height: calc(100vh);
		/* #ifdef H5 */
		height: calc(100vh - var(--window-top));
		/* #endif */
		display: flex;
		flex-direction: column;
		/* border-style: solid; */
	}
	.u-card-wrap {
		background-color: #FFFFFF;
		margin: 20rpx 0rpx 0rpx 0rpx;
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
		float: left;
		text-align: left;
		padding-left: 20rpx;
		/* border-style: solid;  /* TODO */ 
	}

	.info-item-row{
		margin-bottom: 5rpx;
	}
	
	.avatar-item{
		margin-right: 10rpx;
	}
</style>
