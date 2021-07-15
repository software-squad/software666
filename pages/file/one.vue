<template>
	<view>
			<!-- TODO 页面需要重新设计 -->
			<view class="uni-media-list-body">
				<u-tag text="文件名" mode="light" shape="circle" class="tagStyle"/>
				<!-- <u-tag text="要清楚" closeable :show="show" @close="tagClick" /> -->
				<text class="content">{{item.title}}</text>
				<u-gap height="20"></u-gap>
				<u-gap height="15" bg-color="#f9f9f9"></u-gap>
				<u-gap height="5"></u-gap>
				<u-tag text="上传者" mode="light" shape="circle" class="tagStyle"/>
				<text class="content">{{item.username}}</text>
				<u-gap height="10"></u-gap>
				<u-gap height="15" bg-color="#f9f9f9"></u-gap>
				<view class="remark-item">{{item.remark}}</view>
			</view>
			<u-gap height="15" bg-color="#f9f9f9"></u-gap>
			<u-tag text="点击此处下载" mode="light" shape="circle" class="tagStyle"/>
			<u-link :href="fileLink" under-line="true" >{{item.filename}}</u-link>
		</view>
</template>

<script>
	import util from "../../api/util.js"
	export default {
		data() {
			return {
				fileLink:'',
				item: {
					"fileid": '',
					"title": "",
					"filename": "",
					"remark": "",
					"createdate": "",
					"username": "",
					"filepath": ""
				},
			}
		},

		onLoad: function(option) {
			console.log('带参跳转结果', option)
			
			if (option) {
				this.item = JSON.parse(decodeURIComponent(option.item));
				console.log('基础url：',util.dowloadBaseUrl)
				this.fileLink = util.dowloadBaseUrl+this.item.fileid
				uni.setNavigationBarTitle({
					title:this.item.title
				})
			}else{
				this.$u.toast('点击为空')
			}
		},

		methods: {
			
		}
	}
</script>

<style>
	.content{
		font-size: larger;
		font-weight: 500;
		margin-left:20rpx;
		padding-top: 100rpx;
	}
	.remark-item{
		height: 200rpx;
		text-align:justify;
	}
	.tagStyle{
		margin-left:10rpx ;
		margin-top:20rpx ;
	}
</style>
