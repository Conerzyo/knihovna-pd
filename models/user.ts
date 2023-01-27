export interface User {
  firstName: string;
  lastName: string;
  socialNumber: string;
  address: string;
  username: string;
  active: boolean;
  admin: boolean;

  [index: string]: string | boolean;
}
