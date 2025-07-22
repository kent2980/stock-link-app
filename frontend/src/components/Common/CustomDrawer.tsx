"use client";

import {
  Button,
  CloseButton,
  Drawer,
  IconButton,
  Portal,
} from "@chakra-ui/react";
import { Menu } from "lucide-react";

interface CustomDrawerProps {
  open: boolean;
  setOpen: (open: boolean) => void;
}

const CustomDrawer: React.FC<CustomDrawerProps> = ({ open, setOpen }) => {
  return (
    <Drawer.Root
      open={open}
      onOpenChange={(e) => setOpen(e.open)}
      size="xs"
      placement="start"
    >
      <Drawer.Trigger asChild>
        <IconButton
          aria-label="メニューを開く"
          variant="ghost"
          size="xl"
          _hover={{ bg: "gray.600" }}
        >
          <Menu size={20} color="#ffffff" />
        </IconButton>
      </Drawer.Trigger>
      <Portal>
        <Drawer.Backdrop />
        <Drawer.Positioner>
          <Drawer.Content>
            <Drawer.Header>
              <Drawer.Title>Drawer Title</Drawer.Title>
            </Drawer.Header>
            <Drawer.Body>
              <p>
                Lorem ipsum dolor sit amet, consectetur adipiscing elit. Sed do
                eiusmod tempor incididunt ut labore et dolore magna aliqua.
              </p>
            </Drawer.Body>
            <Drawer.Footer>
              <Button variant="outline">Cancel</Button>
              <Button>Save</Button>
            </Drawer.Footer>
            <Drawer.CloseTrigger asChild>
              <CloseButton size="sm" />
            </Drawer.CloseTrigger>
          </Drawer.Content>
        </Drawer.Positioner>
      </Portal>
    </Drawer.Root>
  );
};

export default CustomDrawer;
