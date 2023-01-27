import { FC, useState } from "react";
import { Loan } from "../../models/loan";
import { SearchOptions } from "../../pages";

type LoanListProps = {
  loans: Loan[] | null;
  handleEndLoan: (id: string) => void;
  handleSearch: (searchOptions: SearchOptions | null) => void;
};

export const LoanList: FC<LoanListProps> = ({
  loans,
  handleEndLoan,
  handleSearch,
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
              column: selectedCriteria,
              searchQuery,
            })
          }
          disabled={searchQuery.length < 3}
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

      <div>
        {loans?.length ? (
          <table style={{ minWidth: "100%" }}>
            <thead>
              <tr>
                {/* <th>Identifikator</th> */}
                <th>Nazev Knihy</th>
                <th>Dluznik</th>
                <th>Datum vypujcky</th>
                <th>Datum vraceni</th>
                <th>Termin vraceni</th>
                <th></th>
              </tr>
            </thead>
            <tbody>
              {loans.map((loan: Loan) => (
                <tr key={loan.id}>
                  {/* <td>{book.id}</td> */}
                  <td>{loan.book?.title || "Chybi udaj!"}</td>
                  <td>
                    {`${loan.user?.lastName}, ${loan.user?.firstName}` ||
                      "Chybi udaj!"}
                  </td>
                  <td>
                    {loan.loanDate
                      ? new Date(loan.loanDate).toLocaleDateString()
                      : "Chybi udaj!"}
                  </td>
                  <td>
                    {loan.dueDate
                      ? new Date(loan.endDate).toLocaleDateString()
                      : "Chybi udaj!"}
                  </td>
                  <td>
                    {loan.dueDate
                      ? new Date(loan.dueDate).toLocaleDateString()
                      : "Chybi udaj!"}
                  </td>
                  <td>
                    <button
                      onClick={() => handleEndLoan(loan.id)}
                      disabled={loan.endDate !== null}
                    >
                      Vratit knihu
                    </button>
                  </td>
                </tr>
              ))}
            </tbody>
          </table>
        ) : (
          <div>Zadne evidovane vypujcky</div>
        )}
      </div>
    </div>
  );
};
