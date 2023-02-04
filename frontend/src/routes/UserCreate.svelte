<script>
    import { push } from 'svelte-spa-router'
    import fastapi from "../lib/api"
    import Error from "../components/Error.svelte"

    let error = {detail:[]}

    let username = ''
    let password1 = ''
    let password2 = ''
    let email = ''

    var post_user = (event) => {
        event.preventDefault()
        let url  = "/api/user/create"
        let params = {
            username: username,
            password1: password1,
            password2: password2,
            email: email
        }
        fastapi('post', url, params, (json) => {
                push('/user-login')
            },
            (json_error) => {
                error = json_error
            }
        )
    }
</script>

  <title>Sign Up Page</title>
  <style>
    .signup-container {
      width: 500px;
      background-color: white;
      margin: 100px auto;
      padding: 50px;
      box-shadow: 0px 0px 10px 0px #333;
      border-radius: 10px;
    }

    h1 {
      text-align: center;
      margin-bottom: 50px;
    }

    label {
      font-weight: bold;
      margin-top: 20px;
      display: block;
    }

    input[type="text"],
    input[type="email"],
    input[type="password"] {
      width: 100%;
      padding: 10px;
      margin-top: 10px;
      border: none;
      border-radius: 5px;
      box-shadow: 0px 0px 10px 0px #ccc;
    }

    input[type="submit"] {
      width: 100%;
      padding: 10px;
      margin-top: 20px;
      border: none;
      border-radius: 5px;
      background-color: blue;
      color: white;
      cursor: pointer;
    }
  </style>

  <div class="signup-container">
    <h1>Sign Up</h1>
      <Error error={error} />
    <form action="submit_signup" method="post">
      <label for="username">Username:</label>
      <input type="text" id="username" name="username" bind:value={username}><br><br>
      <label for="email">Email:</label>
      <input type="email" id="email" name="email" bind:value={email}><br><br>
      <label for="password">Password:</label>
      <input type="password" id="password" name="password" bind:value={password1}><br><br>
      <label for="confirm_password">Confirm Password:</label>
      <input type="password" id="confirm_password" name="confirm_password" bind:value={password2}><br><br>
      <input type="submit" value="Sign Up" on:click={post_user}>
    </form>
  </div>