import { FC } from "react";
import { User } from "../../models/user";

type HeaderProps = {
  user: User | null;
  handleOpenLoginForm: () => void;
  handleOpenRegistrationForm: () => void;
  handleLogout: () => void;
};

export const Header: FC<HeaderProps> = ({
  user,
  handleOpenLoginForm,
  handleOpenRegistrationForm,
  handleLogout,
}) => {
  return (
    <div style={containerStyles}>
      <div>Knihovna PD</div>
      {user ? (
        <div style={innerHeader}>
          <div>Welcome</div>
          <div
            style={{ margin: "0 16px" }}
          >{`${user.firstName} ${user.lastName}`}</div>
          <button onClick={handleLogout}>Logout</button>
        </div>
      ) : (
        <div style={innerHeader}>
          <div>Uzivatel neprihlasen {">"}</div>
          <div style={{ marginLeft: "12px" }}>
            <button onClick={handleOpenLoginForm}>Login</button>
          </div>
          <div style={{ marginLeft: "12px" }}>
            <button onClick={handleOpenRegistrationForm}>Registrace</button>
          </div>
        </div>
      )}
    </div>
  );
};

const containerStyles = {
  display: "flex",
  justifyContent: "space-between",
  padding: "8px 12px",
};

const innerHeader = {
  display: "flex",
};
