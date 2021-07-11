<template>
	<view>
		<u-swipe-action :show="item.show" :index="index" :key="item.userid" v-for="(item,index) in userList"
			:options="options" btn-width="180" @click="click" @open="open(index)" @content-click="gotoOne">
			<view class="u-body-item">
				<image :src="item.faceurl" mode="aspectFill" class="avatar-item"></image>
				<view class="info-item">
					<text style="font-weight: bold;">{{item.username}}</text>
				</view>
				<view class="info-item">
					<text style="font-weight: bold;">Tel:{{item.tel}}</text>
				</view>
				<u-tag :text="item.jobname" type="primary" />
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
				userList: [],
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
		onLoad: function() {
			console.log('测试滑动操作')
			uni.setNavigationBarTitle({
				title: '测试滑动操作'
			})
			uni.request({
				url: "/api/staff/showUserByDeptAndJob",
				method: 'GET',
				success: (res) => {
					// console.log(res)
					this.userList = res.data.data
					console.log('设置show')
					for (var i in this.userList) {
						this.userList[i].show = false
					}
					console.log(this.userList)
				}
			})
		},
		methods: {
			click(index, option) {
				if (option == 1) {
					this.delShow = true
					this.delContent = "确认删除" + this.userList[index].username + "？"
					this.delIndex = index
				} else {
					this.navToEdit(index)
				}
			},
			open(index) {
				// 先将正在被操作的swipeAction标记为打开状态，否则由于props的特性限制，
				// 原本为'false'，再次设置为'false'会无效
				console.log('打开中')
				console.log(index)
				console.log(this.userList[index])
				this.userList[index].show = true;
				this.userList.map((val, idx) => {
					if (index != idx) this.userList[idx].show = false;
				})
				console.log(this.userList)
			},
			gotoOne(index) {
				console.log("即将跳转到个人信息页面")
				let item = this.userList[index]
				console.log(item)
				uni.navigateTo({
					url: '../staff/one?userid=' + item.userid
				})
			},
			navToEdit(index) {
				let item = encodeURIComponent(JSON.stringify(this.userList[index]))
				console.log(item)
				uni.navigateTo({
					url: '/pages/staff/edit?item=' + item,
					success() {
						console.log("编辑成功")
					},
					fail() {
						console.log("编辑失败")
					}

				})
			},
			confirmDel() {
				let index = this.delIndex
				uni.request({
					url: '/staff/del',
					method: 'GET',
					success: (res) => {
						// TODO 更友好的提示
						// this.$u.toast(`删除了第${index}个cell`);
						this.userList.splice(index, 1);
					}
				})
				this.delShow = false
				this.$u.toast(`删除成功`);
			},
			cancel() {
				this.delShow = false;
				this.userList[this.delIndex].show = false;
			}
		}
	}
</script>

<style>
	.u-card-wrap {
		background-color: $u-bg-color;
		padding: 1px;
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

	.avatar-item {}
</style>
