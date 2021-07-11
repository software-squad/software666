<template>

	<view>
		<u-notice-bar mode="horizontal" :is-circular="true" type="none" :list="list" padding="60rpx"></u-notice-bar>
		<u-card :title="title" :title-size="37" :sub-title="subTitle" :thumb="thumb" thumb-width="40" margin="40rpx">
				<view class="" slot="body">
					<view class="u-body-item u-flex u-border-bottom u-col-between u-p-t-0">
						<view class="u-body-item-title u-line-2">重要通知：今天吃饭不要钱！</view>
						<image src="https://img11.360buyimg.com/n7/jfs/t1/94448/29/2734/524808/5dd4cc16E990dfb6b/59c256f85a8c3757.jpg" mode="aspectFill"></image>
					</view>
					<view class="u-body-item u-flex u-row-between u-p-b-0">
						<view class="u-body-item-title u-line-2">谨防诈骗！朱某是骗子</view>
						<image src="https://img12.360buyimg.com/n7/jfs/t1/102191/19/9072/330688/5e0af7cfE17698872/c91c00d713bf729a.jpg" mode="aspectFill"></image>
					</view>
				</view>
				
			</u-card>

		<u-row class="rowBtn">
			<u-button class="jobBtn" shape="square" @click="clickJob">
				<view>
				<u-icon name="position" custom-prefix="custom-icon" size="70" color="#888888"></u-icon>
				<view>职位</view>
				</view>
			</u-button>
			<u-button class="deptBtn" shape="square" @click="clickDept">
				<view>
				<u-icon name="bumenguanli" custom-prefix="custom-icon" size="70" color="#888888"></u-icon>
				<view>部门</view>
				</view>
			</u-button>
		</u-row>
		<u-row class="rowBtn">
			<u-button class="fileBtn" shape="square" @click="clickFile">
				<view>
				<u-icon name="xiazai" custom-prefix="custom-icon" size="70" color="#888888"></u-icon>
				<view>下载中心</view>
				</view>
			</u-button>
			<u-button class="noticeBtn" shape="square" @click="clickNotice">
				<view>
				<u-icon name="gonggao" custom-prefix="custom-icon" size="70" color="#888888"></u-icon>
				<view>公告</view>
				</view>
			</u-button>
		</u-row>
	</view>

</template>

<script>
	// import {menuSendData} from "/api/api.js"
	export default {
		data() {
			return {
				list: [
						'欢迎登录CSI员工之家！'
				],
				title: '最新公告',
				subTitle: 'CSI员工之家',
				thumb: '/static/menu/bell.png',
				//变量定义
				notice1id:'',
				title1: '',
				content1:'',
				createdate1:'',
				username1: '',
				noticeid2:'',
				title2: '',
				content2:'',
				createdate2:'',
				username2: ''
			}
		},
		onLoad() {
			// submit(){
			// 	menuSendData(data)
			// 	.then((response) => {
			// 		this.notice1id = response.data[0].noticeid;
			// 		this.title1 = response.data[0].title;
			// 		this.content1 = response.data[0].content;
			// 		this.createdate1 = response.data[0].createdate;
			// 		this.username2 = response.data[1].username;
			// 		this.notice2id = response.data[1].noticeid;
			// 		this.title2 = response.data[1].title;
			// 		this.content2 = response.data[1].content;
			// 		this.createdate2 = response.data[1].createdate;
			// 		this.username2 = response.data[1].username;
			// 	})
			// 	.catch((error) => {
			// 	  console.log(error);
			// 	 })
			// }
		},
		methods: {
				
			clickJob(){
				uni.navigateTo({
					url:'../job/show'
				})
			},
			
			clickDept(){
				uni.navigateTo({
					url:'../dept/show'
				})
			},
				
			clickFile(){
				uni.navigateTo({
					url:'../file/show'
				})
			},
				
			clickNotice(){
				uni.navigateTo({
					url:'../notice/show'
				})
			},
			
			
			
			
		}
	}
</script>

<style scoped>
	
	.homeCard{
		font-size: "40rpx";
	}
	.u-card-wrap { 
			background-color: $u-bg-color;
			padding: 1px;
		},
		
	.u-body-item image {
			width: 120rpx;
			flex: 0 0 120rpx;
			height: 120rpx;
			border-radius: 8rpx;
			margin-left: 12rpx;
		},
	.u-body-item {
		font-size: 32rpx;
		color: #333;
		padding: 20rpx 10rpx;
	},		
	
	.jobBtn{
		width: 210rpx;
		height: 210rpx;
		background-color: #ffffff;
		color: #000000;
		font-size: large;
		margin-top: auto;
	},
	.deptBtn{
		width: 210rpx;
		height: 210rpx;
		background-color: #ffffff;
		color: #000000;
		font-size: large;
		margin-top: auto;
	},
	.fileBtn{
		width: 210rpx;
		height: 210rpx;
		background-color: #ffffff;
		color: #000000;
		font-size: large;
		margin-top: auto;
	},
	.noticeBtn{
		width: 210rpx;
		height: 210rpx;
		background-color: #ffffff;
		color: #000000;
		font-size: large;
		margin-top: auto;
	},
	.rowBtn{
		margin: 50rpx;
/* 		width: 600rpx;
		height: 600rpx; */
	}
</style>
