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
      backgroundColor: "ui.light",
      color: "ui.dark",
      borderStyle: "solid",
      borderColor: "gray.300",
      borderWidth: "1px",
    },
    td: {
      backgroundColor: "ui.light",
      color: "ui.dark",
      borderStyle: "solid",
      borderColor: "gray.300",
      borderWidth: "1px",
    },
  },
  theme: {
    tokens: {
      colors: {
        ui: {
          main: { value: "#434242ff" },
          secondary: { value: "#dedfe1ff" },
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
