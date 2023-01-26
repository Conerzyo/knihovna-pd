import { useState } from "react";
import { URL_STRING } from "../../utils/constants";
import axios from "axios";

export default function Login() {
  const [username, setUsername] = useState<string>("");
  const [password, setPassword] = useState<string>("");

  const handleLogin = async () => {
    //   const data = new FormData();

    //   data.append("username", username);
    //   data.append("password", password);

    // const res = await fetch(URL_STRING + "/login", {
    //   mode: "no-cors",
    //   method: "POST",
    //   body: data,
    //   headers: {
    //     // "Content-Type": "application/json",
    //     "Content-Type": "multipart/form-data",
    //     Accept: "application/json",
    //   },
    // });

    //   console.log(res);
    //   const resData = await res.json();

    //   console.log(resData);

    // const test = await fetch(URL_STRING + "/books/getAll", {
    //   method: "GET",
    //   mode: "no-cors",
    //   headers: {
    //     "Content-Type": "application/json",
    //     // "Content-Type": "multipart/form-data",
    //     Accept: "application/json",
    //   },
    // });
    // console.log(await test.json());

    axios
      .get(URL_STRING + "/books/getAll")
      .then((res) => console.log(res.data));
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
