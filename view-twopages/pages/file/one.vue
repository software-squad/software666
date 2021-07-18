<template>
	<view>
		<view class="uni-media-list-body">
			<u-tag text="文件名" mode="light" shape="circle" class="tagStyle" />
			<text class="content">{{item.title}}</text>
			<u-gap height="20"></u-gap>
			<u-gap height="15" bg-color="#f9f9f9"></u-gap>
			<u-gap height="5"></u-gap>

			<u-tag text="上传者" mode="light" shape="circle" class="tagStyle" />
			<text class="content">{{item.username}}</text>
			<u-gap height="10"></u-gap>
			<u-gap height="15" bg-color="#f9f9f9"></u-gap>
			<u-tag text="备注" mode="light" shape="circle" class="tagStyle" />
			<view class="remark-item">{{item.remark}}</view>
		</view>
		
		<u-gap height="15" bg-color="#f9f9f9"></u-gap>
		<!-- <u-tag text="点击此处下载" mode="light" shape="circle" class="tagStyle" /> -->
		<u-link :href="fileLink" under-line="true">点击链接下载文件</u-link>
	</view>
</template>

<script>
	import util from "../../api/util.js"
	export default {
		data() {
			return {
				fileLink: '',  // 文件访问链接
				item: { // 文件信息
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
			// console.log('文件信息带参跳转', option)

			if (option) {
				this.item = JSON.parse(decodeURIComponent(option.item));
				console.log('基础url：', util.dowloadBaseUrl)
				this.fileLink = util.dowloadBaseUrl + this.item.fileid
				// uni.setNavigationBarTitle({
				// 	// title: this.item.title
				// 	title: '文件查看'
				// })
			} else {
				this.$u.toast('点击为空')
			}
		},

		methods: {}
	}
</script>

<style>
	.content {
		font-size: larger;
		font-weight: 500;
		margin-left: 20rpx;
		padding-top: 100rpx;
	}

	.remark-item {
		height: 200rpx;
		text-align: justify;
	}

	.tagStyle {
		margin-left: 10rpx;
		margin-top: 20rpx;
		font-size: larger;
	}
</style>
