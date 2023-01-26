<script>
  import Router from 'svelte-spa-router'
  import Home from "./routes/Home.svelte"
  import Detail from "./routes/Detail.svelte"

  // 처음 URL을 받으면 해당 경로에 따른 컴포넌트 호출
  const routes = {
      // 처음 서버가 실행되면 Home.svelte 실행
      '/': Home,
      '/detail/:question_id': Detail

  }
</script>

<Router {routes} />