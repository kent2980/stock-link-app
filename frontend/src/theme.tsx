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
      light: "#ffffff",
      dark: "#141313",
      darkSlate: "#252D3D",
      dim: "#f5f5f9",
      text: "#1c244a",
      headerText: "#30303b",
    },
  },
  components: {
    TableContainer: {
      primary: {
        bg: "ui.light",
        borderRadius: "md",
        m: 1,
        p: 2,
        border: "0.5px solid black",
      },
    },
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
        main: {
          table: {
            size: "sm",
          },
          tr: {
            borderColor: "ui.dim",
            borderBottomWidth: "0.5px",
            borderBottomStyle: "solid",
          },
          th: {
            textAlign: "center",
            fontSize: "10px",
          },
          td: {
            textAlign: "center",
            fontSize: "12px",
            whiteSpace: "normal", // テキストを折り返す
            wordWrap: "break-word", // テキストを折り返す
            fontWeight: "500",
          },
        },
      },
    },
    Card: {
      variants: {
        main: {
          borderRadius: "60px",
          BsBorderWidth: "1px",
          boxShadow: "lg",
        },
      },
    },
  },
});

export default theme;
