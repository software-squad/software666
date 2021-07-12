<template>
	<view>
		<u-gap height="40"></u-gap>
		<text>文档标题</text>
		<u-gap height="10"></u-gap>
		<u-input type="text" :border="true" placeholder="请输入文档标题" v-model="item.title"/>
		<u-gap height="30"></u-gap>
		<text>文档描述</text>
		<u-gap height="10"></u-gap>
		<u-input type="textarea" height="700" :border="true" placeholder="请输入文档描述" v-model="item.remark"/>
		<u-gap height="30"></u-gap>
		<text>文档</text>
		<u-image width="10%" height="80" src="/static/tab_icons/download.png"></u-image>
		<u-gap height="40"></u-gap>
		<u-col span="400" justify="center">
			<u-row gutter="20">
				<button @click="navToEdit" type="primary">编辑</button>
				<button @click="navToShow" type="warn">删除</button>
			</u-row>
		</u-col>
	</view>
</template>

<script>
	export default {
		data() {
			return {
				item:{}
			}
		},
		onLoad: function(option) {
			this.item = JSON.parse(decodeURIComponent(option.item));
			console.log(this.item.title); //打印出上个页面传递的参数。
			console.log(this.item.filename); //打印出上个页面传递的参数。
		},
		methods: {
			navToEdit() {
				uni.navigateTo({
					url: 'edit?item=' + encodeURIComponent(JSON.stringify(this.item))
				})
				console.log(this.item.title)
				console.log(this.item.filename)
			},
			navToShow() {
				uni.navigateTo({
					url: 'show?item=' + encodeURIComponent(JSON.stringify(this.item))
				})
				console.log(this.item.title)
				console.log(this.item.filename)
			},



			showDeletSuccessToast() {
				this.$refs.uToast.show({
					title: '删除成功',
					type: 'success'
				})
			},
			showEditSuccessToast() {
				this.$refs.uToast.show({
					title: '编辑成功',
					type: 'success'
				})
			},
			showDeletFalseToast() {
				this.$refs.uToast.show({
					title: '删除失败',
					type: 'false'
				})
			},
			showEditFalseToast() {
				this.$refs.uToast.show({
					title: '编辑失败',
					type: 'false'
				})
			},
			submit() {
				let data = {

				}
				SendData(data)
					.then((response) => {
						this.showEditSuccessToast();
						uni.switchTab({
							url: '/pages/notice/one'
						})
					})
					.catch((error) => {
						console.log(error);
						this.showEditFalseToast();
					})
			},

			delet() {
				let data = {

				}
				SendData(data)
					.then((response) => {
						this.showDeletSuccessToast();
						uni.switchTab({
							url: '/pages/notice/show'
						})
					})
					.catch((error) => {
						console.log(error);
						this.showDeletFalseToast();
					})
			},

		}
	}
</script>

<style>

</style>
