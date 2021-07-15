<!-- 普通用户公告展示界面 -->
<template>
	<view class="whole">
		<u-toast ref="uToast" />
		<view :index="index" v-for="(item,index) in List" @click="navToOne(index)">
			<view class="u-body-item">
				<!-- <image :src="item.faceurl" mode="aspectFill" class="avatar-item"></image> -->
				<u-row class="info-item-row">
					<u-col span="12">
						<view class="info-item" style="font-weight: bold;">{{item.title}}</view>
					</u-col>
				</u-row>
				<u-gap height="10"></u-gap>
				<u-row>
					<u-col span="12">
						<view class="remark-item" style="float: left;">内容：{{item.content}}</view>
					</u-col>
				</u-row>
				<u-gap height="10"></u-gap>
				<u-tag :text="item.createdate" type="info" mode="plain" shape="circle"/>
			</view>
		</view>
		<!-- 自定义tabbar -->
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
	//import mapGetters函数 用于自定义tabbar
	import {
		mapGetters
	} from 'vuex'
	//import sendThis 函数，实现拦截器统一拦截msg码弹窗
	import {
		sendThis
	} from "../../api/request.js"
	import {
		noticeShowGetData
	} from "../../api/api.js"
	export default {
		data() {
			return {
				item: '',
				List: [],
			}
		},
		//自定义tabbar
		computed: {
			...mapGetters([
				'tabBerList',
				'midBtn'
			])
		},
		onLoad() {
			sendThis(this)
			this.submit()
		},
		//顶部导航栏加号跳转页面
		onNavigationBarButtonTap: function(e) {
			uni.navigateTo({
				url: "add"
			})
		},
		methods: {
			//showToast方法，实现异常码弹窗
			showToast(TITLE, TYPE) {
				this.$refs.uToast.show({
					title: TITLE.toString(),
					type: TYPE.toString(),
				})
			},
			//跳转到单个公告展示页面
			navToOne(index) {
				this.item = this.List[index]
				uni.navigateTo({
					url: 'one?item=' + encodeURIComponent(JSON.stringify(this.item))
				})
				console.log(this.item.title);  //打印出上个页面传递的参数。
				console.log(this.item.content);//打印出上个页面传递的参数。
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
	.whole {
		background-color: #f5f5f5;
		height: calc(100vh);
		/* 	#ifdef H5*/
		height: calc(100vh - var(--window-top));
		/* #endif */
	}

	.u-card-wrap {
		background-color: $u-bg-color;
		padding: 1px;
	}

	.u-body-item {
		font-size: 32rpx;
		color: #333;
		padding: 20rpx 20rpx;
		margin-top: -10rpx;
		margin-bottom: 16rpx;
		background-color: #ffffff;
		/* TODO*/
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
	.remark-item{
		font-size: 35rpx;
		color: #a8a7ab;
		float: left;
		text-align: justify;
		padding-left: 10rpx;
		/* padding-left: -60rpx; */
	}
	.avatar-item {}
</style>

