<template>
	<view>
		<u-gap height="40"></u-gap>
		<text>公告标题</text>
		<u-gap height="10"></u-gap>
		<u-input type="text" :border="true" placeholder="请输入文档标题" />
		<u-gap height="30"></u-gap>
		<text>公告内容</text>
		<u-gap height="10"></u-gap>
		<u-input type="textarea" height="700" :border="true" placeholder="请输入文档描述" />
		<u-gap height="80"></u-gap>
		<u-col span="400">
			<u-row gutter="20">
				<button @click="navToShow" type="primary">发布</button>
			</u-row>
		</u-col>
	</view>
</template>

<script>
	export default {
		data() {
			return {
				item:'',
				List: [{
						noticeid: '',
						title: "公告一",
						content: "这是公告一",
						createdate: "2020-11-20",
						userid: "20196666",
					},
					{
						noticeid: '',
						title: "公告二",
						content: "这是公告二",
						createdate: "2020-1-10",
						userid: "20196666",
					},
				]
			}
		},
		onLoad: function(option) {
			this.item = JSON.parse(decodeURIComponent(option.item));
			console.log(this.item.title); //打印出上个页面传递的参数。
			console.log(this.item.content); //打印出上个页面传递的参数。
		},
		methods: {
			navToShow() {
				uni.navigateTo({
					url: 'show?item=' + encodeURIComponent(JSON.stringify(this.item))
				})
				console.log(this.item.title)
				console.log(this.item.content)
			},
			
			
			showSuccessToast() {
				this.$refs.uToast.show({
					title: '发布成功',
					type: 'success'
				})
			},
			showFalseToast() {
				this.$refs.uToast.show({
					title: '发布失败',
					type: 'false'
				})
			},
			submit() {
				let data = {

				}
				SendData(data)
					.then((response) => {
						this.showSuccessToast();
						uni.switchTab({
							url: '/pages/notice/show'
						})
					})
					.catch((error) => {
						console.log(error);
						this.showFalseToast();
					})
			},

		},
	}
</script>

<style>

</style>
