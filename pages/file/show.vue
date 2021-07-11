<template>
	<view>
		<u-gap height="10"></u-gap>
		<u-search @click="navToSearchByFilename" placeholder="请输入文件名称" ></u-search>

		<view :index="index" v-for="(item,index) in filesList" @click="navToOne(index)">
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
				filesList: [{
					fileid: 1,
					title: "《摸鱼：从入职到加薪》",
					filename: "《摸鱼：从入职到加薪》",
					remark: null,
					createdate: "2021-07-09",
					username: "李华",
					filepath: "C:/公司资料"
				}, {
					fileid: 8,
					title: "《加薪》",
					filename: "《摸鱼：从入职到加薪》",
					remark: null,
					createdate: "2021-07-10",
					username: "李华",
					filepath: "C:/公司资料"
				}]

			}
		},
		onLoad: function(option) {
			const item = JSON.parse(decodeURIComponent(option.item));
			console.log(item.title); //打印出上个页面传递的参数。
			console.log(item.filename); //打印出上个页面传递的参数。
		},
		methods: {
			onNavigationBarButtonTap: function(e) {
				uni.navigateTo({
					url: "edit"
				})
			},
			navToOne(index) {
				this.item = this.filesList[index]
				uni.navigateTo({
					url: 'one?item=' + encodeURIComponent(JSON.stringify(this.item))
				})
				console.log(this.item.title);
				console.log(this.item.filename);
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
