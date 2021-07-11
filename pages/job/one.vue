<template>
	<view>
		<u-gap height="40"></u-gap>
		<view class="deptOne">
			<text>职位名字</text>
			<u-input type="text" :border="true" placeholder="请输入职位名字"/>
			<u-gap height="30"></u-gap>
			<text>职位描述</text>
			<u-gap height="10"></u-gap>
			<u-input type="textarea" height="700" :border="true" placeholder="请输入职位描述"/>
			<u-gap height="80"></u-gap>
			<u-col span="400">
				<u-row gutter="20">
					<button @click="navToEdit()" >编辑</button>
					<button @click="del" type="error">删除</button>
				</u-row>
			</u-col>
		</view>
	</view>
</template>

<script>
	export default {
		data() {
			return {
				value: '',
				deptName:'',
				deptDctipt:'',
				item:''
			}
		},
		onLoad: function(option) {
			this.item = JSON.parse(decodeURIComponent(option.item));
			console.log("one");
			console.log(this.item.name);
			console.log(this.item.dcrpt);
		},
		methods: {
			showSuccessToast() {
				this.$refs.uToast.show({
					title: '编辑成功',
					type: 'success'
				})
			},
			showFalseToast() {
				this.$refs.uToast.show({
					title: '编辑失败，该职位已存在',
					type: 'false'
				})
			},
			showDelSuccessToast() {
				this.$refs.uToast.show({
					title: '删除成功',
					type: 'success'
				})
			},
			showDelFalseToast() {
				this.$refs.uToast.show({
					title: '删除失败',
					type: 'false'
				})
			},
			del(){
				let data = {
							
				}
				SendData(data)
					.then((response) => {
						this.showSuccessToast();
						uni.switchTab({
							url: '/pages/job/show'
						})
					})
					.catch((error) => {
						console.log(error);
						this.showFalseToast();
					})		
			},
			navToEdit(){
				uni.navigateTo({
					url: "edit?item="+encodeURIComponent(JSON.stringify(this.item))
				}),
				console.log("one")
				console.log(this.item.name),
				console.log(this.item.dcrpt)
			}
			
			
		}
	}
</script>

<style>
	.deptOne{
		margin: 0 50rpx;
	}

</style>
