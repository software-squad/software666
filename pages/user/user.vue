 <template>
 	<view>
		<u-toast ref="uToast" />
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
		<u-tabbar :list="tabbar0" ></u-tabbar>
 	</view>
 </template>
 
 <script>
	 import {sendThis} from "../../api/request.js"
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
				jobname:'',
				tabbar0: [{
						iconPath: "/static/tab_icons/home.png",
						selectedIconPath: "/static/tab_icons/homeHL.png",
						text: '首页',
						pagePath: "/pages/menu/menu"
					},
					{
						iconPath: "/static/tab_icons/人员.png",
						selectedIconPath: "/static/tab_icons/人员HL.png",
						text: '员工中心',
						pagePath: "/pages/staff/show"
					},
					{
						iconPath: "/static/tab_icons/user.png",
						selectedIconPath: "/static/tab_icons/userHL.png",
						text: '我的',
						pagePath: "/pages/user/user"
				
					},
				],
 			}
 		},
		// 页面加载时
 		onLoad(){
			// 将当前页面的this传到request.js
			sendThis(this)
			// 获取前端存储的uerid
			this.userid = sessionStorage.getItem('userid')
			// 根据userid获取userinfo
			this.GetInfo()
			
 		},
 		methods: {
			// 根据userid获取userinfo
			GetInfo(){
				let data = {
					userid:this.userid
				}
				
				this.$request.request({
									url: '/api/staff/oneByUserid',
									method: "GET",
									data:data,
								})
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
			// 拦截器调用展示msg信息
			showToast(TITLE,TYPE) {
							this.$refs.uToast.show({
								title: TITLE.toString(),
								type: TYPE.toString(),
							})
			},
			// 带参跳转到修改密码页面
 			changePwd() {
 				uni.navigateTo({
 					url: "../user/changepwd?pic="+encodeURIComponent(JSON.stringify(this.faceurl))
 				})
 			},
			// 点击离开后弹窗消失
 			exit() {
 				this.show = true;
 			},
			// 确认离开后跳转到登陆界面，并将token删除
 			confirmExit() {
 				sessionStorage.clear()
				try {
				    uni.clearStorageSync();
				} catch (e) {
				}
 				uni.navigateTo({
 					url: "../login/login"
 				})
 			},
			// 点击取消后弹窗消失
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