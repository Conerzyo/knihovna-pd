import { FC } from "react";
import { Loan } from "../../models/loan";
import { User } from "../../models/user";

type ListProps = {
  columns: ListColumn[];
  data: User[] | Loan[] | undefined | null;
  actionLabel: string;
  action?: (param: string) => void;
};

export type ListColumn = {
  label: string;
  key: string;
};

export const List: FC<ListProps> = ({ columns, data, actionLabel, action }) => {
  const keys = columns.map((c) => c.key);

  return (
    <div style={{ marginBottom: "48px" }}>
      <table>
        <thead>
          <tr>
            {columns.map((column) => (
              <th key={column.key}>{column.label}</th>
            ))}
            {action !== undefined && <th>Akce</th>}
          </tr>
        </thead>

        <tbody>
          {data?.map((entry, i) => (
            <tr key={"line" + i}>
              {keys.map((key: string, i) => (
                <td key={"column" + i}>{entry[key].toString()}</td>
              ))}
              {action !== undefined && (
                <td>
                  <button onClick={() => action(entry.id)}>
                    {actionLabel}
                  </button>
                </td>
              )}
            </tr>
          ))}
        </tbody>
      </table>
    </div>
  );
};
