<template>
	<view>
		<!-- TODO 页面需要重新设计 -->
		<view class="uni-media-list-body">
			<h3 style="padding: 20rpx 10rpx 20rpx 10rpx;">{{item.title}}</h3>
			<u-gap height="5" bg-color="#f9f9f9"></u-gap>
			<text>{{item.username}}</text>
			<u-gap height="5" bg-color="#f9f9f9"></u-gap>
			<text>{{item.remark}}</text>
		</view>
		<u-gap height="15" bg-color="#f9f9f9"></u-gap>
		<u-link :href="fileLink" under-line="true" >{{item.filename}}</u-link>
	</view>
</template>

<script>
	const baseURL = 'http://192.168.0.125:8082/api/file/download?fileid='
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
				this.fileLink = baseURL+this.item.fileid
			}else{
				this.$u.toast('点击为空')
			}
		},

		methods: {
			
		}
	}
</script>

<style>
	
</style>
