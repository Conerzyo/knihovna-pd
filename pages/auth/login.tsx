import { useState } from "react";
import { ApiCall } from "../../utils/api";

export default function Login() {
  const [username, setUsername] = useState<string>("");
  const [password, setPassword] = useState<string>("");

  const handleLogin = async () => {
    const data = new FormData();

    data.append("username", username);
    data.append("password", password);

    const loginRes = await ApiCall.post("/login", data);

    const userDataRes = await ApiCall.get(
      `/users/getById?id=${loginRes.data.loged}`
    );

    console.log(userDataRes);
  };

  return (
    <div style={containerStyles}>
      <h1>Login</h1>
      <label htmlFor="username">Username</label>
      <input
        id="username"
        type="text"
        style={{ margin: "6px 0px" }}
        onChange={(e) => setUsername(e.target.value)}
      />
      <label htmlFor="password">Password</label>
      <input
        id="password"
        type="password"
        style={{ margin: "6px 0px" }}
        onChange={(e) => setPassword(e.target.value)}
      />
      <button style={{ margin: "24px 0px" }} onClick={() => handleLogin()}>
        Sign in
      </button>
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
