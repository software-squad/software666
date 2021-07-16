// const requestBaseUrl = "http://4097h1o714.zicp.vip:25464/" // 有内网穿透
// const dowloadBaseUrl = "http://192.168.0.101:8082/api/file/download?fileid="
// const easyRequestUrl = "http://4097h1o714.zicp.vip:25464"

const dowloadBaseUrl = "http://192.168.0.120:8082/api/file/download?fileid="
const requestBaseUrl = "http://192.168.0.120:8082/" // 有内网穿透
const easyRequestUrl = "http://192.168.0.120:8082"
const default_deptimg = "../../static/deptimg.svg"

const statusList = [{
	label: '管理员',
	value: 1
}, {
	label: '普通用户',
	value: 0
}, ]
const sexList = [{
		value: '0',
		label: '保密'
	}, {
		value: '1',
		label: '男'
	},
	{
		value: '2',
		label: '女'
	}
]
const eduList = [{
		value: '0',
		label: '小学'
	}, {
		value: '1',
		label: '初中'
	},
	{
		value: '2',
		label: '高中'
	}, {
		value: '3',
		label: '专科'
	}, {
		value: '4',
		label: '本科'
	}, {
		value: '5',
		label: '研究生'
	}, {
		value: '6',
		label: '博士'
	},
]
const addRule = { // 表单规则
	username: [{
		required: true,
		message: '姓名不能为空',
		trigger: ['change', 'blur']
	}, ],
	cardid: [{
		type: 'number',
		message: '身份证号码格式不正确',
		trigger: ['change', 'blur']
	}, {
		len: 18,
		message: '身份证号码为18位',
		trigger: ['change', 'blur']
	}, ],
	sex: // Not Null
		[{
			required: true,
			message: '性别不能为空',
			trigger: ['change', 'blur']
		}, ],
	email: [{
		type: 'email',
		message: "邮箱格式不正确",
		trigger: ['change', 'blur']
	}, ],
	tel: // Not Null
		[{
			required: true,
			message: '手机号码不能为空',
			trigger: ['change', 'blur']
		}, {
			// 自定义验证函数，见上说明
			validator: (rule, value, callback) => {
				// 上面有说，返回true表示校验通过，返回false表示不通过
				// this.$u.test.mobile()就是返回true或者false的
				return this.$u.test.mobile(value);
			},
			message: '手机号码格式不正确',
			// 触发器可以同时用blur和change
			trigger: ['change', 'blur'],
		}, ],
	qqnum: [{
		type: 'number',
		message: "QQ号码格式不正确",
		trigger: ['change', 'blur']
	}, ],
	postcode: [{
		type: 'number',
		message: "邮编格式不正确",
		trigger: ['change', 'blur']
	}, ]
}

const editRule = {
	username: [{
		required: true,
		message: '姓名不能为空',
		trigger: ['change', 'blur']
	}, ],
	cardid: [{
		type: 'number',
		message: '身份证号码格式不正确',
		trigger: ['change', 'blur']
	}, {
		len: 18,
		message: '身份证号码为18位',
		trigger: ['change', 'blur']
	}, ],
	sex: // Not Null
		[{
			required: true,
			message: '性别不能为空',
			trigger: ['change', 'blur']
		}, ],
	email: [{
		type: 'email',
		message: "邮箱格式不正确",
		trigger: ['change', 'blur']
	}, ],
	tel: // Not Null
		[{
			required: true,
			message: '手机号码不能为空',
			trigger: ['change', 'blur']
		}, {
			// 自定义验证函数，见上说明
			validator: (rule, value, callback) => {
				// 上面有说，返回true表示校验通过，返回false表示不通过
				// this.$u.test.mobile()就是返回true或者false的
				return this.$u.test.mobile(value);
			},
			message: '手机号码格式不正确',
			// 触发器可以同时用blur和change
			trigger: ['change', 'blur'],
		}, ],
	qqnum: [{
		type: 'number',
		message: "QQ号码格式不正确",
		trigger: ['change', 'blur']
	}, ],

	postcode: [{
		type: 'number',
		message: "邮编格式不正确",
		trigger: ['change', 'blur']
	}, ]

}
const options = [{
	text: '编辑',
	style: {
		backgroundColor: '#007aff'
	}
}, {
	text: '删除',
	style: {
		backgroundColor: '#dd524d'
	}
}]


export default {
	dowloadBaseUrl: dowloadBaseUrl,
	requestBaseUrl: requestBaseUrl,
	easyRequestUrl: easyRequestUrl,
	sexList: sexList,
	eduList: eduList,
	statusList: statusList,
	options: options,
	addRule: addRule,
	editRule:editRule,
	default_deptimg:default_deptimg
};
