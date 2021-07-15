 <template>
 	<view>
		<!-- //u-view 弹窗组件 -->
 		<u-toast ref="uToast" />
 		<u-gap height="40"></u-gap>
 		<view class="jobOne">
			<u-row>
				<u-select v-model="showSelect" :list="list" mode="single-column" @confirm="confirmSelect"></u-select>
				<u-input type="text" :border="true" :placeholder="item.deptname" v-model="deptname" :disabled="true"/>
				<u-button @click="showSelect = true" style="width: 20%;">选择</u-button>
			</u-row>
			<u-gap height="30"></u-gap>
 			<text class="title">职位名称:</text>
 			<u-gap height="30"></u-gap>
 			<u-input  v-model="item.jobname" type="text" :border="true" />
 			<u-gap height="60"></u-gap>
 			<text class="title">职位描述:</text>
 			<u-gap height="30"></u-gap>
 			<u-input  v-model="item.remark" type="text" :border="true" />
 			<u-gap height="80"></u-gap>
 			<u-col span="400">
 				<u-row gutter="20">
 					<u-modal v-model="show" :content="content" :show-cancel-button="true" @confirm="confirm" @cancel="cancel"></u-modal>
 					<button @click="submit" type="primary">提交</button>
 				</u-row>
 			</u-col>
 		</view>
 	</view>
 </template>
 
 <script>
	 //import sendThis 函数，实现拦截器统一拦截msg码弹窗
	import {sendThis} from "../../api/request.js"
 	import {jobEditSendData,deptShowSendData} from "../../api/api.js"
 	export default {
 		data() {
 			return {
				deptname:'',
 				jobid:'',
 				jobname:'',
 				remark:'',
 				item:'',
 				show: false,
 				content: '确认提交？',
				showSelect: false,
				list:[]
 			}
 		},
		// 页面加载时
 		onLoad: function(option) {
			// 将当前页面的this传至request.js
			sendThis(this)
			// 获取带参跳转的值
 			this.item = JSON.parse(decodeURIComponent(option.item))
			// 请求职位信息并展示
			this.DeptShowSendData()
	
 		},
 		methods: {
			// 请求后端职位信息，并在回调函数中展示
			DeptShowSendData(){
				deptShowSendData()
					.then((response) => {
						this.list = []
						for (let i = 0; i < response.data.data.length; i++) {
							let d = {
								value: i,
								label: response.data.data[i].deptname,
							}
							this.list.push(d)
						}
					})
					.catch((error) => {
						console.log(error);
					})
			},
			//showToast方法，实现异常码弹窗
			showToast(TITLE,TYPE) {
							this.$refs.uToast.show({
								title: String(TITLE),
								type: String(TYPE),
							})
			},
			// 显示确认弹窗
 			submit(){
 				this.show = true;
 			},
			// 根据列选择器更新全局变量
			confirmSelect(e) {
				console.log(e[0].label)
				this.deptname = e[0].label
			},
			// 提交编辑过后的信息
 			confirm(){
 				let data = {
 					jobid:this.item.jobid,
					deptname:this.deptname,
 					jobname:this.item.jobname,
 					remark:this.item.remark,
 				}
			// 调用接口
 				jobEditSendData(data)
 					.then((response) => {
 						this.showToast('提交成功','success')
 						// 回调函数里返回show页面并刷新
 						let pages = getCurrentPages(); // 当前页面
 						let beforePage = pages[pages.length - 3]; // 上两页
 						uni.navigateBack({
 							success: function() {
 								console.log("返回上一页并刷新")
 								beforePage.JobShowSendData() // 执行上一页的方法
 							}
 						});
 					})
 					.catch((error) => {
 						console.log(error);
 						this.showToast('提交失败','false')
 					})		
 			},
			// 点击取消后弹窗不再显示
 			cancel(){
 				this.show = false;
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
 