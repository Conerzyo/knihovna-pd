import Link from "next/link";
import { useEffect, useState } from "react";
import { BookList } from "../components/bookList/BookList";
import { Header } from "../components/header/Header";
import { LoginForm } from "../components/loginForm/LoginForm";
import { Book } from "../models/book";
import { User } from "../models/user";
import { ApiCall } from "../utils/api";

export type SearchOptions = {
  column: "id" | "title";
  searchQuery: string;
};

export default function Home() {
  const [user, setUser] = useState<User | null>(null);
  const [isLoginFormOpen, setIsLoginFormOpen] = useState<boolean>(false);
  const [books, setBooks] = useState<Book[] | null>(null);

  // get books on load
  useEffect(() => {
    getBooks(null);
  }, []);

  const getBooks = async (searchOptions: SearchOptions | null) => {
    let books = null;

    if (searchOptions == null) {
      books = await (await ApiCall.get("/books/getAll")).data.books;
    } else if (searchOptions.column === "id") {
      books = await (
        await ApiCall.get(`/books/getById?id=${searchOptions.searchQuery}`)
      ).data.books;
    } else {
      books = await (
        await ApiCall.get(
          `/books/getByTitle?title=${searchOptions.searchQuery}`
        )
      ).data.books;
    }

    setBooks(books);
  };

  const handleLogin = async (data: FormData) => {
    const loginRes = await ApiCall.post("/login", data);

    const userDataRes = await ApiCall.get(
      `/users/getById?id=${loginRes.data.loged}`
    );

    if (userDataRes.status === 200) {
      setUser(userDataRes.data.users[0]);
      setIsLoginFormOpen(false);
    }
  };

  const handleLogout = async () => {
    const res = await ApiCall.get("/logout");

    if (res.status === 200) {
      setUser(null);
    }
  };

  return (
    <>
      <Header
        user={user}
        handleOpenLoginForm={() => setIsLoginFormOpen(!isLoginFormOpen)}
        handleLogout={handleLogout}
      />
      <LoginForm handleLogin={handleLogin} open={isLoginFormOpen} />
      {!isLoginFormOpen && (
        <body style={bodyContainer}>
          <BookList books={books} handleSearch={getBooks} loanBook={() => {}} />
        </body>
      )}
    </>
  );
}

const bodyContainer: any = {
  display: "flex",
  flexDirection: "flex-column",
  justifyContent: "center",
};
