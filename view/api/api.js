import service from "../util/request.js"

	export function menuSendData(data){
		return service.request({
			method:'GET',
			url:'/menu/showNews',
			data:data
		})
	}