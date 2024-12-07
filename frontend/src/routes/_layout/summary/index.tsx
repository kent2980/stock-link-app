import { createFileRoute, Outlet } from "@tanstack/react-router";

export const Route = createFileRoute("/_layout/summary/")({
  component: () => <Summary />,
});

function Summary() {
  return (
    <div>
      <h1>Index</h1>
      <Outlet />
    </div>
  );
}
