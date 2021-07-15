<template>
	<view>
		<u-toast ref="uToast" />
		<u-gap height="40"></u-gap>
		<view class="deptOne">
			<image :src="imageSrc" mode="aspectFill"></image>
			<!-- <text class="title">部门名字:</text> -->
			<text class="name">{{item.deptname}}</text>
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
					<button @click="navToEdit" class="custom-style">编辑</button>
					<u-modal v-model="show" :content="content" :show-cancel-button="true" @confirm="confirmExit"
						@cancel="cancel"></u-modal>
					<button @click="del" type="error" class="custom-style">删除</button>
				</u-row>
			</u-col>
		</view>
	</view>
</template>

<script>
	import {
		sendThis
	} from "../../api/request.js"
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
		onLoad: function(option) {
			sendThis(this)

			this.item = JSON.parse(decodeURIComponent(option.item))
			this.imageSrc = this.item.depturl
			console.log("one")
			console.log(this.imageSrc)
			console.log(this.item.depturl)
			console.log(this.item.remark)
		},
		methods: {
			showToast(TITLE, TYPE) {
				this.$refs.uToast.show({
					title: TITLE.toString(),
					type: TYPE.toString(),
				})
			},

			showDelSuccessToast() {
				this.$refs.uToast.show({
					title: '删除成功',
					type: 'success'
				})
			},
			showDelFalseToast() {
				this.$refs.uToast.show({
					title: '删除失败',
					type: 'false'
				})
			},
			del() {
				this.show = true;
			},
			confirmExit() {
				let data = {
					deptid: this.item.deptid
				}
				console.log(this.item.deptid)
				console.log(data)
				deptOneDelSendData(data)
					.then((response) => {
						this.showToast()
						uni.navigateBack()
					})
					.catch((error) => {
						this.showToast()
						console.log(error);
						uni.navigateBack()
					})
			},
			cancel() {
				this.show = false;
			},
			navToEdit() {
				uni.navigateTo({
						url: "edit?item=" + encodeURIComponent(JSON.stringify(this.item))
					}),
					console.log("one")
				console.log(this.item.name),
					console.log(this.item.dcrpt)
			}


		}
	}
</script>

<style>
	.deptOne {
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
