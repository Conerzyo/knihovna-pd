import { FC } from "react";

type MenuProps = {
  activeTab: string;
  handleTabChange: (tabName: string) => void;
  isUserAdmin: boolean | null;
  isUserLogged: boolean | null;
};

export const Menu: FC<MenuProps> = ({
  activeTab,
  isUserLogged,
  isUserAdmin,
  handleTabChange,
}) => {
  console.log(activeTab);
  return (
    <div style={menuStyles}>
      <div
        className={activeTab === "catalog" ? "menu_item selected" : "menu_item"}
        onClick={() => handleTabChange("catalog")}
      >
        Katalog
      </div>
      {isUserLogged && (
        <div
          className={
            activeTab === "myLoans" ? "menu_item selected" : "menu_item"
          }
          onClick={() => handleTabChange("myLoans")}
        >
          Moje vypujcky
        </div>
      )}
      {isUserAdmin && (
        <div
          className={activeTab === "admin" ? "menu_item selected" : "menu_item"}
          onClick={() => handleTabChange("admin")}
        >
          Admin
        </div>
      )}
    </div>
  );
};

const menuStyles: any = {
  margin: "24px 0 48px 0",
  display: "flex",
  justifyContent: "center",
};
