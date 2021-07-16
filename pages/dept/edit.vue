<template>
	<view>
		<!-- 引入uview弹窗组件，实现异常码拦截弹窗 -->
		<u-toast ref="uToast" />
		<u-gap height="40"></u-gap>
		<view class="whole">
			<!-- 部门信息的编辑页面 -->
			<image :src="item.depturl"></image>
			<u-gap height="60"></u-gap>
			<text class="title">部门名字:</text>
			<u-gap height="30"></u-gap>
			<u-input v-model="item.deptname" type="text" :border="true" />
			<u-gap height="60"></u-gap>
			<text class="title">部门描述:</text>
			<u-gap height="30"></u-gap>
			<u-input v-model="item.remark" type="text" :border="true" />
			<u-gap height="80"></u-gap>
			<!-- uview组件实现照片上传 -->
			<text class="title">部门照片:</text>
			<uni-file-picker fileMediatype="image" limit="1" ref='imagePick' @select="select"
				@success="success" @fail="fail" @progress="progress" />
			<u-gap height="80"></u-gap>
			<u-col span="400">
				<u-row gutter="20">
					<!-- 确认是否提交的模态框 -->
					<u-modal v-model="show" :content="content" :show-cancel-button="true" @confirm="confirm"
						@cancel="cancel"></u-modal>
					<u-button @click="submit" shape="circle" class="custom-style">提交</u-button>
				</u-row>
			</u-col>
		</view>
		<u-gap height="30"></u-gap>
	</view>
</template>

<script>
	// 引入request里封装的返回指向当前页面的指针的函数sendThis
	import {
		sendThis
	} from "../../api/request.js"
	// 引入api统一管理文档里的deptEditSendData接口，实现展示编辑部门信息的请求
	import {
		deptEditSendData
	} from "../../api/api.js"
	export default {
		data() {
			return {
				item: '',
				tempdepturl: '',
				show: false,
				content: '确认提交？',
				// imageValue: '',
			}
		},
		onLoad: function(option) {
			// 接收上个页面的跳转参数
			this.item = JSON.parse(decodeURIComponent(option.item))
			console.log('带参跳转结果：', this.item)
		},
		methods: {
			select(e) {},
			progress(e) {},
			fail(e) {},
			success(e) {
				console.log('上传成功', e)
				this.tempdepturl = e.tempFilePaths[0]
			},
			submit() {
				this.show = true
			},
			// 提交键对应定义发送的data变量，发出对应请求
			confirm() {
				// BUG 这一步必须要，要不然会逻辑错误
				if(!this.tempdepturl){
					this.tempdepturl = this.item.depturl
					if(!this.tempdepturl){
						this.tempdepturl = this.$util.default_deptimg
					}
				}
				console.log('部门照片', this.tempdepturl)
				let data = {
					deptid: this.item.deptid,
					deptname: this.item.deptname,
					remark: this.item.remark,
					depturl: this.tempdepturl
				}
				// 调用接口函数deptEditSendData，发出部门编辑请求
				deptEditSendData(data)
					.then((response) => {
						console.log('编辑成功')
						// 返回上一页并刷新数据的方法
						let pages = getCurrentPages(); // 当前页面
						let beforePage = pages[pages.length - 3]; // 上两页
						console.log('编辑跳转',pages)
						uni.navigateBack({
							delta:2,
							// url:'./show',
							success: function() {
								console.log("返回上一页并刷新")
								// 注意，这一个貌似只能再这里实现
								beforePage.myReload() // 执行上一页的onLoad方法
							}
						});
					})
					.catch((error) => {
						console.log("部门编辑提交失败")
						console.log(error)
					})
			},
			cancel() {
				this.show = false
			}
		}
	}
</script>

<style>
	.whole {
		margin: 0 50rpx;
	}

	.title {
		font-size: larger;
		font-weight: bold;
	}
	.custom-style {
		color: #ffffff;
		background-color: #0167ff;
		font-weight: 550;
		font-size: larger;
		width: 100%;
		height: 90rpx;
	}
</style>
