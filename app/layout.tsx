// app/layout.tsx
import './styles/globals.css'

export const metadata = {
  title: 'LineAlert Dashboard',
  description: 'OT Snapshot Viewer & Upload Tool',
}

export default function RootLayout({ children }: { children: React.ReactNode }) {
  return (
    <html lang="en">
      <body className="bg-gray-100 text-gray-900 p-4">{children}</body>
    </html>
  )
}
