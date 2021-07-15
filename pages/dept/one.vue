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
			<u-gap height="40"></u-gap>
			<u-line color="#bbb" />
			<u-gap height="30"></u-gap>
			<u-col span="40">
				<u-row gutter="100" justify="space-around">
					<!-- 跳转到编辑界面的按钮 -->
					<button @click="navToEdit" class="custom-style">编辑</button>
					<!-- 是否确认删除的模态框 -->
					<u-modal v-model="show" :content="content" :show-cancel-button="true" @confirm="confirm"
						@cancel="cancel"></u-modal>
					<!-- deptid为1的部门为待定部门，里面为待定人员，不可删除，对于管理员隐藏删除键 -->
					<button @click="del" type="error" v-if="item.deptid!=1">删除</button>
				</u-row>
			</u-col>
		</view>
	</view>
</template>

<script>
	// 引入request里封装的返回指向当前页面的指针的函数sendThis
	import {
		sendThis
	} from "../../api/request.js"
	// 引入api统一管理文档里的deptOneDelSendData接口，实现删除部门的请求
	import {
		deptOneDelSendData
	} from "../../api/api.js"
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
			//定义弹窗函数接受request.js的参数
			showToast(TITLE, TYPE) {
				this.$refs.uToast.show({
					title: TITLE.toString(),
					type: TYPE.toString(),
				})
			},
			// 点击删除事件，弹出给用户再次选择是否删除的模态框
			del() {
				this.show = true;
			},
			// 模态框确认事件，定义传给后端的data为部门的id，并调用deptOneDelSendData接口像后端发出请求
			confirm() {
				let data = {
					deptid: this.item.deptid
				}
				console.log("部门id：", this.item.deptid)
				console.log("deptone删除操作返回给后端的数据：", data)
				deptOneDelSendData(data)
					.then((response) => {
						// 返回上一页并刷新数据的方法
						let pages = getCurrentPages(); // 当前页面
						let beforePage = pages[pages.length - 2]; // 上一页
						uni.navigateBack({
							success: function() {
								console.log("返回上一页并刷新")
								beforePage.DeptShowSendData() // 执行上一页的onLoad方法
							}
						});

					})
					.catch((error) => {
						console.log(error);
						uni.navigateBack()
					})
			},
			// 模态框的取消按钮触发cancel事件，弹窗消失
			cancel() {
				this.show = false;
			},
			// 该页面的编辑按钮点击事件，带参跳转到实际的可编辑页面
			navToEdit() {
				uni.navigateTo({
						url: "edit?item=" + encodeURIComponent(JSON.stringify(this.item))
					}),
				console.log("===============one页面==============")
				console.log("部门名称",this.item.name),
				console.log("部门描述",this.item.remark)
			}
		}
	}
</script>

<style>
	.whole {
		margin: 0 50rpx;
	}

	.name {
		text-align: center;
		margin-left: 285rpx;
		font-size: larger;
		font-weight: 550;
	}

	.title {
		font-size: larger;
		font-weight: bold;
		margin-left: 260rpx;
	}

	.custom-style {
		color: #241c32;
		font-weight: 520;
		width: 150rpx;
		height: 90rpx;
	}
</style>
