<template>
	<view>
		<view :index="index" v-for="(item,index) in dept" @click="navToEdit(item,index)">
				<view class="u-body-item" >
					<image :src="item.depturl" mode="aspectFill" class="avatar-item"></image>
					<view class="info-item" style="font-weight: bold;">{{item.deptname}}</view>
					<view class="info-item" >部门简介:{{item.remark}}</view>
				</view>
			</navigator>
		</view>
	</view>
</template>

<script>
	import {deptShowSendData} from "../../api/api.js"
	export default {
		data() {
			return {
				dept: [
				]
				
			}
		},
		onLoad() {
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
