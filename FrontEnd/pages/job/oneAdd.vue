 <template>
  	<view>
		<u-toast ref="uToast" />
  		<u-gap height="40"></u-gap>
  		<view class="jobOne">
			<text>职位所属部门</text>
			<u-select v-model="showSelect" :list="list"></u-select>
			<u-button @click="showSelect = true">选择</u-button>
			<u-gap height="30"></u-gap>
  			<text>职位名称</text>
  			<u-input type="text" :border="true" placeholder="请输入职位名称" v-model="jobname"/>
  			<u-gap height="30"></u-gap>
  			<text>职位描述</text>
  			<u-gap height="10"></u-gap>
  			<u-input type="textarea" height="700" :border="true" placeholder="请输入职位描述" v-model="remark"/>
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
 	import {jobAddSendData,jobAddShowSendData} from "../../api/api.js"
  	export default {
  		data() {
  			return {
				deptname:'',
  				jobname:'',
  				remark:'',
 				show: false,
 				content: '确认提交？',
				showSelect:false,
				list:[]
  			}
  		},
		onLoad() {
			// TODO
			// jobAddShowSendData()
			// 	.then((response) => {
			// 		this.list = response.data.data
			// 	})
			// 	.catch((error) => {
			// 		console.log(error)
			// 		this.showFalseToast()
			// 	})		
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
					deptname:this.deptname,
 					jobname:this.jobname,
 					remark:this.remark,
 				}
 				jobAddSendData(data)
 					.then((response) => {
 						this.showSuccessToast();
 						uni.redirectTo({
 							url: '/pages/job/show'
 						})
 					})
 					.catch((error) => {
 						console.log(error)
 						this.showFalseToast()
 					})		
 			},
 			cancel(){
 				this.show = false;
 			}
  			
  			
  		}
  	}
  </script>
  
  <style>
  	.deptOne{
  		margin: 0 50rpx;
  	}
  
  </style>
 
 
 