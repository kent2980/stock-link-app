import { Store } from "@tanstack/react-store";

interface IndustriesState {
  industry17Code: number | null;
  industry33Code: number[] | null;
  checkedItemsNumber: number[];
}

export const IndustriesStore = new Store<IndustriesState>({
  industry17Code: 0,
  industry33Code: null,
  checkedItemsNumber: [],
});
