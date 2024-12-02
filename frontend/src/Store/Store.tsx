import { Store } from "@tanstack/react-store";
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
