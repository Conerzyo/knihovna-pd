import { FC } from "react";

type MenuProps = {
  activeTab: string;
  handleTabChange: (tabName: string) => void;
};

export const Menu: FC<MenuProps> = ({ activeTab, handleTabChange }) => {
  console.log(activeTab);
  return (
    <div style={menuStyles}>
      <div
        className={activeTab === "catalog" ? "menu_item selected" : "menu_item"}
        onClick={() => handleTabChange("catalog")}
      >
        Katalog
      </div>
      <div
        className={activeTab === "myLoans" ? "menu_item selected" : "menu_item"}
        onClick={() => handleTabChange("myLoans")}
      >
        Moje vypujcky
      </div>
      <div
        className={activeTab === "admin" ? "menu_item selected" : "menu_item"}
        onClick={() => handleTabChange("admin")}
      >
        Admin
      </div>
    </div>
  );
};

const menuStyles: any = {
  margin: "24px 0 48px 0",
  display: "flex",
  justifyContent: "center",
};
