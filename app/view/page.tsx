'use client';

import { useEffect, useState } from 'react';
import Link from 'next/link';

export default function Dashboard() {
  const [alerts, setAlerts] = useState<string[]>([]);
  const [loading, setLoading] = useState(true);

  useEffect(() => {
    async function fetchAlerts() {
      try {
        const res = await fetch('/api/alerts');
        const data = await res.json();
        setAlerts(data.alerts || []);
      } catch (err) {
        console.error('Failed to load alerts', err);
      } finally {
        setLoading(false);
      }
    }

    fetchAlerts();
  }, []);

  return (
    <main style={{ padding: '2rem', fontFamily: 'Arial, sans-serif' }}>
      <h1>🚨 Welcome to LineAlert</h1>
      <p>This is your secure, passive OT monitoring dashboard. LineAlert is live on your Azure VM!</p>

      <section style={{ marginTop: '2rem' }}>
        <h2>📂 Dashboard Navigation</h2>
        <ul>
          <li>
            <Link href="/view">
              <strong>🔍 View Snapshots</strong>
            </Link>
          </li>
          <li>
            <a href="/api/upload" target="_blank" rel="noopener noreferrer">
              <strong>⬆ Upload Snapshot</strong> (temporary direct endpoint)
            </a>
          </li>
        </ul>
      </section>

      <section style={{ marginTop: '2rem' }}>
        <h2>🧠 Active Alerts</h2>
        {loading ? (
          <p>Loading alerts...</p>
        ) : alerts.length === 0 ? (
          <p>No alerts detected.</p>
        ) : (
          <ul>
            {alerts.map((alert, idx) => (
              <li key={idx} style={{ marginBottom: '0.5rem', color: 'darkred' }}>
                ⚠️ {alert}
              </li>
            ))}
          </ul>
        )}
      </section>

      <footer style={{ marginTop: '4rem', fontSize: '0.8rem', color: '#666' }}>
        Running on Next.js 15 · Hosted on Azure
      </footer>
    </main>
  );
}
