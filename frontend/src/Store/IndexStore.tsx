import { Store } from "@tanstack/react-store";

interface IndexStore {
  selectDate: string;
}

export const IndexStore = new Store<IndexStore>({
  selectDate: new Date().toISOString().split("T")[0],
});
