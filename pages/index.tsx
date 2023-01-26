import Link from "next/link";
import { BookList } from "../components/BookList/BookList";
import { Book } from "../models/book";
import { MOCK_BOOKS } from "../models/mocks/books";

export default function Home({ books }: { books: Book[] }) {
  return (
    <>
      <header style={containerStyles}>
        <div>Knihovna PD</div>
        <div style={innerHeader}>
          <div>Logged user</div>
          <Link href="/login">Login</Link>
        </div>
      </header>
      <section style={containerBodyStyle}>
        <h2>Catalog</h2>
        <BookList books={books} />
      </section>
    </>
  );
}

export async function getServerSideProps(context) {
  return {
    props: { books: MOCK_BOOKS }, // will be passed to the page component as props
  };
}

const containerStyles = {
  display: "flex",
  justifyContent: "space-between",
  padding: "8px 12px",
};

const innerHeader = {
  display: "flex",
};

const containerBodyStyle = {
  margin: "auto",
  width: "75vw",
};
