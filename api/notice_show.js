import service from "../api/request.js"

	export function GetData(data){
		return service.request({
			method:'GET',
			url:'/notice/showmany',
			data:data
		})
	}