<template>
	<view>
		<!-- 引入uview弹窗组件，实现异常码拦截弹窗 -->
		<u-toast ref="uToast" />
		<u-gap height="40"></u-gap>
		<view class="whole">
			<image :src="imageSrc" mode="aspectFill"></image>
			<u-gap height="30"></u-gap>
			<u-line color="#bbb" />
			<u-gap height="20"></u-gap>
			<text class="title">部门描述</text>
			<u-gap height="30"></u-gap>
			<text style="font-size: larger; height: 200;">{{item.remark}}</text>
			<u-gap height="40" ></u-gap>
		</view>
	</view>
</template>

<script>
	// 引入request里封装的返回指向当前页面的指针的函数sendThis
	import {
		sendThis
	} from "../../api/request.js"
	export default {
		data() {
			return {
				deptid: '',
				deptname: '',
				remark: '',
				depturl: '',
				item: '',
				imageSrc: '',
				show: false,
				content: '确认删除该部门？'
			}
		},
		// 在页面加载的生命周期
		onLoad: function(option) {
			// 发送指向当前页面的指针
			sendThis(this)
			// 使用定义的item对象接受上一个页面（deptshow部门展示）传递过来的参数
			this.item = JSON.parse(decodeURIComponent(option.item))
			this.imageSrc = this.item.depturl
			console.log("==========deptone页面============")
			console.log("show页面部门照片的url：", this.item.depturl)
			console.log("one页面部门照片的url：", this.imageSrc)
			console.log("部门描述", this.item.remark)
			// 设置动态加载导航栏标题为跳转部门的名字
			uni.setNavigationBarTitle({
				title: this.item.deptname
			})
		},
		methods: {
			//定义弹窗函数接受request.js的参数，实现异常码弹窗
			showToast(TITLE, TYPE) {
				this.$refs.uToast.show({
					title: TITLE.toString(),
					type: TYPE.toString(),
				})
			}
		}
	}
</script>

<style>
	.whole {
		margin: 0 50rpx;
	}

	,
	.title {
		font-size: larger;
		font-weight: bold;
	}
</style>
