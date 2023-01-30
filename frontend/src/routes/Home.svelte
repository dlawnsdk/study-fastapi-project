<script>
    import fastapi from "../lib/api"
    import { link } from 'svelte-spa-router'

    let question_list = []
    let size = 10
    let page = 0
    let total = 0
    //$: ? => 반응형 변수. 실시간으로 다시 계산된다
    $: total_page = Math.ceil(total/size) // 페이지 올림 (ex 12개 데이터라면 2 반환)

    //게시글 리스트 조회
    function get_question_list(_page){
        let params = {
            page: _page,
            size: size,
        }
        // 서버로 보낼 메소드 방식, uri, parameter, callback함수
       fastapi('get', '/api/question/list', params, (json) => {
           question_list = json.question_list
           page = _page
           total = json.total
       })
    }

    // 게시글 리스트 조회 메소드 실행
    get_question_list(0)
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
    <!-- 페이징처리 시작 -->
    <ul class="pagination justify-content-center">
        <!-- 이전 페이지 -->
        <li class="page-item { page <= 0 && 'disabled' }">
            <button class="page-link" on:click="{ () => get_question_list(page-1) }">이전</button>
        </li>
        <!-- 페이지 번호 -->
        {#each Array(total_page) as _, loop_page}
            {#if loop_page >= page-5 && loop_page <= page+5}
                <li class="page-item { loop_page === page && 'active' }">
                    <button on:click="{ () => get_question_list(loop_page) }" class="page-link">{ loop_page+1 }</button>
                </li>
            {/if}
        {/each}
        <!-- 다음 페이지 -->
        <li class="page-item {page >= total_page-1 && 'disabled'}">
            <button class="page-link" on:click="{ () => get_question_list(page+1) }">다음</button>
        </li>
    </ul>
    <!-- 페이징 처리 끝 -->
     <a use:link href="/question-create" class="btn btn-primary">질문 등록하기</a>
</div>