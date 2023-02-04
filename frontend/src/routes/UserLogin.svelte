<script>
    import { push } from 'svelte-spa-router'
    import fastapi from "../lib/api.js"
    import Error from "../components/Error.svelte"
    import { access_token, username, is_login } from "../lib/store.js"

    let error = {detail:[]}
    let login_username = ""
    let login_password = ""

    var login = (event) => {
        event.preventDefault()
        let url = "/api/user/login"
        let params = {
            username: login_username,
            password: login_password,
        }
        fastapi('login', url, params, (json) => {
            $access_token = json.access_token
            $username = json.username
            $is_login = true
            push("/") // 성공시 페이지 이동
        }, (json_error) => {
            error = json_error
        })
    }
</script>

   <style>
      form {
        background-color: white;
        padding: 40px;
        box-shadow: 0 0 10px rgba(0, 0, 0, 0.1);
        border-radius: 10px;
        display: flex;
        flex-direction: column;
        align-items: center;
        width: 500px;
        margin: 0 auto;
      }
      input[type="text"], input[type="password"] {
        height: 50px;
        width: 100%;
        padding: 10px;
        margin-bottom: 20px;
        border: none;
        border-radius: 5px;
        font-size: 18px;
      }
      input[type="submit"] {
        background-color: #4CAF50;
        color: white;
        height: 50px;
        width: 100%;
        border: none;
        border-radius: 5px;
        font-size: 18px;
        cursor: pointer;
      }
      label {
        font-size: 20px;
        margin-bottom: 10px;
      }
    </style>
<div style="padding-top: 100px">
     <h2 style="text-align: center">로그인</h2>
    <Error error="{error}" />
    <form action="post">
      <label for="username">Username:</label>
      <input type="text" id="username" name="username" bind:value={login_username}>
      <label for="password">Password:</label>
      <input type="password" id="password" name="password" bind:value={login_password}>
      <input type="submit" value="로그인" on:click={login}>
    </form>
</div>