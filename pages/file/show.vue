<template>
	<view>
		<u-gap height="10"></u-gap>
		<view class="search">
			<u-sticky>
				<u-search placeholder="请输入文件标题" v-model="searchFileTitle" shape="round" @change="search"
					:show-action="false"></u-search>
			</u-sticky>
		</view>

		<u-swipe-action :show="item.show" :index="index" :key="item.fileid" v-for="(item,index) in itemShows"
			:options="options" btn-width="180" @click="click" @open="open(index)" @content-click="navToOne(index)"
			class="u-card-wrap">
			<view class="u-body-item">
				<!-- <image :src="item.faceurl" mode="aspectFill" class="avatar-item"></image> -->
				<view class="info-item" style="font-weight: bold;">文件标题：{{item.title}}</view>
				<view class="info-item" style="float: left;">文件名称：{{item.filename}}</view>
				<u-tag :text="item.createdate" type="primary" />
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
				delId: '',
				items: [],
				itemShows: [],
				searchFileTitle: '',
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
			}
		},

		async onLoad() {
			await this.$request.request({
				url: '/api/file/showmany',
				method: 'GET',
			}).then(res => {
				if (res.data.msg == "10007") {
					this.items = res.data.data
					this.itemShows = res.data.data
					for (var i in this.itemShows) {
						this.itemShows[i].show = false
					}
				} else {
					this.$u.toast(`数据获取失败`);
				}
			}).catch(err => {})
		},

		onNavigationBarButtonTap() {
			uni.navigateTo({
				url: "upload"
			})
		},

		methods: {
			navToOne(index) {
				let item = encodeURIComponent(JSON.stringify(this.itemShows[index]))
				uni.navigateTo({
					url: 'one?item=' + item
				})
			},

			navToSearchByFilename() {
				uni.navigateTo({
					url: './search',
					success() {
						console.log('回到广场')
					}
				})
			},

			search() {
				if (this.searchFileTitle == "") {
					this.itemShows = this.items
				} else {
					this.itemShows = []
					this.items.forEach((item) => {
						if (item.title.includes(this.searchFileTitle))
							this.itemShows.push(item)
					})
				}
			},

			click(index, option) {
				if (option == 1) {
					this.delShow = true
					this.delContent = "确认删除" + this.itemShows[index].title + "？"
					this.delIndex = index
					this.delId = this.itemShows[index].fileid
				} else {
					uni.navigateTo({
						url: '/pages/file/edit?item=' + encodeURIComponent(JSON.stringify(this.itemShows[index]))
					})
				}
			},

			open(index) {
				// 先将正在被操作的swipeAction标记为打开状态，否则由于props的特性限制，
				// 原本为'false'，再次设置为'false'会无效
				console.log(this.itemShows[index])
				this.itemShows[index].show = true;
				this.itemShows.map((val, idx) => {
					if (index != idx) this.itemShows[idx].show = false;
				})
			},


			confirmDel() {
				let index = this.delIndex
				this.$request.request({
					url: '/api/file/del',
					data: {
						fileid: this.delId,
					},
					method: 'GET',
				}).then(res => {
					this.itemShows.splice(index, 1);
					this.items.splice(index, 1)
				})
				this.delShow = false
				this.$u.toast(`删除成功`);
			},

			cancel() {
				this.delShow = false;
				this.itemShows[this.delIndex].show = false;
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

	.u-card-wrap {
		background-color: #FFFFFF;
		margin: 20rpx 0rpx 0rpx 0rpx;
	}
</style>
