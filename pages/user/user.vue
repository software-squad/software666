 <template>
 	<view>
 		<view class="userimage">
 			<u-image width="250rpx" height="250rpx" :src="faceurl" shape="circle"></u-image>
 		</view>
 		<view class="userinfo">
 			<u-gap height="70"></u-gap>
 			<u-cell-group :border="true">
 				<u-cell-item icon="info-circle" title="姓名" :value="username" :arrow="false"></u-cell-item>
 				<u-cell-item icon="info" title="性别" :value="sex" :arrow="false"></u-cell-item>
 				<u-cell-item icon="phone" title="电话" :value="tel" :arrow="false"></u-cell-item>
 				<u-cell-item icon="account" title="工号" :value="userid" :arrow="false"></u-cell-item>
 				<u-cell-item icon="home" title="部门" :value="deptname" :arrow="false"></u-cell-item>
 				<u-cell-item icon="order" title="职位" :value="jobname" :arrow="false"></u-cell-item>
 
 			</u-cell-group>
 		</view>
 		<view class="userBtn">
 			<u-button @click="changePwd">修改密码</u-button>
 			<u-gap height="20"></u-gap>
 			<u-modal v-model="show" :content="content" :show-cancel-button="true" @confirm="confirmExit"
 				@cancel="cancel"></u-modal>
 			<u-button type="error" @click="exit">退出登录</u-button>
 		</view>
 	</view>
 </template>
 
 <script>
 	import {userSendData} from "../../api/api.js"
 	export default {
 		data() {
 			return {
 				faceurl:'',
 				show: false,
 				content: '确认退出登录？',
 				userid: '',
				username:'',
				sex:'',
				tel:'',
				deptname:'',
				jobname:''
 			}
 		},
 		onLoad(){
			// #ifdef H5
			this.userid = sessionStorage.getItem('userid')
			// #endif
			// #ifndef H5
			this.userid = uni.getStorageSync('userid')
			// #endif
			let data = {
				userid:this.userid
			}
			userSendData(data)
			.then((response) => {
				this.faceurl=response.data.data.faceurl,
				this.username=response.data.data.username,
				this.sex=response.data.data.sex,
				this.tel=response.data.data.tel,
				this.deptname=response.data.data.deptname,
				this.jobname=response.data.data.jobname
			})
			.catch((error) => {
				console.log(error);
			})
 		},
 		methods: {
 
 			changePwd() {
				console.log('123')
 				uni.navigateTo({
 					url: "../user/changepwd?pic="+encodeURIComponent(JSON.stringify(this.faceurl))
 				})
 			},
 			exit() {
 				this.show = true;
 			},
 			confirmExit() {
 				// #ifdef H5
 				sessionStorage.clear()
 				// #endif
				// #ifndef H5
				uni.clearStorage();
				// #endif
 				uni.redirectTo({
 					url: "../login/login"
 				})
 			},
 			cancel() {
 				this.show = false;
 			}
 
 		}
 	}
 </script>
 
 <style>
 	.userimage {
 		align-items: center;
 		display: flex;
 		justify-content: center;
 	}
 
 	.userinfo {
 		margin: auto;
 		width: "200rpx";
 		padding: 0 50rpx;
 		border: #606266;
 	}
 
 	.userBtn {
 		padding: 75rpx;
 	}
 </style>