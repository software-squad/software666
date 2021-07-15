import Vue from 'vue'
import App from './App'
import uView from "uview-ui";
import GoEasy from "js_sdk/goeasy-js/goeasy-1.2.1.js"
import store  from "./store/index"
// import md5Libs from "uview-ui/libs/function/md5.js"
Vue.prototype.$store = store
Vue.config.productionTip = false
Vue.use(uView);

// import request from './api/easy_request.js'
// Vue.prototype.$request = request        //赋值到vue属性里面

import api from './api/api.js'
Vue.prototype.$api = api

Vue.config.productionTip = false

App.mpType = 'app'

const app = new Vue({
    ...App,
	store
})
app.$mount()