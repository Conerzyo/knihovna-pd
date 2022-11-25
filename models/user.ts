export interface User {
  firstName: string;
  lastName: string;
  socialNumber: string;
  address: string;
  username: string;
  status: UserStatus;
  role: UserRole;
}

export enum UserRole {
  LIBRARIAN,
  USER,
}

export enum UserStatus {
  ACTIVE,
  INACTIVE,
}
