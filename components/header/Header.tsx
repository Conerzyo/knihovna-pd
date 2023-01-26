import Link from "next/link";
import { FC } from "react";
import { User } from "../../models/user";

type HeaderProps = {
  user: User | null;
  logout: () => void;
};

export const Header: FC<HeaderProps> = ({ user, logout }) => {
  return (
    <div style={containerStyles}>
      <div>Knihovna PD</div>

      {user && (
        <div style={innerHeader}>
          <div>Logged user</div>
          <div>{`${user.firstName} ${user.lastName}`}</div>
          <button onClick={logout}>Logout</button>
        </div>
      )}
      <div style={innerHeader}>
        <div>No logged user! </div>
        <div style={{ marginLeft: "12px" }}>
          <Link href="/auth/login">LOGIN</Link>
        </div>
      </div>
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
