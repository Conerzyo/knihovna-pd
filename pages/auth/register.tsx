export default function Register() {
  return (
    <div className="form-container">
      <h1>Register a new user</h1>

      <label htmlFor="firstname">First name</label>
      <input id="firstname" type="text" style={{ margin: "6px 0px" }} />

      <label htmlFor="lastname">Last name</label>
      <input id="lastname" type="text" style={{ margin: "6px 0px" }} />

      <label htmlFor="socialnumber">Social Number</label>
      <input id="socialnumber" type="text" style={{ margin: "6px 0px" }} />

      <label htmlFor="address">Address</label>
      <input id="address" type="text" style={{ margin: "6px 0px" }} />

      <label htmlFor="username">Username</label>
      <input id="username" type="text" style={{ margin: "6px 0px" }} />

      <label htmlFor="password">Password</label>
      <input id="password" type="password" style={{ margin: "6px 0px" }} />

      <label htmlFor="password-again">Password again</label>
      <input
        id="password-again"
        type="password"
        style={{ margin: "6px 0px" }}
      />

      <button style={{ margin: "24px 0px" }}>Create new account</button>
    </div>
  );
}
