<template>

	<view>
		<u-notice-bar mode="horizontal" :is-circular="true" type="none" :list="list" padding="60rpx"></u-notice-bar>
		<u-card :title="title" :title-size="37" :sub-title="subTitle" :thumb="thumb" thumb-width="40" margin="40rpx">
				<view class="" slot="body">
					<view class="u-body-item u-flex u-border-bottom u-col-between u-p-t-0" :index="index" v-for="(item,index) in notice" @click="clickNoticeBar(item,index)">
						<view class="u-body-item-title u-line-2">{{item.title}}</view>
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
	import {menuSendData} from "../../api/api.js"
	export default {
		data() {
			return {
				subTitle:"CSI员工之家",
				title:"最新公告",
				thumb:"/static/menu/bell.png",
				//变量定义
				list: [
						'欢迎登录CSI员工之家！'
				],
				notice:[],
			}
		},
		onLoad() {
			menuSendData()
			.then((response) => {
				this.notice = []
				for (let i = 0; i < 2; i++) {
					let d = {
						noticeid: response.data.data[i].noticeid,
						title: response.data.data[i].title,
						content: response.data.data[i].content,
						userid: response.data.data[i].userid,
						createdate: response.data.data[i].createdate,
						username: response.data.data[i].username
					}
					this.notice.push(d)
				}
			})
			.catch((error) => {
				console.log(error);
			})
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
				
			clickNoticeBar(item,index){
				console.log("navtoNotice")
				uni.navigateTo({
					url: "../notice/one?item="+encodeURIComponent(JSON.stringify(item))
				})
				console.log(item.title)
				console.log(item.userid)
			}
			
			
			
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
