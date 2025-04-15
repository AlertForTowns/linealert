'use client';

import { useEffect, useState } from 'react';
import Link from 'next/link';

export default function Dashboard() {
  const [alerts, setAlerts] = useState<string[]>([]);

  useEffect(() => {
    const fetchAlerts = async () => {
      try {
        const res = await fetch('/api/alerts');
        const data = await res.json();
        setAlerts(data.alerts || []);
      } catch (error) {
        console.error('Failed to fetch alerts:', error);
      }
    };

    fetchAlerts();
  }, []);

  return (
    <main className="p-10 font-sans">
      <h1 className="text-4xl font-bold text-red-600 mb-4">🚨 Welcome to LineAlert</h1>
      <p className="text-lg mb-8">
        This is your secure, passive OT monitoring dashboard. LineAlert is live on your Azure VM!
      </p>

      <section className="bg-gray-100 p-6 rounded shadow-md mb-10">
        <h2 className="text-2xl font-semibold mb-4">📌 Quick Actions</h2>
        <ul className="list-disc list-inside space-y-2">
          <li>
            <Link href="/view" className="text-blue-600 hover:underline">
              🔍 <strong>View Snapshots</strong>
            </Link>
          </li>
          <li>
            <a
              href="/api/upload"
              target="_blank"
              rel="noopener noreferrer"
              className="text-blue-600 hover:underline"
            >
              ⬆ <strong>Upload Snapshot</strong>
            </a>
          </li>
        </ul>
      </section>

      <section className="bg-white p-6 rounded shadow-md">
        <h2 className="text-2xl font-semibold mb-4">⚠️ Latest Alerts</h2>
        {alerts.length === 0 ? (
          <p className="text-gray-600">No alerts detected.</p>
        ) : (
          <ul className="list-disc list-inside space-y-2">
            {alerts.map((alert, index) => (
              <li key={index} className="text-red-600 font-medium">
                {alert}
              </li>
            ))}
          </ul>
        )}
      </section>

      <footer className="mt-10 text-sm text-gray-500 text-center">
        Running on Next.js 15 · Hosted on Azure
      </footer>
    </main>
  );
}
