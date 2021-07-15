import service from "./request.js"
import request from "./easy_request.js"

export function menuSendData(data) {
	return service.request({
		method: 'GET',
		url: '/api/menu/showNews',
		data: data
	})
}

export function loginSendData(data) {
	// return service.request({
		return request.request({
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
	return service.request({
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


// TODO 命名组合驼峰
export function userSendData(data) {
	return service.request({
		method: 'POST',
		url: '/api/staff/oneByUserid',
		data: data
	})
}


// ============================================= 我的

export function fileEdit(data) {
	return request.request({
		url: '/api/file/edit',
		method: 'POST',
		data: data
	})
}

export function fileShowMany() {
	return request.request({
		url: '/api/file/showmany',
		method: 'GET',
	})
}

export function fileDel(data) {
	return request.request({
		url: '/api/file/del',
		data: data,
		method: 'GET',
	})
}
export function staffOneByUseridSendData(data) {
	console.log(data)
	return request.request({
		method: 'GET',
		url: '/api/staff/oneByUserid',
		data: data
	})
}

export function staffDelData(data) {
	return request.request({
		method: 'GET',
		url: '/api/staff/del',
		data: data
	})
}

export function staffShowUserByDeptAndJob(data) {
	return request.request({
		method: 'POST',
		url: "/api/staff/showUserByDeptAndJob",
		data: data
	})
}

export function staffIndex() {
	return request.request({
		url: '/api/staff/index',
		method: "GET",
	})
}

export function staffEditByUserid(data) {
	return request.request({
		url: "/api/staff/editByUserid",
		data: data,
		method: 'GET',
	})
}


export function staffEditSubmit(data) {
	return request.request({
		url: "/api/staff/editSubmit",
		data: data,
		method: 'POST'
	})
}

export function staffAdd(data) {
	return request.request({
		url: "/api/staff/add",
		data:data,
		method: 'POST'
	})
}

export function staffShowUserByUsername(data) {
	return request.request({
		url: '/api/staff/showUserByUsername',
		data: data,
		method: 'GET',
	})
}

					
export default {
	fileEdit: fileEdit,
	fileShowMany: fileShowMany,
	fileDel:fileDel,
	staffOneByUseridSendData: staffOneByUseridSendData,
	staffDelData: staffDelData,
	staffShowUserByDeptAndJob: staffShowUserByDeptAndJob,
	staffIndex: staffIndex,
	staffEditByUserid: staffEditByUserid,
	staffEditSubmit: staffEditSubmit,
	staffAdd:staffAdd,
	staffShowUserByUsername:staffShowUserByUsername,
	
	
};
