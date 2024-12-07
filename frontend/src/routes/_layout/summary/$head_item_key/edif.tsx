import { createFileRoute } from '@tanstack/react-router'

export const Route = createFileRoute('/_layout/summary/$head_item_key/edif')({
  component: () => <div>Hello /_layout/summary/$head_item_key/edif!</div>
})