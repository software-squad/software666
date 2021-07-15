<template>
	<view>
		<u-gap height="40"></u-gap>
		<u-field v-model="item.title" label="标题" placeholder="取个标题吧" label-align="center" label-width="150">
		</u-field>
		<u-gap height="40"></u-gap>
		<u-field type="textarea" v-model="item.remark" label="描述" placeholder="说点什么吧" label-align="center"
			label-width="150">
		</u-field>

		<!-- <u-gap height="15" bg-color="#f9f9f9"></u-gap> -->
		<!-- TODO 方案一 多选弹窗限制文件类型的选择 -->
		<!-- <view>
				<u-action-sheet :list="list" v-model="show" @click="click"></u-action-sheet>
				<u-button @click="show = true">选择文件</u-button>
			</view> 
		-->

		<!-- TODO 文件编辑功能暂时不支持更换文件 -->
		<!-- <uni-file-picker fileMediatype="all" :list-styles="listStyle" limit="1" autoUpload='false' @select="select"
				@progress="progress" @success="success" @fail="fail" ref='files' />
			<u-gap height="15" bg-color="#f9f9f9"></u-gap> -->

		<view class="sub_com">
			<u-button class="sub_bott" @click="submit" type="primary">提交</u-button>
		</view>
		<u-toast ref="uToast" />

	</view>
</template>

<script>
	export default {
		data() {
			return {
				// 方案一，选择上传
				// acctionlist
				// list: [{
				// 	text: '上传图片',
				// }, {
				// 	text: '上传视频'
				// }],
				// show: false,

				// 方案二，使用uni-file-picker
				listStyle: {
					"borderStyle": {
						"color": "#eee", // 边框颜色
						"width": "1px", // 边框宽度
						"style": "solid", // 边框样式
						"radius": "5px" // 边框圆角，不支持百分比
					},
					"border": false, // 是否显示边框
					"dividline": true // 是否显示分隔线
				},
				
				// 文件参数传递内容
				item: {
					"fileid": 0,
					"title": "",
					"filename": "",
					"remark": "",
					"userid": 0,
					"username": "",
					"filepath": ""
				},
				tempFilePath: '',  // 文件上传临时路径
				tempFile: null,    // 临时文件信息存储
			}
		},
		methods: {
			// 文件编辑提交
			submit() {
				this.$api.fileEdit(this.item)
					.then((res) => {
						// 异常码处理
						if (res.data.msg == 10005) {
							this.$refs.uToast.show({
								title: '上传成功',
								type: 'success',
								duration: 1000,
							})
							// 返回上一页并刷新数据的方法
							let pages = getCurrentPages(); // 当前页面（index = pages.length）
							let beforePage = pages[pages.length - 2]; // 上一个页面
							// 一定时间后返回
							setTimeout(() => {
								uni.navigateBack({
									delta:1,
									success: function() {
										console.log("返回上一页并刷新")
										beforePage.myReload() // 执行上一页的onLoad方法
									}
								});
							}, 1000)
						}
					})
					.catch((error) => {
						this.$refs.uToast.show({
							title: '上传失败',
							type: 'false'
						})
					})
			}

		},

		onLoad: function(option) {
			// 带参跳转，解析参数，即文件信息
			if (option) {
				let parm = JSON.parse(decodeURIComponent(option.item));
				this.item.fileid = parm.fileid
				this.item.title = parm.title
				this.item.filename = parm.filename
				this.item.remark = parm.remark
				this.item.filepath = parm.filepath
				
				// // #ifdef H5
				// this.item.userid = sessionStorage.getItem('userid')
				// this.item.username = sessionStorage.getItem('username')
				// // #endif
				// // #ifndef H5
				// 获取当前用户信息
				this.item.userid = uni.getStorageSync('userid')
				this.item.username = uni.getStorageSync('userid')
				// // #endif
				
				uni.setNavigationBarTitle({
					title: this.item.title
				})
			} else {
				this.$u.toast('点击为空')
			}
		},
	}
</script>

<style>
	.sub_com {
		width: 100%;
		display: flex;
		align-items: center;
		justify-content: center;
		font-size: 30rpx;
		position: absolute;
		bottom: 0rpx;

	}

	.sub_bott {
		width: 60%;
		margin-bottom: 50rpx;
		/* background-color:#fed404;
  color:#343537; */
	}
</style>
