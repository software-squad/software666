<template>
	<view class="whole">

		<u-field v-model="item.title" label="标题" placeholder="取个标题吧" label-align="center">
		</u-field>

		<u-field type="textarea" v-model="item.remark" label="描述" placeholder="说点什么吧" label-align="center"></u-field>
		<u-gap height="10" bg-color="#f9f9f9"></u-gap>
		<u-gap height="5"></u-gap>
		<!-- 方案一，弹窗限制文件类型 -->
		<!-- <view>
				<u-action-sheet :list="list" v-model="show" @click="click"></u-action-sheet>
				<u-button @click="show = true">选择文件</u-button>
			</view> -->

		<!-- 方案二，使用封装好的库 -->
		<uni-file-picker fileMediatype="all" :list-styles="listStyle" limit="1" :autoUpload="false" @select="select"
			@progress="progress" @success="success" @fail="fail" ref='files' />
		<u-gap height="15" bg-color="#f9f9f9"></u-gap>
		<u-gap height="200"></u-gap>
		<u-button class="sub_bott" @click="submit" type="primary">上传</u-button>
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

				item: { // 文件参数信息
					title: "",
					remark: '',
					username: "",
					userid: "",
				},
				tempFilePath: '', // 临时文件地址
				tempFile: null, // 临时文件
			}
		},
		methods: {
			// 方案一，使用弹窗类型的选择文件
			// click(index) {
			// 	console.log(`点击了第${index + 1}项，内容为：${this.list[index].text}`)
			// 	// TODO 调用文件格式
			// },

			// 方案二，使用uni-file-picker，选择文件中
			select(e) {
				console.log('选择文件结果', e)
				this.tempFilePath = e.tempFilePaths[0]
				this.tempFile = e.tempFiles[0].file
			},

			// 文件提交
			submit() {
				// // #ifdef H5
				// this.item.userid = sessionStorage.getItem('userid')
				// this.item.username = sessionStorage.getItem('username')
				// // #endif
				this.item.userid = uni.getStorageSync('userid')
				this.item.username = uni.getStorageSync('username')

				const uploadTask = uni.uploadFile({
					// 文件提交
					url: '/api/file/upload',
					filePath: this.tempFilePath,
					header: {
						token: uni.getStorageSync('token')
					},
					name: 'file',
					formData: {
						filemsg: JSON.stringify(this.item),
					},
					// 文件信息示例
					// filemsg: '"title": "main", "remark": "remark", "username": "刘骥"', // 后端需要的其他请求参数
					success: (res) => {
						this.$refs.uToast.show({
							title: '上传成功',
							type: 'success',
							duration: 2000,
							// back :true,
							// url: '/pages/file/show'
						})
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
					},
					fail: (err) => {
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
			// // #ifdef H5
			// this.item.userid = sessionStorage.getItem('userid')
			// this.item.username = sessionStorage.getItem('username')
			// // #endif
			// // #ifndef H5
			// 获取当前用户信息
			this.item.userid = uni.getStorageSync('userid')
			this.item.username = uni.getStorageSync('username')
			// // #endif
		}
	}
</script>

<style>
	.whole {
		margin: 0 50rpx;
	}

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
		margin-bottom: 50rpx;
		color: #ffffff;
		background-color: #0167ff;
		font-weight: 550;
		font-size: larger;
		width: 100%;
		height: 90rpx;
		/* background-color:#fed404;
	color:#343537; */
	}
</style>
