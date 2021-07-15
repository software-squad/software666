// tabBar文件为我们创建的tabBer对象数组
 
// 判断用户tabBer类别, 例如
 
// 逻辑判断处理

// midBtn 为设置tabBer中间的凸起，false为不凸起
const state = {
	list: [],
	midBtn:false,
}
 
const mutations = {
        add(state, n) {
			console.log(n)
            state.list = n
        }	
}
 
 
export default {
	namespaced: true,
	state,
	mutations
}