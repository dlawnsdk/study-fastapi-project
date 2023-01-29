const fastapi = (operation, url, params, success_callback, failure_callback) => {
    let method = operation
    let content_type = 'application/json'
    let body = JSON.stringify(params) // body 항목에 전달 받은  parameter를 할당 하려면 JSON 타입으로 변환 해야 한다.

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