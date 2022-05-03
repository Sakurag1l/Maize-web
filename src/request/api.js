/*
 * @Autor: Sakurag1_LSJ
 * @LastEditors: Sakurag1_LSJ
 */
import request from './axios'

export function ModelPre(model) {
    return request({
        method: 'post',
        url: '/model/submit',
        headers: {
            "Content-Type": "application/json"
        },
        data: model
    })
}

export function getResult(taskID) {
    return request({
        method: 'get',
        url: `/model/result?taskID=${taskID}`,
    })
}

export function uploadfile(data, file) {
    return request({
        method: 'post',
        url: `model/file`,
        headers: {
            "Content-Type": "form-data",
        },
        params: data,
        data: file
    })
}

