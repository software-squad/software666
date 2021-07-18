<template>
	<view>
		<u-cell-group>
			<u-cell-item  title="重置密码权限" arrow="true" @click="click"></u-cell-item>
		</u-cell-group>
	</view>
</template>

<script>
	export default {
		data() {
			return {

			}
		},
		methods: {
			click(){
				uni.navigateTo({
					url:'./forgetPassword'
				})
			}
		}
	}
</script>

<style>

</style>
