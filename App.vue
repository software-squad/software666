<script>
	import md5Libs from "uview-ui/libs/function/md5.js"
	import request from '@../../api/request.js'
	export default {
		onLaunch: function() {
			console.log('App Launch')
		},
		onShow: function() {
			console.log('App Show')
		},
		onHide: function() {
			console.log('App Hide')
		}
	}
</script>

<style lang="scss">
    /* 注意要写在第一行，同时给style标签加入lang="scss"属性 */
    @import "./static/iconfont.css";
	@import "uview-ui/index.scss";
</style>