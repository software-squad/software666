<template>
	<view>
		<u-toast ref="uToast" />
		<u-gap height="40"></u-gap>
		<view class="deptOne">
			<image :src="imageSrc" ></image>
			<u-gap height="60"></u-gap>
			<text class="title">部门名字:</text>
			<u-gap height="30"></u-gap>
			<text>{{item.deptname}}</text>
			<u-gap height="60"></u-gap>
			<text class="title">部门描述:</text>
			<u-gap height="30"></u-gap>
			<text>{{item.remark}}</text>
			<u-gap height="80"></u-gap>
			<u-col span="400">
				<u-row gutter="20">
					<button @click="navToEdit" >编辑</button>
					<u-modal v-model="show" :content="content" :show-cancel-button="true" @confirm="confirmExit" @cancel="cancel"></u-modal>
					<button @click="del" type="error">删除</button>
				</u-row>
			</u-col>
		</view>
	</view>
</template>

<script>
	import {deptOneDelSendData} from "../../api/api.js"
	export default {
		data() {
			return {
				deptid:'',
				deptname:'',
				remark:'',
				depturl:'',
				item:'',
				imageSrc:'',
				show: false,
				content: '确认删除该部门？'
			}
		},
		onLoad: function(option) {
			this.item = JSON.parse(decodeURIComponent(option.item))
			this.imageSrc=this.item.depturl
			console.log("one")
			console.log(this.imageSrc)
			console.log(this.item.depturl)
			console.log(this.item.remark)
		},
		methods: {
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
				this.show = true;
			},
			confirmExit(){
				let data = { 
					deptid:this.item.deptid
				}
				console.log(this.item.deptid)
				console.log(data)
				deptOneDelSendData(data)
					.then((response) => {
						this.showDelSuccessToast();
						uni.navigateBack()
					})
					.catch((error) => {
						console.log(error);
						this.showDelFalseToast();
					})		
			},
			cancel(){
				this.show = false;
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
	},
	.title{
		font-size: larger;
		font-weight: bold;
	}
</style>
