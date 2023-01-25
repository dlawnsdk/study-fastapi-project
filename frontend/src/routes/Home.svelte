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

<ul>
    {#each question_list as question}
        <li><a use:link href="/detail/{question.id}">{question.subject}</a></li>
    {/each}
</ul>