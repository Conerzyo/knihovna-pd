export default function Login() {
  return (
    <div style={containerStyles}>
      <h2>Login</h2>
      <label htmlFor="username">Username</label>
      <input id="username" type="text" style={{ margin: "6px 0px" }} />
      <label htmlFor="password">Password</label>
      <input id="password" type="password" style={{ margin: "6px 0px" }} />
      <button style={{ margin: "24px 0px" }}>Sign in</button>
    </div>
  );
}

const containerStyles = {
  display: "flex",
  flexDirection: "column",
  margin: "auto",
  width: "25vw",
  justifyContent: "center",
  height: "100vh",
};
