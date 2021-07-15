// const testABar= [
// 	// 首页
// 	{
// 		// 未点击图标
// 		iconPath: "/static/tabbar/box.png",
// 		// 点击后图标
// 		selectedIconPath: "/static/tabbar/box_normal.png",
// 		// 显示文字
// 		text: '人员列表',
// 		// 是否显示红点
// 		isDot: true,
// 		// 是否使用自定义图标
// 		customIcon: true,
// 		// 页面路径
// 		pagePath: "/pages/A/A"
// 	}, {
// 		// 未点击图标
// 		iconPath: "/static/tabbar/box.png",
// 		// 点击后图标
// 		selectedIconPath: "/static/tabbar/box_normal.png",
// 		text: '我的',
// 		isDot: true,
// 		customIcon: true,
// 		pagePath: "/pages/B/B"
// 	}
// 	// 省略
// ]
 
// const testBBar= [
// 	// 首页
// 	{
// 		// 未点击图标
// 		iconPath: "/static/tabbar/box.png",
// 		// 点击后图标
// 		selectedIconPath: "/static/tabbar/box_normal.png",
// 		text: '车辆列表',
// 		isDot: true,
// 		customIcon: true,
// 		pagePath: "/pages/C/C"
// 	}, {
// 		// 未点击图标
// 		iconPath: "/static/tabbar/box.png",
// 		// 点击后图标
// 		selectedIconPath: "/static/tabbar/box_normal.png",
// 		text: '我的',
// 		isDot: true,
// 		customIcon: true,
// 		pagePath: "/pages/B/B"
// 	}
// 	// 省略
// ]
 
// export default {
// 	testABar,
// 	testBBar
// }

// tabBar文件为我们创建的tabBer对象数组

// 判断用户tabBer类别, 例如

// 逻辑判断处理

// midBtn 为设置tabBer中间的凸起，false为不凸起

const testABar = [{
		"pagePath": "/pages/menu/user_menu",
		"text": '首页',
		"iconPath": "/static/tab_icons/home.png",
		"selectedIconPath": "/static/tab_icons/homeHL.png"
	},
	{
		"pagePath": "/pages/staff/user_index",
		"text": '员工中心',
		"iconPath": "/static/tab_icons/staff.png",
		"selectedIconPath": "/static/tab_icons/staffHL.png"
	},
	{
		"pagePath": "/pages/user/user",
		"text": '个人中心',
		"iconPath": "/static/tab_icons/user.png",
		"selectedIconPath": "/static/tab_icons/userHL.png"
	}
]
const testBBar = [
	{
		"pagePath": "/pages/menu/menu",
		"text": '首页',
		"iconPath": "/static/tab_icons/home.png",
		"selectedIconPath": "/static/tab_icons/homeHL.png"
	},
	{
		"pagePath": "/pages/staff/index",
		"text": '员工中心',
		"iconPath": "/static/tab_icons/staff.png",
		"selectedIconPath": "/static/tab_icons/satffHL.png"
	}, {
		"pagePath": "/pages/user/user",
		"text": '个人中心',
		"iconPath": "/static/tab_icons/user.png",
		"selectedIconPath": "/static/tab_icons/userHL.png"
	}
]

export default {
	testABar,
	testBBar
}