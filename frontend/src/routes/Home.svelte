<script>
    import fastapi from "../lib/api"
    import { link } from 'svelte-spa-router'
    import { page, is_login, keyword } from '../lib/store'
    import moment from 'moment/min/moment-with-locales'
    moment.locale('ko')

    let question_list = []
    let size = 10
    let total = 0
    let kw = ''
    //$: ? => 반응형 변수. 실시간으로 다시 계산된다
    $: total_page = Math.ceil(total/size) // 올림 (ex 12개 데이터라면 2 반환)

    //게시글 리스트 조회
    function get_question_list(){
        let params = {
            page: $page,
            size: size,
            keyword: $keyword,
        }
        // 서버로 보낼 메소드 방식, uri, parameter, callback함수
       fastapi('get', '/api/question/list', params, (json) => {
           question_list = json.question_list
           total = json.total
           kw = $keyword
       })
    }

    // 페이지 또는 키워드가 변경되면 자동으로 해당 함수를 실행한다.
    $:$page, $keyword, get_question_list()
</script>

<div class="container my-3">
    <div class="row my-3">
        <div class="col-6">
            <a use:link href="/question-create"
                class="btn btn-primary {$is_login ? '' : 'disabled'}">질문 등록하기</a>
        </div>
        <div class="col-6">
            <div class="input-group">
                <input type="text" class="form-control" bind:value="{kw}">
                <button class="btn btn-outline-secondary" on:click={() => {$keyword = kw, $page = 0}}>
                    찾기
                </button>
            </div>
        </div>
    </div>
    <table class="table">
        <thead>
            <tr class="text-center table-dark">
                <th>번호</th>
                <th style="width:50%">제목</th>
                <th>글쓴이</th>
                <th>작성일시</th>
            </tr>
        </thead>
        <tbody>
        {#each question_list as question, i}
            <tr>
                <td>{total - ($page * size) - i}</td>
                <td>
                    <a use:link href="/detail/{question.id}">{question.subject}</a>
                    {#if question.answer.length > 0}
                        <span class="text-danger small mx-2">{question.answer.length}</span>
                    {/if}
                </td>
                <td>{ question.user ? question.user.username : "" }</td>
                <td>{moment(question.create_date).format('YYYY. MM. DD a hh시')}</td>
            </tr>
        {/each}
        </tbody>
    </table>
    <!-- 페이징처리 시작 -->
    <ul class="pagination justify-content-center">
        <!-- 이전 페이지 -->
        <li class="page-item { $page <= 0 && 'disabled' }">
            <button class="page-link" on:click="{ () => $page }">이전</button>
        </li>
        <!-- 페이지 번호 -->
        {#each Array(total_page) as _, loop_page}
            {#if loop_page >= $page-5 && loop_page <= $page+5}
                <li class="page-item { loop_page === $page && 'active' }">
                    <button on:click="{ () => $page = loop_page }" class="page-link">{ loop_page+1 }</button>
                </li>
            {/if}
        {/each}
        <!-- 다음 페이지 -->
        <li class="page-item { $page >= total_page-1 && 'disabled'}">
            <button class="page-link" on:click="{ () => $page++ }">다음</button>
        </li>
    </ul>
    <!-- 페이징 처리 끝 -->
</div>