 <template>
 	<view>
 		<u-gap height="40"></u-gap>
 		<view class="deptOne">
 			<text>部门名字</text>
 			<u-input type="text" :border="true" placeholder="请输入部门名字"/>
 			<u-gap height="30"></u-gap>
 			<text>部门描述</text>
 			<u-gap height="10"></u-gap>
 			<u-input type="textarea" height="700" :border="true" placeholder="请输入部门描述"/>
 			<u-gap height="80"></u-gap>
 			<u-col span="400">
 				<u-row gutter="20">
 					<button @click="submit" >提交</button>
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
 				deptDctipt:''
 			}
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
 				let data = {
 							
 				}
 				SendData(data)
 					.then((response) => {
 						this.showDelSuccessToast();
 						uni.switchTab({
 							url: '/pages/dept/show'
 						})
 					})
 					.catch((error) => {
 						console.log(error);
 						this.showDelFalseToast();
 					})		
 			}
 			
 			
 		}
 	}
 </script>
 
 <style>
 	.deptOne{
 		margin: 0 50rpx;
 	}
 
 </style>
 