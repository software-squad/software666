 <template>
 	<view>
 		<u-toast ref="uToast" />
 		<u-gap height="40"></u-gap>
 		<view class="deptOne">
 			<image :src="imageSrc" ></image>
 			<u-gap height="60"></u-gap>
 			<text class="title">部门名字:</text>
 			<u-gap height="30"></u-gap>
			<u-input  v-model="item.deptname" type="text" :border="true" />
 			<u-gap height="60"></u-gap>
 			<text class="title">部门描述:</text>
 			<u-gap height="30"></u-gap>
			<u-input  v-model="item.remark" type="text" :border="true" />
 			<u-gap height="80"></u-gap>
			<text class="title">部门照片:</text>
			<u-input  v-model="item.depturl" type="text" :border="true" />
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
	import {deptEditSendData} from "../../api/api.js"
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
 				content: '确认提交？'
 			}
 		},
 		onLoad: function(option) {
 			console.log(option)
 			this.item = JSON.parse(decodeURIComponent(option.item))
			this.imageSrc = this.item.depturl
			this.value = this.item.deptname
 			console.log("edit")
 			console.log(this.item.deptname)
 			console.log(this.item.remark)
		
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
 				this.show = true
 			},
			confirm(){
				let data = {
					deptid:this.item.deptid,
					deptname:this.item.deptname,
					remark:this.item.remark,
					depturl:this.item.depturl
				}
				deptEditSendData(data)
					.then((response) => {
						this.showSuccessToast()
						uni.navigateTo({
							url: '/pages/dept/show'
						})
					})
					.catch((error) => {
						console.log(error)
						this.showFalseToast()
					})		
			},
			cancel(){
				this.show = false
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
 