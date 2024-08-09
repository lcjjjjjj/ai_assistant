import request from '../utils/request'

export const postText = (data) => {
    return request.post('/textsum',data)
}