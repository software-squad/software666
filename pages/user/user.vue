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
		<u-tabbar :list="tabBerList" :mid-button="midBtn" active-color="#5098FF" inactive-color="#909399"
			:border-top=false bg-color="#F8F8F8"></u-tabbar>
	</view>
</template>

<script>
	import {
		mapGetters
	} from 'vuex'
	import {
		sendThis
	} from "../../api/request.js"
	export default {
		data() {
			return {
				faceurl: '',
				show: false,
				content: '确认退出登录？',
				userid: '',
				username: '',
				sex: '',
				tel: '',
				deptname: '',
				jobname: '',
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
		computed: {
			...mapGetters([
				'tabBerList',
				'midBtn'
			])
		},
		onLoad() {
			sendThis(this)
			// this.userid = sessionStorage.getItem('userid')
			this.userid = uni.getStorageSync('userid')
			this.$api.staffOneByUseridSendData({
				userid:this.userid
			}).then((response) => {
					this.faceurl = response.data.data.faceurl,
						this.username = response.data.data.username,
						this.sex = response.data.data.sex,
						this.tel = response.data.data.tel,
						this.deptname = response.data.data.deptname,
						this.jobname = response.data.data.jobname
					// UPDATE 判断性别
					if (!this.faceurl) {
						if (this.sex == '男') {
							this.faceurl = '/static/boy1.svg'
						} else if (this.sex == '女') {
							this.faceurl = '/static/girl1.svg'
						} else {
							this.faceurl = '/static/头像.svg'
						}
					}
				})
				.catch((error) => {
					console.log(error);
				})
		},
		methods: {
			showToast(TITLE, TYPE) {
				this.$refs.uToast.show({
					title: TITLE.toString(),
					type: TYPE.toString(),
				})
			},

			changePwd() {
				console.log('123')
				uni.navigateTo({
					url: "../user/changepwd?pic=" + encodeURIComponent(JSON.stringify(this.faceurl))
				})
			},
			exit() {
				this.show = true;
			},
			confirmExit() {
				// #ifdef H5
				sessionStorage.clear()
				// #endif
				uni.clearStorageSync()
				uni.reLaunch({
					url:"../login/login"
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
