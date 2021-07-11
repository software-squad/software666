<template>
	<view>
		<u-gap height="40"></u-gap>
		<text>公告标题</text>
		<u-gap height="10"></u-gap>
		<u-input type="text" :border="true" placeholder="请输入公告标题"/>
		<u-gap height="30"></u-gap>
		<text>公告内容</text>
		<u-gap height="10"></u-gap>
		<u-input type="textarea" height="700" :border="true" placeholder="请输入公告内容"/>
		<u-gap height="80"></u-gap>
		<u-col span="400" justify="center">
			<u-row gutter="20">
				<button @click="navToEdit" type="primary">编辑</button>
				<button @click="navToShow" type="warn">删除</button>
			</u-row>
		</u-col>		
	</view>
</template>

<script>
	import {SendData} from "../../api/notice_edit.js"
	export default {
		data() {
			return {
				item:'',
				List: [{
						noticeid: 1,
						title: "公告一",
						content: "这是公告一",
						createdate: "2020-11-20",
						userid: "20196666",
					},
					{
						noticeid: 2,
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
			navToEdit() {
				uni.navigateTo({
					url: 'edit?item=' + encodeURIComponent(JSON.stringify(this.item))
				})
				console.log(this.item.title)
				console.log(this.item.content)
			},
			navToShow() {
				uni.navigateTo({
					url: 'show?item=' + encodeURIComponent(JSON.stringify(this.item))
				})
				console.log(this.item.title)
				console.log(this.item.content)
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
					title:this.title,
					content:this.content,
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
