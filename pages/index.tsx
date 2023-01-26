import Link from "next/link";
import { useState } from "react";
import { Header } from "../components/header/Header";
import { User } from "../models/user";
import { getUser } from "../utils/userCache";

export default function Home() {
  const [user, setUser] = useState<User | null>(getUser());

  const handleLogout = () => {
    setUser(null);
  };

  return (
    <>
      <Header user={user} logout={handleLogout} />
      <div style={bodyContainer}>Body</div>
    </>
  );
}

const bodyContainer: any = {
  maxWidth: "85%",
  display: "flex",
  flexDirection: "flex-column",
  margin: "32px",
};
