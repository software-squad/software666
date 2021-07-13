<template>
	<view class="page-inner">
		<u-swipe-action :show="item.show" :index="index" :key="item.userid" v-for="(item,index) in searchResults"
			:options="options" btn-width="180" @click="click" @open="open(index)" @content-click="gotoOne(item.userid)"
			 class="u-card-wrap">
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
		<u-modal v-model="delShow" :content="delContent" :show-cancel-button="true" :async-close="true"
			@confirm="confirmDel"></u-modal>
	</view>

</template>

<script>
	export default {
		data() {
			return {
				delShow: false,
				delContent: '',
				delIndex: '',
				searchResults: [],
				verticalLine:"  |  ",
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
			console.log('点击加号')
			let data = {
				isadd: true,
				employee: ''
			}
			let item = encodeURIComponent(JSON.stringify(data))
			uni.navigateTo({
				url: '/pages/staff/add'
			})
		},
		onLoad: function(item) {
			console.log('根据部门和职业搜索员工')
			console.log(item)
			uni.setNavigationBarTitle({
				title: item.jobname
			})
			this.$request.request({
				url: "/api/staff/showUserByDeptAndJob",
				data: {
					deptid: item.deptid,
					jobid: item.jobid
				},
				method:'POST',
				}).then(res=>{
					this.searchResults = res.data.data
					for (var i in this.searchResults) {
						this.searchResults[i].show = false
						if(!this.searchResults[i].remark){
							this.searchResults[i].remark = '无详细描述'
						}
					}
				})
		},
		methods: {
			click(index, option) {
				if (option == 1) {
					this.delShow = true
					this.delContent = "确认删除" + this.searchResults[index].username + "？"
					this.delIndex = index
					this.delId = this.searchResults[index].userid
				} else {
					this.navToEdit(index)
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
				uni.navigateTo({
					url: '../staff/one?userid=' + userid
				})
			},
			navToEdit(index) {
				// console.log('准备编辑')
				// console.log(this.searchResults[index])
				uni.navigateTo({
					url: '/pages/staff/edit?userid=' + this.searchResults[index].userid,
				})
			},
			confirmDel() {
				let index = this.delIndex
				console.log('删除的id')
				console.log(this.delId)
				this.$request.request({
					url: '/api/staff/del',
					data:{userid:this.delId,},
					method: 'GET',
					}).then(res=>{
						// TODO 更友好的提示
						// this.$u.toast(`删除了第${index}个cell`);
						this.searchResults.splice(index, 1);
					})
				this.delShow = false
				this.$u.toast(`删除成功`);
			},
			cancel() {
				this.delShow = false;
				this.searchResults[this.delIndex].show = false;
			}
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
