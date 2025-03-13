import { createSystem, defaultConfig } from "@chakra-ui/react";
import { buttonRecipe } from "./theme/button.recipe";

export const system = createSystem(defaultConfig, {
  globalCss: {
    html: {
      fontSize: "16px",
    },
    body: {
      fontSize: "0.875rem",
      margin: 0,
      padding: 0,
    },
    ".main-link": {
      color: "ui.main",
      fontWeight: "bold",
    },
    th: {
      backgroundColor: "ui.main",
      color: "gray.800",
      fontWeight: "800 !important",
    },
    td: {
      backgroundColor: "white",
      color: "ui.dark",
    },
  },
  theme: {
    tokens: {
      colors: {
        ui: {
          main: { value: "#ffffffff" },
          secondary: { value: "#d9d9d7ff" },
          dark: { value: "#333333" },
          light: { value: "#f5f5f5" },
        },
      },
    },
    recipes: {
      button: buttonRecipe,
    },
  },
});
