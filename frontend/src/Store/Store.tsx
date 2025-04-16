import { Store } from "@tanstack/react-store";
import { BiCategory, BiHome } from "react-icons/bi";
interface StockListState {
  [key: string]: {
    scrollPosition: number;
  };
}

export const StockListStore = new Store<StockListState>({});

interface SummaryState {
  [key: string]: {
    year: string;
    prevYear: string;
    period: string;
  };
}

export const SummaryStore = new Store<SummaryState>({});

export interface MenuList {
  menuLabel: string;
  menuUrl: string | null | undefined;
  menuIcon: JSX.Element | null | undefined;
}

interface MenuListState {
  menuList: MenuList[];
}
export const MenuListStore = new Store<MenuListState>({
  menuList: [
    { menuLabel: "Home", menuUrl: "/", menuIcon: <BiHome /> },
    {
      menuLabel: "Category",
      menuUrl: "/category",
      menuIcon: <BiCategory />,
    },
  ],
});
