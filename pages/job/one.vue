<template>
	<view>
			<u-toast ref="uToast" />
			<view class="jobOne">
				<u-gap height="30"></u-gap>
				<text class="title">所属部门</text>
				<u-gap height="30"></u-gap>
				<text>{{item.deptname}}</text>
				<u-line color="#bbb" />
				<u-gap height="30"></u-gap>
				<text class="title">职位名字</text>
				<u-gap height="30"></u-gap>
				<text>{{item.jobname}}</text>
				<u-gap height="40"></u-gap>
				<u-line color="#bbb" />
				<u-gap height="15"></u-gap>
				<text class="title">职位描述</text>
				<u-gap height="30"></u-gap>
				<text>{{item.remark}}</text>
				<u-gap height="40"></u-gap>
				<u-line color="#bbb" />
				<u-gap height="40"></u-gap>
				<u-col span="400">
					<u-row gutter="20">
							<u-button @click="navToEdit"  shape="circle" class="custom-style">编辑</u-button>
							<u-modal v-model="show" :content="content" :show-cancel-button="true" @confirm="confirm" @cancel="cancel"></u-modal>
							<u-button @click="del" v-if="item.deptname!='待定'" type="error" shape="circle" class="custom1-style" >删除</u-button>
						</u-row>
					</u-col>
			</view>
		</view>
</template>

<script>
	import {sendThis} from "../../api/request.js"
	import {jobOneDelSendData} from "../../api/api.js"
	export default {
		data() {
			return {
				jobid:'',
				value: '',
				jobname:'',
				deptname:'',
				remark:'',
				item:'',
				show: false,
				content:'确认删除？',
			}
		},
		// 页面加载时
		onLoad: function(option) {
			// 将指向当前页面的指针传给request.js
			sendThis(this)
			// 取到上一个页面带参跳转的值
			this.item = JSON.parse(decodeURIComponent(option.item));
			// 设置title
			uni.setNavigationBarTitle({
				title:this.item.jobname+" | "+this.item.deptname
			})

		},
		methods: {
			// 拦截器调用显示错误信息
			showToast(TITLE,TYPE) {
							this.$refs.uToast.show({
								title: String(TITLE),
								type: String(TYPE),
							})
			},
			// 点击删除后显示弹窗
			del(){
				this.show = true;	
			},
			// 点击确认后将删除的职位的id发给后端，根据后端的返回码显示删除成功的信息
			confirm(){
				let data = {
					jobid:this.item.jobid		
				}
				jobOneDelSendData(data)
					.then((response) => {
						this.showToast('删除成功','success');
						// 回调函数里返回show页面并刷新
						let pages = getCurrentPages(); // 当前页面
						let beforePage = pages[pages.length - 2]; // 上一页
						uni.navigateBack({
							success: function() {
								console.log("返回上一页并刷新")
								beforePage.JobShowSendData() // 执行上一页的方法
							}
						});
					})
					.catch((error) => {
						console.log(error);
						this.showToast('删除失败','false');
					})	
			},
			// 点击取消，弹窗消失
			cancel(){
				this.show = false;
			},
			// 跳转到编辑页面，带参
			navToEdit(){
				// TODO 记得检验一下登录逻辑
				uni.navigateTo({
					url: "edit?item="+encodeURIComponent(JSON.stringify(this.item))
				})
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
		margin-left: 260rpx;
	}
	.custom-style{
		color: #241c32;
		font-weight: bold;
		/* background-color: #a8a7ab; ; */
		width: 150rpx;
		height: 90rpx;
	}
	.custom1-style{
		color: #241c32;
		font-weight: bold;
		background-color: #e6e6e6; 
		width: 150rpx;
		height: 90rpx;
	}
</style>
