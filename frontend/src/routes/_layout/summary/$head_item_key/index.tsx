import { createFileRoute, Outlet } from "@tanstack/react-router";

export const Route = createFileRoute("/_layout/summary/$head_item_key/")({
  component: () => <Summary />,
});

function Summary() {
  const { head_item_key } = Route.useParams();
  return (
    <div>
      <h1>Index</h1>
      <p>head_item_key: {head_item_key}</p>
      <Outlet />
    </div>
  );
}
