import { FC, useState } from "react";
import { Book } from "../../models/book";
import { SearchOptions } from "../../pages";

type BookListProps = {
  books: Book[] | null;
  handleSearch: (searchOptions: SearchOptions | null) => void;
  loanBook: (bookId: string) => void;
};

export const BookList: FC<BookListProps> = ({
  books,
  handleSearch,
  loanBook,
}) => {
  const [searchQuery, setSearchQuery] = useState<string>("");
  const [selectedCriteria, setSelectedCriteria] = useState<string>("title");

  const resetSearch = () => {
    setSearchQuery("");
    setSelectedCriteria("title");

    handleSearch(null);
  };

  const handleChange = (event: any) => {
    setSearchQuery(event.target.value);
  };

  return (
    <div style={{ display: "flex", flexDirection: "column", minWidth: "100%" }}>
      <div
        style={{
          width: "80%",
          margin: "auto",
          display: "flex",
          justifyContent: "space-around",
          marginBottom: "32px",
        }}
      >
        <div>
          <label>
            <input
              type="radio"
              name="search-by"
              value="id"
              checked={selectedCriteria === "id"}
              onChange={(e) => setSelectedCriteria(e.target.id)}
            />
            Identifikator
          </label>
          <label>
            <input
              type="radio"
              name="search-by"
              value="title"
              checked={selectedCriteria === "title"}
              onChange={(e) => setSelectedCriteria(e.target.id)}
            />
            Nazev knihy
          </label>
        </div>
        <div>
          <input
            type="text"
            id="search-query"
            placeholder="Zadejte hledaný výraz"
            value={searchQuery}
            onChange={handleChange}
          />
          <button
            type="button"
            id="search-button"
            onClick={() =>
              handleSearch({
                column: selectedCriteria as "id" | "title",
                searchQuery,
              })
            }
          >
            Vyhledat
          </button>
          <button
            onClick={() => resetSearch()}
            style={{ marginLeft: "12px" }}
            disabled={searchQuery.length === 0}
          >
            Zrusit vyhledavani
          </button>
        </div>
      </div>
      {/* <input
          type="text"
          name="search"
          id="search"
          placeholder="Hledej knihu..."
        />

        <button onClick={() => handleSearch(searchQuery)}>Vyhledat</button> */}

      <div>
        {books ? (
          <table style={{ minWidth: "100%" }}>
            <thead>
              <tr>
                {/* <th>Identifikator</th> */}
                <th>Nazev</th>
                <th>Autor</th>
                <th>Rok vydani</th>
                <th>Pocet dostupnych knih</th>
                <th>Celkovy pocet knih</th>
                <th> </th>
              </tr>
            </thead>
            <tbody>
              {books.map((book: Book) => (
                <tr key={book.id}>
                  {/* <td>{book.id}</td> */}
                  <td>{book.title}</td>
                  <td>{book.author}</td>
                  <td>{book.year}</td>
                  <td>{book.countAvailable}</td>
                  <td>{book.countOverall}</td>
                  <td>
                    <button onClick={() => loanBook(book.id)}>
                      Pujcit knihu
                    </button>
                  </td>
                </tr>
              ))}
            </tbody>
          </table>
        ) : (
          <div>Takovou knihu nemame</div>
        )}
      </div>
    </div>
  );
};
