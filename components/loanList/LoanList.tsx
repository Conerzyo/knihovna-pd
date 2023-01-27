import { FC, useState } from "react";
import { Loan } from "../../models/loan";
import { SearchOptions } from "../../pages";

type LoanListProps = {
  loans: Loan[] | null;
};

export const LoanList: FC<LoanListProps> = ({ loans }) => {
  return (
    <div style={{ display: "flex", flexDirection: "column", minWidth: "100%" }}>
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
