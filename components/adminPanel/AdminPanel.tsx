import mitt from "next/dist/shared/lib/mitt";
import { FC, useEffect, useState } from "react";
import { User } from "../../models/user";
import { ApiCall } from "../../utils/api";
import { List, ListColumn } from "../genericList/List";

type AdminPanelProps = {};

export const AdminPanel: FC<AdminPanelProps> = ({}) => {
  const pendingRegistrationColumns: ListColumn[] = [
    {
      label: "Jmeno",
      key: "firstName",
    },
    {
      label: "Prijemni",
      key: "lastName",
    },
    {
      label: "Adresa",
      key: "address",
    },
  ];

  const allUsersData: ListColumn[] = [
    {
      label: "Jmeno",
      key: "firstName",
    },
    {
      label: "Prijemni",
      key: "lastName",
    },
    {
      label: "Adresa",
      key: "address",
    },
    {
      label: "Admin",
      key: "admin",
    },
    {
      label: "Aktivni",
      key: "active",
    },
  ];

  const [users, setUsers] = useState<User[] | null>(null);

  const getUsers = async () => {
    const users = (await ApiCall.get("/users/getAll")).data.users;

    setUsers(users);
  };

  const handleConfirmUser = async (userId: string) => {
    const res = await ApiCall.get(`/admin/activateUser?userId=${userId}`);

    if (res.status === 200) {
      getUsers();
    }
  };

  // Load users
  useEffect(() => {
    getUsers();
  }, []);

  return (
    <body>
      <div>
        <h2 style={{ textAlign: "center" }}>Cekajici registrace uzivatelu</h2>
      </div>
      <div style={bodyContainer}>
        <List
          columns={pendingRegistrationColumns}
          data={users?.filter((u) => !u.active)}
          actionLabel="Potvrdit uzivatele"
          action={handleConfirmUser}
        />
      </div>

      <div>
        <h2 style={{ textAlign: "center" }}>Vsichni uzivatele</h2>
      </div>
      <div style={bodyContainer}>
        <List
          columns={allUsersData}
          data={users}
          actionLabel="Potvrdit uzivatele"
        />
      </div>
    </body>
  );
};

const bodyContainer: any = {
  display: "flex",
  flexDirection: "flex-column",
  justifyContent: "center",
  minWidth: "80vw",
};
