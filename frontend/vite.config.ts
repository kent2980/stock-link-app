import { TanStackRouterVite } from "@tanstack/router-vite-plugin";
import react from "@vitejs/plugin-react-swc";
import dotenv from "dotenv";
import path from "path";
import { defineConfig } from "vite";
import { VitePWA } from "vite-plugin-pwa";

const envFiles = [".env.local", ".env"];
envFiles.forEach((file) => {
  dotenv.config({ path: path.resolve(__dirname, file) });
});

export default defineConfig({
  plugins: [
    react(),
    TanStackRouterVite(),
    VitePWA({
      registerType: "autoUpdate",
      includeAssets: ["public/assets/images/favicon.png"],
      manifest: {
        name: "My Awesome App",
        short_name: "MyApp",
        start_url: "/",
        display: "standalone",
        background_color: "#ffffff",
        theme_color: "#000000",
        icons: [
          {
            src: "icon-192x192.png",
            sizes: "192x192",
            type: "image/i_192.png",
          },
          {
            src: "icon-512x512.png",
            sizes: "512x512",
            type: "image/i_512.png",
          },
        ],
      },
    }),
  ],
  define: {
    "process.env": process.env,
  },
  server: {
    host: "0.0.0.0",
    port: 3000,
  },
});
