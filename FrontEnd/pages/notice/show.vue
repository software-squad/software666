<template>
	<view>
		<u-toast ref="uToast" />
		<view :index="index" v-for="(item,index) in List" @click="navToOne(index)">
			<view class="u-body-item">
				<!-- <image :src="item.faceurl" mode="aspectFill" class="avatar-item"></image> -->
				<view class="info-item" style="font-weight: bold;">公告标题：{{item.title}}</view>
				<view class="info-item" style="float: left;">公告内容：{{item.content}}</view>
				<u-tag :text="item.createdate" type="primary" />
			</view>
		</view>
	</view>
</template>

<script>
	import {
		noticeShowGetData
	} from "../../api/api.js"
	export default {
		data() {
			return {
				item: '',
				List: [],
				//noticeid: '',
				// title: '',
				// content: '',
				// createdate: '',
				// userid: '',
			}
		},
		computed: {},
		onLoad() {
			this.submit()
		},
		onNavigationBarButtonTap: function(e) {
			uni.navigateTo({
				url: "add"
			})
		},
		methods: {
			navToOne(index) {
				this.item = this.List[index]
				uni.navigateTo({
					url: 'one?item=' + encodeURIComponent(JSON.stringify(this.item))
				})
				console.log(this.item.title);
				console.log(this.item.content);
			},

			submit() {
				let data = {
					noticeid: this.item.noticeid,
					title: this.item.title,
					content: this.item.content,
					createdate: this.item.createdate,
					userid: this.item.userid,
					username: this.item.username,
				}
				noticeShowGetData(data)
					.then((response) => {
						this.List = []
						for (let i = 0; i < response.data.data.length; i++) {
							let l = {
								noticeid: response.data.data[i].noticeid,
								title: response.data.data[i].title,
								content: response.data.data[i].content,
								createdate: response.data.data[i].createdate,
								userid: response.data.data[i].userid,
								username: response.data.data[i].userid,
								show: false
							}
							this.List.push(l)
						}
					})
					.catch((error) => {
						console.log(error);
					})
			},

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
