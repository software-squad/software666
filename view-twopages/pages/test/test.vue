<template>
	<view>
		<u-cell-group>
			<u-cell-item class="" :value='user.username' :valueStyle='valueStyle' :title-style="titleStyle"
				:arrow='false'>
				<u-image width='120rpx' height='120rpx' slot="title" :src="user.faceurl" shape="circle"
					@click='changeHead'></u-image>
			</u-cell-item>
			<u-gap height="15" bg-color="#f9f9f9"></u-gap>

			<u-cell-group>
				<u-cell-item v-for="(value,key) in labelDict" :title='value' :value='user[key]' :valueStyle='valueStyle'
					:title-style="titleStyle" :arrow='false' v-show="user[key]?true:false">
				</u-cell-item>
			</u-cell-group>

			<!-- <u-cell-item @click='changeSex' title="性别" :value="sex" :valueStyle='valueStyle' :title-style="titleStyle"
				:arrow='false'></u-cell-item>
			<u-cell-item title="年龄" value="29" :valueStyle='valueStyle' :title-style="titleStyle" :arrow='false'>
			</u-cell-item> -->
			<!-- <u-gap height="15" bg-color="#f9f9f9"></u-gap>
			<u-cell-item title="行业" value="互联网" :valueStyle='valueStyle' :title-style="titleStyle"></u-cell-item>
			<u-cell-item title="职业" value="web开发" :valueStyle='valueStyle' :title-style="titleStyle"></u-cell-item>
			<u-cell-item title="个性签名" :valueStyle='valueStyle' :title-style="titleStyle">
				<view class="u-line-1">
					{{profile}}
				</view>
			</u-cell-item> -->
		</u-cell-group>
	</view>
</template>

<script>
	export default {
		computed: {
			getPhone() {
				var reg = /^(\d{3})\d{4}(\d{4})$/;
				return this.phone.replace(reg, "$1****$2");
			}
		},
		data() {
			return {

				// phone: '13088888888',
				// profile: '欢迎加扣群(325021815)交流学习',
				// sex: '男',
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
					username: 'picca', // Not Null
					cardid: '520131415926771111',
					sex: '男', // Not Null
					deptname: '技术部', // Not Null
					jobname: 'java工程师', // Not Null
					education: '本科',
					email: '199@qq.com',
					tel: '15387622222', // Not Null
					party: '群众',
					qqnum: '111',
					address: 'aaaaaaa',
					postcode: '111',
					// birthday: '2020-03-12',

					loginname: 'huachenyu',
					password: 'huahcenyu',
					status: '0',
					faceurl: '/static/logo.png',
					// '民族',
					// '所学专业',
					// '爱好',
					// '备注'
				},
				tesst: [{
					"deptid": 1,
					"deptname": "技术部",
					"jobs": [{
							"jobid": 1,
							"jobname": "java工程师",
						},
						{
							"jobname": "python工程师",
							"jobid": 2,
						},
					]
				}, {
					"deotid": 2,
					"name": "生活部",
					"jobs": [{
							"jobid": 1,
							"jobname": "主厨",

						},
						{
							"jobname": "供应商",
							"jobid": 2,
						},
					]
				}, {
					"deptid": 1,
					"deptname": "后勤部",
					"jobs": [{
						"jobname": "清洁工",
						"jobid": 1,
					}, {
						"jobname": "门卫",
						"jobid": 2,
					}]
				}],
			}
		},
		methods: {
			changeHead() {
				console.log("图片选择中")
				uni.chooseImage({
					count: 1,
					success: (res) => {
						this.user.faceurl = res.tempFilePaths[0]
						console.log("图片选择成功")
						console.log(this.user.faceurl)
					}
				});
			},
			changeSex() {
				const arr = ['男', '女', '保密']
				uni.showActionSheet({
					itemList: arr,
					success: (res) => {
						this.sex = arr[res.tapIndex]
					},
					fail: function(res) {
						console.log(res.errMsg);
					}
				});
			}
		}
	}
</script>

<style>
	page {
		background-color: #f9f9f9;
	}

	.avatar-item {
		margin: 20rpx;
	}
</style>
