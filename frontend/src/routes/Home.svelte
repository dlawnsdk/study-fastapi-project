<script>
    import fastapi from "../lib/api"
    import { link } from 'svelte-spa-router'

    let question_list = []

    //게시글 리스트 조회
    function get_question_list(){
        // 서버로 보낼 메소드 방식, uri, parameter, callback함수
       fastapi('get', '/api/question/list', {}, (json) => {
           question_list = json
       })
    }

    // 게시글 리스트 조회 메소드 실행
    get_question_list()
</script>

<div class="container my-3">
    <table class="table">
        <thead>
        <tr class="table-dark">
            <th>번호</th>
            <th>제목</th>
            <th>작성일시</th>
        </tr>
        </thead>
        <tbody>
        {#each question_list as question, i}
        <tr>
            <td>{i+1}</td>
            <td>
                <a use:link href="/detail/{question.id}">{question.subject}</a>
            </td>
            <td>{question.create_date}</td>
        </tr>
        {/each}
        </tbody>
    </table>
     <a use:link href="/question-create" class="btn btn-primary">질문 등록하기</a>
</div>