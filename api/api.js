import service from "../api/request.js"
import request from "../api/easy_request.js"

export function menuSendData(data) {
	return service.request({
		method: 'GET',
		url: '/api/menu/showNews',
		data: data
	})
}

export function loginSendData(data) {
	return service.request({
		method: 'POST',
		url: '/api/login',
		//url:'https://www.fastmock.site/mock/c8376d6981ddc3969681a61793cc783d/api/login',
		data: data
	})
}

export function noticeShowGetData(data) {
	return service.request({
		method: 'GET',
		url: '/api/notice/showmany',
		//url:'https://www.fastmock.site/mock/c8376d6981ddc3969681a61793cc783d/api/notice/showmany',
		data: data
	})
}

export function noticeEditSendData(data) {
	return service.request({
		method: 'POST',
		url: '/api/notice/edit',
		//url: 'https://www.fastmock.site/mock/c8376d6981ddc3969681a61793cc783d/api/notice/edit',
		data: data
	})
}

export function noticeDeletSendData(data) {
	return service.request({
		method: 'POST',
		url: '/api/notice/del',
		//url: 'https://www.fastmock.site/mock/c8376d6981ddc3969681a61793cc783d/api/notice/del',
		data: data
	})
}

export function noticeAddSendData(data) {
	return service.request({
		method: 'POST',
		url: '/api/notice/add',
		//url: 'https://www.fastmock.site/mock/c8376d6981ddc3969681a61793cc783d/api/notice/add',
		data: data
	})
}

export function changePwdSendData(data) {
	return service.request({
		method: 'POST',
		url: '/api/user/changepwd',
		//url: 'https://www.fastmock.site/mock/c8376d6981ddc3969681a61793cc783d/api/user/changepwd',
		data: data
	})
}

export function deptShowSendData(data) {
	// TODO 这里为啥不行
	return request.request({
		method: 'GET',
		url: '/api/dept/showAll',
		data: data
	})
}

export function deptOneDelSendData(data) {
	return service.request({
		method: 'POST',
		url: '/api/dept/del',
		data: data
	})
}

export function deptEditSendData(data) {
	return service.request({
		method: 'POST',
		url: '/api/dept/edit',
		data: data
	})
}

export function deptAddSendData(data) {
	return service.request({
		method: 'POST',
		url: '/api/dept/add',
		data: data
	})
}

export function jobShowSendData(data) {
	return service.request({
		method: 'GET',
		url: '/api/job/show',
		data: data
	})
}

export function jobOneDelSendData(data) {
	return service.request({
		method: 'POST',
		url: '/api/job/del',
		data: data
	})
}

export function jobEditSendData(data) {
	return service.request({
		method: 'POST',
		url: '/api/job/edit',
		data: data
	})
}

export function jobAddSendData(data) {
	return service.request({
		method: 'POST',
		url: '/api/job/add',
		data: data
	})
}

export function jobAddShowSendData(data) {
	return service.request({
		method: 'GET',
		url: '/api/job/deptshow',
		data: data
	})
}

export function userSendData(data) {
	return service.request({
		method: 'POST',
		url: '/api/staff/oneByUserid',
		data: data
	})
}
