<template>

	<view>
		<u-toast ref="uToast" />
		<view class="whole">
			<u-notice-bar mode="horizontal" :is-circular="true" type="none" :list="list" padding="50rpx" font-size="40"
				color="#4d669e" volume-size="40rpx"></u-notice-bar>
			<u-card :title="title" :title-size="35" :sub-title="subTitle" sub-title-size="28" :thumb="thumb"
				thumb-width="40" margin="50rpx" padding="30">
				<view class="" slot="body">
					<view class="u-body-item u-flex u-border-bottom u-col-between u-p-t-0" :index="index"
						v-for="(item,index) in notice" @click="clickNoticeBar(item,index)">
						<view class="u-body-item-title u-line-2">{{item.title}}</view>
					</view>
				</view>

			</u-card>

			<u-row class="rowBtn">
				<u-button class="jobBtn" shape="square" @click="clickJob">
					<view>
						<u-icon name="position" custom-prefix="custom-icon" size="70" color="#2467cd"></u-icon>
						<view>职位</view>
					</view>
				</u-button>
				<u-button class="deptBtn" shape="square" @click="clickDept">
					<view>
						<u-icon name="bumenguanli" custom-prefix="custom-icon" size="70" color="#2467cd"></u-icon>
						<view>部门</view>
					</view>
				</u-button>
			</u-row>
			<u-row class="rowBtn">
				<u-button class="fileBtn" shape="square" @click="clickFile">
					<view>
						<u-icon name="xiazai" custom-prefix="custom-icon" size="70" color="#2467cd"></u-icon>
						<view>下载中心</view>
					</view>
				</u-button>
				<u-button class="noticeBtn" shape="square" @click="clickNotice">
					<view>
						<u-icon name="gonggao" custom-prefix="custom-icon" size="70" color="#2467cd"></u-icon>
						<view>公告</view>
					</view>
				</u-button>
			</u-row>
		</view>
		<u-tabbar
			:list="tabBerList"
			:mid-button="midBtn"
			active-color="#5098FF"
			inactive-color="#909399"
			:border-top= false
			bg-color = "#F8F8F8"
		></u-tabbar>
	</view>

</template>

<script>
	import {
		mapGetters
	} from 'vuex'
	import {
		sendThis
	} from "../../api/request.js"
	import {
		menuSendData
	} from "../../api/api.js"
	export default {
		data() {
			return {
				subTitle: "CSI员工之家",
				title: "最新公告",
				thumb: "/static/menu/bell.png",
				//变量定义
				list: [
					'欢迎登录CSI员工之家！'
				],
				notice: [],
			}
		},
		computed: {
			...mapGetters([
				'tabBerList',
				'midBtn'
			])
		},
		onShow() {
			sendThis(this)
			this.submit()
		},
		methods: {
			
			submit(){
				menuSendData()
					.then((response) => {
						console.log('notice申请数据',response)
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
			
			//showToast方法，实现异常码弹窗
			showToast(TITLE, TYPE) {
				this.$refs.uToast.show({
					title: TITLE.toString(),
					type: TYPE.toString(),
				})
			},
			clickJob() {
				uni.navigateTo({
					url: '../job/show'
				})
			},

			clickDept() {
				uni.navigateTo({
					url: '../dept/show'
				})
			},

			clickFile() {
				uni.navigateTo({
					url: '../file/show'
				})
			},

			clickNotice() {
				uni.navigateTo({
					url: '../notice/show'
				})
			},

			clickNoticeBar(item, index) {
				console.log("navtoNotice")
				console.log(item)
				uni.navigateTo({
					url: "../notice/one?item=" + encodeURIComponent(JSON.stringify(item))
				})
				console.log(item.title)
				console.log(item.userid)
			}



		}
	}
</script>

<style scoped>
	.whole {
		background-color: #f5f5f5;
		/* background-color: #fdfbfa; */
		height: calc(100vh);
		/* #ifdef H5 */
		height: calc(100vh - var(--window-top));
		/* #endif */
	}

	.homeCard {
		font-size: "40rpx";
	}

	.u-card-wrap {
		background-color: $u-bg-color;
		padding: 1px;
	}

	,

	.u-body-item {
		font-size: 32rpx;
		color: #333;
		padding: 20rpx 10rpx;
		/* margin: 10rpx; */
	}

	,

	.jobBtn {
		width: 210rpx;
		height: 210rpx;
		background-color: #ffffff;
		color: #000000;
		font-size: large;
		margin-top: -60rpx;
		margin-bottom: -10rpx;
	}

	,
	.deptBtn {
		width: 210rpx;
		height: 210rpx;
		background-color: #ffffff;
		color: #000000;
		font-size: large;
		margin-top: -60rpx;
		margin-bottom: -10rpx
	}

	,
	.fileBtn {
		width: 210rpx;
		height: 210rpx;
		background-color: #ffffff;
		color: #000000;
		font-size: large;
		margin-top: -140rpx;
	}

	,
	.noticeBtn {
		width: 210rpx;
		height: 210rpx;
		background-color: #ffffff;
		color: #000000;
		font-size: large;
		margin-top: -140rpx;
	}

	,
	.rowBtn {
		margin: 20rpx;
		/* width: 600rpx; */
		height: 314rpx;
	}
</style>
