import { User } from "../models/user";

export const saveUser = (user: User) => {
  localStorage.setItem("user", JSON.stringify(user));
};

export const getUser = (): User | null => {
  const userRaw = localStorage.getItem("user");

  return userRaw ? JSON.parse(userRaw) : null;
};
