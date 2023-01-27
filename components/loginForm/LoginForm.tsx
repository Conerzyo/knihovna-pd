import { FC, useState } from "react";

type LoginFormProps = {
  handleLogin: (data: FormData) => Promise<void>;
  open: boolean;
};

export const LoginForm: FC<LoginFormProps> = ({ handleLogin, open }) => {
  const [username, setUsername] = useState<string>("");
  const [password, setPassword] = useState<string>("");
  const [success, setSuccess] = useState<boolean | null>(null);

  const login = () => {
    const data = new FormData();

    data.append("username", username);
    data.append("password", password);

    handleLogin(data);
  };

  return (
    <>
      {open && (
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
          <button style={{ margin: "24px 0px" }} onClick={login}>
            Sign in
          </button>
        </div>
      )}
    </>
  );
};

const containerStyles: any = {
  display: "flex",
  flexDirection: "column",
  margin: "auto",
  width: "25vw",
  justifyContent: "center",
  height: "25vh",
};
