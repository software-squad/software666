<template>
	<view>
		<u-cell-group>
			<u-cell-item class="" :value='user.username' :valueStyle='valueStyle' :title-style="titleStyle"
				:arrow='false'>
				<u-image width='120rpx' height='120rpx' slot="title" :src="user.faceurl" shape="circle"></u-image>
			</u-cell-item>
			<u-gap height="15" bg-color="#f9f9f9"></u-gap>

			<!-- 动态实现方法一 -->
			<u-cell-group>
				<u-cell-item v-for="(value,key) in labelDict" :key='key' :title='value' :value='user[key]'
					:valueStyle='valueStyle' :title-style="titleStyle" :arrow='false' v-show="user[key]?true:false">
				</u-cell-item>
			</u-cell-group>

			<!-- 动态实现方法二 -->
			<!-- 先定一个数组，然后把这两条数据关联起来，组成对象，然后根据空值，加个是否显示的条件。然后便利数组 -->

		</u-cell-group>
	</view>
</template>

<script>
	export default {
		data() {
			return {
				valueStyle: {
					'text-align': 'left'
				},
				titleStyle: {
					'width': '160rpx'
				},

				labelDict: {
					// username: '姓名',
					sex: '性别',
					birthday: '出生日期',
					cardid: '身份证号码',
					deptname: '部门',
					jobname: '职位',
					education: '学历',
					email: '邮箱',
					tel: '手机',
					qqnum: 'QQ号码',
					party: '政治面貌',
					address: '联系地址',
					postcode: '邮政编码',
					// loginname:'账户名', 
					// password:'密码', 
					// status:'权限', 
					// '民族',
					// '所学专业',
					// '爱好',
					// '备注'
				},
				user: {}
			}
		},
		onLoad(item) {
			console.log(item)
			this.$request.request({
				url: '/api/staff/oneByUserid',
				method: 'GET',
				data: {
					userid: item.userid
				},
			}).then(res => {
				this.user = res.data.data
				uni.setNavigationBarTitle({
					title: this.user.username
				})
				if (!this.user.faceurl) {
					if (this.user.sex == '男') {
						this.user.faceurl = '/static/boy1.svg'
					} else if (this.user.sex == '女') {
						this.user.faceurl = '/static/girl1.svg'
					} else {
						this.user.faceurl = '/static/头像.svg'
					}
				}
			})
		},
		methods: {}
	}
</script>

<style>

</style>
