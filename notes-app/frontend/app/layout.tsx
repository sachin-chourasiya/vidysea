import './globals.css'
import type { Metadata } from 'next'

export const metadata: Metadata = {
  title: 'Notes App',
  description: 'A simple notes application with authentication',
}

export default function RootLayout({
  children,
}: {
  children: React.ReactNode
}) {
  return (
    <html lang="en">
      <body>{children}</body>
    </html>
  )
}
