<template>
	<view>
		<u-gap height="10"></u-gap>
		<u-search @click="navToSearchByFilename" placeholder="请输入文件名称" ></u-search>
		
		<view :index="index" :key="item.fileid" v-for="(item,index) in filesList" @click="navToOne(index)">
			<view class="u-body-item">
				<!-- <image :src="item.faceurl" mode="aspectFill" class="avatar-item"></image> -->
				<view class="info-item" style="font-weight: bold;">文件标题：{{item.title}}</view>
				<view class="info-item" style="float: left;">文件名称：{{item.filename}}</view>
				<u-tag :text="item.createdate" type="primary" />
			</view>
		</view>
	</view>
</template>

<script>
	export default {
		data() {
			return {
				filesList: [],
			}
		},
			
		async onLoad(){
			await uni.request({
				url:'/api/file/showmany',
				method:'GET',
				success: (res) => {
					if(res.data.msg=="10001"){
						this.filesList = res.data.data
					}else{
						this.$u.toast(`数据获取失败`);
					}
				},
				fail(){
					this.$u.toast(`数据获取失败`);
				}
			})
		},
		methods: {
			onNavigationBarButtonTap: function(e) {
				uni.navigateTo({
					url: "edit"
				})
			},
			navToOne(index) {
				let item = encodeURIComponent(JSON.stringify(this.filesList[index]))
				uni.navigateTo({
					url: 'one?item=' + item
				})
			},	
			navToSearchByFilename(){
				uni.navigateTo({
					url:'./search',
					success() {
						console.log('回到广场')
					}
				})
			},
			
			
			submit() {
				GetData()
					.then((response) => {
						this.List = []
						for (let i = 0; i < response.data.data.length; i++) {
							let l = {
								fileid: response.data.data[i].fileid,
								title: response.data.data[i].title,
								filename: response.data.data[i].filename,
								createdate: response.data.data[i].createdate,
								username: response.data.data[i].username,
								remark: response.data.data[i].remark,
								filepath: response.data.data[i].filepath,
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
