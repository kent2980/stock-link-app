import { extendTheme } from "@chakra-ui/react";

const disabledStyles = {
  _disabled: {
    backgroundColor: "ui.main",
  },
};

const theme = extendTheme({
  colors: {
    ui: {
      main: "#064160",
      secondary: "#B43F3F",
      success: "#48BB78",
      danger: "#E53E3E",
      light: "#fefefe",
      dark: "#1A202C",
      darkSlate: "#252D3D",
      dim: "#ecf1f6",
      text: "#1c244a",
    },
  },
  components: {
    Button: {
      variants: {
        primary: {
          backgroundColor: "ui.main",
          color: "ui.light",
          _hover: {
            backgroundColor: "#00766C",
          },
          _disabled: {
            ...disabledStyles,
            _hover: {
              ...disabledStyles,
            },
          },
        },
        danger: {
          backgroundColor: "ui.danger",
          color: "ui.light",
          _hover: {
            backgroundColor: "#E32727",
          },
        },
      },
    },
    Tabs: {
      variants: {
        enclosed: {
          tab: {
            _selected: {
              color: "ui.main",
            },
          },
        },
      },
    },
    Table: {
      variants: {
        dividend: {
          table: {
            size: "sm",
          },
          tr: {
            borderColor: "ui.dim",
            borderBottomWidth: "0.5px",
            borderBottomStyle: "solid",
            height: "30px",
          },
          th: {
            textAlign: "center",
            fontSize: "12px",
            whiteSpace: "normal", // テキストを折り返す
            wordWrap: "break-word", // テキストを折り返す
          },
          td: {
            textAlign: "center",
            fontSize: "12px",
            whiteSpace: "normal", // テキストを折り返す
            wordWrap: "break-word", // テキストを折り返す
          },
        },
      },
    },
  },
});

export default theme;
