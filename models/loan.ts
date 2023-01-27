import { Book } from "./book";
import { User } from "./user";

export interface Loan {
  id: string;
  loanDate: Date;
  dueDate: Date;
  endDate: Date;
  book: Book;
  user: User;

  [index: string]: string | Date | Book | User;
}

export interface LoanRaw {
  id: string;
  loanDate: Date;
  dueDate: Date;
  endDate: Date;
  bookId: string;
  userId: string;
}
