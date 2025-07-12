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
          background: { value: "rgb(236, 229, 228)" },
          main: { value: "green.600" },
          secondary: { value: "rgba(217, 217, 215, 1)" },
          dark: { value: "#333333" },
          light: { value: "rgb(255, 255, 255)" },
          dataBack: { value: "rgb(244, 244, 246)" },
          description: { value: "#5c4c7d71" },
          bgGradation: {
            value:
              "linear-gradient(90deg, rgb(255, 255, 255) 0%, rgb(244, 246, 251) 100%)",
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
