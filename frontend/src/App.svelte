<script>
  import Router from 'svelte-spa-router'
  import Home from "./routes/Home.svelte"
  import Detail from "./routes/Detail.svelte"
  import QuestionCreate from "./routes/QuestionCreate.svelte"
  import Navigation from "./components/Navigation.svelte"
  import UserCreate from "./routes/UserCreate.svelte"
  import UserLogin from "./routes/UserLogin.svelte";
  import QuestionModify from "./routes/QuestionModify.svelte"
  import AnswerModify from "./routes/AnswerModify.svelte"

  // 처음 URL을 받으면 해당 경로에 따른 컴포넌트 호출
  const routes = {
      // 처음 서버가 실행되면 Home.svelte 실행
      '/': Home,
      '/detail/:question_id': Detail,
      '/question-create': QuestionCreate,
      '/user-create': UserCreate,
      '/user-login': UserLogin,
      '/question-modify/:question_id': QuestionModify,
      '/answer-modify/:answer_id': AnswerModify,
  }
</script>

<Navigation />
<Router {routes} />