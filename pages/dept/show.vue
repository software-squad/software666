<template>
	<view>
		<view :index="index" v-for="(item,index) in dept" @click="navToEdit(item,index)">
				<view class="u-body-item" >
					<image :src="item.depturl" mode="aspectFill" class="avatar-item"></image>
					<view class="info-item" style="font-weight: bold;">{{item.name}}</view>
					<view class="info-item" >部门简介:{{item.dcrpt}}</view>
				</view>
			</navigator>
		</view>
	</view>
</template>

<script>
	export default {
		data() {
			return {
				dept: [
					{
						name:'干饭部',
						depturl:'/static/dept/dept.jpg',
						dcrpt:'负责消灭粮食，强身健体'
					},
					{
						name:'技术部',
						depturl:'/static/dept/dept.jpg',
						dcrpt:'专注技术，攻克难题，勇攀高峰'
					},
					{
						name:'摸鱼部',
						depturl:'/static/dept/dept.jpg',
						dcrpt:'本部门主要负责不用负责的事务'
					},
					{
						name:'干饭部',
						depturl:'/static/dept/dept.jpg',
						dcrpt:'负责消灭粮食，强身健体'
					},
					{
						name:'干饭部',
						depturl:'/static/dept/dept.jpg',
						dcrpt:'负责消灭粮食，强身健体'
					}
				]
				
			}
		},
		onLoad() {
			
		},
		onNavigationBarButtonTap:function(e){
		    uni.navigateTo({
		    	url:"oneAdd"
		    })
		},
		methods: {
			navToEdit(item,index){
				uni.navigateTo({
					url: "one?item="+encodeURIComponent(JSON.stringify(item))
				}),
				
				console.log("show")
				console.log(item.name),
				console.log(item.dcrpt)
			},
		}
	}
</script>

<style>
	
	
	.u-card-wrap {
		background-color: $u-bg-color;
		padding: 1rpx;
		margin: 0 50rpx;
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
