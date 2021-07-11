<template>
	<view>
		<view :key='item.userid' v-for="(item,index) in searchResults">
			<my-card :index="index" :item="item" ></my-card>
		</view>
		<my-card ref="myCard"></my-card>
	</view>
</template>

<script>
	import myCard from '../../components/my-ui/myCard.vue'
	// import myCard from 'D:/CodeFiles/App/dev-view/components/my-ui/myCard.vue'
	export default {
		components: {
			'my-card': myCard,
		},
		data() {
			return {
				searchResults: [],
			}
		},
		onLoad() {
			console.log('父组件请求后端数据')
			uni.request({
				url: "/api/staff/showUserByDeptAndJob",
				method: 'GET',
				success: (res) => {
					// console.log(res)
					this.searchResults = res.data.data
					console.log('父组件设置滑块show中')
					for (var i in this.searchResults) {
						this.searchResults[i].show = false
					}
					console.log(this.searchResults.length)
				},
			})
			this.$refs.myCard.onLoad(this.searchResults)
		},
		methods: {

			click(index, option) {
				if (option == 1) {
					this.delShow = true
					this.delContent = "确认删除" + this.searchResults[index].username + "？"
					this.delIndex = index
				} else {
					this.navToEdit(index)
				}
			},
			open(index) {
				// 先将正在被操作的swipeAction标记为打开状态，否则由于props的特性限制，
				// 原本为'false'，再次设置为'false'会无效
				console.log('打开中')
				console.log(index)
				console.log(this.searchResults[index])
				this.searchResults[index].show = true;
				this.searchResults.map((val, idx) => {
					if (index != idx) this.searchResults[idx].show = false;
				})
				console.log(this.searchResults)
			},
			gotoOne(index) {
				uni.navigateTo({
					url: '../staff/one?userid=' + this.searchResults[index].userid
				})
			},
			navToEdit(index) {
				let item = encodeURIComponent(JSON.stringify(this.searchResults[index]))
				console.log(item)
				uni.navigateTo({
					url: '/pages/staff/edit?item=' + item,
					success() {
						console.log("编辑成功")
					},
					fail() {
						console.log("编辑失败")
					}

				})
			},
			confirmDel(index) {
				uni.request({
					url: '/staff/del',
					method: 'GET',
					success: (res) => {
						// TODO 更友好的提示
						// this.$u.toast(`删除了第${index}个cell`);
						this.searchResults.splice(index, 1);
					}
				})
				this.$u.toast(`删除成功`);
			},
			cancelDel(index) {
				this.searchResults[index].show = false;
			}

		}
	}
</script>

<style>

</style>
