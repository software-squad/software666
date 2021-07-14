<template>
	<view>
		<u-toast ref="uToast" />
		<u-gap height="40"></u-gap>
		<view class="deptOne">
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

			<text class="title">部门照片:</text>

			<uni-file-picker v-model="imageValue" fileMediatype="image" limit="1" ref='imagePick' @select="select"
				@success="success" @fail="fail" @progress="progress" />

			<u-gap height="80"></u-gap>
			<u-col span="400">
				<u-row gutter="20">
					<u-modal v-model="show" :content="content" :show-cancel-button="true" @confirm="confirm"
						@cancel="cancel"></u-modal>
					<button @click="submit">提交</button>
				</u-row>
			</u-col>
		</view>
	</view>
</template>

<script>
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
				imageValue: '',
			}
		},
		onLoad: function(option) {
			this.item = JSON.parse(decodeURIComponent(option.item))
			console.log('带参跳转结果',this.item)
		},
		methods: {
			select(e) {},
			progress(e) {},
			fail(e) {},
			success(e) {
				console.log('上传成功', e)
				this.tempdepturl = e.tempFilePaths[0]
				console.log('部门新照片',this.tempdepturl)
			},
			submit() {
				this.show = true
			},
			confirm() {
				let data = {
					deptid: this.item.deptid,
					deptname: this.item.deptname,
					remark: this.item.remark,
					depturl: this.tempdepturl
				}
				deptEditSendData(data)
					.then((response) => {
						this.$refs.uToast.show({
							title: '提交成功',
							type: 'success'
						})
						// TODO 延迟
						uni.redirectTo({
							url: '/pages/dept/show'
						})
					})
					.catch((error) => {
						this.$refs.uToast.show({
							title: '提交失败',
							type: 'false'
						})
					})
			},
			cancel() {
				this.show = false
			}
		}
	}
</script>

<style>
	.deptOne {
		margin: 0 50rpx;
	}

	,
	.title {
		font-size: larger;
		font-weight: bold;
	}
</style>
