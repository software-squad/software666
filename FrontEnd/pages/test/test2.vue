<template>
	<view>
		<view class="userimage">
			<u-image width="250rpx" height="250rpx" :src="imageSrc" shape="circle"></u-image>
		</view>
		<view class="userinfo">
			<u-gap height="70"></u-gap>
			<u-cell-group :border="true" >
				<u-cell-item icon="info-circle" title="姓名" value="朱某" :arrow="false"></u-cell-item>
				<u-cell-item icon="info-circle" title="性别" value="男" :arrow="false"></u-cell-item>
				<u-cell-item icon="phone" title="电话" value="177555666" :arrow="false"></u-cell-item>
				<u-cell-item icon="account" title="工号" value="20196666" :arrow="false"></u-cell-item>
				<u-cell-item icon="home" title="部门" value="搬砖部" :arrow="false"></u-cell-item>
				<u-cell-item icon="order" title="职位" value="总经理" :arrow="false"></u-cell-item>
				
			</u-cell-group>
		</view>
		<view class="userBtn">
			<u-button @click="changePwd" >修改密码</u-button>
			<u-gap height="20"></u-gap>
			<u-modal v-model="show" :content="content" :show-cancel-button="true" @confirm="confirmExit" @cancel="cancel"></u-modal>
			<u-button type="error" @click="exit">退出登录</u-button>
		</view>
	</view>
</template>

<script>
	export default {
		data() {
			return {
				imageSrc:"/static/头像1.svg",
				show: false,
				content: '确认退出登录？'
				
			}
		},
		methods: {
				
			changePwd(){
				uni.navigateTo({
					url:"./changepwd"
				})
			},
			exit(){
				this.show = true;
			},
			confirmExit(){
				uni.navigateTo({
					url:"../login/login"
				})
			},
			cancel(){
				this.show = false;
			}
			
		}
	}
</script>

<style>
	.userimage{
		align-items: center;
		display: flex;
		justify-content: center;
		margin-top: 20rpx;
	},
		
	.userinfo{
		margin: auto;
		width: "200rpx";
		padding: 0 50rpx;
		border: #606266;
	}
		
	.userBtn{
		padding: 75rpx;
	}

</style>