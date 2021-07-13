<template>
	<view>
		<u-form :model="form" ref="uForm" label-position="top" :required=true>
			
			<u-form-item label="姓名" prop="username">
				<u-input v-model="form.username"  placeholder='请输入姓名'/>
			</u-form-item>

			<u-form-item label="身份证号码" prop="cardid">
				<u-input v-model="form.cardid"  placeholder='请输入身份证号码'/>
			</u-form-item>

			<u-form-item label="性别" prop="sex">
				<u-select v-model="sexSelShow" mode="single-column" :list="sexList" @confirm="sexConfirm"></u-select>
				<u-input v-model="form.sex" type="select" @click="sexSelShow = true"  placeholder='请选择性别'/>
			</u-form-item>

			<u-form-item label="出生日期" prop='birthday'>
				<u-calendar v-model="calSelShow" mode="date" @change="calChange">
					<view slot="tooltip">
						<view class="title">
							请选择出生日期
						</view>
					</view>
				</u-calendar>
				<u-input v-model="form.birthday" type="select" @click="calSelShow = true"  placeholder='请选择出生日期'/>
			</u-form-item>

			<u-form-item label="职位" prop="position">
				<u-select v-model="posSelShow" mode="mutil-column-auto" :list="posList" @confirm="posConfirm">
				</u-select>
				<u-input v-model="posSelRes" type="select" @click="posSelShow = true"  placeholder='请选择职位'/>
			</u-form-item>

			<u-form-item label="学历" prop="education">
				<u-select v-model="eduSelShow" mode="single-column" :list="eduList" @confirm="eduConfirm"></u-select>
				<u-input v-model="form.education" type="select" @click="eduSelShow = true"  placeholder='请选择学历'/>
			</u-form-item>

			<u-form-item label="邮箱" prop='email'>
				<u-input v-model='form.email' type='text'  placeholder='请输入邮箱'/>
			</u-form-item>

			<u-form-item label="电话号码" prop='tel'>
				<u-input v-model='form.tel' type='digit'  placeholder='请输入电话号码'/>
			</u-form-item>

			<u-form-item label="政治面貌" prop='party'>
				<u-input v-model='form.party' type='text'  placeholder='请输入政治面貌'/>
			</u-form-item>

			<u-form-item label="QQ号码" prop='qqnum'>
				<u-input v-model='form.qqnum' type='digit'  placeholder='请输入QQ号码'/>
			</u-form-item>

			<u-form-item label="联系地址" prop='address'>
				<u-picker v-model="addressSelShow" mode="region" @confirm="addressConfirm" :mask-close-able=true>
				</u-picker>
				<u-input v-model="rangeAddress" type="select" placeholder="请选择地区" @click="addressSelShow = true" />
				<u-input v-model="detailAddress" type="text" placeholder="请输入详细地址" />
			</u-form-item>

			<u-form-item label="邮政编码" prop='postcode'>
				<u-input v-model='form.postcode' type='text'  placeholder='请输入邮政编码'/>
			</u-form-item>

			<u-button class="form-button" type="primary" @click="formSubmit">提交</u-button>
		</u-form>
	</view>
</template>

<script>
	export default {
		name: 'staffForm',
		props:{
			form
		},
		data(){
			return{
				rules: {
					username: [{
						required: true,
						message: '姓名不能为空',
						trigger: ['change', 'blur']
					}, ],
					cardid: [{
						type: 'number',
						message: '身份证号码格式不正确',
						trigger: ['change', 'blur']
					}, {
						len: 18,
						message: '身份证号码为18位',
						trigger: ['change', 'blur']
					}, ],
					sex: // Not Null
						[{
							required: true,
							message: '性别不能为空',
							trigger: ['change', 'blur']
						}, ],
					// TODO 职位
					// position: [{
					// 	required: true,
					// 	message: '职位不能为空',
					// 	trigger: ['change', 'blur']
					// }, ],
					email: [{
						type: 'email',
						message: "邮箱格式不正确",
						trigger: ['change', 'blur']
					}, ],
					tel: // Not Null
						[{
							required: true,
							message: '手机号码不能为空',
							trigger: ['change', 'blur']
						}, {
							// 自定义验证函数，见上说明
							validator: (rule, value, callback) => {
								// 上面有说，返回true表示校验通过，返回false表示不通过
								// this.$u.test.mobile()就是返回true或者false的
								return this.$u.test.mobile(value);
							},
							message: '手机号码格式不正确',
							// 触发器可以同时用blur和change
							trigger: ['change', 'blur'],
						}, ],
					qqnum: [{
						type: 'number',
						message: "QQ号码格式不正确",
						trigger: ['change', 'blur']
					}, ],
				
					postcode: [{
						type: 'number',
						message: "邮编格式不正确",
						trigger: ['change', 'blur']
					}, ]
				
				},
				// 文字提示
				errorType: ['message']
				// 不提示
				// errorType: ['none'],
				// 文字和下划线提示
				// errorType: ['message', 'border-bottom'],
			}
		},

		methods: {
			formSubmit() {
				this.$refs.uForm.validate(valid => {
					console.log("正在提交")
					console.log(this.form)
					this.form.address = this.rangeAddress + this.detailAddress
					if (valid) {
						console.log('验证通过');
					} else {
						console.log('验证失败');
					}
				});
			},
			statusConfirm(e) {
				console.log(e)
				this.form.status = e[0].value
				this.statusLabel = e[0].label
			},
			sexConfirm(e) {
				console.log(e)
				this.form.sex = e[0].label
			},
			posConfirm(e) {
				this.posSelRes = e[0].label + " " + e[1].label
				this.form.deptname = e[0].label
				this.form.jobname = e[1].label
				console.log(e)
			},
			eduConfirm(e) {
				console.log(e)
				this.form.education = e[0].label
			},
			addressConfirm(e) {
				console.log(e)
				this.rangeAddress = e.province.label + e.city.label + e.area.label
			},
			calChange(e) {
				console.log(e)
				this.form.birthday = e.result
			}

		},
		// 必须要在onReady生命周期，因为onLoad生命周期组件可能尚未创建完毕
		onReady() {
			console.log('onready中')
			console.log('姓名' + this.form.username)
			this.$refs.uForm.setRules(this.rules);
			console.log('onready后')
		},
		onLoad(){
			
		}

	}
</script>

<style>
	.title {
		color: $u-type-primary;
		text-align: center;
		padding: 20rpx 0 0 0;
	}

	.form-button {
		width: min-content
	}
</style>
