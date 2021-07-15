<template>
	<view>
		<u-toast ref="uToast" />
		<view class="whole">
					<view :index="index" v-for="(item,index) in dept" @click="navToEdit(item,index)">
						<view class="u-body-item">
							<image :src="item.depturl" mode="aspectFill" class="avatar-item"></image>
							<u-row class="info-item-row">
								<u-col span="12">
									<view class="info-item">{{item.deptname}}</view>
								</u-col>
							</u-row>
							<u-row>
								<u-col span="12">
									<view class="remark-item">简介:{{item.remark}}</view>
								</u-col>
							</u-row>
							<u-gap height="10"></u-gap>
							
						</view>
						</navigator>
					</view>
				</view>
	</view>
</template>

<script>
	import {sendThis} from "../../api/request.js"
	import {deptShowSendData} from "../../api/api.js"
	export default {
		data() {
			return {
				dept: [
				]
				
			}
		},
		onLoad() {
			sendThis(this)
			deptShowSendData()
			.then((response) => {
				this.dept = []
				for (let i = 0; i < response.data.data.length; i++) {
					let d = {
						deptid: response.data.data[i].deptid,
						deptname: response.data.data[i].deptname,
						depturl: response.data.data[i].depturl,
						remark: response.data.data[i].remark,
					}
					this.dept.push(d)
				}
			})
			.catch((error) => {
				console.log(error);
			})
		},
		onNavigationBarButtonTap:function(e){
		    uni.navigateTo({
		    	url:"oneAdd"
		    })
		},
		methods: {
			showToast(TITLE,TYPE) {
							this.$refs.uToast.show({
								title: TITLE.toString(),
								type: TYPE.toString(),
							})
			},
			navToEdit(item,index){
				uni.navigateTo({
					url: "one?item="+encodeURIComponent(JSON.stringify(item))
				}),
				
				console.log("show")
				console.log(item.deptname),
				console.log(item.remark)
			},
		}
	}
</script>

<style>
	.whole {
		background-color: #f5f5f5;
		height: calc(100vh);
		weight: calc(100vw);
		/* #ifdef H5 */
		height: calc(100vh - var(--window-top));
		/* #endif */
		/* margin: 0 50rpx; */
	}

	.u-card-wrap {
		background-color: $u-bg-color;
		padding: 1rpx;
		margin: 0 50rpx;
	}

	.u-body-item {
		font-size: 32rpx;
		padding: 20rpx 20rpx;
		margin-bottom: 16rpx;
		/* border-style: solid; */
		/* TODO */
		overflow: hidden;
		background-color: #ffffff;
		/* margin: 0rpx 30rpx 0rpx 30rpx; */
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
		font-style: normal;
		float: left;
		font-weight:500;
		text-align: left;
		padding-left: 10rpx;
		/* border-style: solid;  /* TODO */
	}
	.remark-item{
		font-size: large;
		color: #a8a7ab;
		float: left;
		text-align: justify;
		padding-left: 10rpx;
		/* padding-left: -60rpx; */
	}
	.avatar-item {}
	.info-item-row{
		margin-bottom: 5rpx;
	}
	
</style>
