<template>
	<view>
		<u-gap height="40"></u-gap>
		<text>文档标题</text>
		<u-gap height="10"></u-gap>
		<u-input type="text" :border="true" placeholder="请输入文档标题" />
		<u-gap height="30"></u-gap>
		<text>文档描述</text>
		<u-gap height="10"></u-gap>
		<u-input type="textarea" height="700" :border="true" placeholder="请输入文档描述" />
		<u-gap height="30"></u-gap>
		<text>文档</text>
		<u-image width="10%" height="80" src="/static/tab_icons/download.png"></u-image>
		<u-gap height="40"></u-gap>
		<button @click="navToShow(index)" class="loginButtonActivity" type="primary">上传</button>
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
			this.item = JSON.parse(decodeURIComponent(option.item));
			console.log(this.item.title); //打印出上个页面传递的参数。
			console.log(this.item.filename); //打印出上个页面传递的参数。
		},
		methods: {
			navToShow() {
				uni.navigateTo({
					url: 'show?item=' + encodeURIComponent(JSON.stringify(this.item))
				})
				console.log(this.item.title)
				console.log(this.item.filename)
			},





			showSuccessToast() {
				this.$refs.uToast.show({
					title: '上传成功',
					type: 'success'
				})
			},
			showFalseToast() {
				this.$refs.uToast.show({
					title: '上传失败',
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
							url: '/pages/file/show'
						})
					})
					.catch((error) => {
						console.log(error);
						this.showFalseToast();
					})
			},

		}
	}
</script>

<style>

</style>
