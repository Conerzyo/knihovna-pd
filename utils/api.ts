import axios from "axios";
import { URL_STRING } from "./constants";

export const ApiCall = axios.create({
  baseURL: URL_STRING,
  withCredentials: true,
});
