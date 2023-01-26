import { FC, useState } from "react";
import { Book } from "../../models/book";

interface BookListProps {
  books: Book[];
}

export const BookList: FC<BookListProps> = ({ books }) => {
  const [searchQuery, setSearchQuery] = useState<string>("");

  const submitSearch = () => {
    if (searchQuery.length < 3) {
      alert("Search query is too short.");
    } else {
      console.log("Searching....", searchQuery);
    }
  };

  return (
    <>
      <label htmlFor="search-book-list">Search: </label>
      <input
        id="search-book-list"
        type="text"
        style={{ marginBottom: "12px " }}
        onChange={(e) => setSearchQuery(e.target.value)}
      />
      <button onClick={submitSearch}>Search</button>
      <table style={{ width: "100%" }}>
        <tr style={{ textAlign: "left" }}>
          <th>Book Title</th>
          <th>Author</th>
          <th>Year of Publishing</th>
          <th>Available books</th>
          <th>Actions</th>
        </tr>
        <tbody>
          {books.map((book: Book) => (
            <tr key={book.id} style={{ padding: "4px" }}>
              <td>{book.title}</td>
              <td>{book.author}</td>
              <td>{book.year}</td>
              <td>{book.countAvailable}</td>
              <td>
                <button disabled={book.countAvailable === 0}>
                  Loan this book
                </button>
              </td>
            </tr>
          ))}
        </tbody>
      </table>
    </>
  );
};
