<script>
  import Router from 'svelte-spa-router'
  import Home from "./routes/Home.svelte"
  import Detail from "./routes/Detail.svelte"

  const routes = {
      // 처음 서버가 실행되면 Home.svelte 실행
      '/': Home,
      '/detail/:question_id': Detail

  }
</script>

<Router {routes} />