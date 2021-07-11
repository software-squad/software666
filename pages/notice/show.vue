<template>
	<view>
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
		GetData
	} from "../../api/notice_show.js"
	export default {
		data() {
			return {
				item:'',
				List: [{
						noticeid: '',
						title: "公告一",
						content: "这是公告一",
						createdate: "2020-11-20",
						userid: "20196666",
					},
					{
						noticeid: '',
						title: "公告二",
						content: "这是公告二",
						createdate: "2020-1-10",
						userid: "20196666",
					},
				]
			}
		},
		computed: {},
		onLoad: function(option) {
		
		},
		methods: {
			onNavigationBarButtonTap: function(e) {
				uni.navigateTo({
					url: "edit"
				})
			},
			
			navToOne(index) {
				this.item = this.List[index]
				uni.navigateTo({
					url: 'one?item=' + encodeURIComponent(JSON.stringify(this.item))
				})
				console.log(this.item.title);
				console.log(this.item.content);
			},

			submit() {
				GetData()
					.then((response) => {
						this.List = []
						for (let i = 0; i < response.data.data.length; i++) {
							let l = {
								noticeid: response.data.data[i].noticeid,
								title: response.data.data[i].title,
								content: response.data.data[i].content,
								createdate: response.data.data[i].createdate,
								userid: response.data.data[i].userid,
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
