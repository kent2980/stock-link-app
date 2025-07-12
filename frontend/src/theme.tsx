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
      fontFamily: "Noto Sans JP, sans-serif",
    },
    ".main-link": {
      fontWeight: "bold",
    },
    th: {
      fontSize: "10.5px",
      textAlign: "center",
    },
    td: {
      fontSize: "12px",
      textAlign: "center",
    },
  },
  theme: {
    tokens: {
      colors: {
        ui: {
          background: { value: "#ece5e4" },
          main: { value: "green.600" },
          secondary: { value: "#d9d9d7ff" },
          dark: { value: "#333333" },
          light: { value: "#ffffff" },
          dataBack: { value: "#f4f4f6" },
          description: { value: "#5c4c7d71" },
          bgGradation: {
            value: "linear-gradient(90deg, #ffffff 0%, #f4f6fb 100%)",
          },
          link: { value: "#556898" },
          link_hover: { value: "#2d404e" },
        },
      },
    },
    recipes: {
      button: buttonRecipe,
    },
  },
});
