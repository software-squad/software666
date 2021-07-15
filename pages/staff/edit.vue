<template>
	<view class="form-box">
		<!-- label-position="top" -->

		<!-- 员工头像 -->
		<view class="u-flex-col u-p-30 u-col-center" @click='changeHead'>
			<u-image width='150rpx' height='150rpx' :src="tempFilePath" shape="circle"></u-image>
		</view>

		<u-form :model="form" ref="uForm" label-width="160rpx">

			<u-form-item label="姓名" prop="username" required>
				<u-input v-model="form.username" placeholder='请输入姓名' />
			</u-form-item>

			<u-form-item label="身份证号码" prop="cardid">
				<u-input v-model="form.cardid" placeholder='请输入身份证号码' />
			</u-form-item>

			<u-form-item label="性别" prop="sex" required>
				<u-select v-model="sexSelShow" mode="single-column" :list="sexList" @confirm="sexConfirm"></u-select>
				<u-input v-model="form.sex" type="select" @click="sexSelShow = true" placeholder='请选择性别' />
			</u-form-item>

			<u-form-item label="出生日期" prop='birthday'>
				<u-calendar v-model="calSelShow" mode="date" @change="calChange">
					<view slot="tooltip">
						<view class="title">
							请选择出生日期
						</view>
					</view>
				</u-calendar>
				<u-input v-model="form.birthday" type="select" @click="calSelShow = true" placeholder='请选择出生日期' />
			</u-form-item>

			<u-form-item label="职位" prop="position" required>
				<u-select v-model="posSelShow" mode="mutil-column-auto" :list="posList" @confirm="posConfirm">
				</u-select>
				<u-input v-model="posSelRes" type="select" @click="posSelShow = true" placeholder='请选择职位' />
			</u-form-item>

			<u-form-item label="学历" prop="education">
				<u-select v-model="eduSelShow" mode="single-column" :list="eduList" @confirm="eduConfirm"></u-select>
				<u-input v-model="form.education" type="select" @click="eduSelShow = true" placeholder='请选择学历' />
			</u-form-item>

			<u-form-item label="邮箱" prop='email'>
				<u-input v-model='form.email' type='text' placeholder='请输入邮箱' />
			</u-form-item>

			<u-form-item label="电话号码" prop='tel' required>
				<u-input v-model='form.tel' type='digit' placeholder='请输入电话号码' />
			</u-form-item>

			<u-form-item label="政治面貌" prop='party'>
				<u-input v-model='form.party' type='text' placeholder='请输入政治面貌' />
			</u-form-item>

			<u-form-item label="QQ号码" prop='qqnum'>
				<u-input v-model='form.qqnum' type='digit' placeholder='请输入QQ号码' />
			</u-form-item>

			<u-form-item label="联系地址" prop='address'>
				<u-picker v-model="addressSelShow" mode="region" @confirm="addressConfirm" :mask-close-able=true>
				</u-picker>
				<u-input v-model="rangeAddress" type="select" placeholder="请选择地区" @click="addressSelShow = true" />
				<u-input v-model="detailAddress" type="text" placeholder="请输入详细地址" />
			</u-form-item>

			<u-form-item label="邮政编码" prop='postcode'>
				<u-input v-model='form.postcode' type='text' placeholder='请输入邮政编码' />
			</u-form-item>

			<u-form-item label="备注信息" prop='remark'>
				<!-- TODO 美化，添加Field -->
				<u-input v-model='form.remark' type='text' placeholder='' />
			</u-form-item>

			<u-button class="form-button" type="primary" @click="formSubmit">提交</u-button>

		</u-form>
		<u-toast ref="uToast" />
	</view>
</template>

