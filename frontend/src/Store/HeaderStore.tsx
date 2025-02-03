import { Store } from "@tanstack/react-store";

export interface HeaderAddressItem {
  label: string;
  href: string;
}

interface HeaderState {
  title: string;
  height: number;
  HeaderAddressItems: HeaderAddressItem[];
}

export const HeaderStore = new Store<HeaderState>({
  title: "",
  height: 0,
  HeaderAddressItems: [],
});
