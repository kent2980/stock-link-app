import { Store } from "@tanstack/react-store";

interface StockIndexState {
  head_item_key: string;
}

export const StockIndexStore = new Store<StockIndexState>({
  head_item_key: "",
});
