<template>
	<view>
		<u-swipe-action :show="item.show" :index="index" :key="item.userid" :options="options" btn-width="180"
			@click="click" @open="open(index)" @content-click="gotoOne">
			<view class="u-body-item">
				<image :src="item.faceurl" mode="aspectFill" class="avatar-item"></image>
				<view class="info-item">
					<text style="font-weight: bold;">{{item.username}}</text>
				</view>
				<view class="info-item">
					<text style="font-weight: bold;">Tel:{{item.tel}}</text>
				</view>
				<u-tag :text="item.jobname" type="primary" />
			</view>
		</u-swipe-action>
		<u-modal v-model="delShow" :content="delContent" :show-cancel-button="true" :async-close="true"
			@confirm="confirmDel"></u-modal>
	</view>

</template>

<script>
	export default {
		name: 'myCard',
		props: {
			// 一个card展示的对象
			item: {
				type: Object,
				default () {
					return {
						show: false,
						userid: 0,
						faceurl: '../../static/头像.svg',
						username:'无',
						userjob:'无',
						usertel:'无'
					}
				}
			},
			index:{
				type:Number,
				default:0
			}
		},
		data() {
			return {
				delShow: false,
				delContent: '',
				delIndex: '',
				options: [{
						text: '编辑',
						style: {
							backgroundColor: '#007aff'
						}
					},
					{
						text: '删除',
						style: {
							backgroundColor: '#dd524d'
						}
					}
				],
			};
		},
		methods: {
			click(index, option) {
				if (option == 1) {
					this.delShow = true
					this.delContent = "确认删除" + item.username + "？"
					this.delIndex = index
				} else {
					console.log('子组件申请跳转')
					this.$emit('navToEdit',index)
				}
			},
			open(index) {
				// 先将正在被操作的swipeAction标记为打开状态，否则由于props的特性限制，
				// 原本为'false'，再次设置为'false'会无效
				console.log('子组件申请打开一个')
				this.$emit('open',index)
			},
			gotoOne() {
				console.log('子组件申请跳转one')
				this.$emit('gotoOne',index)
			},
			
			confirmDel() {
				console.log('子组件申请确认删除')
				let index = this.delIndex
				this.delShow = false
				this.$emit('confirmDel',index)
				// this.$u.toast(`删除成功`);
			},
			
			cancel() {
				console.log('子组件申请取消删除')
				this.delShow = false;
				this.$emit('cancelDel',this.delIndex)
			}
		}
	}
</script>

<style>
	.u-card-wrap {
		background-color: $u-bg-color;
		padding: 1px;
	}

	.u-body-item {
		font-size: 32rpx;
		color: #333;
		padding: 20rpx 20rpx;
		margin: 30rpx 20rpx;
		border-style: solid;
		/* TODO */
		overflow: hidden;
	}

	.u-body-item image {
		width: 120rpx;
		flex: 0 0 120rpx;
		height: 120rpx;
		border-radius: 8rpx;
		margin-left: 12rpx;
		/* border-style: solid;  /* TODO */
		float: left;
	}

	.info-item {
		font-size: large;
		float: left;
		text-align: left;

		padding-left: 10rpx;
		/* border-style: solid;  /* TODO */
	}

	.avatar-item {}
</style>
