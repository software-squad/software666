<template>
	<view>

		<u-field v-model="item.title" label="标题" placeholder="取个标题吧" label-align="center">
		</u-field>
		
		<u-field type="textarea" v-model="item.remark" label="描述" placeholder="说点什么吧" label-align="center"></u-field>
		<u-gap height="15" bg-color="#f9f9f9"></u-gap>

		<!-- 方案一，弹窗限制文件类型 -->
		<!-- <view>
			<u-action-sheet :list="list" v-model="show" @click="click"></u-action-sheet>
			<u-button @click="show = true">选择文件</u-button>
		</view> -->

		<!-- 方案二，使用封装好的库 -->
		<uni-file-picker fileMediatype="all" :list-styles="listStyle" limit="1" :autoUpload="false" @select="select"
			@progress="progress" @success="success" @fail="fail" ref='files' />
		<u-gap height="15" bg-color="#f9f9f9"></u-gap>

		<view class="sub_com">
			<u-button class="sub_bott" @click="submit" type="primary">上传</u-button>
		</view>
		
		<u-toast ref="uToast"/>
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

				item: {
					title: "",
					remark: '',
					username: "",
				},
				tempFilePath: '',
				tempFile: null,
			}
		},
		methods: {
			// 方案一，使用弹窗类型的选择文件
			// click(index) {
			// 	console.log(`点击了第${index + 1}项，内容为：${this.list[index].text}`)
			// 	// TODO 调用文件格式
			// },

			// 方案二，使用uni-file-picker
			select(e) {
				console.log('选择文件结果', e)
				this.tempFilePath = e.tempFilePaths[0]
				this.tempFile = e.tempFiles[0].file
			},

			submit() {
				// TODO 获取用户名字，感觉传当前用户id更加妥当
				const uploadTask = uni.uploadFile({
					url: '/api/file/upload',
					filePath: this.tempFilePath,
					name: 'file',
					formData: {
						fileMsg: JSON.stringify(this.item),
					},
					// fileMsg: '"title": "main", "remark": "remark", "username": "刘骥"', // 后端需要的其他请求参数
					success: (res) => {
						console.log('服务器请求结果', res)
						this.$refs.uToast.show({
							title: '上传成功',
							type: 'success',
							duration:2000,
							// back :true,
							// url: '/pages/file/show'
						})
						uni.redirectTo({
							url:'/pages/file/show'
						})
					},
					fail: (err) => {
						console.log('服务器请求失败', err)
						this.$refs.uToast.show({
							title: '上传失败',
							type: 'false'
						})
					}
				});

				// TODO 优化方案，实现app端兼容
				// $.ajax({
				// 	url: this.tempFilePath, //后台文件，绝对路径相对路径都可以，但写绝对路径要注意可能出现的跨域问题
				// 	data: formdata,
				// 	processData: false, //必须
				// 	contentType: false, //必须
				// 	async: false, //必须
				// 	type: "post",
				// 	success: function(msg) {
				// 		//alert("here");
				// 	},
				// 	error: function(xhr, status, error) {
				// 		console.log(xhr);
				// 		console.log(status);
				// 		console.log(error);
				// 	}
				// });

				// TODO 一些骚操作拓展，添加上传文件进度
				// uploadTask.onProgressUpdate((res) => {
				// 	console.log('上传进度' + res.progress);
				// 	console.log('已经上传的数据长度' + res.totalBytesSent);
				// 	console.log('预期需要上传的数据总长度' + res.totalBytesExpectedToSend);
				// });
			}

		},
		onLoad() {
			uni.setNavigationBarTitle({
				title: '文件上传'
			})
		}
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
		width: 100%;
		/* background-color:#fed404;
  color:#343537; */
	}
</style>
