<!-- 注意，
由于uView框架Bug，需要将./static/iconfont.css 中注释了的url改为您当前
static文件夹所在的绝对路径，以保证运行的软件图片能正常执行
-->
<script>
	import md5Libs from "uview-ui/libs/function/md5.js"
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
