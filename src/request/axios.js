/*
 * @Autor: Sakurag1_LSJ
 * @LastEditors: Sakurag1_LSJ
 */
import axios from 'axios'

export default function request(config) {
    const instance = axios.create({
        baseURL: "http://121.43.161.186"
    })


    return instance(config);
}
