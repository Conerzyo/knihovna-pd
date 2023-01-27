import axios from "axios";

export const URL_STRING = "http://127.0.0.1:5000";

export const ApiCall = axios.create({
  baseURL: URL_STRING,
  withCredentials: true,
});
