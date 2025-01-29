import { Store } from "@tanstack/react-store";

interface HeaderState {
  title: string;
}

export const HeaderStore = new Store<HeaderState>({
  title: "",
});
