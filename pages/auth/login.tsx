export default function Login() {
  return (
    <div className="form-container">
      <h1>Login</h1>
      <label htmlFor="username">Username</label>
      <input id="username" type="text" style={{ margin: "6px 0px" }} />
      <label htmlFor="password">Password</label>
      <input id="password" type="password" style={{ margin: "6px 0px" }} />
      <button style={{ margin: "24px 0px" }}>Sign in</button>
    </div>
  );
}
