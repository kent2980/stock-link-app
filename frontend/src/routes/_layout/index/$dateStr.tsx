import { createFileRoute } from '@tanstack/react-router'

export const Route = createFileRoute('/_layout/index/$dateStr')({
  component: () => <div>Hello /_layout/index/$dateStr!</div>
})