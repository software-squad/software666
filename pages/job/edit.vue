 <template>
 	<view>
 		<u-toast ref="uToast" />
 		<u-gap height="40"></u-gap>
 		<view class="jobOne">
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
 					<button @click="submit" >提交</button>
 				</u-row>
 			</u-col>
 		</view>
 	</view>
 </template>
 
 <script>
 	import {jobEditSendData} from "../../api/api.js"
 	export default {
 		data() {
 			return {
 				jobid:'',
 				jobname:'',
 				remark:'',
 				item:'',
 				show: false,
 				content: '确认提交？'
 			}
 		},
 		onLoad: function(option) {
 			console.log(option)
 			this.item = JSON.parse(decodeURIComponent(option.item))
 	// 		console.log("edit");
 	// 		console.log(this.item.deptname);
		
 	// 		console.log(this.item.remark);	
	
 		},
 		methods: {
 			showSuccessToast() {
 				this.$refs.uToast.show({
 					title: '提交成功',
 					type: 'success'
 				})
 			},
 			showFalseToast() {
 				this.$refs.uToast.show({
 					title: '提交失败',
 					type: 'false'
 				})
 			},
 			submit(){
 				this.show = true;
 			},
 			confirm(){
 				let data = {
 					jobid:this.item.jobid,
 					jobname:this.item.jobname,
 					remark:this.item.remark,
 				}
 				jobEditSendData(data)
 					.then((response) => {
 						this.showSuccessToast();
 						uni.navigateTo({
 							url: '/pages/job/show'
 						})
 					})
 					.catch((error) => {
 						console.log(error);
 						this.showFalseToast();
 					})		
 			},
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
 