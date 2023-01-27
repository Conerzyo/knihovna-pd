import { useEffect, useState } from "react";
import { AdminPanel } from "../components/adminPanel/AdminPanel";
import { BookList } from "../components/bookList/BookList";
import { Header } from "../components/header/Header";
import { LoanList } from "../components/loanList/LoanList";
import { LoginForm } from "../components/loginForm/LoginForm";
import { Menu } from "../components/menu/Menu";
import { Book } from "../models/book";
import { Loan } from "../models/loan";
import { User } from "../models/user";
import { ApiCall } from "../utils/api";

export type SearchOptions = {
  column: "id" | "title";
  searchQuery: string;
};

export default function Home() {
  const [user, setUser] = useState<User | null>(null);
  const [userId, setUserId] = useState<string | null>(null);
  const [isUserAdmin, setIsUserAdmin] = useState<boolean | null>(null);
  const [isLoginFormOpen, setIsLoginFormOpen] = useState<boolean>(false);
  const [books, setBooks] = useState<Book[] | null>([]);
  const [loans, setMyLoans] = useState<Loan[] | null>([]);
  const [activeTab, setActiveTab] = useState<string>("catalog");

  // get data on load
  useEffect(() => {
    handleTabChange("catalog");
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

  const getMyLoans = async () => {
    const res = (await ApiCall.get(`/loans/getByUserId?userId=${userId}`)).data;

    setMyLoans(res.loans);
  };

  const handleLogin = async (data: FormData) => {
    const loginRes = await ApiCall.post("/login", data);

    setUserId(loginRes.data.loged);

    const userDataRes = await ApiCall.get(
      `/users/getById?id=${loginRes.data.loged}`
    );

    if (userDataRes.status === 200) {
      const user: User = userDataRes.data.users[0];
      setUser(user);
      setIsUserAdmin(user.admin && user.active);
      setIsLoginFormOpen(false);
    }
  };

  const handleLogout = async () => {
    const res = await ApiCall.get("/logout");

    if (res.status === 200) {
      setUser(null);
    }
  };

  const handleTabChange = (tabName: string) => {
    if (tabName === "catalog") {
      setActiveTab(tabName);
      getBooks(null);
    } else if (tabName === "myLoans") {
      setActiveTab(tabName);
      getMyLoans();
    } else if (tabName === "admin") {
      setActiveTab(tabName);
    }
  };

  const handleCreateLoan = async (bookId: string) => {
    const data = new FormData();

    if (userId) {
      data.append("userId", userId);
      data.append("bookId", bookId);

      console.log(`CREATING LOAN FOR:\nUSER ${userId} \nBOOK ${bookId} `);
      const res = await ApiCall.post("/loans/create", data);

      if (res.status === 200) {
        getBooks(null);
      }
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
        <>
          <Menu
            activeTab={activeTab}
            isUserLogged={!!userId}
            isUserAdmin={isUserAdmin}
            handleTabChange={handleTabChange}
          />
          <div style={bodyContainer}>
            {activeTab === "catalog" && (
              <BookList
                books={books}
                handleSearch={getBooks}
                handleLoanBook={handleCreateLoan}
                isUserLogged={!!userId}
              />
            )}

            {activeTab === "myLoans" && <LoanList loans={loans} />}

            {activeTab === "admin" && <AdminPanel />}
          </div>
        </>
      )}
    </>
  );
}

const bodyContainer: any = {
  display: "flex",
  flexDirection: "flex-column",
  justifyContent: "center",
  minWidth: "80vw",
};
