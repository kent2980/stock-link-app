import { Store } from "@tanstack/react-store";
interface StockListState {
  [key: string]: {
    scrollPosition: number;
  };
}

export const StockListStore = new Store<StockListState>({});
