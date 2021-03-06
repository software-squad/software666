import Vue from 'vue'
import App from './App'
import uView from "uview-ui";
// import md5Libs from "uview-ui/libs/function/md5.js"
Vue.use(uView);

import request from './api/easy_request.js'
Vue.prototype.$request = request//赋值到vue里面

Vue.config.productionTip = false

App.mpType = 'app'

const app = new Vue({
    ...App
})
app.$mount()
