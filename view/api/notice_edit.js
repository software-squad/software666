import service from "../api/request.js"

	export function SendData(data){
		return service.request({
			method:'POST',
			url:'/notice/edit',
			data:data
		})
	}