<script>
	import util from "../../api/util.js"
	export default {
		name: 'staffForm',
		data() {
			return {
				// 图像占位符
				tempFilePath: '',

				// 选择结果占位符显示
				statusLabel: '',
				posSelRes: '',
				rangeAddress: '',
				detailAddress: '',

				// 选择栏显示或隐藏
				statusShow: false,
				sexSelShow: false,
				posSelShow: false,
				eduSelShow: false,
				calSelShow: false,
				addressSelShow: false,

				// 选择栏的各个选项
				statusList: util.statusList,
				sexList: util.sexList,
				eduList: util.eduList,
				posList: [],

				// 整个表单信息
				form: {
					userid: 0,
					password: '',
					status: '',
					loginname: '',
					faceurl: '',
					facepath: '',
					deptid: '',
					jobid: '',
					username: '',
					cardid: '',
					address: '',
					postcode: '',
					tel: '',
					qqnum: '',
					email: '',
					sex: '',
					party: '',
					birthday: '',
					education: '',
					// createdate: '',
					deptname: '',
					jobname: '',
					remark: '',
				},

				// 表单验证
				rules: util.editRule,
				// 表单验证错误提示
				errorType: ['message'], // 文字提示
			}
		},

		methods: {
			// 改变员工头像
			changeHead() {
				// 调用系统选择文件
				uni.chooseImage({
					count: 1,
					success: (res) => {
						this.tempFilePath = res.tempFilePaths[0]
						// 上传文件到阿里云服务器，并获取图片网址
						uniCloud.uploadFile({
							filePath: this.tempFilePath,
							cloudPath: res.tempFiles[0].name,
							success: (e) => {
								console.log('云存储上传成功', e)
								this.form.faceurl = e.fileID
							},
							fail() {
								this.$refs.uToast.show({
									title: '图片上传失败',
									type: 'error',
								})
							},
						});
					}
				});
			},


			// 表单提交
			formSubmit() {
				// 职位单独验证，form的验证好像不能看组合的结果验证
				// console.log('选中的职位', this.posSelRes)
				if (!this.posSelRes) {
					uni.showToast({
						title: '职位不能为空',
						icon: 'none',
					})
					return;
				}
				// form验证
				this.$refs.uForm.validate(valid => {
					if (valid) {
						console.log("正在提交表单", this.form)
						this.form.address = this.rangeAddress + this.detailAddress
						this.$api.staffEditSubmit(...this.form)
							.then(res => {
								// 10005 更新成功
								if (res.data.msg == 10005) {
									this.$refs.uToast.show({
										title: '提交成功',
										type: 'success',
									})
									// 添加时限逻辑。避免猛地返回
									setTimeout(() => {
										uni.navigateBack()
									}, 1000)
								}
								// easy_request会有提示框，无需toast
							})
					} else {
						// 会有提示框，无需toast
						console.log('验证失败')
					}
				});
			},

			// ======================================================================
			// 选择项目确认处理
			sexConfirm(e) {
				// console.log('性别选择结果',e)
				this.form.sex = e[0].label
			},
			posConfirm(e) {
				// console.log('职位选择结果',e)
				// 多选框，职位分别赋值
				this.posSelRes = e[0].label + " " + e[1].label
				this.form.deptname = e[0].label
				this.form.deptid = e[0].value
				this.form.jobname = e[1].label
				this.form.jobid = e[1].value
			},
			eduConfirm(e) {
				// console.log('教育选择结果',e)
				this.form.education = e[0].label
			},
			addressConfirm(e) {
				// console.log('地址选择结果',e)
				// 地址组合
				this.rangeAddress = e.province.label + e.city.label + e.area.label
			},
			calChange(e) {
				// console.log('日历选择结果',e)
				this.form.birthday = e.result
			}
		},

		// 表单规则确认加载
		onReady() {
			// 必须要在onReady生命周期，因为onLoad生命周期组件可能尚未创建完毕
			this.$refs.uForm.setRules(this.rules);
		},

		// 加载获取职位列表，以供选择
		onLoad: function(parm) {
			console.log('userid带参跳转结果', parm)
			// 获取职位列表
			this.$api.staffIndex()
				.then(res => {
					this.posList = res.data.data
				})
			this.$api.staffEditByUserid({
					userid: parm.userid,
				})
				.then(res => {
					let form = res.data.data
					this.form = form
					// console.log('表单信息',this.form)
					this.posSelRes = form.deptname + " " + form.jobname
					this.rangeAddress = form.address
					if (this.form.faceurl) {
						this.tempFilePath = this.form.faceurl
					} else {
						// 默认头像处理
						if (this.form.sex == '男') {
							this.tempFilePath = '/static/boy1.svg'
						} else if (this.form.sex == '女') {
							this.tempFilePath = '/static/girl1.svg'
						} else {
							this.tempFilePath = '/static/头像.svg'
						}
						this.form.faceurl = this.tempFilePath
					}
				})
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

	.form-box {
		margin: 20rpx;
	}
</style>
