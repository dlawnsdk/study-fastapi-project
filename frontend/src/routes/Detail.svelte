<script>
    import fastapi from "../lib/api"
    export let params = {} // 파라미터 받아주는 변수

    let question_id = params.question_id
    let question = {}

    function get_question(){
        fastapi("get", "/api/question/detail/" + question_id, {}, (json) => {
            question = json
        })
    }

    get_question()
</script>

<h1>{question.subject}</h1>
<div>
    {question.content}
</div>
