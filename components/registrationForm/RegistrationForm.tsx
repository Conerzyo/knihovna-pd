import { FC, useState } from "react";

type RegistrationLoginFormProps = {
  handleRegistration: (data: FormData) => Promise<void>;
  open: boolean;
};

export const RegistrationForm: FC<RegistrationLoginFormProps> = ({
  handleRegistration,
  open,
}) => {
  const [username, setUsername] = useState<string>("");
  const [password, setPassword] = useState<string>("");
  const [firstName, setFirstName] = useState<string>("");
  const [lastName, setLastName] = useState<string>("");
  const [socialNumber, setSocialNumber] = useState<string>("");
  const [address, setAddress] = useState<string>("");

  const register = () => {
    const data = new FormData();

    data.append("username", username);
    data.append("password", password);
    data.append("firstName", firstName);
    data.append("lastName", lastName);
    data.append("socialNumber", socialNumber);
    data.append("address", address);

    handleRegistration(data);
  };

  return (
    <>
      {open && (
        <div style={containerStyles}>
          <h1>Registrace</h1>
          <label htmlFor="username">Uzivatelske jmeno</label>
          <input
            id="username"
            type="text"
            style={{ margin: "6px 0px" }}
            onChange={(e) => setUsername(e.target.value)}
          />

          <label htmlFor="password">Heslo</label>
          <input
            id="password"
            type="password"
            style={{ margin: "6px 0px" }}
            onChange={(e) => setPassword(e.target.value)}
          />

          <label htmlFor="username">Jmeno</label>
          <input
            id="firstName"
            type="text"
            style={{ margin: "6px 0px" }}
            onChange={(e) => setFirstName(e.target.value)}
          />

          <label htmlFor="username">Prijmeni</label>
          <input
            id="lastName"
            type="text"
            style={{ margin: "6px 0px" }}
            onChange={(e) => setLastName(e.target.value)}
          />

          <label htmlFor="username">Rodne cislo</label>
          <input
            id="socialNumber"
            type="text"
            style={{ margin: "6px 0px" }}
            onChange={(e) => setSocialNumber(e.target.value)}
          />

          <label htmlFor="username">Adresa</label>
          <input
            id="address"
            type="text"
            style={{ margin: "6px 0px" }}
            onChange={(e) => setAddress(e.target.value)}
          />

          <button style={{ margin: "24px 0px" }} onClick={register}>
            Registrovat!
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
  height: "50vh",
};
