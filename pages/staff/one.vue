<template>
	<view>
		<u-cell-group>
			<u-cell-item class="" :value='user.username' :valueStyle='valueStyle' :title-style="titleStyle"
				:arrow='false'>
				<u-image width='120rpx' height='120rpx' slot="title" :src="user.faceurl" shape="circle"
					@click='changeHead'></u-image>
			</u-cell-item>
			<u-gap height="15" bg-color="#f9f9f9"></u-gap>

			<!-- 动态实现方法一 -->
			<u-cell-group>
				<u-cell-item v-for="(value,key) in labelDict" :title='value' :value='user[key]' :valueStyle='valueStyle'
					:title-style="titleStyle" :arrow='false' v-show="user[key]?true:false">
				</u-cell-item>
			</u-cell-group>

			<!-- 动态实现方法二 -->
			<!-- 你先定一个数组，然后把这两条数据关联起来，组成对象，然后根据空值，加个是否显示的条件。然后便利数组 -->

		</u-cell-group>
	</view>
</template>

<script>
	import request from '@../../api/request.js'
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
				user: {
					// username: 'picca', // Not Null
					// cardid: '520131415926771111',
					// sex: '男', // Not Null
					// deptname: '技术部', // Not Null
					// jobname: 'java工程师', // Not Null
					// education: '本科',
					// email: '199@qq.com',
					// tel: '15387622222', // Not Null
					// party: '群众',
					// qqnum: '111',
					// address: '四川省南充市仪陇县四组',
					// postcode: '111',
					// birthday: '2020-03-12',
					// 	loginname: 'huachenyu',
					// 	password: 'huahcenyu',
					// 	status: '0',
					// 	faceurl: '/static/logo.png',
					// '民族',
					// '所学专业',
					// '爱好',
					// '备注'
				}
			}
		},
		// onLoad(item) {
		onLoad(item) {
			console.log(item)
			request({
				url: '/api/staff/oneByUserid',
				method: 'GET',
				data: {
					userid: item.userid
				},
			}).then(res => {
				console.log(res)
				this.user = res.data.data
				console.log("申请结果")
				console.log(this.user)
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
		methods: {
			
		}
	}
</script>

<style>

</style>
