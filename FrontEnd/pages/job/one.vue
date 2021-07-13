<template>
	<view>
		<u-toast ref="uToast" />
		<view class="jobOne">
			<u-gap height="60"></u-gap>
			<text class="title">职位名字:</text>
			<u-gap height="30"></u-gap>
			<text>{{item.jobname}}</text>
			<u-gap height="60"></u-gap>
			<text class="title">职位描述:</text>
			<u-gap height="30"></u-gap>
			<text>{{item.remark}}</text>
			<u-gap height="80"></u-gap>
			<u-col span="400">
				<u-row gutter="20">
						<button @click="navToEdit" >编辑</button>
						<u-modal v-model="show" :content="content" :show-cancel-button="true" @confirm="confirm" @cancel="cancel"></u-modal>
						<button @click="del" type="error">删除</button>
					</u-row>
				</u-col>
		</view>
	</view>
</template>

<script>
	import {jobOneDelSendData} from "../../api/api.js"
	export default {
		data() {
			return {
				jobid:'',
				value: '',
				jobname:'',
				remark:'',
				item:'',
				show: false,
				content:'确认删除？'
			}
		},
		onLoad: function(option) {
			this.item = JSON.parse(decodeURIComponent(option.item));
			// console.log("one");
			// console.log(this.item.name);
			// console.log(this.item.remark);
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
			confirm(){
				let data = {
					jobid:this.item.jobid		
				}
				jobOneDelSendData(data)
					.then((response) => {
						this.showDelSuccessToast();
						uni.navigateTo({
							url: '/pages/job/show'
						})
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
				// console.log(this.item.name),
				// console.log(this.item.dcrpt)
			}
			
			
		}
	}
</script>

<style>
	.jobOne{
		margin: 0 50rpx;
	},
	.title{
		font-size: larger;
		font-weight: bold;
	}

</style>
