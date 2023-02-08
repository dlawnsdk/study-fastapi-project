<script>
    import fastapi from "../lib/api";
    import Error from "../components/Error.svelte"
    import { link, push } from 'svelte-spa-router'
    import { is_login, username } from "../lib/store.js";
    import moment from 'moment/min/moment-with-locales'
    moment.locale('ko')

    export let params = {} // 파라미터 받아주는 변수

    let error = {detail:[]}
    let question_id = params.question_id
    let question = {answer:[]}
    let content = ""

    function get_question(){
        fastapi("get", "/api/question/detail/" + question_id, {}, (json) => {
            question = json
        })
    }

    get_question()

    function post_answer(event){
        event.preventDefault()
        let url = "/api/answer/create/" + question_id
        let params = {
            content: content
        }
        fastapi('post', url, params, (json) =>{
            content = ''
            get_question()
        })
    }

    function delete_question(_question_id){
        if(window.confirm('삭제 하시겠습니까?')){
            let url = "/api/question/delete"
            let params = {
                question_id: _question_id
            }
            fastapi('delete', url, params, (json) => {
                push('/')
            }, (err_json) => {
                error = err_json
            })
        }
    }
</script>
<div class="container my-3">
      <!-- 질문 -->
    <h2 class="border-bottom py-2">{question.subject}</h2>
    <div class="card my-3">
        <div class="card-body">
            <div class="card-text" style="white-space: pre-line;">{question.content}</div>
            <div class="d-flex justify-content-end">
                <div class="badge bg-light text-dark p-2 text-start">
                    <div calss="mb-2">{ question.user ? question.user.username : ""}</div>
                    <div>{moment(question.create_date).format("YYYY. MM. DD a hh시")}</div>
                </div>
            </div>
            <div class="my-3">
                {#if question.user && $username === question.user.username}
                    <a use:link href="/question-modify/{question.id}" class="btn btn-sm btn-outline-secondary">수정</a>
                    <button class="btn btn-sm btn-outline-secondary" on:click={() => delete_question(question.id)}>삭제</button>
                {/if}
            </div>
        </div>
    </div>
    <button class="btn btn-secondary" on:click={() => push('/')}>목륵</button>
    <!-- 답변 목록 -->
     <Error error={error} />
    <h5 class="border-bottom my-3 py-2">{question.answer.length}개의 답변이 있습니다.</h5>
   {#each question.answer as answer}
        <div class="card my-3">
            <div class="card-body">
                <div class="card-text" style="white-space: pre-line;">{answer.content}</div>
                <div class="d-flex justify-content-end">
                    <div class="badge bg-light text-dark p-2 text-start">
                        <div class="mb-2">{ answer.user ? answer.user.username : "" }</div>
                        <div>{moment(answer.create_date).format("YYYY. MM. DD a hh시")}</div>
                    </div>
                </div>
            </div>

        </div>
    {/each}
    <form method="post" class="my-3">
        <div class="mb-3">
            <textarea rows="10" bind:value={content} class="form-control" />
        </div>
        <input type="submit" value="답변등록" class="btn btn-primary" on:click="{post_answer}" />
    </form>
</div>