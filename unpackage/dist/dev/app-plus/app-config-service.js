
var isReady=false;var onReadyCallbacks=[];
var isServiceReady=false;var onServiceReadyCallbacks=[];
var __uniConfig = {"pages":["pages/login/login","pages/menu/menu","pages/menu/user_menu","pages/test/test","pages/login/facelogin","pages/staff/show","pages/job/show","pages/job/user_show","pages/job/edit","pages/job/oneAdd","pages/job/one","pages/job/user_one","pages/file/show","pages/file/edit","pages/file/one","pages/file/upload","pages/notice/show","pages/notice/user_show","pages/notice/edit","pages/notice/one","pages/notice/user_one","pages/notice/add","pages/dept/show","pages/dept/user_show","pages/dept/one","pages/dept/user_one","pages/dept/oneAdd","pages/dept/edit","pages/staff/index","pages/staff/edit","pages/staff/one","pages/user/user","pages/user/changepwd","pages/staff/index","pages/staff/add","pages/staff/search","pages/test/test2","pages/test/test3","pages/staff/user_index","pages/staff/user_search","pages/staff/user_show","pages/file/user_show"],"window":{"navigationBarTextStyle":"black","navigationBarTitleText":"CSI员工之家","navigationBarBackgroundColor":"#fafafa","backgroundColor":"#ffffff","titleNView":true},"tabBar":{"selectedColor":"#52a500","backgroundColor":"#fafafa","borderStyle":"black","list":[{"pagePath":"pages/menu/menu"},{"pagePath":"pages/staff/index"},{"pagePath":"pages/staff/user_index"},{"pagePath":"pages/user/user"},{"pagePath":"pages/menu/user_menu"}]},"nvueCompiler":"uni-app","nvueStyleCompiler":"uni-app","renderer":"auto","splashscreen":{"alwaysShowBeforeRender":true,"autoclose":false},"appname":"welcome","compilerVersion":"3.1.8","entryPagePath":"pages/staff/index","entryPageQuery":"","networkTimeout":{"request":60000,"connectSocket":60000,"uploadFile":60000,"downloadFile":60000}};
var __uniRoutes = [{"path":"/pages/login/login","meta":{"isQuit":true},"window":{"navigationBarTitleText":"登录界面","enablePullDownRefresh":false}},{"path":"/pages/menu/menu","meta":{"isQuit":true,"isTabBar":true},"window":{"navigationBarTitleText":"首页","enablePullDownRefresh":false,"backgroundColor":"#376CBD"}},{"path":"/pages/menu/user_menu","meta":{"isQuit":true,"isTabBar":true},"window":{"navigationBarTitleText":"首页","enablePullDownRefresh":false,"backgroundColor":"#376CBD"}},{"path":"/pages/test/test","meta":{},"window":{"navigationBarTitleText":"测试界面","enablePullDownRefresh":true}},{"path":"/pages/login/facelogin","meta":{},"window":{"navigationBarTitleText":"","enablePullDownRefresh":false}},{"path":"/pages/staff/show","meta":{},"window":{"navigationBarTitleText":"搜索结果","enablePullDownRefresh":true,"titleNView":{"buttons":[{"fontSrc":"/static/iconfont.ttf","fontSize":"22px","float":"right","text":""}]}}},{"path":"/pages/job/show","meta":{},"window":{"navigationBarTitleText":"职位展示","enablePullDownRefresh":false,"titleNView":{"buttons":[{"text":"","fontSrc":"/static/iconfont.ttf","fontSize":"22px","float":"right"}]}}},{"path":"/pages/job/user_show","meta":{},"window":{"navigationBarTitleText":"职位信息","enablePullDownRefresh":false}},{"path":"/pages/job/edit","meta":{},"window":{"navigationBarTitleText":"职位编辑","enablePullDownRefresh":false}},{"path":"/pages/job/oneAdd","meta":{},"window":{"navigationBarTitleText":"新增职位","enablePullDownRefresh":false}},{"path":"/pages/job/one","meta":{},"window":{"navigationBarTitleText":"职位信息","enablePullDownRefresh":false}},{"path":"/pages/job/user_one","meta":{},"window":{"navigationBarTitleText":"职位信息","enablePullDownRefresh":false}},{"path":"/pages/file/show","meta":{},"window":{"navigationBarTitleText":"下载中心","enablePullDownRefresh":true,"titleNView":{"buttons":[{"text":"","fontSrc":"/static/iconfont.ttf","fontSize":"22px"}]}}},{"path":"/pages/file/edit","meta":{},"window":{"navigationBarTitleText":"文件名称","enablePullDownRefresh":false}},{"path":"/pages/file/one","meta":{},"window":{"navigationBarTitleText":"文件名称","enablePullDownRefresh":false}},{"path":"/pages/file/upload","meta":{},"window":{"navigationBarTitleText":"文件上传","enablePullDownRefresh":false}},{"path":"/pages/notice/show","meta":{},"window":{"navigationBarTitleText":"公告","enablePullDownRefresh":false,"titleNView":{"buttons":[{"text":"","fontSrc":"/static/iconfont.ttf","fontSize":"22px"}]}}},{"path":"/pages/notice/user_show","meta":{},"window":{"navigationBarTitleText":"公告","enablePullDownRefresh":false}},{"path":"/pages/notice/edit","meta":{},"window":{"navigationBarTitleText":"公告编辑","enablePullDownRefresh":false}},{"path":"/pages/notice/one","meta":{},"window":{"navigationBarTitleText":"公告标题","enablePullDownRefresh":false}},{"path":"/pages/notice/user_one","meta":{},"window":{"navigationBarTitleText":"公告标题","enablePullDownRefresh":false}},{"path":"/pages/notice/add","meta":{},"window":{"navigationBarTitleText":"发布公告","enablePullDownRefresh":false}},{"path":"/pages/dept/show","meta":{},"window":{"navigationBarTitleText":"部门展示","enablePullDownRefresh":false,"titleNView":{"buttons":[{"text":"","fontSrc":"/static/iconfont.ttf","fontSize":"22px","float":"right"}]}}},{"path":"/pages/dept/user_show","meta":{},"window":{"navigationBarTitleText":"部门名称","enablePullDownRefresh":false}},{"path":"/pages/dept/one","meta":{},"window":{"navigationBarTitleText":"部门展示","enablePullDownRefresh":false}},{"path":"/pages/dept/user_one","meta":{},"window":{"navigationBarTitleText":"部门展示","enablePullDownRefresh":false}},{"path":"/pages/dept/oneAdd","meta":{},"window":{"navigationBarTitleText":"新建部门","enablePullDownRefresh":false}},{"path":"/pages/dept/edit","meta":{},"window":{"navigationBarTitleText":"部门编辑","enablePullDownRefresh":false}},{"path":"/pages/staff/index","meta":{"isQuit":true,"isTabBar":true},"window":{"navigationBarTitleText":"CSI员工之家","enablePullDownRefresh":false}},{"path":"/pages/staff/edit","meta":{},"window":{"navigationBarTitleText":"编辑信息","enablePullDownRefresh":false,"titleNView":true}},{"path":"/pages/staff/one","meta":{},"window":{"navigationBarTitleText":"","enablePullDownRefresh":false}},{"path":"/pages/user/user","meta":{"isQuit":true,"isTabBar":true},"window":{"navigationBarTitleText":"个人信息","enablePullDownRefresh":false}},{"path":"/pages/user/changepwd","meta":{},"window":{"navigationBarTitleText":"修改密码","enablePullDownRefresh":false}},{"path":"/pages/staff/add","meta":{},"window":{"navigationBarTitleText":"新增用户","enablePullDownRefresh":false,"titleNView":true}},{"path":"/pages/staff/search","meta":{},"window":{"enablePullDownRefresh":true,"titleNView":{"buttons":[{"fontSrc":"/static/iconfont.ttf","fontSize":"22px","float":"right","text":""}]}}},{"path":"/pages/test/test2","meta":{},"window":{"navigationBarTitleText":"","enablePullDownRefresh":false}},{"path":"/pages/test/test3","meta":{},"window":{"navigationBarTitleText":"","enablePullDownRefresh":false}},{"path":"/pages/staff/user_index","meta":{"isQuit":true,"isTabBar":true},"window":{"navigationBarTitleText":"员工中心","enablePullDownRefresh":false}},{"path":"/pages/staff/user_search","meta":{},"window":{"enablePullDownRefresh":true}},{"path":"/pages/staff/user_show","meta":{},"window":{"navigationBarTitleText":"搜索结果","enablePullDownRefresh":true}},{"path":"/pages/file/user_show","meta":{},"window":{"navigationBarTitleText":"下载中心","enablePullDownRefresh":true}}];
__uniConfig.onReady=function(callback){if(__uniConfig.ready){callback()}else{onReadyCallbacks.push(callback)}};Object.defineProperty(__uniConfig,"ready",{get:function(){return isReady},set:function(val){isReady=val;if(!isReady){return}const callbacks=onReadyCallbacks.slice(0);onReadyCallbacks.length=0;callbacks.forEach(function(callback){callback()})}});
__uniConfig.onServiceReady=function(callback){if(__uniConfig.serviceReady){callback()}else{onServiceReadyCallbacks.push(callback)}};Object.defineProperty(__uniConfig,"serviceReady",{get:function(){return isServiceReady},set:function(val){isServiceReady=val;if(!isServiceReady){return}const callbacks=onServiceReadyCallbacks.slice(0);onServiceReadyCallbacks.length=0;callbacks.forEach(function(callback){callback()})}});
service.register("uni-app-config",{create(a,b,c){if(!__uniConfig.viewport){var d=b.weex.config.env.scale,e=b.weex.config.env.deviceWidth,f=Math.ceil(e/d);Object.assign(__uniConfig,{viewport:f,defaultFontSize:Math.round(f/20)})}return{instance:{__uniConfig:__uniConfig,__uniRoutes:__uniRoutes,global:void 0,window:void 0,document:void 0,frames:void 0,self:void 0,location:void 0,navigator:void 0,localStorage:void 0,history:void 0,Caches:void 0,screen:void 0,alert:void 0,confirm:void 0,prompt:void 0,fetch:void 0,XMLHttpRequest:void 0,WebSocket:void 0,webkit:void 0,print:void 0}}}});
