<template>
	<view>
		<view class="userimage">
			<u-image width="250rpx" height="250rpx" :src="imageSrc" shape="circle"></u-image>
		</view>
		<u-gap height="200"></u-gap>
		<view class="password">
			<u-input type="password" :border="true" v-model="password" placeholder="请输入原密码" />
			<u-gap height="30"></u-gap>
			<u-input type="password" :border="true" v-model="password" placeholder="请输入新密码" />
			<u-gap height="30"></u-gap>
			<u-input type="password" :border="true" v-model="password" placeholder="请再次输入新密码" />
			<u-gap height="180"></u-gap>
		</view>
		<u-row>
			<u-button type="primary" @click="confirm" >确认</u-button>
			<u-button  type="error" @click="cancel" >取消</u-button>
		</u-row>
	</view>
</template>

<script>
	export default {
		data() {
			return {
				imageSrc: "/static/user/userImage.png"
			}
		},
		methods: {
			confirm(){
				uni.navigateTo({
					url:"./user"
				})
			},
			cancel(){
				uni.navigateTo({
					url:"./user"
				})
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

	,
	.password {
		align-items: center;
		width: 100%;
		padding: 0 50rpx;
	}
</style>
