import qs from "qs"
import { access_token, username, is_login } from "./store.js"
import { get } from 'svelte/store'
import { push } from 'svelte-spa-router'

const fastapi = (operation, url, params, success_callback, failure_callback) => {
    let method = operation
    let content_type = 'application/json' // body에 들어갈 데이터 타입을 header에 명시
    let body = JSON.stringify(params) // body 항목에 전달 받은  parameter를 할당 하려면 JSON 타입으로 변환 해야 한다.
    console.log(body)
    // OAuth2의 로그인 수행
    if(operation === 'login') {
        method = 'post'
        content_type = 'application/x-www-form-urlencoded'
        body = qs.stringify(params) // x-www-form-urlencoded에 맞게금 변환
    }

    let _url = import.meta.env.VITE_SERVER_URL + url // 사이트 URL(도메인)을 .env 파일에서 상수 값으로 받아온다.(개발환경 세팅)

    // 메소드가 GET방식인 경우 URL 세팅
    if(method === 'get'){
        _url += "?" + new URLSearchParams(params)
    }

    let options = {
        method: method,
        headers: {
           "Content-Type": content_type,
        },
    }
    // fastpi함수는 스토어 변수를 사용할 때 $기호를 사용할 수 없다.
    // 스토어 변수를 읽으려면 get 함수를 사용 저장할때는 set함수
    const _access_token = get(access_token)
    if(_access_token){
        options.headers["Authorization"] = "Bearer " + _access_token
    }

    if(method !== 'get'){
        options['body'] = body
    }

    // Server로 URL 전달
    // fetch: Client에서 직접 API 호출
     fetch(_url, options)
        .then(response => {
            if(response.status === 204){
                if(success_callback){
                    success_callback()
                }
                return
            }
            response.json()
                .then(json => {
                    // 성공했을때 프로토콜 응답코드(200 ~ 299)
                    if(response.status >= 200 && response.status < 300) {
                        if(success_callback) {
                            success_callback(json)
                        }else if(operation !== 'login' && response.status === 401){
                            access_token.set('')
                            username.set('')
                            is_login.set(false)
                            alert("로그인이 필요합니다.")
                            push('/user-login')
                        }
                    }else {
                        if (failure_callback) {
                            failure_callback(json)
                        }else {
                            alert(JSON.stringify(json))
                        }
                    }
                })
                .catch(error => {
                    alert(JSON.stringify(error))
                })
        })
}

export default fastapi