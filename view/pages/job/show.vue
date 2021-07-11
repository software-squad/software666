<template>
	<view>
		<view class="search">
			<u-search placeholder="请输入职位名称" v-model="searchJobName" shape="round" @change="search" :show-action="false"></u-search>
		</view>
		<view :index="index" v-for="(item,index) in jobsShow" @click="navToEdit(item,index)" >
				<view class="u-body-item" >
					<image :src="item.depturl" mode="aspectFill" class="avatar-item"></image>
					<view class="info-item" style="font-weight: bold;">{{item.name}}</view>
					<view class="info-item" >职位描述:{{item.dcrpt}}</view>
				</view>
			</navigator>
		</view>
	</view>
</template>

<script>
	export default {
		data() {
			return {
				searchJobName:'',
				keyword:'',
				jobs: [{
						name:'干饭工程师',
						depturl:'/static/dept/dept.jpg',
						dcrpt:'负责干饭'
					},
					{
						name:'java工程师',
						depturl:'/static/dept/dept.jpg',
						dcrpt:'专注技术，攻克难题，勇攀高峰'
					},
					{
						name:'摸鱼工程师',
						depturl:'/static/dept/dept.jpg',
						dcrpt:'负责摸鱼'
					},
					{
						name:'摸鱼工程师',
						depturl:'/static/dept/dept.jpg',
						dcrpt:'负责摸鱼'
					},
					{
						name:'摸鱼工程师',
						depturl:'/static/dept/dept.jpg',
						dcrpt:'负责摸鱼'
					},
					{
						name:'摸鱼工程师',
						depturl:'/static/dept/dept.jpg',
						dcrpt:'负责摸鱼'
					}],
				jobsShow:[]
				
			}
		},
		onLoad() {
			this.jobsShow = this.jobs
		},
		onNavigationBarButtonTap:function(e){
		    uni.navigateTo({
		    	url:"oneAdd"
		    })
		},
		methods: {
			search(){
				if(this.searchJobName == ""){
					this.jobsShow = this.jobs
				}
				else {
					this.jobsShow = []
					this.jobs.forEach((item) => {
						if(item.name.includes(this.searchJobName))
						this.jobsShow.push(item)
					})
				}
			},
			
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
	
	.search{
		margin: 0 50rpx;
		margin-top: 30rpx;
	}
	
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
	
	.u-search-box {
		padding: 18rpx 30rpx;
	}
	
	.u-search-inner {
		background-color: rgb(234, 234, 234);
		border-radius: 100rpx;
		display: flex;
		align-items: center;
		padding: 10rpx 16rpx;
	}
	
	.u-search-text {
		font-size: 26rpx;
		color: $u-tips-color;
		margin-left: 10rpx;
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
