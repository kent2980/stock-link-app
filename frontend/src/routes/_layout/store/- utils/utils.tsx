import { Badge } from "@chakra-ui/react";

export const shortBusinessName = (name: string) => {
  let shortName = "";
  let color = "";
  if (name.match(".*売上.*|.*営業収益.*")) {
    shortName = "売";
    color = "green";
  } else if (name == "営業利益") {
    shortName = "営";
    color = "blue";
  } else if (name == "経常利益" || name == "税引前利益") {
    shortName = "経";
    color = "purple";
  } else if (name.match(".*親会社.*当期.*利益.*|.*純利益.*")) {
    shortName = "純";
    color = "red";
  } else if (name.match(".*当期利益.*")) {
    shortName = "当";
    color = "orange";
  } else if (name.match(".*包括利益.*")) {
    shortName = "包";
    color = "teal";
  } else {
    shortName = name;
  }
  return <Badge colorPalette={color}>{shortName}</Badge>;
};

export const shortBusinessValue = (value: number | null | undefined) => {
  if (value == null) {
    return "-";
  }

  return value.toFixed(1).replace("-", "▲") + "%";
};
